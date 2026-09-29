"""Exercise PDF publication and failure behavior with fictional candidate data."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "cover-letter/scripts/render_cover_letter.py"
FIXTURE = ROOT / "tests/fixtures/cover-letter.json"


class RendererTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.output = self.directory / "letter.pdf"

    def render(self, source=FIXTURE, *options):
        return subprocess.run(
            [sys.executable, str(RENDERER), str(source), "--output", str(self.output), *options],
            capture_output=True, text=True, check=False,
        )

    def test_publishes_verified_selectable_pdf(self):
        result = self.render()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["pages"], 1)
        self.assertEqual(set(report["content_verified"]), {"pypdf", "pdfplumber"})
        extracted = PdfReader(self.output).pages[0].extract_text()
        self.assertIn("Alex Example", extracted)
        self.assertIn("DEMO-001", extracted)
        self.assertIn("<, >, and &", extracted)

    def test_refuses_overwrite_and_preserves_original(self):
        self.output.write_bytes(b"Original document")
        result = self.render()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.output.read_bytes(), b"Original document")

    def test_failed_revision_leaves_published_pdf_intact(self):
        self.output.write_bytes(b"Original document")
        data = json.loads(FIXTURE.read_text())
        data["paragraphs"] = ["A lengthy synthetic paragraph. " * 150] * 4
        source = self.directory / "too-long.json"
        source.write_text(json.dumps(data))
        result = self.render(source, "--overwrite")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("allowed maximum", result.stderr)
        self.assertEqual(self.output.read_bytes(), b"Original document")

    def test_rejects_executable_contact_links(self):
        data = json.loads(FIXTURE.read_text())
        data["contact_lines"][0][0]["href"] = "javascript:alert(1)"
        source = self.directory / "invalid.json"
        source.write_text(json.dumps(data))
        result = self.render(source)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
