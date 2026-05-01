# Phase 1B — Color Schemes + Backlight Glow

_Designed by Agent B, 2026-05-01. For the procedural stained-glass floor system on the character-creation page. All colors drawn from or derived from the AE canonical palette. Cells receive a CSS dark overlay (linear-gradient rgba(14,12,24,0.55)) on top of the SVG — colors are specified BEFORE that overlay is applied._

---

## Color Schemes

### Scheme 1: Cool
- **Vibe:** Deep midnight cathedral. Blue dominates, purple frames, slate anchors the shadows. The feel of moonlight through ancient church glass — cold, ecclesiastical, still. This is the floor's default "presence" scheme: unmistakably stained glass without competing with the content above it.
- **Colors:** `['#1d3370', '#2a4a8c', '#3a1a4d', '#4d2470', '#2a2128']`
  - #1d3370 — deep navy (anchor shard; takes backlight well, reads blue-black at small size)
  - #2a4a8c — mid blue (primary lit shard; the most visible color at small size)
  - #3a1a4d — deep violet (shadow shard; low-luminance, reads as "depth")
  - #4d2470 — purple-violet (the color that absorbs the most backlight glow; reads violet under gold light)
  - #2a2128 — dark slate (leading-adjacent shard; almost neutral, makes the blues pop)
- **Per-shard opacity:** 0.76
- **Notes:** The backlight gold-to-orange reads through the blue shards as a pale greenish-gold — a beautiful side effect. Do NOT use more than one #2a2128 shard per cell or it kills the glass effect. Pair this scheme with cells that have 4-5 shards for maximum depth.

---

### Scheme 2: Warm
- **Vibe:** Hellfire-adjacent sunset. Blue provides contrast foundation; amber and ember shards do the heavy lifting. At small cell size the amber shard catches the backlight and reads like an ember coal. The rust inclusion prevents it from reading "tropical" — this is infernal warmth, not warm-Mediterranean. Use near character-stat zones where a little fire energy is appropriate.
- **Colors:** `['#1d3370', '#5a2810', '#8c4818', '#b54a32', '#2a2128']`
  - #1d3370 — deep navy (the contrast anchor; the warm shards need a dark cool foil)
  - #5a2810 — dark amber (shadow-ember; barely reads at cell-size but feeds into the backlight glow)
  - #8c4818 — mid amber (the primary "fire" shard; catches backlight best of the set)
  - #b54a32 — rust (--rust from palette; the brightest shard in this scheme — use sparingly, max 1 per cell)
  - #2a2128 — dark slate (same anchor role as Scheme 1 — keeps the cell from reading orange-dominant)
- **Per-shard opacity:** 0.72
- **Notes:** Lower opacity than Scheme 1 because the amber/rust shards are higher-luminance and would overpower the leading lines at 0.76+. The dark overlay CSS will bring these back to appropriate floor-level. Avoid placing this scheme in adjacent cells — alternate with Scheme 1 or 4 to prevent the floor from reading as "fire zone" overall.

---

### Scheme 3: Mixed
- **Vibe:** Tertiary richness — purple crosses into teal, amber provides a single warm note. Less saturated than Scheme 2, less cold than Scheme 1. This is the "complexity" scheme: a cell with Mixed glass reads as the most "decorated," as if the window-maker used leftover off-cuts from several other windows. Appropriate in zones with dense game-mechanical content where the floor should feel "rich" but not compete.
- **Colors:** `['#3a1a4d', '#1a4040', '#2a6060', '#5a2810', '#b8b0c6']`
  - #3a1a4d — deep purple (anchor shard; provides the cold-warm bridge)
  - #1a4040 — dark teal (shadow-teal; absorbs backlight as a cool green-gold)
  - #2a6060 — mid teal (the only relatively "bright" shard in this scheme; reads as sea-glass under backlight)
  - #5a2810 — dark amber (single warm note; stops the cell from reading all-cold)
  - #b8b0c6 — lavender-grey (--muted from palette; highly unusual as a shard color — at 0.70 opacity over the backlight it reads as frosted glass, a distinct texture break)
- **Per-shard opacity:** 0.70
- **Notes:** The #b8b0c6 shard is the signature move of this scheme — it reads as translucent "clear" glass against the colored shards. Keep it to 1 shard per cell maximum. Do not let the procedural generator place it adjacent to a leading line on the same edge as a teal shard or the two will merge visually. This scheme works best with 3-4 shards, not 5 — the frosted shard needs open leading-line "breathing room."

---

