#!/usr/bin/env python3
"""
Build project-highlight assets from the PowerPoint decks in
files/ProjectHighlightsSource/, for display on the /highlights page.

Each source filename must start with a date stamp (YYYY-MM-DD, or
YYYY.MM.DD) -- that date drives the most-recent-first ordering on the
/highlights page.

For each *.pptx in that folder, this script:
  1. Reads the slide title and speaker notes with python-pptx.
  2. Renders the slide to a full-size PDF with LibreOffice (`soffice`).
  3. Rasterizes page 1 of that PDF to a PNG thumbnail with `pdftoppm`.
  4. Writes/updates the corresponding entry in _data/highlights.yml,
     sorted by date, most recent first.

Requirements (macOS): `brew install --cask libreoffice` (gives `soffice`)
and `brew install poppler` (gives `pdftoppm`). Both are checked for below.

Re-running is safe: existing "caption" text in _data/highlights.yml is
never overwritten by this script, since captions are hand-edited to keep
their tone accurate and non-provocative. New decks get a placeholder
caption that starts with "TODO" -- search for that and write a real one
before publishing.

Usage:
    python3 scripts/build_highlights.py
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml
from pptx import Presentation

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "files" / "ProjectHighlightsSource"
OUTPUT_DIR = REPO_ROOT / "files" / "highlights"
DATA_FILE = REPO_ROOT / "_data" / "highlights.yml"

THUMBNAIL_WIDTH = 1100  # px, applied with `sips`

# Preferred slugs + display order for known source files. Anything not
# listed here falls back to an auto-slugified version of the filename
# stem, appended after these, so new decks "just work" without edits.
KNOWN_SLUGS = {
    "2025-06-24-ASCR Highlight PESO-HPSF.pptx": "hpsf",
    "2026-08-04-PESO-DAVTOOLS-highlight.pptx": "dav-tools",
    "2026-08-04-ASCR_Highlight_PESO-UDX.pptx": "udx",
    "2026-08-05-PESO-Spack-Highlight.pptx": "spack",
    "2026-08-06-E4S Highlight - Dont Debug It Alone .pptx": "e4s",
    "2026-08-07-ASCR.Highlight.PESO.ZeroToLAMMPS.pptx": "zero-to-lammps",
}

# Matches a YYYY-MM-DD or YYYY.MM.DD stamp at the start of a filename.
DATE_RE = re.compile(r"^(\d{4})[-.](\d{2})[-.](\d{2})")

PLACEHOLDER_CAPTION = (
    "TODO: write a short, plainly-factual caption for this highlight. "
    "Summarize the talking points from the deck's notes, avoid absolute "
    "claims of credit ('critical', 'essential', 'the only'), and credit "
    "the broader community/consortium rather than PESO alone."
)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def extract_date(filename_stem: str):
    """Return a 'YYYY-MM-DD' string parsed from a filename's leading date
    stamp, or None if the filename doesn't start with one."""
    m = DATE_RE.match(filename_stem)
    if not m:
        return None
    year, month, day = m.groups()
    return f"{year}-{month}-{day}"


def check_tools():
    missing = [t for t in ("soffice", "pdftoppm", "sips") if shutil.which(t) is None]
    if missing:
        sys.exit(
            "Missing required tool(s): "
            + ", ".join(missing)
            + "\nInstall with: brew install --cask libreoffice && brew install poppler"
        )


def extract_slide_title(slide) -> str:
    for shape in slide.shapes:
        if shape.has_text_frame and shape.name and "title" in shape.name.lower():
            text = shape.text_frame.text.strip()
            if text:
                return text
    return ""


def extract_notes(slide) -> str:
    if slide.has_notes_slide:
        return slide.notes_slide.notes_text_frame.text.strip()
    return ""


def convert_to_pdf(pptx_path: Path, out_dir: Path) -> Path:
    subprocess.run(
        [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(out_dir),
            str(pptx_path),
        ],
        check=True,
        capture_output=True,
    )
    pdf_path = out_dir / (pptx_path.stem + ".pdf")
    if not pdf_path.exists():
        sys.exit(f"soffice did not produce expected PDF: {pdf_path}")
    return pdf_path


