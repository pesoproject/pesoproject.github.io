# Project Highlights pipeline

Turns the PowerPoint decks in `files/ProjectHighlightsSource/` into the
thumbnails, PDFs, and data that back the [`/highlights`](../highlights.md)
page.

## Adding a new highlight slide

1. Drop the `.pptx` into `files/ProjectHighlightsSource/`. It should be a
   single slide whose speaker notes hold the talking points -- that's what
   this pipeline expects (only slide 1 of each file is processed).
2. Run:
   ```
   python3 scripts/build_highlights.py
   ```
   This renders a thumbnail (`files/highlights/<slug>/thumbnail.png`) and a
   full-size PDF (`files/highlights/<slug>/slide.pdf`), and adds/updates a
   matching entry in `_data/highlights.yml`.
3. Open `_data/highlights.yml`, find the new entry (its `caption` starts
   with `TODO:`), and write a short, plainly-factual caption. Keep the tone
   even-handed -- this is public-facing text, and the talking points in
   PowerPoint speaker notes are written for a live audience, not a general
   web audience. In particular:
   - Avoid absolute claims of credit ("critical," "essential," "the only").
   - Credit the broader community/consortium (CASS, HPSF, the Spack/E4S
     communities, etc.) rather than framing outcomes as PESO's alone.
   - Keep specific numbers (benchmarks, growth stats) but caveat one-off
     measurements (e.g., "in one test on a laptop...") rather than stating
     them as general guarantees.
4. Commit the `.pptx`, the new `files/highlights/<slug>/` folder, and the
   updated `_data/highlights.yml`.

Re-running the script is always safe: it regenerates thumbnails/PDFs from
the source decks but never overwrites a `title` or `caption` that's already
been hand-edited, so you can re-run it after touching up a slide's artwork
without losing caption edits.

## One-time setup (macOS)

```
brew install --cask libreoffice   # gives `soffice`, used for .pptx -> PDF
brew install poppler              # gives `pdftoppm`, used for PDF -> PNG
pip3 install python-pptx pyyaml
```

`sips` (thumbnail resizing) ships with macOS already.
