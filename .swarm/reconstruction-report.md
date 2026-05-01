# Reconstruction Report — Locomotive Redesign

**Date:** 2026-05-01
**Agent:** Reconstruction Agent
**Base commit:** f57c135 (10930 lines, healthy)

---

## Stages Completed

All 7 stages completed and committed incrementally.

| Stage | Commit | Lines | What was done |
|---|---|---|---|
| Stage 1 | 7814928 | 10967 | ENGINE_LAYOUT replaced with new Locomotive data: The Hellfire Boiler, The Reliquary (with subStructure), The Pulpit (hex/A1), The Apse (Work/A/B), The Tinker Wall (Maintenance/A/B), The Crew Niche (Life/A/B) |
| Stage 2 | 651a0c9 | 11011 | renderEngineFloor updated: A/B install slot rendering, hex Pulpit SVG, Reliquary subStructure label, tile name labels, legend code chips, A/B selection in legend |
| Stage 3 | 004e5ad | 11302 | CSS added: Reliquary, Pulpit hex, engine-tile-name, legend-code, engine-slot-ab, engine-slot-option selected/unselected/badge, Acquisition Atlas grid/cards |
| Stage 4 | 6283dd0 | 11311 | Carriages tab updated: h3 "The Locomotive", section sub-text with new names, fuel rules updated (Active chamber/PLUG storage/Emergency swap), Reliquary panel added, hellfire-boiler.png in .is-engine CSS |
| Stage 5 | 0efe9e9 | 11434 | Acquisition Atlas section added: 6 cards (Co-Pilot Cradle, Fold-Down Bunk, Toolkit & Boiler Kit, Engineer's Manual, Reinforced Bookshelf, Tabletop Game Set) with Bought/Salvaged/Faction/Crafted/Story rows |
| Stage 6a | 2e73939 | 11603 | Engine tab nav button (⚙ The Engine, data-tab=motor) + empty panel scaffold + engine-altarpiece CSS + engine-hero, engine-bands-table, engine-prob-widget, engine-part-divider CSS |
| Stage 6b | 58ec28c | 11673 | Engine tab Hero block + The Roll section + bands table + probability calculator HTML |
| Stage 6c | a832710 | 11712 | initEngineProbWidget() JS function + DOMContentLoaded wiring |
| Stage 6d | fe40edc | 11765 | Sections Fit, Threshold, Outcome |
| Stage 6e | 9323482 | 11846 | Part II divider + Sections Dispatch, Events, Rest |
| Stage 6f | d27f29e | 11948 | Part III divider + Traits + Worked Example (Marlow's Medium Run) |
| Stage 7 | d27f29e | 11948 | QA pass — no changes needed, file already healthy |

---

## File Size Progression

| Commit | Lines | Bytes |
|---|---|---|
| f57c135 (base) | 10930 | ~474 KB |
| After Stage 1 | 10967 | +37 lines |
| After Stage 2 | 11011 | +44 lines |
| After Stage 3 | 11302 | +291 lines |
| After Stage 4 | 11311 | +9 lines |
| After Stage 5 | 11434 | +123 lines |
| After Stage 6a | 11603 | +169 lines |
| After Stage 6b | 11673 | +70 lines |
| After Stage 6c | 11712 | +39 lines |
| After Stage 6d | 11765 | +53 lines |
| After Stage 6e | 11846 | +81 lines |
| After Stage 6f (final) | 11948 | 518 KB |

Net: +1018 lines, +44 KB from base.

---

## Issues Encountered

1. **Edit tool truncation (critical, resolved):** The first attempt at Stage 1 using the standard Edit tool caused file truncation (10930 → 10914 lines). The Edit tool writes through the Windows path mount and truncated the tail of the file. All subsequent edits were made using Python `str.replace()` via the bash workspace tool, which is safe and does not truncate. The file was restored from git before proceeding.

2. **§ entity encoding:** The factions tab nav button contains the literal § character, not `&sect;` HTML entity. The Python script needed to match the literal character to locate the insertion point.

3. **Stage 7 no-op:** The Stage 7 "QA verified" commit was redundant — the file had no uncommitted changes after Stage 6f. The QA checks all passed and the stage is considered complete without a new commit.

---

## Open Issues for Coordinator

1. **No interactive A/B toggle:** The `selected: 'a'` field is in the data and renders the selected/unselected CSS states, but clicking an option in the browser does not swap selection. This was deferred per the carriages-engine-ab-update spec.

2. **Pulpit hex name label hidden:** `.carriage-tile.is-slot.is-pulpit .engine-tile-name { display: none; }` — the name "The Pulpit" is suppressed on the floor tile (replaced by the A1 hex code). The legend resolves A1 → The Pulpit. QA should verify the legend code chip renders clearly.

3. **Engine tab content source:** The worked example uses content from phase1d-worked-example.md (Marlow's run), condensed into HTML code-block style rather than prose-narrative format. The full atmospheric prose is preserved in the source file; the tab shows the mechanical skeleton. If the coordinator wants the narrative voice restored, the phase1d file is the source.

4. **cadence-section-card class re-use:** The engine sections use `class="cadence-section-card"` for section wrappers — this reuses an existing class from the Cadence tab. If that class has styles that conflict, the engine sections may need a dedicated class `.engine-section-wrapper`.

5. **hellfire-boiler.png availability:** The CSS references `img/textures/hellfire-boiler.png`. The spec noted this file is already on disk; QA should verify the path is correct relative to the docs/ directory.
