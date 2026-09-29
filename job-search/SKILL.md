---
name: job-search
description: "Find and refresh job opportunities against a saved candidate profile, verify posting and salary evidence, and maintain an Excel shortlist while preserving application tracking. Use for job discovery, role shortlists, or research refreshes; application progress updates and follow-up reviews belong to application-tracker when available."
---

# Job Search Workflow

Produce a current, evidence-backed shortlist that the candidate can act on, and save enough context to repeat the search without losing preferences or application tracking. Enter at the requested stage: a refresh or narrow role search does not require repeating completed profile work.

## Load the candidate and existing work

Read the project's instructions, active candidate's saved profile, latest resume evidence, previous results and tracker before searching. Reuse existing file locations and a single canonical preference record. For a new project, `candidate/profile.json` within the candidate's workspace and dated result folders are practical defaults; a Markdown overview can be derived when useful. Keep different candidates' records separate.

Capture or confirm only missing inputs that materially affect matching: role families and seniority, geography and remote eligibility, work arrangements, compensation target and its basis, and relevant exclusions. Distinguish hard constraints from preferences. Do not repeatedly ask for known answers or delay independent searches for optional application details.

- Save user preferences separately from resume facts and inferred fit. Keep resume evidence in its authoritative source and link to it. Record changed preferences with their confirmation date and source; derive any overview from the canonical record. A search-only exception should not overwrite a lasting preference. Use candidate-profile for explicit preference management when available; a search can still use supplied preferences without it.
- Keep candidate-specific names, salary amounts, currencies, locations and file paths in the project profile, not this skill.
- Calculate experience as of the search date from documented employment intervals; do not double-count overlapping roles, round upward to satisfy a requirement, or assume unlisted employment. Preserve education and formal job titles.
- Select an appropriate existing resume variant when available. Producing a new resume is a separate task unless requested.
- Search using role and skill criteria. Do not put private resume contents, contact details or current compensation into public search queries.

## Choose available research capabilities

Use any suitable available combination of job-search connectors, search engines, web APIs, crawlers, page readers, browser tools or direct employer/ATS pages. Search discovery and page retrieval may use different providers. **No named provider, plugin, CLI, account or API key is a prerequisite.** Follow a current user provider choice when given; otherwise choose according to access, coverage and reliability.

Use existing authorized capabilities. Do not install software, buy credits or create accounts merely because a preferred provider is unavailable. If retrieval fails, try a materially different available route, such as the canonical employer page or another reader. Do not retry the same failure indefinitely. Mark unresolved listings as unverified and explain any coverage limitation. Without live access, organize supplied evidence and label its age; do not claim a fresh search or current verification.

## Discover and verify opportunities

Search across the requested role families, useful title variants and eligible locations. For a freshness-first search, start with the user's requested window; absent one, the last 7 days, then 30 days, then older active roles is a useful widening sequence. Cover relevant employer career sites, ATS pages and job boards without assuming that one provider is exhaustive. Prefer a smaller supported shortlist over padding a numerical target.

For each promising result, read the job description and check the role-specific application destination. Prefer the employer or its ATS as the authoritative source. An aggregator can help discover a vacancy, but its snippet alone does not establish requirements, availability or fixed pay.

- **Availability:** Check that the page describes the actual vacancy and offers an application route. A successful HTTP response, generic careers page, talent pool or cached snippet is insufficient. Record the verification date and source. Distinguish a live page from a tested submission; do not submit to test a form.
- **Freshness:** Preserve the reported date, source and confidence. A crawl timestamp, search indexing date, page update or relative freshness label is not automatically the original posting date. Anchor relative dates to retrieval time, mark them approximate, and retain conflicts. Keep undisclosed posting dates unknown. Record a repost separately from the original date when known.
- **Eligibility:** Check location restrictions on remote roles, work arrangement, required experience, core responsibilities and material mandatory qualifications. “Remote” does not imply worldwide eligibility.
- **Compensation:** Preserve the source wording, currency, pay period and whether it refers to fixed/base pay, variable pay, equity, total compensation or an estimate. Do not label salary as confirmed fixed pay unless the source explicitly supports that basis. A compatible advertised range is a potential budget fit, not a personal offer. Undisclosed or ambiguous pay needs confirmation. A target range is not a ceiling unless the user says so.
- **Provenance:** Save source URLs, retrieval dates and short evidence notes sufficient to justify material decisions. Keep useful local extracts when available, with resolvable relative paths. Provider result IDs may be retained, but URLs and job identity must remain usable without that provider.

