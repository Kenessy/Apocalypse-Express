# Engine Carriage A/B Install Update — Implementation Report

**File:** `docs/character-creation.html`
**Date:** 2026-05-01

---

## What was built

### Task 1 — ENGINE_LAYOUT data updated
The 3 install slots in `const ENGINE_LAYOUT` now carry full A/B option data:
- `install-small-a` (col 14, row 2) — **Maintenance** axis: Toolkit & Boiler Kit (A) / Engineer's Manual (B)
- `install-small-b` (col 11, row 5) — **Life** axis: Reinforced Bookshelf (A) / Tabletop Game Set (B)
- `install-big` (col 13, row 4) — **Work** axis: Co-Pilot Cradle (A) / Fold-Down Bunk (B)

Each slot adds: `axis`, `selected: 'a'`, and `options: { a: {…}, b: {…} }` with `name`, `icon`, `effect`, `flavor`, `acquisition` per option.

### Task 2 — renderEngineFloor() updated
The renderer now branches on `s.options`: install slots with A/B data render a `has-ab` tile containing an `.engine-axis-label` eyebrow and an `.engine-slot-ab` two-column grid of `.engine-slot-option` sub-cards. Selected option gets class `is-selected`, the other `is-unselected`. Each sub-card shows icon, name, effect, and an A/B badge. Driver post and non-option slots use the original renderer unchanged. The legend renderer was also updated to show the selected option's details plus a dimmed Alt B line.

### Task 3 — Acquisition Atlas section added
A new `<section class="carriage-section acquisition-atlas">` appears immediately after the engine floor plan section, inside `.carriage-altarpiece`. Contains:
- `.cadence-section-header` with cath-eyebrow, h3 "Where to find them", and a setup sub-paragraph
- `.acquisition-grid` (2-col, 1-col mobile) with 6 `.acquisition-card` elements — one per install option
- Each card: icon + name header, axis label, 5 `.efr-row` rows (Bought / Salvaged / Faction / Crafted / Story) using the established `.efr-key`/`.efr-val` pattern

### Task 4 — CSS additions (~130 lines)
Added immediately before the `/* FOOTER */` block:
- `.carriage-tile.is-slot.has-ab` — flex-column override for AB tiles
- `.engine-axis-label` — gold eyebrow text above the pair
- `.engine-slot-ab` — 2-column sub-card grid
- `.engine-slot-option` — base card (border, bg, hover transition)
- `.engine-slot-option.is-selected` — gold border + radial glow
- `.engine-slot-option.is-unselected` — dashed border + opacity 0.45
- `.engine-slot-option .badge` — corner A/B tag
- `.slot-opt-icon`, `.slot-opt-name`, `.slot-opt-effect` — icon/name/effect typography
- `.acquisition-atlas`, `.acquisition-grid`, `.acquisition-card`, `.acquisition-card-header`, `.acq-icon`, `.acq-name`, `.acq-axis`, `.acq-rows` — Atlas section layout
- `.acquisition-card .efr-row / .efr-key / .efr-val` — scoped row grid matching engine-fuel-rules pattern
- Responsive breakpoint: `@media (max-width: 680px)` collapses Atlas to 1-col

No new color tokens or font families introduced. All values use existing variables.

---

## Verification output
```
Length: 546495
Has Co-Pilot Cradle: true
Has Acquisition Atlas: true
Has Tabletop: true
Has ENGINE_LAYOUT options: true
Has engine-slot-ab CSS: true
Has acquisition-card CSS: true
Has is-selected CSS: true
Has axis Work: true
Has axis Maintenance: true
Has axis Life: true
```

**File size delta:** +17,087 bytes (517 KB → ~534 KB)

---

## Deviations from spec

- `install-small-a` is the **Maintenance** slot and `install-small-b` is the **Life** slot. The spec listed Small Slot 1 as Maintenance and Small Slot 2 as Life, which maps to the existing `install-small-a` / `install-small-b` IDs respectively — consistent.
- The legend renderer shows selected option info inline; the spec did not define legend behavior for A/B slots, so a minimal "selected A / Alt B" pattern was used.
- `slot-opt-name` uses 7px Cinzel (not 13px) inside the small floor-plan tiles to avoid overflow — the 13px spec size is appropriate for the Acquisition Atlas card headers (`acq-name`) where it is applied.

---

## Open issues for QA

1. **No interactive toggle yet.** The `selected: 'a'` field is in the data but clicking an option does not swap selection — deferred to v2 per spec.
2. **Big slot proportions** — the 2×2 tile is visually larger than the 1×1 small slots; the 2-column sub-card layout may feel cramped at lower zoom levels. QA should verify at 80% and 100% browser zoom.
3. **`install-small-b` position** (col 11, row 5) puts it at the bottom-left of the living area — may overlap with floor cells depending on how the grid renders. Confirm visually in browser.
4. **Emoji rendering** — `♟` (chess piece, U+265F) renders differently across OS/browser; QA to confirm it reads clearly at tile scale.
