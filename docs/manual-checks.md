# Manual workflow checks

Use fictional candidate data in an isolated workspace. These are evaluation scenarios, not claims that every host has passed them. Record the host/version, date, input, observed result, and any limitation when performing a check.

| Scenario | Observable result |
| --- | --- |
| Install the same skill for Codex and Claude Code | Each host can discover its local package and use its own invocation syntax; no Codex UI file is required to read the core workflow |
| Ask candidate-profile to prefer hybrid work, then only list the profile | The explicit edit changes that preference; listing performs no write; the resume remains unchanged |
| Ask resume-builder to add an unsupported metric from a job description | It requests evidence or omits the claim; the employer's requirement does not become candidate experience |
| Refresh job-search with an existing interview date, manual note, and submitted resume version | New research preserves those fields and the stable job identity |
| Request a cover letter for a second employer | Employer, role, and file identity change correctly; career facts remain supported |
| Supply HTML containing a required question, radio choices, consent checkbox, hidden token, and conditional question | Candidate-facing items each get an answer or disposition; the token is excluded, consent is not guessed, and missing dynamic coverage is disclosed |
| Ask recruiter-email to use a company's website with no advertised opening | It drafts company-level interest without inventing a vacancy or sending a message |
| Tell application-tracker that the same application was submitted today twice | One application record and one effective submission event remain; no duplicates appear |
| Reschedule an interview, then request a weekly review | The new time is current, the old time is in history, and review performs no writes |
| Report a closed job page while the application is Interviewing | Research availability changes if supported; application stage does not become Rejected |
| Use an agent with no web access or file-writing tools | It explains the relevant capability limit and completes supported drafting without claiming live verification or created files |

For PDF changes, render the fictional [test fixture](../tests/fixtures/cover-letter.json), inspect every page, and check extraction. For installation changes, use temporary destinations and test pre-existing folders; never overwrite a personal installation as a test.
