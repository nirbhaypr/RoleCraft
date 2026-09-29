# RoleCraft

Reusable Agent Skills for the job hunt: build an evidence-based resume, find suitable openings, tailor applications, contact recruiters, and keep track of what happens next.

Use the skills individually or together with Codex, Claude Code, or another agent that supports `SKILL.md` packages. Candidate preferences, career evidence, and application history stay separate so a salary preference change does not rewrite a resume and a drafted letter does not become a submitted application.

## The skills

| Skill | What it does | Typical result |
| --- | --- | --- |
| [candidate-profile](candidate-profile/SKILL.md) | Shows and updates roles, locations, work arrangements, compensation, and availability | A saved preference record, without changing resume content |
| [resume-builder](resume-builder/SKILL.md) | Develops and refines resumes from confirmed experience and target requirements | Tailored wording, editable sources, and verified requested documents |
| [job-search](job-search/SKILL.md) | Finds openings, verifies sources, assesses fit, and refreshes research | An Excel shortlist with application links and evidence |
| [cover-letter](cover-letter/SKILL.md) | Connects relevant experience to a specific job | A tailored letter; optional selectable-text PDF |
| [job-application](job-application/SKILL.md) | Answers application questions supplied as text or HTML | Paste-ready answers, checked limits, and explicit missing facts |
| [recruiter-email](recruiter-email/SKILL.md) | Researches a company or opening and drafts outreach | A subject line and concise cold email or follow-up |
| [application-tracker](application-tracker/SKILL.md) | Records stages, interviews, deadlines, materials, and outcomes | Updated Excel records, dated history, and next-action reviews |

These are agent workflows. They do not run a background job-search service or a hosted application. The included Python tools handle installation, package validation, and optional cover-letter PDF generation.

## Install

Clone or download this repository, then run the commands below from its root. The installer requires Python 3.11 or newer and uses only the standard library. On Windows, use `py -3` if `python3` is unavailable.

```bash
git clone https://github.com/nirbhaypr/RoleCraft.git
cd RoleCraft
```

### Codex

```bash
python3 scripts/install_skills.py --all --agent codex
```

