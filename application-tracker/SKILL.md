---
name: application-tracker
description: "Create, update, or review a candidate's Excel application tracker. Use to record applications, stage changes, interviews, outcomes, document versions, and follow-up dates, or to review upcoming and overdue actions. Shares the job-search workbook and preserves manual edits; does not submit applications or send messages."
---

# Application Tracker

Maintain an accurate record of the candidate's progress for each job opening. Use conversational updates to keep the current state, next actions, and dated history together in the candidate's existing Excel workbook.

## Recover the candidate and tracker

Read workspace instructions, the active candidate's context, and the latest workbook before working. Keep each candidate's records separate. Resolve ambiguous candidate identity before accessing personal records and ambiguous application identity before changing a row. A company name alone may match several openings.

Reuse the workbook maintained by job-search, preserving its sheets, columns, formulas, and manual edits. Excel is authoritative for application tracking; JSON exports are derived snapshots and must not overwrite newer workbook changes. Research extracts may supply new job facts, but cannot establish application progress. Do not create a second master tracker.

When creating a tracker or extending its structure, read [records, stages, and history](references/records-and-history.md). If none exists and creation is in scope, use `outputs/job_tracker.xlsx` within the candidate's workspace, with an `Applications` sheet and a `History` sheet. A review-only request should report a missing tracker rather than create one. Use the available spreadsheet skill for file creation or editing when present; otherwise use suitable workbook tools. This workflow does not require a particular library, job-search service, or email integration.

## Record an update

Treat a clear statement such as “I applied to this role today” as sufficient candidate confirmation. Do not demand a receipt or repeat an approval question. Match by the existing stable job ID, employer and requisition, or the role-specific application URL; use title and location when necessary. If the opening is new, add the known details and leave unsupported research facts unknown rather than making a live search a prerequisite.

Extract the event, effective date, affected fields, and source. Resolve relative dates using the conversation date and applicable timezone; ask only when ambiguity materially changes the record. Record an interview's timezone explicitly. An unknown event date stays unknown; the date the update was recorded is not automatically the date the event happened.

- Update only supported fields. Preserve unrelated applications, research assessments, contacts, notes, custom columns, and existing document links.
- Allow stages to be skipped, corrected, or reopened when supported. An interview invitation can establish `Interviewing` without an invented application date or screening event. An older event added late should not silently move the current stage backward.
- Set `Applied` only from candidate confirmation, supplied submission evidence, or observed successful submission within an authorized workflow. Drafting answers, preparing a letter, saving a job, and emailing a recruiter do not establish submission.
- Keep job availability, fit category, and application stage separate. A closed posting or unanswered message is not proof of rejection.
- Distinguish documents being prepared from the exact versions actually submitted. A new resume recommendation or regenerated letter must not replace the submitted-version record. Use existing versioned paths where available; do not claim a mutable file preserves the original submitted bytes.
- Keep next action, follow-up date, application deadline, and interview schedule distinct. On rescheduling or completing an action, update the relevant pending item while preserving the previous event in history. A cancelled interview does not by itself mean rejection.

Append a history entry for each meaningful recorded change, including corrections. Retain when the event happened separately from when it was recorded. Avoid duplicate events when repeating a request whose changes are already present. Do not invent missing historical transitions or attribute an unexplained manual edit to the candidate at a guessed time.

## Review progress and next actions

For “what needs my attention?” or a weekly review, read without changing stages, dates, or last activity. Use the requested time window and timezone; if none is supplied, show the next seven days and state that window. Surface overdue pending actions first, then upcoming interviews and deadlines, due follow-ups, and preparation work. Keep terminal applications out of routine follow-up queues unless they have an explicit outstanding action.

Show awaiting-response applications with the known date of their last relevant contact or submission. Do not infer that a response is overdue or an application unsuccessful from elapsed time alone. If a follow-up cadence is requested, distinguish suggested dates from candidate- or employer-confirmed commitments. Missing dates belong in a short “needs scheduling” note when actionable, not in overdue counts.

Derive totals from the saved records, distinguishing tracked applications from newly discovered leads. Keep the report concise: application identity, current stage, next action, and relevant date or timezone. A workbook date or chat review does not create a proactive reminder. Calendar events, scheduled notifications, inbox monitoring, and outbound messages require a separately requested and available workflow.

## Save, verify, and deliver

Before saving, check for intervening workbook edits and reconcile them instead of replacing the file from a stale copy. Preserve the previous workbook as a dated snapshot for ordinary updates, then save and reopen the updated workbook. Keep one clearly identified current file. If the available tool cannot preserve important workbook features, produce a separate reviewable copy and explain the limitation rather than silently losing them.

Verify the changed rows against the request, stable IDs and record counts, history entries, dates/timezones, document links, formulas, and preservation of unrelated fields. Confirm that repeated updates do not create duplicate rows or history events. Inspect affected formatting and readable widths when creating or changing layout. Report any verification limits. Regenerate optional JSON exports only from the successfully saved workbook, and identify stale exports if regeneration fails.

For an update, return the workbook link and a brief account of the changed application and next action. For a review, return the requested view without rewriting the workbook. Keep candidate details in their workspace, outside this skill.

Job-search owns discovery and research refreshes. When requested, resume-builder, cover-letter, and job-application can provide artifact links; recruiter-email can use tracking context for drafts and record confirmed outreach when tracking is in scope. These handoffs never turn draft creation into a submitted application. Tracking an event does not send messages, accept an offer, withdraw an application with an employer, or change candidate preferences.
