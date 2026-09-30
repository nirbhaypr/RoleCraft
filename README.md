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

These are agent workflows. They do not run a background job-search service or a hosted application. The included Python helpers support local package validation and optional cover-letter PDF generation.

## Install

With Node.js and npm installed, run this from the project where you want to use the skills:

```bash
npx skills add nirbhaypr/RoleCraft
```

The [Skills CLI](https://github.com/vercel-labs/skills#usage) lets you choose which skills to install and which agents to use. Installation is project-scoped by default; add `--global` to make the skills available across your projects. You do not need to clone this repository or install Python to install the skills.

### All skills for a specific agent

```bash
# Codex
npx skills add nirbhaypr/RoleCraft --skill '*' --agent codex

# Claude Code
npx skills add nirbhaypr/RoleCraft --skill '*' --agent claude-code

# Both agents, available across projects
npx skills add nirbhaypr/RoleCraft --skill '*' --agent codex claude-code --global
```

### Browse or install selected skills

```bash
# List available skills without installing them.
npx skills add nirbhaypr/RoleCraft --list

# Install only candidate preferences and resume building for Claude Code.
npx skills add nirbhaypr/RoleCraft --skill candidate-profile resume-builder --agent claude-code
```

Choose another supported agent in the interactive installer, or pass its identifier with `--agent`. Keep the `'*'` quoted so your shell does not expand it into filenames. See the [Skills CLI options](https://github.com/vercel-labs/skills#options) for installation methods and supported flags.

### List and update installed skills

```bash
npx skills list
npx skills update resume-builder
```

The update command above targets the selected skill. Python and document tools are only needed when running workflows that use them; see the optional PDF renderer and development setup below.

## Agent compatibility

The resume skill is named `resume-builder` to avoid colliding with Claude Code's [built-in `/resume` session command](https://code.claude.com/docs/en/commands). If you used an earlier local copy named `resume`, move that installed copy outside the discovery directory before installing `resume-builder`.

The portable entrypoint is each folder's `SKILL.md`, with standard `name` and `description` frontmatter. References use relative paths, scripts are local Python commands, and workflows select available capabilities rather than requiring a particular provider or tool name.

`agents/openai.yaml` supplies optional Codex UI labels and suggested prompts. Other agents can ignore it; no workflow depends on it. The skills do not require Claude-specific hooks, dynamic command injection, or Codex-only execution APIs.

| Host | How to use the collection |
| --- | --- |
| Codex CLI / IDE | Install with `--agent codex`; invoke with `$skill-name` |
| Claude Code | Install with `--agent claude-code`; invoke with `/skill-name` |
| Other Agent Skills hosts | Select a supported agent in the Skills CLI and use its invocation mechanism |
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

The cover-letter skill includes a standalone renderer with bundled Source Sans 3 fonts. It verifies complete extracted text using two PDF readers before publishing a PDF. Visual inspection remains part of the workflow. To run the helper directly, use the following commands from a local checkout of this repository.

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

For contributions or local validation, use Python 3.11 or newer, clone the repository, and run the checks from its root:

```bash
git clone https://github.com/nirbhaypr/RoleCraft.git
cd RoleCraft
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
