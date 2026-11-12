# Design system: the decisions that make a deck look designed

Slide dimensions 16:9 → 13.33in × 7.5in (12192000 × 6858000 EMU). All spacing
below assumes this canvas; scale proportionally for 4:3.

## Spacing: pick a unit and multiply

Base unit **u = 0.25in** (240000 EMU). Every gap is a multiple:

| Token | Value | Use |
|---|---|---|
| u ×1 | 0.25in | text line gap, icon-to-label |
| u ×2 | 0.5in | title→body, card inner padding |
| u ×3 | 0.75in | column gutters |
| u ×4 | 1.0in | slide margins (all four sides, never less) |

Grid: 12 columns inside the margins; content blocks snap to column edges.
Nothing floats at an arbitrary x — if two slides place a header at different
heights, the deck reads as unmade.

## Type scale (one scale per deck, Arial/Calibri-safe list for body)

| Role | Size | Weight | Notes |
|---|---|---|---|
| Slide title | 28–32pt | bold | assertion sentence, ≤ 2 lines |
| Section header | 20pt | bold | |
| Body | 16–18pt | regular | never below 14pt on a projected deck |
| Caption / source | 10–12pt | regular | grey, bottom edge |
| Hero number | 60–72pt | bold | one per slide, max |

Line spacing 1.15–1.3. Titles never wrap mid-phrase — break at the punctuation.

## Color: the 60/30/10 contract

- **60%** dominant (usually background) · **30%** secondary (text) · **10%**
  accent (one saturated color, only on the thing that matters)
- Semantic pairs: use the accent for "the answer", never for decoration AND
  meaning at the same time
- Palette sources: topic-informed, not default blue. Check every
  text/background pair with `scripts/contrast.py fg bg` — **≥ 4.5:1 body,
  ≥ 3:1 large text**. Test the accent on both light and dark slides.
- Dark background slides: drop pure white text to `F2F4F8` (pure white on dark
  vibrates), and lighten body grey by one step.

## Motif

Pick ONE repeatable visual device and use it on every slide: same-corner
kicker label, same icon-circle treatment, same card corner radius. The motif
is what makes six different slides feel like one deck. Retire the classic
"top color bar" — it is decoration, not a motif.

## Motion (if the tooling supports it)

One entrance rule per deck (e.g., fade for everything). Animation is for
revealing sequence (build a list point by point), never for entertainment.
Bullet-by-bullet builds only when the bullet count > 4.

## Density governor

Max ~40 words visible per content slide. More than that and the audience
reads instead of listening — move prose to speaker notes (that is what notes
are for) and keep 5–8 keywords on the slide.