Deduplicate using an employer requisition ID when available; otherwise compare canonical application URLs and normalized company, title and location. Reconcile evidence across duplicates without merging distinct requisitions or location-specific vacancies solely because their titles match. Remove tracking parameters only when they are unnecessary for reaching the correct role.

Stop when the requested scope is covered and plausible candidates have been checked, or when further searches mainly repeat existing results. Report meaningful coverage and remaining gaps; do not describe the search as exhaustive.

## Assess fit and prioritize

Map the job's actual requirements to documented candidate evidence. Explain the strongest match and material gaps in plain language; overlapping keywords or a senior title do not establish suitability. Separate mandatory requirements from preferred qualifications. Avoid invented ATS scores or unsupported match percentages.

Keep resume fit, availability, freshness and compensation status as separate judgments. Use understandable categories, adapted to the user's scope:

- **Shortlist:** Verified relevant vacancies with a defensible fit. Unknown pay can remain here if clearly labeled and the user has not required disclosed compensation.
- **Stretch:** Relevant roles with an explicit experience, technical or responsibility gap. Identify the gap rather than inflating candidate experience.
- **Unverified leads:** Promising results whose full requirements or active application route could not be checked.
- **Screened out:** Closed vacancies, duplicates, non-vacancy pages or material mismatches, with a reason and source. Do not silently discard an existing application record.

When newer postings are preferred, sort newest credible posting dates first within the relevant category and label any secondary or approximate date used for prioritization. Do not give undated roles a fabricated date; keep their date uncertainty visible. Use fit and eligibility to break ties. Preserve user-directed ordering when it differs.

## Save results and maintain the tracker

For a new dataset or changes to an existing result format, read [records and refresh rules](references/records-and-refresh.md). Preserve established schemas where they already serve the task; add evidence fields without forcing a needless migration.

Share the candidate's existing workbook with application-tracker when available. For a new tracker, `outputs/job_tracker.xlsx` is a practical default. Excel is authoritative for application progress and manual edits; exports containing tracking fields are derived from the saved workbook. Research-owned JSON may supply new job evidence, but must not replace tracking state. A request only to change application stages, record interviews, or review follow-ups belongs to application-tracker and does not require a new job search.

Save newly confirmed lasting preferences when establishing or updating the search profile; otherwise preserve the existing profile. Save structured job records and an Excel workbook unless the user requests a different deliverable. Use the available spreadsheet skill for workbook creation or editing when present; otherwise use suitable workbook tools. The workflow is independent of a particular spreadsheet library.

Make the primary shortlist easy to scan. Use sheets or a category column for stretch roles, unverified leads and exclusions according to volume and the existing design. Include role-specific application and source links, resume-fit notes, gaps, posting evidence, salary status, last verification date and application tracking. Put key requirements and search limitations near the results. Use native dates where known, filterable headers, readable widths and wrapping, and frozen headers where helpful.

For refreshes, reconcile current workbook edits before regenerating anything from saved JSON. Preserve application status, application dates, follow-up dates, notes, contacts, resume versions and other user-entered information. Update research-owned fields separately. Mark a known closure explicitly; a listing merely missing from this search or temporarily inaccessible is not proof of closure. Retain history and explain newly added roles or material changes.

Preserve the application's stable ID, event history, interview schedule, pending actions, and exact submitted document versions. A newly recommended resume variant must not replace the resume recorded as submitted. Do not advance application stage, last application activity, or follow-up dates merely because research was refreshed; a closed vacancy is not evidence of candidate rejection.

Validate the final saved deliverable: reconcile counts and categories against structured records, confirm each application link maps to the correct job, check date and salary labels, and inspect formulas and representative rendered areas when supported. Verify that existing tracking survived a refresh. Distinguish a syntactically valid URL from an inspected live destination, and report any checks the available tooling could not perform.

Deliver the workbook link, the saved profile location, category counts and the most material caveats. Keep historical research dates explicit. The research workflow does not itself authorize applications, recruiter outreach, recurring monitoring or resume uploads; perform those only when included in the user's authorized scope.
