---
name: cover-letter
description: "Create or revise job-specific cover letters from a resume and confirmed candidate experience, including formatted, selectable-text PDFs when requested. Use for new applications and follow-ups such as 'now for this role'; not for rewriting resumes or submitting applications."
---

# Cover Letter Creation Workflow

Turn a candidate's actual experience into a concise letter that explains why it matters for the target role. Preserve successful content and design decisions while keeping each application separate.

## Recover the current application context

Read the latest resume, authoritative content source, candidate corrections, and established output preferences. Prefer the resume variant closest to the role. Explicit recent clarifications supersede older drafts; neither an old cover letter nor a sample letter is independent evidence.

Read relevant saved candidate preferences when they affect the letter. Keep compensation, notice period, and other private screening details out of the letter unless requested or required for this application; do not update the profile from generated prose. A request for a short recruiter email belongs to recruiter-email when available, while a requested cover letter remains this workflow.

For follow-ups such as "now for this job," carry forward the established output format, directory and design. A previous PDF request can therefore authorize another PDF. A text-only request should remain text-only. Use `cover_letters/` for files when no directory is established, and separate filenames by employer and requisition where available. Do not replace a different application or modify the resume as a side effect.

Capture application identity before writing: employer or recruiting agency, exact advertised title, requisition if supplied, target location(s), intended letter date, and candidate contact details. If a heading and description use different titles, use the advertised heading and requisition to identify the application; tailor to the actual responsibilities. Candidate location does not establish willingness to relocate, travel, or work a particular schedule. An agency listing does not identify its undisclosed client.

Use the supplied full job description directly. Research only missing or material information. If responsibilities are absent, ask for them while doing independent drafting work; an exact public posting can fill the gap when title, recruiter/employer, location and other identifying details agree. Do not borrow requirements from a merely similar role. If no full description is recovered, disclose title-based tailoring outside the letter. A search-index copy does not establish that an opening is still live.

## Select evidence and write

Choose two or three strong connections between the role and the candidate's work. A coherent example usually explains more than a long inventory of technologies: describe the problem, the candidate's contribution, and the supported outcome.

- Keep skills, implemented features, production operation, architecture scope, and leadership distinct. A listed framework is not evidence of a deployed project or daily use.
- Join components and metrics into one system narrative only when the evidence links them. Do not assign portfolio-wide results to one feature or a recent promotion.
- Preserve ranges, approximations, peak-use qualifiers, units and denominators. Token reduction is not equivalent to money saved; hours saved do not acquire a weekly or per-query denominator. Published benchmarks never become the candidate's achievements.
- Frame a new business domain as interest or a transferable application of experience, not prior domain expertise. Do not infer adjacent tools, credentials, seniority thresholds or tenure from the target requirements.
- Omit unsupported claims rather than filling every keyword. Material unknowns can prompt a focused question, but an unmet requirement does not automatically require an apologetic paragraph.

Default to a focused, roughly 250-350-word letter with a specific opening, a few connected evidence paragraphs, and a brief closing. Adjust to the user's instructions and the substance available. Use natural prose rather than a resume bullet list or a paraphrase of the job description. Avoid ungrounded praise of the company, invented motivations, and repeated skill inventories. Keep source citations, fit analysis, evidence gaps and operating notes outside the submitted letter.

## Produce the requested format

Keep an editable text or structured source for the final wording. For files, check employer, title, requisition, date, recipient, filename and document metadata together so a reused layout does not retain another application's details. Use the current date in the user's timezone unless a different date is requested; preserve historical dates on unrelated letters.

Match the candidate's latest accepted resume/letter styling when appropriate, including font, colour and contact formatting. Do not assume that the font or palette of an earlier application remains current. A one-page, single-column layout is a useful default, not a reason to shrink text excessively or remove substantive evidence. Avoid text boxes, layout tables, icons as contact labels, and substantive text in page headers/footers when parseability matters.

For PDF work, read [PDF production](references/pdf-production.md). The optional [renderer](scripts/render_cover_letter.py) accepts a per-application JSON source, supports supplied fonts and styling, and verifies complete extracted content. It contains no candidate details or employer-specific wording. Use an available PDF skill for environment-specific authoring requirements and visual QA. For another requested format, use the corresponding available document workflow rather than adding unsolicited companions.

## Verify and deliver

Check claims against the current evidence, then check the actual final artifact:

- Inspect rendered pages for readable type, spacing, wrapping, isolated final words, clipping and page count. Fix wording or spacing before reducing type size.
- Compare complete extracted text with the editable source in reading order, including contacts and application identifiers. For a parsable PDF, use independent extraction engines when available; the helper uses `pypdf` and `pdfplumber`.
- Recheck affected outputs after edits. Distinguish selectable/extractable text from a guarantee about an employer's ATS; local checks establish only the former.

Deliver the finished letter or requested file with a brief statement of what was tailored and verified. Preserve the source for subsequent revisions. Creating a cover letter does not authorize sending it, applying for the job, or updating an application tracker.

If the user also asks to record the letter in their tracker, use application-tracker when available and link the exact prepared file to the matching opening. Preserve any previously submitted letter version and application stage; drafting or revising a letter is not submission evidence.