def render_thumbnail(pdf_path: Path, out_png_no_ext: Path):
    subprocess.run(
        ["pdftoppm", "-png", "-r", "150", "-singlefile", str(pdf_path), str(out_png_no_ext)],
        check=True,
        capture_output=True,
    )
    png_path = out_png_no_ext.with_suffix(".png")
    subprocess.run(
        ["sips", "--resampleWidth", str(THUMBNAIL_WIDTH), str(png_path)],
        check=True,
        capture_output=True,
    )
    return png_path


def load_existing_data():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            entries = yaml.safe_load(f) or []
    else:
        entries = []
    return {e["slug"]: e for e in entries}


def main():
    check_tools()

    if not SOURCE_DIR.is_dir():
        sys.exit(f"Source directory not found: {SOURCE_DIR}")

    pptx_files = sorted(SOURCE_DIR.glob("*.pptx"))
    if not pptx_files:
        sys.exit(f"No .pptx files found in {SOURCE_DIR}")

    existing_by_slug = load_existing_data()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    ordered_slugs = []
    new_or_updated = []
    placeholder_slugs = []

    for pptx_path in pptx_files:
        slug = KNOWN_SLUGS.get(pptx_path.name) or slugify(pptx_path.stem)
        ordered_slugs.append(slug)

        slide_dir = OUTPUT_DIR / slug
        slide_dir.mkdir(parents=True, exist_ok=True)

        prs = Presentation(pptx_path)
        slide = prs.slides[0]
        slide_title = extract_slide_title(slide)
        notes = extract_notes(slide)

        date_str = extract_date(pptx_path.stem)
        if date_str is None:
            print(
                f"WARNING: {pptx_path.name} has no leading date stamp "
                "(expected YYYY-MM-DD-...); it will sort last on the page."
            )

        pdf_path = convert_to_pdf(pptx_path, slide_dir)
        final_pdf = slide_dir / "slide.pdf"
        pdf_path.replace(final_pdf)

        thumb_path = render_thumbnail(final_pdf, slide_dir / "thumbnail")

        existing = existing_by_slug.get(slug, {})
        entry = {
            "slug": slug,
            "source": pptx_path.name,
            # date is always re-derived from the filename, not preserved,
            # since renaming the source file is how you correct it.
            "date": date_str,
            "title": existing.get("title") or slide_title,
            "caption": existing.get("caption") or PLACEHOLDER_CAPTION,
            "notes_excerpt": notes,
            "thumbnail": f"/files/highlights/{slug}/{thumb_path.name}",
            "pdf": f"/files/highlights/{slug}/slide.pdf",
        }
        if entry["caption"] == PLACEHOLDER_CAPTION:
            placeholder_slugs.append(slug)
        existing_by_slug[slug] = entry
        new_or_updated.append(slug)
        print(f"Processed {pptx_path.name} -> {slug}")

    # Preserve entries whose source .pptx no longer exists (in case a
    # deck is temporarily removed). Final order is most-recent-first by
    # date; the highlights.md template also sorts defensively, but
    # sorting here too keeps the generated YAML readable as a changelog.
    all_slugs = ordered_slugs + [s for s in existing_by_slug if s not in ordered_slugs]
    ordered_entries = [existing_by_slug[s] for s in all_slugs]
    ordered_entries.sort(key=lambda e: str(e.get("date") or "0000-00-00"), reverse=True)

    with open(DATA_FILE, "w") as f:
        f.write("# Generated by scripts/build_highlights.py -- do not hand-edit\n")
        f.write("# asset paths, but DO hand-edit the 'title' and 'caption' fields;\n")
        f.write("# they are preserved across re-runs. 'date' comes from each source\n")
        f.write("# filename's leading date stamp; rename the file to change it.\n")
        yaml.dump(
            ordered_entries,
            f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=100,
        )

    print(f"\nWrote {DATA_FILE} with {len(ordered_entries)} entries.")
    if placeholder_slugs:
        print(
            "\nNeeds a real caption before publishing (placeholder found): "
            + ", ".join(placeholder_slugs)
        )


if __name__ == "__main__":
    main()
