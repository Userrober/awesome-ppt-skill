---
name: ppt-design
description: "Use this skill when planning, structuring, or reviewing any slide deck or presentation — before and after building .pptx files. Covers turning raw material into a storyline (SCQA / pyramid principle), writing assertion-style slide titles, budgeting slide counts per scenario (weekly reports, tech talks, pitch decks, project reviews, course lectures), choosing charts that match the message, designing with a spacing/typography/contrast system (including CJK decks), and running a reviewer-style QA pass. Trigger whenever the user mentions PPT, slides, deck, 汇报, 幻灯片, 路演, 答辩, or asks to make a presentation — even before any file is created. Pairs with any pptx tooling (python-pptx, pptxgenjs, office plugins); this skill decides WHAT to say and HOW it should look, not how to write the XML."
---

# PPT Design: story first, slides second

Most machine-made decks fail at **deciding**, not at writing XML: ten bullets where
one assertion belongs, a pie chart for a trend, walls of text at 14pt. This skill
makes you operate like a designer + consultant: plan the story, storyboard the
slides, build with whatever pptx tooling is available, then review like a
distrustful editor.

Load the reference you need, when you need it — do not read everything upfront:

| Phase | Read | Purpose |
|---|---|---|
| 1. Story | `references/storytelling.md` | raw material → storyline, slide budget, what to cut |
| 2. Storyboard | `references/playbooks.md` | scenario skeletons (weekly report / tech talk / pitch / review / lecture); `references/chart-choices.md` when data slides appear; `references/cjk-decks.md` for Chinese decks |
| 3. Build | your pptx tooling | mechanical work is NOT this skill's job — see "Composing with tooling" below |
| 4. Review | `references/qa-checklist.md` | reviewer pass before anyone sees it |

Design decisions (spacing, type scale, color, motif) live in
`references/design-system.md` — read it once per deck before storyboarding.

## The four phases

### Phase 1 — Story (no slides allowed yet)

From the user's raw material, answer three questions **in writing** before
touching any tool:

1. **Who is the audience and what do they must believe/decide when it ends?**
   One sentence. If you cannot write it, ask the user — do not guess on
   decisions-only decks.
2. **What is the one-line message?** Write it as a full assertion sentence
   ("Q4 确认转入增长：营收 +18%，但获客成本恶化需要决策"), not a topic ("Q4 回顾").
3. **What is the slide budget?** Count against the scenario skeleton in
   `references/playbooks.md`. A 10-minute weekly report is 6–8 slides, not 20.
   List the slides as titles first — every title an assertion the audience can
   disagree with. **Cut every slide whose title is not an assertion or a
   deliberate divider.**

Deliverable of Phase 1: an ordered list of slide titles (the "storyboard wire")
plus per-slide notes on evidence needed. Show it to the user for decks where
the stakes are high (pitch, review, 答辩) — 30 seconds of confirmation saves a
rebuild.

### Phase 2 — Storyboard

For each title, pick the **body layout** and the **evidence type** from the
playbook for the scenario. Rules that override habit:

- **One message per slide.** If a slide needs "and", it is two slides.
- **Evidence before prose**: a number, a chart, a screenshot, a quote — the
  title claims it, the body proves it. If you cannot find evidence, the slide
  is an opinion; mark it for the user to source.
- Data slides: choose the chart from `references/chart-choices.md` by the
  *message*, not by what the data looks like. If the only honest chart is a
  table, use a table.

### Phase 3 — Build

Use the pptx tooling the environment offers (python-pptx, pptxgenjs, office
plugins, or editing OOXML directly). This skill does not duplicate those
mechanics; the canonical reference implementation is
[anthropics/skills → pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) —
read its gotchas when you use pptxgenjs or edit OOXML by hand.

Apply `references/design-system.md` while building: spacing scale, type scale,
one motif, palette with contrast checked (`scripts/contrast.py fg bg` returns
the WCAG ratio — body text needs ≥ 4.5:1, large text ≥ 3:1).

### Phase 4 — Review

Run `references/qa-checklist.md` as a reviewer, not an author: open the deck
(most tooling can export slides to images; LibreOffice renders pptx headless)
and grade every slide against the checklist. Fix, re-export, re-check the
failures only. Report the deck with the checklist verdicts, not "done".

## Composing with tooling

This skill is deliberately tool-agnostic and stacks cleanly:

- **anthropics/skills pptx** for build/edit mechanics + validation
- **python-pptx / pptxgenjs** for scripted generation
- **office plugins (e.g. Qoder/Claude office connectors)** for interactive build
- **Marp / Slidev** when the user prefers markdown-driven decks — the story
  phases are identical; only Phase 3 changes

## Anti-patterns (instant rewrite)

- Title is a topic ("市场分析") instead of an assertion ("下沉市场贡献了全部增量")
- Slide has 5+ bullets that are full sentences — split or summarize to keywords
- A pie chart with 8 slices, or any chart whose takeaway needs a paragraph
- Decorative gradient/clip-art that adds no meaning
- Deck ends without an ask: decision needed / next steps / owner + date
