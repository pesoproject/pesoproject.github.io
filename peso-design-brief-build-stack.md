# PESO Website Redesign — Design Brief
**Direction: "Build Stack"** (dark, terminal/HPC-native)

Reference mockup: `peso-redesign-A-buildstack.html`

---

## 1. Concept

The site should feel native to the audience it actually serves — people who live in build systems, package managers, and dependency graphs. The visual language borrows directly from that world: terminal panes, changelogs, build pipelines, and a literal software-stack diagram — rather than a generic "government project" template look.

---

## 2. Color tokens

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#0B1220` | Page background |
| `--panel` | `#101B2D` | Card / panel background (one step up from page bg) |
| `--paper` | `#EDEFF2` | Primary text on dark |
| `--signal` | `#5EEAD4` | Primary accent — links, active states, "resolve" states, CTA |
| `--ember` | `#F0A050` | Secondary accent — warnings/highlights, "diagnose" states, DOE energy nod |
| `--line` | `#22314A` | Borders, dividers, hairlines |
| `--muted` | `#8FA0B8` | Secondary/body text, captions |

**Rules:**
- Backgrounds are always dark (`--ink` or `--panel`) — no light sections.
- `--signal` (teal) and `--ember` (amber) are never used together in the same component for the same purpose — teal = affirmative/primary, amber = attention/secondary. Keep them as a two-note system, not decoration.
- Borders are always `--line` at 1px — no heavier borders, no box-shadows for depth (depth comes from `--panel` vs `--ink` contrast only).

---

## 3. Typography

| Role | Typeface | Weight | Notes |
|---|---|---|---|
| Display / headings | IBM Plex Mono | 600 | Used for all `h1`/`h2`, nav brand, section tags — the monospace *is* the personality of the page |
| Body | Inter | 400–500 | Paragraph text, nav links, list items |
| Labels / data / code | IBM Plex Mono | 400–500 | Chips, log dates, thrust codes, terminal headers, buttons |

**Rules:**
- Never substitute a generic sans for headings — the monospace display face is the signature choice and should not be diluted.
- Section eyebrows/tags are always uppercase, IBM Plex Mono, letter-spacing ~0.12em, colored `--signal`.
- Body copy stays in Inter for readability; don't set long paragraphs in mono.

---

## 4. Signature components

These are the reusable patterns that should extend to every new page — not just the homepage.

### Stack diagram
Horizontal layered bands (label column + content column), used to represent any layered/architectural concept. Built for the homepage hero (Applications → Libraries & Tools → E4S/Spack → Hardware), but the same component works for e.g. a "how a thrust fits into the ecosystem" diagram on a thrust detail page.

### Terminal pane / diagnose-resolve pattern
Two-column bordered panel styled like a terminal window, with a `$ command` style header (`term-head` class) and a checklist body. Use for any "problem → solution" or "before → after" content, not just the homepage challenges section.

### Chips
Small pill-style tags (`.chip`) with border + transparent fill, in three states: neutral (`--line` border), highlighted (`--signal` border, for E4S/Spack-tier concepts), and warm (`--ember` border, for hardware/infra-tier concepts). Use for tagging content by category anywhere in the site (e.g. tagging news items by thrust, or resources by tool).

### Pipeline rows
Two-column rows (short code + body) with a bordered acronym/code badge on the left. This is the pattern for the six thrusts, and should extend to any other "parallel workstreams" content (e.g. team/PI listings, working groups).

### Changelog / log rows
Date (mono, muted) + linked title, bottom-bordered rows. This is the pattern for News, and should extend to any chronological content (releases, publications, event archive).

### Connect cards
Three-column bordered cards with a mono eyebrow tag, heading, and one-line description. Reusable for any "pick one of a few paths" content — not just the contact section.

---

## 5. Structural rules

- **No numbered markers (01/02/03)** unless content is a genuine sequence. The six thrusts use acronym codes (SW-INT, UDX, COMM, IMPACT, E4S, SPACK) instead of numbers, because they're parallel, not sequential — preserve this logic on any new page with parallel content.
- **Borders over shadows.** All depth/separation is done with 1px `--line` borders and background-shade steps (`--ink` → `--panel`), never `box-shadow`.
- **Border-radius stays small** — 3px on cards/chips/buttons throughout. Don't introduce larger radii.
- **One animated moment only:** the blinking cursor after the hero headline. Don't add additional motion/animation elsewhere — the restraint is intentional.

---

## 6. Content/IA notes for expansion

Carried over from the initial site audit — worth keeping in mind as new pages get built in this system:
- Current site is a single long homepage plus a `/thrusts` page and standalone news-item pages (e.g. `/cs-pi-2026`). Some "Latest News" items are already stale — a real publish/archive workflow would help.
- No dedicated team/people page exists yet, despite named PIs (Michael Heroux, Lois Curfman McInnes) and thrust leads (e.g. Sameer Shende for E4S, Johanna Cohoon for UDX) being relevant to visitors.
- Consider whether each of the six thrusts eventually gets its own detail page using the stack-diagram and terminal-pane components above, rather than staying homepage-only.

---

## 7. Assets referenced

- Logo: `https://pesoproject.org/images/peso-logo-no-bg.png` (inverted to white via CSS filter on dark backgrounds)
- DOE sponsor mark: `https://pesoproject.org/images/doe-logo.png`
- Fonts: IBM Plex Mono, Inter — both loaded via Google Fonts in the reference mockup