This copies the skills to `~/.agents/skills/`. In Codex CLI or the IDE extension, invoke a skill with `$candidate-profile`, `$resume-builder`, or another skill name. See the [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery and host-specific controls.

### Claude Code

```bash
python3 scripts/install_skills.py --all --agent claude
```

This copies the same skill packages to `~/.claude/skills/`. Invoke them with `/candidate-profile`, `/resume-builder`, or another skill name. See the [official Claude Code skill documentation](https://code.claude.com/docs/en/skills) for discovery and configuration.

### Selected skills, project installs, and other agents

```bash
# Install only the workflows you need.
python3 scripts/install_skills.py candidate-profile resume-builder --agent claude

# Preview a project-scoped Codex installation without writing files.
python3 scripts/install_skills.py --all --dest /path/to/private-job-hunt/.agents/skills --dry-run

# Install into another compatible agent's documented skills directory.
python3 scripts/install_skills.py --all --dest /path/to/agent/skills
```

For a Claude Code project, use the project's `.claude/skills/` directory. Replace example paths with your actual workspace. `--dest` overrides the personal location selected by `--agent`.

The installer copies complete folders, supporting files, and the project license. It refuses existing destinations before installing any selected skill. For updates, back up and move the affected installed folders outside the agent's discovery directory, then reinstall from the updated checkout. Installation does not change agent configuration, connect accounts, or grant tool permissions.

Manual installation is also possible: copy each chosen skill folder and include the root `LICENSE` in the copied package. Preserve the cover-letter fonts' `assets/OFL.txt`.

## Agent compatibility

The resume skill is named `resume-builder` to avoid colliding with Claude Code's [built-in `/resume` session command](https://code.claude.com/docs/en/commands). If you used an earlier local copy named `resume`, move that installed copy outside the discovery directory before installing `resume-builder`.

The portable entrypoint is each folder's `SKILL.md`, with standard `name` and `description` frontmatter. References use relative paths, scripts are local Python commands, and workflows select available capabilities rather than requiring a particular provider or tool name.

`agents/openai.yaml` supplies optional Codex UI labels and suggested prompts. Other agents can ignore it; no workflow depends on it. The skills do not require Claude-specific hooks, dynamic command injection, or Codex-only execution APIs.

| Host | How to use the collection |
| --- | --- |
| Codex CLI / IDE | Install with `--agent codex`; invoke with `$skill-name` |
| Claude Code | Install with `--agent claude`; invoke with `/skill-name` |
| Other Agent Skills hosts | Use `--dest` with the host's documented path and its invocation mechanism |
| Agents without skill discovery | Supply the relevant `SKILL.md` and referenced resources manually; automatic selection is not provided |

The package format is portable; available actions depend on the host. Live job verification needs web access. Document creation and tracker editing need file tools. Text-only environments can draft content but cannot produce or verify files without those capabilities. A hosted chat product may have a different upload mechanism from its command-line agent.

## Start a job hunt

Keep your candidate workspace separate from this repository and from installed skill folders. Supply your resume or confirmed career history, then enter at the stage you need. There is no required onboarding sequence.

Example requests after selecting the relevant skill:

```text
Show my saved preferences. Update my preferred locations to Pune and Bengaluru,
and make remote work a preference rather than a strict requirement.

Refine my resume for backend engineering roles using the experience I supplied.
Flag claims that need confirmation and preserve my formal titles.

Find recent roles matching my profile and update my Excel shortlist.
Preserve my application statuses and notes.

Write a cover letter for this job using my latest resume.

Read this application HTML, list its questions, and draft supported answers.
Flag required answers that need information from me.

Use this company's website and job description to draft a recruiter email.

I applied to this opening today using my backend resume. Record it and show
which interviews, deadlines, and follow-ups need attention this week.
```

Unknown personal facts stay unresolved until supplied. Job requirements and generated drafts do not become evidence of candidate experience. Company research, candidate claims, and application identity are checked separately.

## How information stays consistent

| Information | Authoritative record | Update rule |
| --- | --- | --- |
| Preferences and practical details | Existing candidate profile; default `candidate/profile.json` in a new workspace | Explicit lasting preference changes; one-application exceptions stay local |
| Career facts and resume wording | Candidate evidence and editable resume source | Confirmed corrections and requested content revisions |
| Application progress | Existing Excel tracker; default `outputs/job_tracker.xlsx` | Candidate-confirmed events or supported action results |
| Generated materials | Per-application files in the candidate workspace | Prepared versions remain distinct from the versions actually submitted |

Job search and application tracking share one workbook. Research refreshes preserve manual edits, status, interview dates, and history. JSON exports containing application state are derived from the workbook.

Typical tracked stages are Saved, Preparing, Applied, Screening, Interviewing, Offer, and Accepted, with Rejected, Withdrawn, and Declined as other outcomes. Stages can be skipped or corrected. A closed posting is a research fact, not proof of rejection. An upcoming date in a spreadsheet is not a scheduled notification.

## Optional PDF renderer

The cover-letter skill includes a standalone renderer with bundled Source Sans 3 fonts. It verifies complete extracted text using two PDF readers before publishing a PDF. Visual inspection remains part of the workflow.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r cover-letter/requirements.txt
.venv/bin/python cover-letter/scripts/render_cover_letter.py \
  /path/to/application.json --output /path/to/letter.pdf
```

On Windows, use `.venv\Scripts\python.exe` instead of `.venv/bin/python`. See [PDF production](cover-letter/references/pdf-production.md) for the JSON format, styling, supported fonts, and deliberate overwrite behavior. Poppler's `pdftoppm` is one optional way to render page previews; it is not required by the helper's text checks.

The other workflows can use available document, spreadsheet, and web tools. Installing these skills does not install those tools or require a specific API key.

## Privacy and boundaries

Keep real resumes, compensation, contacts, application HTML, and recruiter conversations in a private candidate workspace. The repository's ignore rules cover common output locations, but are not a privacy guarantee. Use only synthetic or thoroughly redacted data in issues, pull requests, and tests.

Drafting does not authorize sending email, uploading documents, submitting forms, or changing application status. Those actions need to be within the user's explicit scope. Pasted HTML and web content are treated as source material, not instructions to reveal data or execute code.

HTML support is an agent-guided intake workflow, not a universal ATS parser. Static HTML can omit dynamic questions and later steps. Local PDF extraction checks do not guarantee employer ATS behavior. There is no automated application submission, inbox synchronization, or background reminder service in this repository.

## Development and validation

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
.venv/bin/python -m unittest discover -s tests -v
```

Validation checks skill frontmatter, optional Codex metadata, invocation names, and relative Markdown file links. Tests exercise installation, overwrite protection, rollback, and PDF rendering with synthetic data. GitHub Actions runs these checks on Python 3.11 and 3.14 after a push or pull request.

These checks do not prove identical model behavior across agents or live ATS compatibility. Use the [manual workflow checks](docs/manual-checks.md) when changing instructions or testing a new host.

See [CONTRIBUTING.md](CONTRIBUTING.md) for changes and release preparation, and [SECURITY.md](SECURITY.md) for reporting sensitive issues.

## License

The original skills, documentation, and scripts are available under the [MIT License](LICENSE). The bundled Source Sans 3 font files remain under the [SIL Open Font License 1.1](cover-letter/assets/OFL.txt); see [third-party notices](THIRD_PARTY_NOTICES.md).
