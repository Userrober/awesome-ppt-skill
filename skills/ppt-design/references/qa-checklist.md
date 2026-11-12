# QA checklist: review the deck like a distrustful editor

Run AFTER building, before delivering. Export slides to images (LibreOffice
headless renders pptx: `soffice --headless --convert-to pdf deck.pptx`, then
`pdftoppm -png -r 80`), view them, and grade every slide. Fix, re-export,
re-check only the failures.

## A. Argument (deck level)

- [ ] Titles read top-to-bottom as a paragraph that makes the argument
- [ ] Ending slide contains the ask (decision / owner / date)
- [ ] Slide count within the scenario budget (±2)
- [ ] Every claim with a number has its unit, time range, and source line

## B. Slide level (every slide)

- [ ] Title is an assertion (topics get rewritten) — dividers exempt
- [ ] One message: no "and" joining two ideas in the title
- [ ] Body ≤ ~40 words; full sentences live in speaker notes
- [ ] Evidence present: number / chart / screenshot / quote proving the title
- [ ] The 5-second test: what is this slide about? (ask someone, or wait 5s and re-look)

## C. Visual

- [ ] Contrast: all text pairs ≥ 4.5:1 (`scripts/contrast.py fg bg`); accent tested on both slide themes
- [ ] Alignment: headers at identical y across sibling slides; nothing at arbitrary x
- [ ] Margins ≥ 1.0in on all sides; nothing touches the slide edge (full-bleed images exempt)
- [ ] Overflow check per text box — the last line is not clipped (renders, don't trust the editor)
- [ ] One motif repeated; no top color bars, no clip-art, no 3-D charts
- [ ] Chart sanity: sorted bars, axis starts at 0 for bars, legend only when ≥ 2 series, units on the axis

## D. Chinese decks (附加)

- [ ] 中英混排时英文两侧留空格（"提升 40% 的吞吐"）
- [ ] 标点在行首的禁则处理（，。：不可开头）— 工具不处理时手动改写换行
- [ ] 中文正文 ≥ 16pt（投影可读下限），字体用思源黑体/微软雅黑等常见装机字体
- [ ] 数字与单位之间不换行（"40%" 不拆成 "40" + "%"）

## Verdict format (report to the user)

```
QA: 12 slides — 10 pass, 2 issues fixed (slide 4 overflow, slide 9 contrast 3.9→5.2)
Remaining known issue: none / <describe>
```

Do not report "done" without the verdict line.
