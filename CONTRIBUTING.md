# Contributing

Contributions should improve a concrete job-hunt workflow without inventing candidate facts, adding unnecessary approval gates, or binding the collection to one agent or provider.

## Set up and check changes

Use Python 3.11 or newer. From the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
.venv/bin/python -m unittest discover -s tests -v
```

On Windows, replace `.venv/bin/python` with `.venv\Scripts\python.exe`.

Keep a pull request focused on a workflow or a specific failure. Describe the trigger, resulting behavior, and checks performed. Include a synthetic reproduction for a bug; do not attach real candidate records. Instructions-only changes need a realistic manual scenario where behavior matters, not tests that assert exact prose.

## Skill conventions

- Put each skill in a root folder whose lowercase hyphenated name matches `SKILL.md` frontmatter.
- Keep the entrypoint short enough to scan. Put substantial conditional guidance in linked references.
- Use portable frontmatter and ordinary Markdown. Keep host UI metadata in optional companion files.
- Refer to capabilities such as web research, PDF generation, and workbook editing. Named services should be optional or chosen by the user.
- Preserve candidate facts, units, qualifiers, provenance, and authorization boundaries. Keep preferences, evidence, research, and application progress distinct.
- Keep data and environment paths out of installed skills. Examples and fixtures must be clearly fictional.
- Add scripts when deterministic execution improves the workflow. Include dependencies and tests for consequential behavior, such as avoiding overwritten artifacts.
- Preserve relevant licenses when adding fonts, assets, or third-party code.

Adding a skill also requires a README catalog entry, an invocation example, and a manual evaluation scenario. `agents/openai.yaml` is optional for portability, but use it for consistent Codex presentation when adding a skill to this collection. Its default prompt must invoke the actual skill name.

## Test a host

Install into an isolated skills directory or temporary home, avoiding existing personal installations. Use [manual checks](docs/manual-checks.md) to review discovery, missing capabilities, factual grounding, and file preservation. Record the host, date, scenario, and observed limitations. Do not claim support for a hosted interface merely because its CLI understands the package format.

## Prepare a GitHub release

1. Run validation and tests from a clean checkout and review the staged files for private data or generated outputs.
2. Confirm installation instructions against the hosts being documented and exercise relevant manual scenarios.
3. Review dependency updates, font notices, and the license. Keep GitHub Actions pinned to reviewed commit hashes.
4. Create the GitHub repository when publishing is authorized, enable Actions, and configure private vulnerability reporting and branch protection as appropriate.
5. Push the reviewed commits, confirm CI passes on GitHub, and create a tag/release only when intentionally publishing a version.

No release version or cross-host behavioral certification is implied by the initial repository packaging. Keep release notes tied to changes and validation actually completed.
