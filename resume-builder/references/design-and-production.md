# Design and production

## Choose a usable presentation

For template research, present a small shortlist with an actual visual preview, original source, editing format, and practical tradeoffs. Distinguish a downloadable template from a hosted editor or paid service. Evaluate the exported document rather than relying on an ATS-friendly label or claimed hiring outcomes.

When the user has already selected a template, apply it directly. When the user explicitly wants to choose, provide the comparison and preserve current outputs until that choice is made. Do not change accepted section order or content merely because the sample template uses a different order.

Prefer a clear primary text flow, recognizable headings, readable type, visible contact information, and real links. Avoid placing important content in text boxes, graphics, or headers/footers. Inspect actual layout structures before calling a template table-free; role/date alignment can hide table usage. A conservative adaptation may use ordinary paragraphs and tab stops. Verify extraction even when the layout appears simple.

Choose length from the candidate's evidence, requested constraints, and readability. Improve hierarchy, repetition, spacing, and page breaks before shrinking all text. Preserve substantive engineering or delivery detail. Keep headings with the content they introduce and avoid stranded bullets; keep an entry together when practical without imposing one role per page.

## Generate reproducibly

Use a canonical editable content model with shared identity, education, employment facts, and explicit wording for each requested variant. Separate design settings from factual content. Generate final documents and any useful plain-text companion from this source rather than manually maintaining independent copies.

Use the chosen template's native rendering path when it gives the intended result. Retain editable inputs and document the actual build command, dependency versions, and necessary font assets. Resolve paths for the current workspace rather than copying machine-specific paths from another project. Use existing format skills or runtime discovery when available.

An editable companion can use different layout primitives while preserving the same content, hierarchy, typography, and palette. State material differences if relevant; do not claim pixel identity between formats without checking. Keep content as editable paragraphs and bullets. Verify hyperlink targets, font substitution, and theme inheritance, which can override a selected font. Retain licenses for bundled fonts and embed them only when permitted and useful for portability.

A practical workspace convention is:

- `research/`: job evidence, reference analysis, candidate clarifications, and decisions.
- `source/`: authoritative content, design inputs, and build/verification helpers.
- `output/`: clearly identified current deliverables.
- `tmp/`: intermediate renders and experiments.
- `archive/`: prior accepted revisions with enough source to reproduce them.

Adapt to the existing project rather than reorganizing it unnecessarily. Distinguish content revisions from design revisions. Preserve the previous accepted source and outputs before replacing them; do not silently present historical ZIPs or alternatives as current.

## Iterate without unintended changes

For content changes, update the canonical model, all affected role variants, and requested formats. Honor additions, removals, section reordering, and summary corrections consistently. Mark old notes as superseded when they would otherwise resurrect resolved questions.

For layout-only changes, record the content baseline and preserve every fact and wording choice. Adjust the requested spacing or typography and inspect pagination in each format. Editable-document rendering can add a page even when the native PDF remains stable. Make format-specific spacing changes when needed, then verify the source content again.

For colour or other visual options, create actual rendered alternatives from the accepted layout. A comparison should reflect the real documents, with full-page files available when needed. For a colour-only request, vary accents while preserving text, fonts, sizes, and placement; check extracted text and, where practical, character coordinates. Keep current deliverables intact while alternatives are being considered.

After selection, apply the chosen properties to editable sources and all requested formats. Compare final outputs with the selected preview. Refresh labels and manifests so they describe the actual current design rather than the previous default. Recheck the affected final files using [Verification](verification.md).
