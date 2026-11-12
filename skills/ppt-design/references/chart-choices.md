# Chart choices: match the chart to the message, not the data

## Message → chart mapping

| The slide claims... | Chart | Notes |
|---|---|---|
| A comparison across categories | horizontal bar | sort by value, never alphabetical by accident |
| A trend over time | line | ≥ 3 points; annotate the event that caused the inflection |
| Composition of one whole, ≤ 5 parts | stacked bar (single) or pie | pie needs ≥ 2:1 dominance to be readable |
| Composition of a whole over time | stacked area / 100% bar | label the ends, not a legend far away |
| Distribution | histogram / box | state n and bin width |
| Relationship of two variables | scatter | annotate the outliers; a trendline needs R² stated |
| Flow / conversion between stages | funnel / Sankey image | Sankey has no native chart — export as image |
| One hero number | big stat callout, no chart | 60–72pt number, 12pt context line |

## Before any chart, three questions

1. What is the sentence the audience should say after seeing it? The chart
   exists to earn that sentence.
2. Is a chart even needed — would a 40pt number beat it?
3. Can the table say it more honestly? (Exact values audited later → table.)

## Anti-patterns (rewrite on sight)

- Pie with > 5 slices or slices within 2% of each other — humans can't compare angles
- Dual y-axes on unrelated units — the classic way to fake a correlation
- 3-D, exploded, or shadowed charts — every added dimension costs honesty
- Legend for a single series — label the line directly instead
- Truncated y-axis on a bar chart (bars encode length!) — line charts may
  truncate; bar charts must start at 0
- Rainbow palettes — encode order with a single hue ramp instead
- The chart that took 30 minutes to make but supports one bullet of the story —
  if the claim is minor, the chart is a backup slide

## Number formatting in slides

- Round to the precision the decision needs (19.3% not 19.307%)
- One comparison anchor per chart: "vs 上季度" or "vs 目标" — pick one
- State the denominator on every percentage; 环比/同比 label explicitly
