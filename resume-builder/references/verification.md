# Verification

## Routine delivery checks

Verify the actual files to be delivered after the last relevant change. For an audit-only request, inspect current artifacts without modifying or regenerating them. Identify current files explicitly so archives, temporary renders, and historical bundles do not enter the result accidentally.

Use two complementary checks:

1. **Visual:** render and inspect every final page for clipping, overlap, hidden text, missing glyphs, crowded sections, awkward wrapping, unwanted spillover, and page breaks. Check hierarchy and whitespace at a readable scale. Render the editable document independently of a native PDF and inspect its pages too.
2. **Source fidelity:** compare complete extracted text with the canonical content, including identity/contact fields, section headings, summaries, qualifications, every skill row, employer, title, date, and full bullet. Verify section order and that each date and bullet remains associated with the right entry. Presence of a few keywords is insufficient.

Compare the whole ordered sequence, or ordered source blocks with explicit entry boundaries, so omissions, duplicates, and unintended additions are visible. A right-aligned date may appear after the employer or degree rather than beside the title; accept that only if it remains in the correct entry before its detail. When page placement is part of the agreed design, check it against the actual rendered pages.

For PDFs, confirm selectable text, readable technical terms, valid contact link targets, and no extraction-blocking encryption. Investigate unembedded/substituted fonts, replacement characters, or text outside page bounds when they threaten the output. For editable documents, check readable paragraph order, real bullets/links, and any embedded fonts or package relationships that custom generation code creates.

Normalize only justified presentation differences: ordinary whitespace runs, documented Unicode equivalences, bullet glyphs, and known repeated page footers. If a line wrap splits an existing hyphenated compound, retain its hyphen when rejoining it. Preserve raw extracts. Do not delete all punctuation or spaces, sort words, or use only a similarity score to make an incorrect extraction pass.

Keep a concise verification record tying results to the final filenames, source revision, checks performed, and unresolved issues. Rebuild and recheck affected outputs after a correction. Once relevant checks pass, do not repeat a broad audit without a new change or concern.

## Dedicated ATS/extraction audit

Use this deeper pass when the user specifically requests parsing assurance or when routine checks expose a concern. It is not required for every small edit.

Run more than one independent parser engine when available; a strong comparison uses three engines and their useful normal/layout modes. Multiple modes of one library are not independent engines. Record engine/version, mode, file identity or hash, page count, complete-block recovery, bullet recovery, reading-order findings, and any anomalies. Save extracted text and machine-readable results when the scope warrants them.

Test visible contact details, employer/title/date association, full skills, and complete achievements rather than merely whether the document opens. Compare against the authoritative source, not a second extraction alone: parsers can agree on the same omission. Confirm alternatives share content and geometry before generalizing results between them.

If an optional raw/content-stream mode joins words, report that separately from the normal/layout results. Equal non-whitespace characters can prove that letters survived while still exposing broken word boundaries. A character-preservation check cannot establish readable tokenization. Retain failures in the report instead of hiding them behind a successful aggregate metric.

Describe results at the level tested:

| Check | What it establishes |
| --- | --- |
| Visual inspection | Readable appearance in the inspected renders |
| Complete source comparison | Expected content survives the tested extraction |
| Reading-order and entry checks | Sections and employment details stay meaningfully associated |
| Independent parser comparison | Agreement or differences across the tested engines/modes |
| Actual employer ATS test, only if performed | Observed behavior of that specific system and submission |

Do not convert local extraction results into a universal ATS guarantee, ranking score, or promise of correct employer field classification. Follow an application's requested file format and inspect autofilled fields when that application workflow is separately in scope. Resume creation or a local audit does not itself authorize uploading candidate data to an external scoring service or submitting applications.

## Handoff

Link the current requested files and their editable sources. Briefly state the substantive change, visual/content checks completed, and any material limitation. Distinguish final files from alternatives and historical bundles. Keep candidacy questions, research provenance, build instructions, and audit notes outside the application documents.
