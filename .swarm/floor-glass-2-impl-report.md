# Phase 2 Implementation Report — Procedural Stained-Glass Floor

_Agent: Implementation Agent (Phase 2). Date: 2026-05-01._

---

## What was added

**JS constants (inserted before `renderEngineFloor`):**
- `SHARD_TEMPLATES` — 4-element array (pinwheel / fold / fan / split) with exact polygon points and leading paths verbatim from 1A spec.
- `COLOR_SCHEMES` — 4-element array (cool / warm / mixed / dim) with exact hex colors and per-scheme opacities from 1B spec.
- `BACKLIGHT_STOPS` / `BACKLIGHT_STOPS_DIM` — string constants for the standard and dim-scheme radial gradient stops from 1B spec.
- `_shardHighlight(pts)` — helper that computes the 1–2 topmost edges of a polygon and emits `<polyline>` inner highlights (stroke `#f8f5f0`, width 0.6, opacity 0.28) as specified by 1B.
- `buildStainedGlassSvg(r, c)` — deterministic SVG builder. Seed = `r*31 + c*17`; template = `seed % 4`; color scheme = `(seed >> 2) % 4`. Focal point offset ±8% via seed per 1B optional-variation suggestion.

**JS render change:** `renderEngineFloor` floor-tile line now injects `${buildStainedGlassSvg(r, c)}` as div content.

**CSS changes** (replacing the old `::after` dot decoration rule):
- `.carriage-tile.is-floor` — added `overflow: hidden`, `border-color: rgba(201,156,90,0.06)`.
- `.carriage-tile.is-floor > svg.floor-glass` — `position: absolute; inset: 0; width/height: 100%; pointer-events: none; display: block`.
- `.carriage-tile.is-floor::before` — dark overlay `linear-gradient(rgba(14,12,24,0.55),…)` with `z-index: 1`, sitting on top of SVG.
- `.carriage-tile.is-floor::after` — reset to `content: none`.

---

## File size delta

Original: 448,973 bytes → Final: 455,013 bytes (+6,040 bytes / +1.3%)

---

## Verification output

```
size: 455013
has buildStainedGlassSvg: true
has SHARD_TEMPLATES:       true
has COLOR_SCHEMES:         true
has BACKLIGHT_STOPS:       true
floor PNG removed:         true
floor-glass class:         true
JS eval OK — SVG, radialGradient, polygon, var(--gold), polyline all present
3 sampled cells:           [ 'ok', 'ok', 'ok' ]
```

---

## Deviations from spec

1. **No template-literal backtick strings in BACKLIGHT_STOPS** — the 1B spec used template literals; the constants are plain string concatenation to avoid truncation issues with the file-write toolchain. Runtime behavior is identical.
2. **CSS anchor differs from audit** — the 1C audit referenced `line 5260` with an existing `is-floor { background: …png… }` block that was absent in the actual committed file. The existing `::after` dot rule was replaced instead. The net CSS result matches the spec's intent.
3. **`--` comments in gradient notes replaced with `-` in JS** — to avoid inadvertent `-->` HTML-comment closure in the inline `<script>` block.

---

## Open issues for QA

- **`z-index` stacking with slot tile children:** The `::before` overlay uses `z-index: 1` within `.carriage-tile`. If any slot-tile child content (hex SVG, text spans) has no explicit z-index, the overlay on floor tiles should not affect them — but confirm in-browser that the Pulpit hex and slot tile text render above floor overlays.
- **Gradient ID uniqueness:** Each SVG uses `id="bg-{r}-{c}"`. If `renderEngineFloor` is ever called multiple times (e.g., re-render), duplicate IDs are possible within the page. Low risk given current single-render pattern.
- **`preserveAspectRatio="none"` stretch:** At non-square cell aspect ratios (16:5 grid), polygons will stretch. This is intentional (matches the 1A viewBox design) but visually confirm on narrow-viewport breakpoints.
