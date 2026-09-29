# Records, stages, and history

Read when creating or extending the workbook, reconciling identity or stage changes, or changing history and scheduling fields. These conventions support the existing tracker; preserve established equivalents rather than imposing a migration.

## Workbook identity and ownership

Use one current workbook per candidate. In a new workbook, `Applications` holds the current record for each opening and `History` holds dated events linked by stable job ID. Research categories can be columns or existing sheets. If the workbook already has a canonical row elsewhere, update it there rather than adding a competing editable copy in a new sheet. Preserve unfamiliar sheets and fields.

Match records by existing ID, then employer plus requisition, then a canonical role-specific application URL. Company, title, and location are a fallback requiring judgment. Stable IDs must survive sorting, moving between sheets, URL changes, and refreshes; row numbers are not IDs. Keep useful aliases. Different requisitions at the same company remain separate. A repost is not automatically a new application or a new submission date.

The current row summarizes the candidate's latest known progress for that opening. If the candidate explicitly reapplies to the same requisition, record a separate submission event and distinguish attempts in history; preserve earlier dates, materials, and outcomes. Do not merge a different requisition simply because the title matches. Company-level cold outreach with no identified opening should not create a fictitious job application; keep it in an existing outreach record, or a separate `Outreach` sheet only when tracking it is requested.

The workbook is authoritative for tracking. Job-search may update researched posting details, availability, compensation, and fit, while preserving the tracking fields below. Raw research JSON can remain research evidence. JSON containing the combined tracking state is an export of the workbook, not an independently editable master. Resolve material provenance conflicts rather than selecting whichever source was generated most recently.

## Current application fields

Add fields as needed; a narrow update should not require all columns to be populated. Keep unknowns blank with an explanation when material, not zero or a fabricated date.

| Group | Information to preserve |
| --- | --- |
| Identity | Stable job ID, employer, exact role, requisition, location, application URL, useful identity aliases |
| Research | Existing availability, fit category, posting and verification dates, salary evidence and source URLs; separate from application state |
| Progress | Application stage, confirmed application date, interview round, last meaningful activity date, stage/event source |
| Next action | Action description, pending/completed/cancelled state, due date, source or suggested/confirmed basis |
| Timing | Application deadline, follow-up date, next interview date/time, timezone, and known offer-response deadline |
| Contacts | Known recruiter or interviewer name, relevant contact details, supplied conversation reference |
| Materials | Prepared resume/letter/answers links and distinct submitted versions or submission-event references |
| Notes | Candidate notes, interview context and outcomes, unresolved details; preserve existing custom fields |

`last_activity` reflects the most recent known application event, not viewing the workbook, searching for the role, or saving a metadata correction. Keep uncertain dates qualified. A mutable document path can be saved as a reference but does not verify which content was submitted. Do not copy whole inbox messages or private profile fields into the tracker when a short source reference is sufficient.

## Stage meanings

These are useful defaults, not a mandatory sequential state machine. Preserve equivalent labels and custom stages in an existing workbook.

| Stage | Basis |
| --- | --- |
| Not tracked / blank | Newly discovered opportunity with no established candidate application state |
| Saved | Candidate explicitly chose to track the opening for consideration; not proof they have never applied |
| Preparing | Candidate is preparing materials and recording that activity is within the requested tracking scope |
| Applied | Candidate confirms submission, or successful submission evidence is available |
| Screening | Confirmed employer screening is underway; a generic application receipt is insufficient |
| Interviewing | An interview is scheduled or in progress; preserve the specific round separately |
| Offer | An actual offer has been reported or supplied; positive interview feedback is insufficient |
| Accepted | Candidate confirms acceptance or evidence shows it already happened; setting this stage does not accept an offer externally |
| Rejected | Confirmed employer rejection, distinct from a closed listing or no response |
| Withdrawn | Candidate confirms withdrawing from consideration; record an explicit uncommunicated decision as such rather than inventing a message to the employer |
| Declined | Candidate confirms declining an offer; retain the offer history |

Accepted, Rejected, Withdrawn, and Declined are normally terminal for application follow-ups. Preserve explicit remaining actions, such as returning paperwork. A clear correction or reopened process may change a terminal stage. If an update reports an event earlier than the current stage, append the historical event without regressing the stage unless a correction or reopening is intended. Do not fabricate intermediate stages to make the history look complete.

## History entries

Each entry should have a stable event ID, job ID, event type, effective event date/time if known, recorded-at timestamp, changed fields with previous/new values where useful, and a concise source or note. Sources may be a candidate statement, supplied recruiter message, manual workbook reconciliation, or observed action result. Candidate confirmation is sufficient; a live email integration is optional.

Use entries for submission, stage changes, interviews scheduled/rescheduled/cancelled/completed, confirmed contact, next-action changes, linked materials, and corrections. Capture submitted document versions on the relevant submission event. If several related fields change in one event, one coherent entry is enough. A repeated instruction that has already been recorded is a no-op; a distinct second interview or submission must not be discarded solely because its label matches.

Append corrections that identify the superseded value/event rather than rewriting ordinary history. Read-only reviews and job-search refreshes are not candidate application events. Do not manufacture the exact timing or actor behind pre-existing manual edits. On an explicit request to erase sensitive data, remove it from maintained views/history as authorized instead of copying it into a new correction entry or backup, and explain any records outside the deletion scope.

## Dates and actionable reviews

Use native Excel dates for known calendar dates and native date/time values with a separate timezone for timed events. Use ISO timestamps with offset or timezone context in structured exports. Preserve a date-only deadline as a date; do not invent a midnight time. Resolve “today,” “tomorrow,” and weekday references against the candidate's applicable timezone and the date of the statement. Clarify ambiguous weekday or timezone meanings when they affect a scheduled event.

An overdue action is pending and has a known due date/time before the review's as-of date/time. A date-only action due today is due today, not overdue before that day ends. Keep completed, cancelled, and superseded actions out of due counts. On rescheduling, replace the current scheduled value and retain the previous value in history; do not report both as upcoming interviews. Completing an interview does not automatically establish success, rejection, or the next round.

Use confirmed pending actions for deadline and follow-up queues. Show proposed follow-up dates separately until adopted or explicitly saved as tentative. Do not manufacture a default outreach cadence, write suggested deadlines as employer commitments, or claim a notification has been scheduled when only a workbook cell changed.
