# Locomotive Redesign — Implementation Report

## Layout Positions Verified

New 5×16 grid coordinates applied exactly per spec:

| Element | col | row | span_col | span_row |
|---|---|---|---|---|
| Hellfire Boiler | 1 | 1 | 7 | 5 |
| The Pulpit | 8 | 2 | 1 | 1 |
| The Apse | 11 | 2 | 2 | 2 |
| The Tinker Wall | 14 | 3 | 1 | 1 |
| The Crew Niche | 13 | 5 | 1 | 1 |
| The Reliquary | 15 | 1 | 2 | 2 |

## All 7 Names Applied

- Carriage heading: "The Locomotive" (h3, aria-label, section sub-text, JS comment)
- Hellfire Boiler: block `label` field + JS comment
- The Pulpit: slot `name` field, JS comment, task text
- The Apse: slot `name` field (big install, Work axis)
- The Tinker Wall: slot `name` field (small install, Maintenance axis)
- The Crew Niche: slot `name` field (small install, Life axis)
- The Reliquary: block `label` field, info panel heading, two inline fuel-rule references, Cab Floor referenced only in section sub-text description

## Pulpit Hexagonal Styling

`shape: 'hex'` flag in slot data → renderer appends `is-pulpit` class. CSS rule:
`.carriage-tile.is-slot.is-pulpit { clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); }`

Additionally: `.engine-tile-name` renders Cinzel 9px gold2 name label inside the tile.

## Reliquary Dual-Function Info Panel

Added `reliquary-panel` secondary block beneath the main fuel-rules table. Contains:
- ACTIVE CHAMBER row: 1 PLUG actively burning, burns at journey rate
- PLUG STORAGE row: 3 extra canisters (TNY weight), mid-journey swap mechanic (1 phase action)
- AESTHETIC row: full brass-and-leaded-glass flavor text
`subStructure: { active: 1, storage: 3 }` in block data; renderer injects "1 active + 3 storage" sub-label on the tile.

## Acquisition Atlas Titles Updated

All 6 cards updated with slot parentheticals:
- Co-Pilot Cradle (Apse · A), Fold-Down Bunk (Apse · B)
- Toolkit & Boiler Kit (Tinker Wall · A), Engineer's Manual (Tinker Wall · B)
- Reinforced Bookshelf (Crew Niche · A), Tabletop Game Set (Crew Niche · B)

Acquisition data rows unchanged.

## Verification Output

All 12 grep checks passed inline:
- The Locomotive ✓ | Hellfire Boiler ✓ | The Pulpit ✓ | The Apse ✓
- Tinker Wall ✓ | Crew Niche ✓ | The Reliquary ✓ | clip-path: polygon ✓
- acq-slot ✓ | engine-tile-name ✓ | is-pulpit ✓ | reliquary-panel ✓

## File Size Delta

~279 lines added (12,596 → 12,875 lines). CSS additions: ~70 lines. HTML additions: ~20 lines. ENGINE_LAYOUT replacement: ~10 net lines. renderEngineFloor patch: ~8 lines.

## Open Issues for QA

1. The Reliquary block uses `kind: 'reliquary'` — `.carriage-block.is-reliquary` CSS is new; the old `.is-tender` CSS is preserved but no longer used.
2. Pulpit hex clip-path will crop the `engine-tile-name` label — QA should verify the name is readable or adjust clip region / reduce font size.
3. `engine-slot-name` inside the axis-label row on AB tiles may overflow at narrow tile widths — check Apse tile at small viewport.
4. The old `carriage 1 · the locomotive` eyebrow text already said "locomotive" (pre-existing); h3 now reads "The Locomotive" consistently.
