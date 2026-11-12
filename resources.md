# Curated resources for slide-making agents

The "awesome" part of this repo — everything here is used by real deck-making
workflows. PRs welcome with a one-line "why it's good".

## Skills & references

- [anthropics/skills → pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) — the production-grade pptx mechanics skill (pptxgenjs gotchas, OOXML editing, validation). Composes with this skill.
- [anthropics/skills → docx / xlsx / pdf](https://github.com/anthropics/skills) — same family, same quality bar.

## Build tooling

- [pptxgenjs](https://github.com/gitbrent/PptxGenJS) — JS generation library; the gotchas list in the anthropics skill is required reading
- [python-pptx](https://github.com/scanny/python-pptx) — Python generation; cannot duplicate slides, see anthropics skill notes
- [Marp](https://github.com/marp-team/marp) / [Slidev](https://github.com/slidevjs/slidev) — markdown-driven decks; great for tech talks, identical story phase
- [LibreOffice headless](https://help.libreoffice.org/) — `soffice --headless --convert-to pdf` is the standard way to render decks for QA without Office

## Images & icons (license-safe)

- [unDraw](https://undraw.co/) — MIT illustrations, recolorable
- [react-icons](https://github.com/react-icons/react-icons) — icon sets rendered to SVG, rasterize ≥256px before inserting
- [Excalidraw](https://github.com/excalidraw/excalidraw) — hand-drawn diagrams that survive screenshot scaling

## Inspiration / taste

- [assertion-evidence slides](https://www.assertion-evidence.com/) — the title style this skill enforces, from Penn State's Michael Alley
- [Pyramid Principle](https://en.wikipedia.org/wiki/Minto_Pyramid_Principle) — Barbara Minto's answer-first structure (SCQA's parent)
- [Data Ink Ratio](https://infovis-wiki.net/wiki/Data-Ink_Ratio) — Tufte's rule behind every "delete it" in the chart anti-patterns list
