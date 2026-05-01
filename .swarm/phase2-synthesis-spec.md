# Phase 2 — Synthesis Spec

> Reconciles outputs from Phase 1A (canon + aesthetic), 1B (mechanics content), 1C (UX + structure), 1D (worked example). Locks decisions for Phase 3 implementation.

---

## 1. Locked: Tab name + key + classification

- **Display name:** `The Engine`
- **`data-tab` key:** `motor` (Hungarian for engine/motor — fits existing convention: test / lelek / szem / vagon / cadence / factions)
- **Panel id:** `tab-motor`
- **Classification:** `tab-reference` (rules tab, like Cadence and Factions; not a numbered chargen layer)
- **Sigil:** `⚙` (gear/cog, matching engine + cathedral-industrial theme)

**Tab nav button (insert after `factions`):**
```html
<button class="tab tab-reference" data-tab="motor"><span class="num">⚙</span>The Engine</button>
```

**Tab panel shell:**
```html
<section class="tab-panel" id="tab-motor">
  <div class="engine-altarpiece">
    <!-- hero + 10 sections -->
  </div>
</section>
```

---

## 2. Locked: Section structure (10 sections in 3 named parts)

| # | Anchor | Section | Source file |
|---|---|---|---|
| 1 | `#engine-hero` | Hero / Quick Start | NEW (~80 words, gothic-procedural) |
| 2 | `#roll` | The Roll (2d6 + Fit vs Threshold, bands) | `phase1b` §The Roll + **probability widget** |
| 3 | `#fit` | Fit (formula, examples, range) | `phase1b` §Fit |
| 4 | `#threshold` | Threshold (5-tier scale, modifiers) | `phase1b` §Threshold |
| 5 | `#outcome` | Outcome — Four fields | `phase1b` §Outcome |
| — | `#part-world` | **Part II divider** | NEW (eyebrow row) |
| 6 | `#dispatch` | Dispatch & Journey Clock | `phase1b` §Dispatch |
| 7 | `#events` | Events (4 triggers, anatomy, 3 examples) | `phase1b` §Events |
| 8 | `#rest` | Rest (pools, wake costs, double-up) | `phase1b` §Rest |
| — | `#part-synthesis` | **Part III divider** | NEW (eyebrow row) |
| 9 | `#traits` | Trait integration | `phase1b` §Traits |
| 10 | `#worked-example` | Marlow's Medium Run (end-to-end) | `phase1d` full doc |

