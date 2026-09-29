# Records and refresh rules

Use these field groups when creating a new tracker or extending an existing one. They describe information to preserve, not a mandatory schema or sheet layout. Keep unknown values null with a readable explanation; do not encode unknown salary or dates as zero. ISO dates are useful in JSON; use actual date cells for known dates in Excel.

## Candidate profile

Persist role families, seniority preferences, eligible geographies, remote restrictions, accepted work arrangements, compensation target with currency/period/basis, hard exclusions, and newest-first preference. Keep current compensation only when supplied and useful; it is private context, not a public search term.

Link to authoritative resume and candidate evidence sources; keep employment intervals, education, evidenced skills and outcomes in those sources or separate search evidence notes. Keep evidence review dates and fit inferences outside preference fields. Do not make a second editable copy of career facts inside the search profile. Preserve the distinction between a user requirement, a documented resume fact and an inference. Provider choice is optional and changeable; do not turn the last-used provider into a permanent requirement.

Reuse the candidate's canonical preference record, including field-level confirmation dates where present. If older JSON and Markdown profiles disagree, recover the latest explicit candidate edits before updating either; do not blindly overwrite one from the other. An optional human-readable overview should be derived from the canonical record. Current and expected compensation remain separate, and a one-search exception does not become a lasting profile edit.

## Job records

| Field group | Information to retain |
| --- | --- |
| Identity | Stable local job ID; employer; title; location; employer requisition ID where available; canonical application URL; source URL |
| Research status | Live verified, closed, unverified, or temporarily inaccessible; checked-at date; verification basis |
| Posting date | Reported text; normalized date when supported; date type (original, repost, secondary signal); source; precision/confidence; conflicting evidence |
| Requirements | Work arrangement and geographical eligibility; experience wording; mandatory and preferred qualifications; role responsibilities |
| Compensation | Original wording; minimum/maximum if disclosed; currency; period; fixed/base versus total or unknown basis; source; budget assessment |
| Candidate fit | Shortlist/stretch/unverified/excluded category; specific supporting resume evidence; material gaps; selected resume variant |
| Evidence | Source URLs; retrieval dates; concise support for date, salary, availability and fit; optional local extract paths |
| Tracking | Application stage; applied date; last application activity; next action and completion state; deadlines and follow-up dates; interview round, schedule and timezone; candidate notes; relevant contacts; prepared materials and distinct submitted document versions; other pre-existing user fields |
| History | Research first seen, last checked, last seen live and identity aliases; preserve the separate application event history with stable job/event IDs, effective dates, recorded timestamps, changed values and sources |

Do not conflate the research category with the application status. A job can be a stretch role with an application already submitted. For a newly discovered job with no application history, use an unset or “Not tracked” status unless “Not applied” is actually known or the user has chosen that default.

Compensation assessments should distinguish a compatible advertised range on the requested basis, below-target pay on that basis, pay with a different or ambiguous basis, estimates, and undisclosed pay. Preserve a maximum figure's qualifier such as “up to”; it is not a guaranteed salary. Treat a minimum or preferred target according to the user's wording, and do not reject higher-paying positions automatically.

For example, if a candidate targets 25–28 lakh annually in fixed pay, an advertised 18–30 lakh explicitly fixed range supports potential budget compatibility. A 30 lakh CTC figure does not establish fixed-pay compatibility. Neither establishes the candidate's eventual offer. These figures are illustrative, not defaults.

## Refresh ownership and merging

Use the same current workbook as application-tracker when present. Excel is authoritative for application tracking; structured exports of tracking fields are derived from it. Keep raw research records distinct from those exports. For a new workbook, `Applications` can hold one row per opening, including research categories and tracking fields; application-tracker adds a `History` sheet when recording events. Preserve established sheet layouts and avoid competing editable rows for the same opening.

1. Read the current workbook and structured records before fetching updates. If application tracking differs, preserve the latest user edits; ask only about conflicts that cannot be resolved from provenance or dates. Never let a stale generated source overwrite workbook edits silently.
2. Match by requisition and employer, then stable canonical URL; use company/title/location comparisons as a fallback requiring judgment. Keep old IDs or URLs as aliases when identity is clear. Do not silently merge ambiguous matches.
3. Refresh research fields with newly verified evidence. Preserve user-owned tracking fields, including unfamiliar columns, and retain custom formulas or workbook features when editing. Keep recommended resume variants separate from submitted versions; do not append application events, change application stage, or update last application activity merely because a listing was refreshed.
4. Carry forward existing records absent from the latest results. Update `last_checked` when rechecked; advance `last_seen_live` only on positive evidence. Mark closed only with supporting evidence. Keep past applications and notes even when the role closes or is screened out.
5. Save a dated snapshot before replacing the current workbook, or produce the refreshed workbook as a new dated file. State which file is now current; avoid competing master copies.
6. Reconcile added, updated, unchanged and closed counts using stable IDs. Regenerate exports containing tracking state from the successfully saved workbook; identify stale exports if regeneration fails. Include a concise refresh summary without copying the whole tracker into chat.

Keep dated research notes limited to useful provenance: search scope and windows, providers used, sources checked, unresolved retrieval gaps and the as-of date. Count queries or pages only when known; do not equate search-result volume with verified jobs.

## Final workbook checks

- Compare exported row identities and category totals with the intended records; ensure duplicates were not introduced or existing applications dropped.
- Inspect native hyperlinks and their targets, including roles with similar titles. Source and application links may point to the same authoritative page.
- Verify date sorting does not elevate unknown dates and salary cells preserve basis, units and qualifiers.
- Check tracking values against the pre-refresh workbook, including notes, dates and customized fields. Test relevant status-count formulas when present.
- Inspect representative long-text rows, headers and links for clipping and usability. Report any unsupported workbook features before a lossy replacement.