### Scheme 4: Dim
- **Vibe:** Full recession. This is the safety-net scheme: near-neutral slate and near-black purples that will barely read as "glass" after the dark overlay is applied. The backlight glow gives them just enough translucency to confirm they are stained glass, but they vanish under any busy content above. Deploy this aggressively near slot tiles, stat grids, or any zone where floor decoration would fight the interactive UI.
- **Colors:** `['#2a2128', '#3a2d3c', '#1d3370', '#3a1a4d', '#2a1a14']`
  - #2a2128 — dark slate (the dominant shard; very near-black)
  - #3a2d3c — deep slate-purple (slightly warmer than the above; barely distinguishable at cell size but adds subtle texture)
  - #1d3370 — deep navy (the single "color" in the scheme; at 0.68 opacity it will barely read as blue)
  - #3a1a4d — deep violet (provides depth gradient at the shard border with the navy)
  - #2a1a14 — near-black amber-brown (keeps the scheme from reading "just black" — gives the cell floor some material warmth when backlit)
- **Per-shard opacity:** 0.68
- **Notes:** At this opacity, after the dark overlay CSS, these cells will be nearly invisible. That is intentional. The backlight gradient is STILL required — without it the cell reads as a flat dark rectangle rather than glass. If the procedural generator assigns Scheme 4 to a cell, reduce backlight center opacity from the standard 0.55 to 0.45 for consistency with the recessive intent.

---

## Backlight Gradient

The backlight is a `<radialGradient>` that sits BEHIND all shards. Its function is to simulate a warm cathedral sun source, making the translucent shards glow from within. Without it, colored polygons at 0.68–0.76 opacity look like translucent film, not glass.

**Standard gradient (Schemes 1–3):**

```svg
<radialGradient id="backlight" cx="50%" cy="45%" r="68%" fx="50%" fy="38%">
  <stop offset="0%"   stop-color="#ffe8a8" stop-opacity="0.55"/>
  <stop offset="30%"  stop-color="#ffc060" stop-opacity="0.30"/>
  <stop offset="65%"  stop-color="#c97820" stop-opacity="0.10"/>
  <stop offset="100%" stop-color="#8c4808" stop-opacity="0"/>
</radialGradient>
```

**Dim gradient (Scheme 4 only — reduce center opacity):**

```svg
<radialGradient id="backlight-dim" cx="50%" cy="45%" r="68%" fx="50%" fy="38%">
  <stop offset="0%"   stop-color="#ffe8a8" stop-opacity="0.42"/>
  <stop offset="30%"  stop-color="#ffc060" stop-opacity="0.18"/>
  <stop offset="65%"  stop-color="#c97820" stop-opacity="0.06"/>
  <stop offset="100%" stop-color="#8c4808" stop-opacity="0"/>
</radialGradient>
```

