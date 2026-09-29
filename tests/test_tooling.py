"""Observable packaging behavior using synthetic skills and isolated directories."""

from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import install_skills
import validate_skills


class SkillFixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.repo = self.base / "repo"
        self.repo.mkdir()
        (self.repo / "LICENSE").write_text("Synthetic fixture license\n")
        self.skill = self.add_skill("example-skill")
        self.destination = self.base / "installed"

    def add_skill(self, name):
        path = self.repo / name
        path.mkdir()
        (path / "SKILL.md").write_text(
            f'---\nname: {name}\ndescription: "A synthetic test workflow."\n---\n\n# Example\n'
        )
        return path


class InstallerTests(SkillFixture):
    def test_copies_supporting_files_and_license(self):
        (self.skill / "assets").mkdir()
        (self.skill / "assets" / "example.bin").write_bytes(b"synthetic asset")
        targets = install_skills.install(["example-skill"], self.destination, root=self.repo)
        self.assertEqual((targets[0] / "assets/example.bin").read_bytes(), b"synthetic asset")
        self.assertEqual((targets[0] / "LICENSE").read_text(), "Synthetic fixture license\n")
        self.assertEqual((targets[0] / "SKILL.md").read_bytes(), (self.skill / "SKILL.md").read_bytes())

    def test_conflict_preserves_existing_files_and_prevents_partial_install(self):
        self.add_skill("second-skill")
        existing = self.destination / "second-skill"
        existing.mkdir(parents=True)
        (existing / "custom.md").write_text("Keep my edits")
        with self.assertRaisesRegex(ValueError, "Already exists"):
            install_skills.install(["example-skill", "second-skill"], self.destination, root=self.repo)
        self.assertFalse((self.destination / "example-skill").exists())
        self.assertEqual((existing / "custom.md").read_text(), "Keep my edits")

    def test_unknown_skill_and_traversal_do_not_write(self):
        for name in ("missing", "../outside"):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "Unknown skills"):
                install_skills.install([name], self.destination, root=self.repo)
        self.assertFalse(self.destination.exists())

    def test_dry_run_has_no_side_effects(self):
        targets = install_skills.install(["example-skill"], self.destination, root=self.repo, dry_run=True)
        self.assertEqual(targets, [self.destination / "example-skill"])
        self.assertFalse(self.destination.exists())

    def test_rejects_destination_inside_source(self):
        with self.assertRaisesRegex(ValueError, "inside a source"):
            install_skills.install(["example-skill"], self.skill / "nested", root=self.repo)

    def test_rejects_link_to_external_content(self):
        private = self.base / "private.txt"
        private.write_text("Not for installation")
        try:
            (self.skill / "external.txt").symlink_to(private)
        except OSError:
            self.skipTest("Symlinks unavailable on this platform")
        with self.assertRaisesRegex(ValueError, "symlinks"):
            install_skills.install(["example-skill"], self.destination, root=self.repo)
        self.assertFalse(self.destination.exists())

    def test_io_failure_rolls_back_only_new_installation(self):
        self.add_skill("second-skill")
        self.destination.mkdir()
        unrelated = self.destination / "unrelated.txt"
        unrelated.write_text("Keep this")
        original = shutil.copytree

        def fail_second(source, target, *args, **kwargs):
            if Path(target) == self.destination / "second-skill":
                raise OSError("Simulated copy failure")
            return original(source, target, *args, **kwargs)

        with mock.patch.object(install_skills.shutil, "copytree", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "Simulated"):
                install_skills.install(["example-skill", "second-skill"], self.destination, root=self.repo)
        self.assertEqual(list(self.destination.iterdir()), [unrelated])

    def test_agent_destinations(self):
        with mock.patch.object(install_skills.Path, "home", return_value=self.base):
            self.assertEqual(install_skills.default_destination("codex"), self.base / ".agents/skills")
            self.assertEqual(install_skills.default_destination("claude"), self.base / ".claude/skills")


class ValidatorTests(SkillFixture):
    def test_portable_skill_does_not_require_codex_metadata(self):
        count, errors = validate_skills.validate_repository(self.repo)
        self.assertEqual(count, 1)
        self.assertEqual(errors, [])

    def test_detects_invalid_frontmatter(self):
        (self.skill / "SKILL.md").write_text("---\nname: [broken\n---\n")
        self.assertTrue(validate_skills.validate_skill(self.skill))

    def test_detects_wrong_invocation(self):
        (self.skill / "agents").mkdir()
        (self.skill / "agents/openai.yaml").write_text(
            'interface:\n  display_name: "Example"\n'
            '  short_description: "A useful synthetic workflow for testing"\n'
            '  default_prompt: "Use $another-skill to do this."\n'
        )
        self.assertTrue(any("default_prompt" in error for error in validate_skills.validate_skill(self.skill)))

    def test_rejects_host_specific_frontmatter(self):
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text().replace("name: example-skill", "name: example-skill\ncontext: fork"))
        self.assertTrue(any("nonportable" in error for error in validate_skills.validate_skill(self.skill)))

    def test_checks_real_links_but_ignores_code_examples(self):
        path = self.repo / "README.md"
        path.write_text(
            "[Skill](example-skill/SKILL.md)\n[Missing](missing.md)\n"
            "```markdown\n[Illustrative](not-a-file.md)\n```\n"
        )
        errors = validate_skills.validate_links(path, self.repo)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing.md", errors[0])


if __name__ == "__main__":
    unittest.main()