**Part dividers** use the existing `.fac-section-divider` ornament-row pattern with eyebrow text:
- (no divider before Part I — the hero IS Part I's opener)
- `PART II · THE WORLD IN MOTION` before #dispatch
- `PART III · SYNTHESIS` before #traits

---

## 3. Locked: Probability calculator widget

- **Location:** Inside `#roll` section, below the bands table
- **Visual treatment:** stained-glass `.info-panel` style container, collapsible summary/details `<details>` element so it doesn't dominate
- **Inputs:** two `<input type="number">` — Fit (default 0, range -5..+10), Threshold (default 9, range 5..18)
- **Output:** 4-row band probability table with horizontal bars (CSS width%) + numeric percent + a "Modal outcome" caption line
- **Compute:** 36-case 2d6 distribution, exact probabilities (no floating math hacks). Math:
  - For each die-sum 2..12 (frequency 1,2,3,4,5,6,5,4,3,2,1 / 36): total = die_sum + Fit
  - Margin = total − Threshold
  - Margin ≥ +3 → CS; 0..+2 → S; −1..−3 → F; ≤ −4 → CF
- **Implementation:** self-contained `<script>` block, ~60 lines, attaches to widget on DOM-ready, listens for `input` events on both number inputs

---

## 4. Locked: Hero block

Reference tab opens with a bespoke hero, NOT `.layer-header`. Mirror `.cadence-hero` stained-glass panel pattern.

**Hero contents:**
- Eyebrow: `Reference · the roll that runs the train`
- h2 (Cinzel, gold2, ~32px): `THE ENGINE`
- Lead line (Cormorant Garamond italic, single sentence, gothic-procedural): something like *"Every task, every journey, every event resolves through one grammar — roll two dice, add your Fit, compare to the Threshold; everything downstream is consequence."*
- Body prose (IBM Plex Mono, ~16px, line-height 1.7, 2-3 sentences): the 30-second TL;DR — what the tab covers, why one mechanic for everything, what the reader will know by the end.
- Inline jump-link (small, gold): `See it all fire at once → Marlow's run`  pointing to `#worked-example`

---

## 5. CSS additions needed

- `.engine-altarpiece` — flex column wrapper (mirror `.cadence-altarpiece`: `display: flex; flex-direction: column; gap: 24px`)
- `.engine-hero` — stained-glass panel with two-column layout (text left, optional decorative ornament right; or single-column if simpler) — mirror `.cadence-hero` if it exists, else `.fac-hero`
- `.engine-section-card` — code-block style display for formula cards and event-card snippets (monospace, gold border, dark fill, like `.efr-row` row containers but for whole blocks)
- `.engine-bands-table` — outcome bands table (4 rows, color-tagged left border per band)
- `.engine-prob-widget` — probability calculator container (info-panel base + custom inputs + bar grid)
- `.engine-part-divider` — extends `.fac-section-divider`, just specifying tab-scoped vertical margins

All other styling reuses existing classes: `.cath-eyebrow`, `.cadence-section-header`, `.cadence-section-title`, `.info-panel`, `.cadence-stage-placeholder` (none expected here), table base styles.

---

## 6. JS additions needed

Single function attached at DOM-ready in the existing JS block:

```js
function initEngineProbWidget() {
  const fitInput = document.getElementById('engine-prob-fit');
  const thInput = document.getElementById('engine-prob-threshold');
  if (!fitInput || !thInput) return;
  // 2d6 distribution: index 2..12 → frequency 1..6..1
  const freq = [0,0,1,2,3,4,5,6,5,4,3,2,1];
  function recompute() {
    const fit = +fitInput.value || 0;
    const th = +thInput.value || 9;
    const counts = { CF: 0, F: 0, S: 0, CS: 0 };
    for (let s = 2; s <= 12; s++) {
      const m = s + fit - th;
      if (m >= 3) counts.CS += freq[s];
      else if (m >= 0) counts.S += freq[s];
      else if (m >= -3) counts.F += freq[s];
      else counts.CF += freq[s];
    }
    const total = 36;
    // Update bars + percentages
    for (const band of ['CF', 'F', 'S', 'CS']) {
      const pct = Math.round((counts[band] / total) * 100);
      const bar = document.querySelector(`.engine-prob-bar[data-band="${band}"]`);
      const pctEl = document.querySelector(`.engine-prob-pct[data-band="${band}"]`);
      if (bar) bar.style.width = pct + '%';
      if (pctEl) pctEl.textContent = pct + '%';
    }
    // Modal outcome
    const modal = ['CF','F','S','CS'].reduce((a,b) => counts[a] >= counts[b] ? a : b);
    const modalLabel = { CF: 'Critical Failure', F: 'Failure', S: 'Success', CS: 'Critical Success' }[modal];
    const modalEl = document.getElementById('engine-prob-modal');
    if (modalEl) modalEl.textContent = `Modal outcome: ${modalLabel}`;
  }
  fitInput.addEventListener('input', recompute);
  thInput.addEventListener('input', recompute);
  recompute();
}
// Add to DOMContentLoaded init or call from existing init function.
```

No tab-switch hook needed (Engine is purely static rules content with no cross-tab state dependency).

---

## 7. Cross-link verification

Implementation agent must verify these anchor IDs exist in destination tabs and add them if missing:

| Anchor | Tab | Existing? |
|---|---|---|
| `#personality-traits` | Personality | Likely exists as `personalityTraitsHeader` — verify and use that id, OR add `#personality-traits` as additional id on grid container |
| `#engine` | Carriages | Verify — Driver post / Engine layout section likely has an id; if not, add `id="engine"` to that section |
| `#cl-ladder` | Cadence (Chaos & Harmony) | Likely exists as `clLadderHeader` — verify |
| `#faction-relations` | Factions | Probably missing — add `id="faction-relations"` to the relationship-matrix section |
| `#soul-index` | Soul | Probably missing — add to skill-list section if present, or to a relevant header |

Cross-links from Engine tab use plain in-tab `<a href="#anchor">` for in-page jumps and prose-text + sigil notation (`§Factions`, `Body tab`) for cross-tab references — matching existing AE convention.

---

## 8. Voice & flavor injection (constrained)

Agent B's content is clear-tutorial English; Agent D's worked example has full atmospheric voice. The tab should preserve B's clarity but inject minor gothic-procedural flavor at:
- Hero block (1-2 lines)
- Part divider eyebrows (just the part name, terse)
- Maybe one line at the start of #dispatch and #events to reset register before the rules content kicks in

DO NOT over-inject. Reference tabs (Cadence, Factions) lean rules-first. Engine should match that — clarity dominant, atmosphere as garnish.

---

## 9. Implementation order (suggested staging)

1. **Scaffold:** add tab nav button + empty `<section id="tab-motor">` + `.engine-altarpiece` flex container + needed CSS in main `<style>` block
2. **Hero:** write hero block (eyebrow + h2 + lead line + body prose + jump-link)
3. **Part I (sections 2-5):** Roll → Fit → Threshold → Outcome
4. **Probability widget:** HTML markup inside #roll + JS function + CSS for inputs/bars
5. **Part II divider + sections 6-8:** Dispatch → Events → Rest
6. **Part III divider + section 9:** Traits
7. **Section 10 worked example:** reformat phase1d content as in-tab HTML (preserve code blocks for cards; convert markdown tables to HTML)
8. **Cross-link verification:** check anchor IDs in destination tabs, add missing ones
9. **Render check:** JSDOM headless render or simpler — load the file in Node + cheerio to verify it parses without syntax errors and the new tab + all sections exist

---

## 10. Open issues for QA (Phase 4)

- Verify probability widget actually computes correctly (test with Fit=0/Th=9: should be CF≈28%, F≈44%, S≈25%, CS≈3%)
- Confirm worked example narrative reads cleanly when extracted from markdown into HTML (check code-block/card/table conversion didn't break flow)
- Confirm voice register matches existing reference tabs — not too dry, not too purple
- Confirm Part divider eyebrows visually match `.fac-section-divider` pattern
- Confirm tab activates correctly via existing JS tab-switch handler

---

*Document: phase2-synthesis-spec.md — Coordinator synthesis output*
