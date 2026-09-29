# Profile structure and update rules

Use this structure for a new profile when the workspace has no established equivalent. Preserve existing schemas and paths when they already separate preferences from career evidence. These are storage conventions, not an intake questionnaire or defaults to impose on a candidate.

## Canonical record

Use a candidate-scoped JSON object with `schema_version`, `candidate_id`, `updated_at`, `preferences`, `practical_details`, and optional `evidence_sources`. Put no resume bullets, employment history, or inferred skill scores into the preference record. `evidence_sources` contains paths to authoritative career evidence, not copied facts.

Store each known preference or practical detail as an entry:

```json
{
  "value": ["remote", "hybrid"],
  "status": "confirmed",
  "strength": "preference",
  "confirmed_at": "2026-09-29",
  "source": "Candidate explicitly prefers remote or hybrid work"
}
```

The values and date above illustrate the format; use the actual candidate's answer and confirmation date. `strength` applies to matching preferences: `requirement` excludes mismatches, while `preference` affects ranking. Omit it for factual practical details such as current compensation. Use `status: "unknown"` and `value: null` when unknown, `status: "cleared"` and `value: null` after an explicit reset, and `status: "declined"` only for an explicit disclosure preference. An empty list is ambiguous; store an explicit `unrestricted` status when the candidate states that there is no constraint.

Only add populated fields or unknowns that matter to the active task. Do not populate every possible key with invented defaults. Preserve the candidate's qualifications in the value or a short `notes` field; a lossy normalized label should not replace the original meaning. Use ISO dates and record field-level confirmation dates so viewing the record does not falsely refresh old facts.

## Useful field groups

| Group | Fields and distinctions |
| --- | --- |
| Target work | Target roles, seniority, employment types (permanent, contract, internship), preferred industries and company stages |
| Location | Preferred job locations, countries from which the candidate can work remotely, willingness to relocate, travel constraints |
| Arrangement | Remote/hybrid/on-site; commuting radius or maximum office days only when supplied; distinguish preferences from requirements |
| Schedule | Acceptable timezones, overlap hours, shifts, and working days when relevant |
| Compensation expectations | Target range and basis, minimum acceptable amount only if explicitly stated, negotiability, and currency/period |
| Exclusions | Employers, industries, contract types, or other explicit exclusions with their scope |
| Practical details | Current location, current compensation, notice period, notice negotiability, resignation/release status, earliest joining date |
| Eligibility | Confirmed country-specific work authorization and sponsorship needs only when supplied for this purpose; keep them separate |
| Search preferences | Freshness preference and other explicit ranking choices; a temporarily selected tool/provider is not a permanent preference |

Store personal contact details only when needed in the established candidate record. Do not duplicate them merely to satisfy this format.

## Compensation values

Represent a compensation value with `currency`, `period`, `basis`, and `amount` or `target_min`/`target_max`. Use full currency units for normalized numbers, retaining `original_text`. Useful basis values include `fixed_base`, `total_ctc`, `total_cash`, and `unknown`; preserve component breakdowns only when supplied. Equity and variable pay do not silently become fixed pay.

For example, an explicit “expected INR 25–30 lakh per year, total CTC” supports `target_min: 2500000`, `target_max: 3000000`, `currency: "INR"`, `period: "year"`, and `basis: "total_ctc"`. It does not establish a minimum acceptable offer, hard maximum, current compensation, or permission to disclose current pay. An unqualified “30” needs clarification. Preserve a supplied ambiguous amount as original text while leaving unresolved normalized components null.

Current compensation belongs in `practical_details.current_compensation`; expected compensation belongs in `preferences.expected_compensation`. A suggested negotiation range is not a confirmed target until the candidate adopts it. Multiple currencies or employment types may need separate targets; do not overwrite one with the other or compare them without a stated basis.

## Existing profiles and update integrity

If an older JSON/Markdown pair exists, determine which source contains the latest explicit candidate edits before choosing the canonical record. Resolve material conflicts from provenance or a focused question. Once established, derive the other format from the canonical source; do not alternate authority between them.

For explicit edits, preserve unrelated keys, update field-level provenance, and verify the saved diff. A displayed review is not a new confirmation of every field. Do not copy private values into general logs, filenames, or reusable skill examples. A clear/forget request should not leave the removed value in a newly created backup or history entry.
