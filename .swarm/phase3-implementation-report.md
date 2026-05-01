# Phase 3 — Implementation Report

**Agent:** Implementation (Phase 3)
**Target file:** `S:\Git\Apocalypse-Express\docs\character-creation.html`
**Original size:** ~299 KB (~10,759 lines) · **Final size:** 517 KB (~12,300+ lines)

---

## What Was Built

### Tab scaffold
- Added `<button class="tab tab-reference" data-tab="motor"><span class="num">⚙</span>The Engine</button>` after the Factions nav button.
- Added `<section class="tab-panel" id="tab-motor">` with `<div class="engine-altarpiece">` container after the Factions panel, before `</main>`.

### CSS additions (~350 lines, inserted before `</style>`)
New classes: `.engine-altarpiece`, `.engine-hero` (+`::before`/`::after`/`.engine-hero-inner`/`.engine-hero-*`), `.engine-section`, `.engine-section-card`, `.engine-bands-table`, `.engine-part-divider`, `.engine-prob-widget` (+`.engine-prob-widget-body`/`.engine-prob-inputs`/`.engine-prob-field`/`.engine-prob-bars`/`.engine-prob-row`/`.engine-prob-bar`/`.engine-prob-pct`/`.engine-prob-modal`), `.engine-crosslink`, `.engine-body`, `.engine-fields-table`, `.engine-dispatch-table`, `.engine-we-subhead`, `.engine-we-time`, `.engine-we-teaching`, `.engine-threshold-table`, `.engine-rest-table`, `.engine-segment-table`, `.engine-crew-table`, `.engine-notes-table`, `.engine-rest-sum-table`. Reuses existing `.cadence-section-header`, `.cath-eyebrow`, `.efr-row`, `.cadence-section-title`, `.cadence-section-sub`.

### Hero block (Section 1, `#engine-hero`)
Eyebrow → h2 (THE ENGINE) → Cormorant Garamond italic lead → IBM Plex Mono body prose → jump-link to `#worked-example`. Mirrors `.fac-hero` pattern with gold strip, radial gradient glow, stained-glass background.

### Part I — Core Roll (Sections 2–5)
- `#roll`: Bands table (color-coded left border by band), task-card code block, beat-by-beat Mira example, probability calculator widget.
- `#fit`: Formula pre block, efr-row breakdown grid, three worked examples in single code card.
- `#threshold`: 5-tier difficulty table, environment/time-pressure efr-row grid, worked modifier example.
- `#outcome`: 4-field table, Methodical live example, Yield reference table, Duration note.

### Probability Calculator Widget
`<details class="engine-prob-widget">` (collapsed by default). Two `<input type="number">` inputs (Fit default 0, Threshold default 9). 4-row bar grid with CSS-width bars and text percentages. `initEngineProbWidget()` function added to JS block with DOMContentLoaded init pattern matching existing code. Also fires on `<details>` toggle (once) so bars populate correctly on first expand.

**Math verified:** Fit=0, Threshold=9 → CF: 28%, F: 44%, S: 25%, CS: 3%. Matches spec exactly.

### Part II — World in Motion (Sections 6–8)
- `#part-world` divider with `PART II · THE WORLD IN MOTION`
- `#dispatch`: Journey length/clock table, movement table, outcome ladder table, notes.
- `#events`: Four trigger types as efr-rows, event card anatomy code block, three full event cards (Boiler Stress, Stowaway, Chronoshear Flare) as `<pre class="engine-section-card">` blocks with original ASCII formatting preserved.
- `#rest`: Pool sizes table, wake cost state table, double-up breakdown.

### Part III — Synthesis (Sections 9–10)
- `#part-synthesis` divider with `PART III · SYNTHESIS`
- `#traits`: Trait card schema, three trait cards (Methodical, Hyperfocus, Service Intelligence) as code blocks with condition/field/modifier structure.
- `#worked-example`: Full Marlow medium run — crew table, 4 phase Fit calculation cards, journey clock ASCII art, mid-journey Boiler Stress event (ASCII box card preserved), Coupling Slack event (ASCII box preserved), segment log table, journey ladder code block, rest summary table, closing mechanics table (14 rows).

### Cross-link anchors added to destination tabs
- `id="personality-traits"` added to `.personality-section` in Personality tab (was `personalityTraitsHeader` on the h3 only)
- `id="engine"` added to `.carriage-section` in Carriages tab
- `id="cl-ladder"` added to `.cadence-cl-ladder` section in Cadence tab
- `id="faction-relations"` added to `.fac-rel-matrix` div in Factions tab
- `id="soul-index"` added to `.layer-header` div in Soul tab

---

## Deviations from Spec

1. **`#soul-index` anchored to `.layer-header`** rather than a skill list (none exists at the section level yet). The layer header is the top of the Soul tab and contains the "Soul Index & Skill Mandala" h2 — appropriate as the target.
2. **Cross-links use tab-panel ids** (`#tab-lelek`, `#tab-factions`, `#tab-vagon`, `#tab-cadence`) rather than in-section anchors for the cross-tab references in the Engine tab prose, because the spec's cross-link convention (per phase1a §Cross-link patterns) uses prose text, not hyperlinks. Where destination anchors were added, those are also used.

---

## Open Issues for QA

- Probability widget bars fire correctly on DOMContentLoaded; QA should also verify they update live on input changes in browser.
- Worked example is ~2,800 words of HTML content; visual flow check recommended (especially ASCII box cards that rely on monospace pre rendering).
- The `id="engine"` on the Carriages section may conflict if any existing JS targets `.carriage-section` by id — check `renderEngineFloor()` which targets `id="engineFloor"`, not the section wrapper (no conflict expected).

---

## Verification Output

```
File length (chars): 529,527 (~517 KB, was ~299 KB)
Has tab-motor panel: true
Has motor nav button: true
Has engine-hero: true
Has prob widget: true
Has worked-example: true
Has initEngineProbWidget: true
Has all 10 section anchors: true (roll, fit, threshold, outcome, dispatch, events, rest, traits, worked-example + hero)
Has personality-traits anchor: true
Has engine anchor: true
Has cl-ladder anchor: true
Has faction-relations anchor: true
Has soul-index anchor: true
Div balance: 419 open / 419 close (delta 0)
Section balance: 36 open / 36 close (delta 0)
Details balance: 1 real HTML open / 1 close (second apparent hit is inside <script> comment string — false positive)
```
