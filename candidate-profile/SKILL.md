---
name: candidate-profile
description: "Show, create, or edit a candidate's job-search and application preferences, including target roles, locations, remote/hybrid/on-site work, current and expected compensation, notice period, and exclusions. Use for profile reviews and preference updates; keep resume content and career evidence separate."
---

# Candidate Profile

Maintain the candidate's confirmed preferences and practical application details so other job-hunt tasks can reuse them. A profile update changes matching and future draft answers; it does not rewrite a resume, change career evidence, or revise past applications.

## Find the right record

Recover the active candidate and existing profile from the workspace and conversation. Keep candidate data in their workspace, never in the installed skill. In a workspace with several candidates, use a stable candidate identifier and separate directories. If the intended candidate is ambiguous, resolve that before reading or changing personal records; never select the first profile by default.

Reuse an established profile path and schema. For a new profile, read [profile structure](references/profile-structure.md); use `candidate/profile.json` within the candidate's workspace as a practical default. Keep one authoritative profile. A Markdown overview is a derived view, not a second independently editable master. Do not silently migrate older `job_search_profile` files or discard unfamiliar fields.

## Show or update the profile

For a request to list, inspect, or review preferences, read without writing. Present known values grouped into target roles, location/work arrangements, compensation, availability, and exclusions as relevant. Distinguish unknown, unrestricted, declined disclosure, and explicitly cleared values. Mention stale or unresolved details only when they matter. Do not require a complete questionnaire before showing a partial profile.

For an explicit update, apply the requested changes without another approval step. Ask only about ambiguity that changes the value or scope. “Remote only from India” can set a location eligibility constraint and a hard work-arrangement constraint; “prefer remote” must not exclude hybrid roles. An application-specific exception does not become a lasting preference unless the user asks to save it.

- Change only the requested fields, preserving other candidate details, custom fields, evidence links, and the existing schema.
- Keep current compensation, expected compensation, and any minimum acceptable amount distinct. Preserve currency, period, units, and fixed/base versus total CTC. Do not infer a hard ceiling from a target range or assume an unqualified salary amount means annual fixed pay.
- Separate current location, acceptable job locations, remote hiring eligibility, and relocation willingness. A location or previous job does not establish work authorization, sponsorship, travel, shifts, or willingness to relocate.
- Store notice period, negotiability, and earliest joining date separately when known. Do not calculate a committed joining date without the necessary resignation or release facts.
- Record the date and source of each changed value. Reuse confirmed details; generated draft answers, employer requirements, and inferred fit do not become candidate facts.
- Clearing a value means it becomes unknown or unset, not “No” or zero. If asked to forget a detail, remove it from maintained derived views and do not preserve the deleted value in a change log; state any storage outside this workflow that was not modified.

Sensitive declarations, demographic answers, and government identifiers are not routine profile fields. Save a reusable sensitive answer only when explicitly requested and needed; do not infer it. Current compensation is private context and must not enter public search queries. Having a saved value does not itself authorize recruiter outreach or broad disclosure.

## Save and hand off

Validate structured data and field semantics before saving. Re-read the source before replacing it to preserve intervening edits; write a complete valid replacement safely. Update any established derived overview from the canonical record. Verify the saved values and that unrelated fields survived. Keep factual resume evidence in its own authoritative source, linked only when useful.

Return a concise account of the changed fields and the profile location. Explain relevant effects, such as including hybrid vacancies in the next search. Do not refresh a tracker, regenerate resumes, rewrite existing letters, or change application statuses as a side effect. A request to use the updated profile for another task authorizes that task within its stated scope.

When available, job-search reads this profile for matching; job-application reads it for practical screening questions; recruiter-email and cover-letter read only details relevant to the requested draft. These skills remain usable independently with candidate-supplied information.
