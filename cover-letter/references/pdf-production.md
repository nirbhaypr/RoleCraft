# PDF production

Use this reference only when a PDF is requested or established by the ongoing workflow. Prefer an existing suitable renderer when it already preserves the accepted design. Otherwise use the helper below. It uses ReportLab, embeds TrueType fonts, and validates final text through `pypdf` and `pdfplumber` before publishing the output.

Discover the available Python runtime and PDF rendering tools rather than hardcoding machine-specific paths. The required packages are `reportlab`, `pypdf`, and `pdfplumber`. Use an existing managed runtime when the host provides one. Follow any applicable PDF skill's authoring setup; this helper does not implement environment-specific artifact registration.

The standalone dependency list is [requirements.txt](../requirements.txt). In an appropriate Python environment, install it with `python -m pip install -r /path/to/cover-letter/requirements.txt` when dependency installation is within the task's scope.

## Per-application source

Save UTF-8 JSON outside the installed skill. Personal details, draft text, and employer data belong to the application workspace, not the skill package. Example shape (illustrative content only):

```json
{
  "name": "Alex Morgan",
  "contact_lines": [
    [
      {"text": "Current city, country"},
      {"text": "+10000000000", "href": "tel:+10000000000"},
      {"text": "alex@example.com", "href": "mailto:alex@example.com"}
    ],
    [{"text": "example.com/alex", "href": "https://example.com/alex"}]
  ],
  "date": "29 September 2026",
  "company": "Example Company",
  "role": "AI Engineer",
  "reference": "REQ-123",
  "recipient": ["Hiring Team", "Example Company, Target city"],
  "salutation": "Dear Hiring Team,",
  "paragraphs": ["The completed first paragraph.", "The completed second paragraph."],
  "closing": "Sincerely,",
  "signature": "Alex Morgan",
  "style": {
    "page_size": "A4",
    "accent": "#333333",
    "body_size": 11.5,
    "leading": 15.5
  }
}
```

Required fields: `name`, `date`, `company`, `role`, `recipient` (nonempty array of lines), and `paragraphs` (nonempty array of paragraphs). `contact_lines` is optional. Each contact is visible text with an optional `http`, `https`, `mailto`, or `tel` link. Link text and URLs are escaped before rendering. Body paragraphs are plain text; markup is not interpreted.

Optional fields:

- `reference`: appended to the default application subject exactly as provided; include a label such as `Req ID` when wanted.
- `subject`: overrides the default `Application for <role> | <reference>`.
- `salutation`, `closing`, `signature`: default to `Dear Hiring Team,`, `Sincerely,`, and the candidate's name.
- `style.page_size`: `A4` (default) or `Letter`.
- `style.accent`: six-digit hex colour, default neutral `#333333`.
- `style.font_regular` and `style.font_bold`: supply both TrueType paths to match an existing design. Relative paths resolve from the JSON file's directory, not the working directory. The fallback is the bundled, openly licensed Source Sans 3 pair; it is not a universal style preference. Missing glyphs produce an error, so choose fonts that cover the candidate's language.
- `style.body_size`, `leading`, `paragraph_spacing`, `margin_x`, `margin_y`, `name_size`, `contact_size`: sizes in points. Defaults are `11.5`, `15.5`, `10`, `50`, `42`, `24`, and `10.25` respectively. Override them to honour current user preferences, not merely to force excessive content onto one page.

Dates are explicit to prevent stale examples from silently becoming new letters. Populate the intended date for every new application. A target office belongs in `recipient` or the letter, while the candidate's actual location stays in `contact_lines`.

## Build and validate

```bash
python /path/to/cover-letter/scripts/render_cover_letter.py \
  application.json --output cover_letters/Candidate_Company_REQ-123.pdf
```

Use the actual available Python executable. The helper refuses to overwrite an existing PDF unless `--overwrite` is passed for an intended revision. It builds into a temporary file, verifies text and page boundaries, and publishes only a passing result. It leaves an existing PDF intact on validation failure.

The default is a maximum of one page. Use `--max-pages 2` only for a deliberately longer letter or a temporary diagnostic output, not to bypass an unintended spill. Overflow is an error; the helper does not silently shrink text, truncate paragraphs, or rewrite the letter. Unicode dash variants are rendered as ASCII hyphens; other supplied text is preserved.

Successful output is a compact JSON report containing the final path, page count, extraction checks, and any paragraphs ending in a single isolated word. These warnings guide visual review, not automatic rewriting. Contact wrapping and visual quality still require inspection.

Render the final PDF with an available renderer, for example:

```bash
pdftoppm -r 130 -png cover_letters/Candidate_Company_REQ-123.pdf tmp/pdfs/letter/page
```

Create the preview directory first. Inspect every page, fix any actual defects, rebuild, and inspect again. Keep previews and audit output out of the final deliverables folder. The helper does not establish PDF/UA accessibility or test a live ATS.