**Gradient design rationale:**
- `cy="45%"` and `fy="38%"` offsets the focal point slightly above center, simulating a sun source above the "floor horizon." This makes the top portion of each cell brighter, which reads naturally as "light from above."
- Four stops rather than three: the intermediate `#ffc060` at 30% is the key stop that gives the warm orange ring before the fade to transparency. Without it the glow is too uniform (looks like a lamp shade, not sunlight).
- `#ffe8a8` at center is warm near-white gold — not pure white (too cold), not `--gold` (#c99c5a, too saturated). This specific tone is the "sunlight through amber glass" color: slightly desaturated warm yellow-white.
- Outer stop color `#8c4808` allows the gradient to fade toward a dark amber-brown at opacity 0 — if any rendering engine interpolates toward the stop color even at zero opacity (premultiplied alpha), it will fade toward warm brown rather than toward grey, which keeps the cell edges warm-tinted.

**Procedural variation (optional, for Agent C):** Offset `cx` and `cy` by ±8% via the seed to create subtle variation in which corner of each cell is "brightest." All four stops and opacities remain fixed — only the center position shifts. This prevents the floor from having a perfectly uniform grid of centered glows, which would look mechanical.

---

## Leading Style

The gold leading lines are the structural skeleton of the stained-glass illusion. They must be the strongest visual element in each cell — more opaque than any shard, heavier than the shard borders.

- **Stroke color:** `var(--gold)` / `#c99c5a`
- **Stroke width:** `1.6` (on a 100×100 viewBox — thinner than this and they disappear at floor cell size; thicker and they dominate the shards)
- **Stroke opacity:** `0.90`
- **Stroke-linecap:** `round` — the round cap softens the shard-tip intersections and reads more like cast metal leading than laser-cut lines
- **Stroke-linejoin:** `round` — required alongside linecap for consistent intersections
- **Optional drop-shadow filter:**
  ```svg
  <filter id="lead-shadow" x="-20%" y="-20%" width="140%" height="140%">
    <feDropShadow dx="0" dy="0" stdDeviation="0.8" flood-color="#000000" flood-opacity="0.55"/>
  </filter>
  ```
  Apply as `filter="url(#lead-shadow)"` on all leading `<line>` or `<polyline>` elements. The 0.8px spread shadow behind the gold lines creates a micro 3D "the metal is slightly raised" effect. At small cell sizes this reads as richness rather than individual shadows. This is RECOMMENDED — it costs one SVG `<filter>` definition per SVG file and meaningfully elevates the visual quality.

- **Gold fill for shard-intersection nodes (optional):** Where 3+ leading lines meet (a typical shard corner), place a `<circle r="1.2" fill="#c99c5a" opacity="0.85"/>` at the intersection point. These small nodes suggest the lead came or solder joint where real leading lines would be physically joined. Agent C's procedural generator can emit these automatically at each polygon vertex that is shared by 2+ shards.

---

## Inner-Shard Highlights

**Decision: YES — include, with constraints.**

A single thin highlight line at the "top" edge of each shard (the edge with the highest Y-coordinate centroid from the gradient source) simulates light catching the inner curve of the glass. This is the detail that separates "colored polygons on a gradient" from "actual glass."

**Spec:**
- A `<polyline>` or `<line>` tracing only the topmost 1–2 edges of each shard polygon (the edges nearest the backlight focal point at cy=38%)
- `stroke="#f8f5f0"` (--text, warm near-white rather than pure white)
- `stroke-width="0.6"` (thin — half the leading width)
- `stroke-opacity="0.28"`
- `fill="none"`
- No filter applied to the highlight (adding shadow to a highlight is contradictory)

**Implementation note for Agent C:** "Topmost edges" means the shard polygon edges whose midpoint Y-coordinate is below (closer to) the gradient focal point at `fy="38%"`. For a 100×100 viewBox, sort the polygon's edge midpoints by Y value ascending (lower Y = higher in the viewport = closer to the light source) and take the top 1–2 edges. Emit the highlight polyline only for those edges.

**Complexity assessment:** One additional `<polyline>` per shard. At 2-5 shards per cell this is 2-5 extra elements. Acceptable. The visual payoff at even 80px cell size is noticeable — the highlights break the flat "colored filter" appearance and confirm the material is glass with interior dimensionality.

---

## Mental Render Check

**Scheme 1 (Cool) at ~80px cell:**
The cell reads as a deep blue-violet mosaic with a pale gold glow at the center-top. The backlight makes the #2a4a8c shard read as bright cobalt blue at its top edge, fading to near-navy at the bottom. The #4d2470 shard reads as deep purple with a hint of violet warmth where it overlaps the glow. Leading lines in gold #c99c5a read strongly against the dark shards — they are the visual "frame" that makes it read as glass rather than a dark blob. Inner highlights add faint white edge gleam. After the CSS dark overlay, this cell is unmistakably "midnight cathedral floor" — present but not competing.

**Scheme 2 (Warm) at ~80px cell:**
The #8c4818 amber shard centered on the backlight focal point reads as a glowing coal or ember — the gold backlight and amber shard color compound into a warm orange-gold that is the dominant impression. The deep navy anchor shard reads as a dark foil that makes the amber pop. The #b54a32 rust shard if present reads as deep red. The cell has a "hellfire window" energy at full opacity; after the dark overlay it reads as a dimly glowing infernal-warm tile. Strong contrast with adjacent Cool cells.

**Scheme 3 (Mixed) at ~80px cell:**
The teal shards catch the gold backlight and read as sea-glass or verdigris — a cool grey-green that is distinctly different from either blue or warm amber. The #b8b0c6 frosted shard is the visual interest point: at 0.70 opacity over the gold backlight it reads as slightly luminous milky glass, a texture break. The amber shard provides a single warm-node that stops the cell reading "cold teal." This is the most "artisanal stained glass" of the four schemes — looks hand-assembled rather than patterned. Complex and rich without being loud.

**Scheme 4 (Dim) at ~80px cell:**
The cell reads as deep dark glass with the faintest internal warmth. At a glance it could be mistaken for a plain dark tile — but the backlight (even at the reduced 0.42 opacity) creates a subtle center-warm edge-dark gradient that confirms it is glass. The leading lines in gold are the most visible element in this cell — they stand out against the near-black shards more starkly than in the other schemes. After the dark overlay this cell is near-invisible content. Pure floor, zero competition with anything above it.

---

_Output file: floor-glass-1b-colors.md — Agent B color specification_
