# Phase 1C — Codebase Integration Audit (Agent C)

## Floor-cell render code

**File:** `S:\Git\Apocalypse-Express\docs\character-creation.html`
**Function:** `renderEngineFloor` at line 12752

**Loop structure (lines 12829–12835):**
```js
// Render walkable floor on every uncovered cell.
for (let r = 1; r <= L.rows; r++) {
  for (let c = 1; c <= L.cols; c++) {
    const key = `${r},${c}`;
    if (covered.has(key)) continue;
    html += `<div class="carriage-tile is-floor" style="grid-column:${c}; grid-row:${r};" aria-hidden="true"></div>`;
  }
}
grid.innerHTML = html;
```

**Cleanest injection point:** Modify line 12833 to call `buildStainedGlassSvg(r, c)`:
```js
html += `<div class="carriage-tile is-floor" style="grid-column:${c}; grid-row:${r};" aria-hidden="true">${buildStainedGlassSvg(r, c)}</div>`;
```

## Current floor CSS (line 5260)

```css
.carriage-tile.is-floor {
  background:
    linear-gradient(rgba(14, 12, 24, 0.55), rgba(14, 12, 24, 0.55)),
    url('img/textures/floor-stained-glass.png') center / 100% 100% no-repeat;
  border-color: rgba(201,156,90,0.06);
}
.carriage-tile.is-floor::after {
  content: none;
}
```

**Replace background:** drop the PNG url, keep only the dark overlay:
```css
background: linear-gradient(rgba(14, 12, 24, 0.55), rgba(14, 12, 24, 0.55));
```

## Grid container

```css
.carriage-floor {
  display: grid;
  grid-template-columns: repeat(16, minmax(36px, 1fr));
  grid-template-rows: repeat(5, minmax(36px, 1fr));
  gap: 2px;
  aspect-ratio: 16 / 5;
  min-width: 640px;
}
```

Cells fill grid track via flex. No explicit width/height. Min ~36px, expands.

## Existing inline SVG pattern (pulpit-hex at line 12822)

```js
const hexSvg = `<svg class="pulpit-hex" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><polygon class="frame" points="20,3 35,11 35,29 20,37 5,29 5,11"/><text class="code" x="20" y="21" text-anchor="middle" dominant-baseline="middle">${code}</text></svg>`;
```

**Conventions:** `viewBox="0 0 40 40"` (BUT for stained-glass we use 0 0 100 100 since templates are designed at that scale — preserveAspectRatio="none" stretches). `aria-hidden="true"`. CSS vars `var(--gold)` for colors.

## CSS variables in :root (lines 10–39)

`--gold` `#c99c5a` · `--gold2` `#e6cfa1` · `--ember` `#ff7b5c` · `--muted` `#b8b0c6` · `--text` `#f8f5f0` · `--bg` `#0e0c18` · `--void` `#05040a`

## Integration plan

1. **Define `buildStainedGlassSvg(r, c)`** near line 12750 (just before renderEngineFloor)
2. **Modify line 12833** — inject SVG result as innerHTML of the is-floor div
3. **CSS at line 5260** — drop PNG, keep dark overlay
4. **Add new CSS rule** for `.carriage-tile.is-floor > svg` — `width:100%; height:100%; position:absolute; top:0; left:0; pointer-events:none; display:block;`
5. **Carriage tile container** needs `position: relative` for absolute SVG — already has `position: relative` per existing `.carriage-tile` rule. ✅
