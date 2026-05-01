# Phase 1C: UX + Structure Spec

## Tab name

Top recommendation: **The Engine**
Rationale: The locomotive is the literal and symbolic heart of the Apocalypse Express — it is what moves, what burns, what decides. "The Engine" maps cleanly onto "the rules engine" without sounding like a glossary page. It is short enough for the tab bar (unlike "Liturgy of the Roll"), doesn't collide with any existing tab name, carries the cathedral-industrial aesthetic already present in the carriage floor-plan section, and feels like a proper noun rather than a genre label. It also allows the tab content to open with the locomotive framing ("the engine that drives every roll") without forced metaphor.

Other candidates considered:

- **The Wheel** — Evocative (steering, fate, fortune's wheel), but wheel-as-mechanic is ambiguous; could be read as a factions-of-power reference rather than a rules primer. Also slightly passive — the wheel turns things, the engine *drives* things.
- **Rolls & Dispatch** — Accurate and clear, but reads like a procedure manual subtitle, not a stained-glass label. Too functional, zero atmosphere.
- **Liturgy of the Roll** — Strong cathedral resonance, good flavour, but at 4 words it is too long for the tab bar and implies a ritual text rather than a learnable system. Better as a section eyebrow inside the tab than as the tab name itself.
- **Resolution** — Clean, matches existing one-word tab conventions (Soul, Body), but clinical — it names the outcome category, not the whole system. A new player seeing "Resolution" in the nav might not know it covers dispatch, events, and rest.
- **The Mechanic** — Genre-aware, punchy, fits the post-apocalyptic register. Risks sounding like a character class. Also collides conceptually with the "Mechanic" archetype that may exist in the system.

---

## Section order (with rationale)

1. **Quick Start / Hero / Overview** — Why first: the player needs 30 seconds of orientation before any formula. Sets up the framing ("this tab covers everything that happens when a die hits the table"), prevents the dense sections that follow from arriving without context. Mirrors the pattern of every other tab (Chaos & Harmony opens with a "two scales at a glance" hero; Body opens with the race altarpiece; Factions opens with a faction-count summary). The hero is also where the cross-link to the Worked Example lives — "want to see it all at once? jump to Marlow's run."

2. **The Roll (2d6 + Fit vs Threshold, bands)** — Why second: it is the atomic unit. Every subsequent section is either an input to the roll (Fit, Threshold), an output of the roll (Outcome), or a context that generates rolls (Dispatch, Events). Reader must understand the roll structure before anything else makes sense. The bands table (fail / partial / success / crit) is also visually compact — it can sit in a small card-style block that rewards a quick skim before the detail sections open.

3. **Fit (formula, examples, range)** — Why third: immediately follows the roll because Fit *is* the modifier going into the roll. Reader has just seen "2d6 + Fit" and is naturally asking "what is Fit?" Answering it here keeps causal flow. Examples with concrete numbers here prime readers to understand why Threshold matters next.

4. **Threshold (scale, modifiers)** — Why fourth: the other side of the roll equation. Fit and Threshold are co-dependent; presenting them consecutively lets the reader mentally simulate a roll before they reach the Outcome section. The Threshold scale also introduces the modifier vocabulary (terrain, crowd, faction hostility) that appears again in Events and Dispatch.

5. **Outcome (Resolution / Yield / Duration / Complication)** — Why fifth: the roll now produces something; this section explains what. Placing Outcome here — after the inputs (Fit, Threshold) but before the contexts (Dispatch, Events) — means the reader understands the grammar of results before encountering the situations that trigger them. The four-way split (Resolution / Yield / Duration / Complication) is the most conceptually dense non-narrative section; it belongs in the core cluster where the reader is still in "learning mode" rather than "reference mode."

6. **Dispatch & Journey Clock (phases, segments, outcome ladder)** — Why sixth: Dispatch is the first *context* layer — it is what rolls happen *inside*. With the roll grammar established, the reader can now read the Dispatch section as "here is one scenario that uses everything above." The Journey Clock phases and segment structure give sequence to what otherwise feels like an abstract ruleset. Cross-links to Carriages tab go here.

7. **Events (4 triggers, anatomy, examples)** — Why seventh: Events are the other major context for rolls, and they connect outward to Chaos Level and faction relations. Placing Events after Dispatch keeps the "contexts" cluster together and allows the Events section to reference the Dispatch outcome ladder without forward-referencing. The 4-trigger anatomy is best understood once the player knows what a completed dispatch looks like.

8. **Rest (pools, wake costs, double-up)** — Why eighth: Rest is the recovery valve for everything above — it is not a roll-trigger but a roll-resource replenisher. It belongs after the two roll-generating contexts (Dispatch, Events) so the player has felt the "spend" before reading the "refill." It is also the shortest true-rules section and works as a natural pace break before the more synthetic sections.

9. **Trait integration (how traits plug in)** — Why ninth: Traits are a modifier layer, not a foundational rule. By section 9, the reader knows what a roll is, what Fit is, what modifies Threshold, how Dispatch and Events generate rolls, and how Rest restores resources. Traits now slot cleanly into that picture as "here is another modifier source." Placing this near the end also means the cross-link to the Personality tab arrives when the reader is ready to go deep on individual traits rather than before they understand what a trait modifies.

10. **Worked Example (Marlow's medium journey, all systems firing)** — Why last: synthesis section, not motivation section. The argument for putting Worked Example first is "it creates motivation by showing the whole system" — but that argument applies better to games with very simple cores (a 1-page RPG). Apocalypse Express has enough moving parts (Fit formula, Threshold scale, Outcome four-way, Journey Clock phases, Events, Rest, Traits all simultaneously active) that a worked example at position 1 would feel bewildering rather than motivating. Putting it last means every sub-system referenced in Marlow's run has been explained, and the example becomes a test of comprehension rather than a preview of complexity. The hero section at position 1 already provides the "30-second motivation" that an intro example would otherwise need to deliver.

**Sub-grouping: Yes — three named parts**

The 10 sections split naturally into three clusters. Naming them helps readers navigate a long single-page tab and provides visual breathing room between dense sections.

- **Part I — The Core Roll** (sections 1–5): Hero + Roll + Fit + Threshold + Outcome. The atomic grammar of resolution.
- **Part II — The World in Motion** (sections 6–8): Dispatch + Events + Rest. How the roll lives inside scenarios.
- **Part III — Synthesis** (sections 9–10): Trait integration + Worked Example. How all layers stack.

Sub-group headers should use the same `cath-eyebrow` + ornament treatment as section dividers in Chaos & Harmony, keeping visual language consistent.

---

## Anchor structure

- `#engine-hero` — Quick Start / Hero / Overview
- `#roll` — The Roll (2d6 + Fit vs Threshold)
- `#fit` — Fit (formula, examples, range)
- `#threshold` — Threshold (scale, modifiers)
- `#outcome` — Outcome (Resolution / Yield / Duration / Complication)
- `#dispatch` — Dispatch & Journey Clock
- `#events` — Events (4 triggers, anatomy, examples)
- `#rest` — Rest (pools, wake costs, double-up)
- `#traits` — Trait integration
- `#worked-example` — Worked Example (Marlow's run)

Intra-part divider anchors (for nav jump-links within the tab):
- `#part-core` — Part I anchor
- `#part-world` — Part II anchor
- `#part-synthesis` — Part III anchor

---

## Cross-links

| From section | Link text | Destination tab + anchor |
|---|---|---|
| `#fit` | "Skills that feed Fit live in the Soul tab" | Soul tab → `#soul-index` (best-guess: skill list section) |
| `#outcome` | "Trait phases can flip Complication into Yield — see Personality" | Personality tab → `#trait-phases` (best-guess: per-trait phase section) |
| `#dispatch` | "Each carriage sets its own Threshold floor — see Carriages" | Carriages tab → `#engine` (existing anchor for engine floor-plan section) |
| `#dispatch` | "The Driver post modifies Fit on all Engine dispatch — see Carriages" | Carriages tab → `#engine` |
| `#events` | "Events can push or pull Chaos Level — see Chaos & Harmony" | Chaos & Harmony tab → `#cl-ladder` (best-guess: CL ladder section) |
| `#events` | "Faction relations shift on Complication — see Factions" | Factions tab → `#faction-relations` (best-guess: relationship matrix section) |
| `#traits` | "Full trait list with phase details in the Personality tab" | Personality tab → `#personality-traits` (existing: `personalityTraitsHeader`) |
| `#engine-hero` | "Jump to Marlow's full run ↓" | same tab → `#worked-example` |

Notes on destination anchors: The Personality tab's existing JS-rendered grid is ID'd as `personalityTraitsGrid`; the section header is `personalityTraitsHeader`. The Chaos & Harmony tab has a `clLadderGrid` element with a corresponding header `clLadderHeader`. The Factions tab has a relationship matrix section that will need an anchor assigned at build time — `#faction-relations` is the recommended name. These IDs are best-guesses based on the naming patterns observed in the existing HTML; Phase 3 (coding) should confirm them.

---

## Interactive widget decision

**Yes — include the probability calculator widget, placed inside `#roll` (section 2), below the bands table.**

Rationale:

The core mechanical claim of the system is that 2d6 produces a bell curve that makes partial successes the modal outcome. This is not obvious to players coming from d20 systems where every face is equally probable. A small widget that lets the player type in their Fit and the Threshold and immediately see "you hit a full success ~42% of the time, partial ~35%, fail ~23%" makes that bell-curve argument viscerally rather than theoretically. It reduces cognitive load for the Fit and Threshold sections that follow — once the player has played with the widget, they arrive at those sections already understanding *why* Fit matters (a +2 Fit shifts the entire probability distribution meaningfully).

Cons addressed:
- JS complexity: the widget is genuinely simple — three inputs, one output table, pure arithmetic on the 2d6 distribution. No async, no state, no framework dependency. It can be a self-contained `<script>` block that is under 60 lines.
- Distraction risk: mitigated by placement (after the bands table, not before; inside a collapsible or visually subordinate card rather than as the section hero) and by keeping it compact (no animations, no sliders, two number inputs and a results grid).
- Failure modes: since it is pure client-side arithmetic it cannot fail in unexpected ways. Graceful degradation is trivial — if JS is off, the widget simply does not appear and the bands table stands alone.

Widget wireframe (text-based):

```
┌─────────────────────────────────────────────────────────┐
│  PROBABILITY CALCULATOR                                  │
│  eyebrow: "bell curve · 2d6 distribution"               │
├──────────────────────────┬──────────────────────────────┤
│  Fit modifier: [ ±  0 ]  │  Threshold: [  8  ]          │
│  (integer spinner −5→+10)│  (integer spinner 2→18)      │
├──────────────────────────┴──────────────────────────────┤
│  OUTCOME BANDS                                          │
│  ┌──────────────┬─────────────────┬──────────────────┐  │
│  │ Band         │ Roll needed     │ Probability      │  │
│  ├──────────────┼─────────────────┼──────────────────┤  │
│  │ Fail         │ < Threshold     │    ██ 23%        │  │
│  │ Partial      │ Threshold       │    ████ 35%      │  │
│  │ Success      │ Threshold + 2   │    ████ 31%      │  │
│  │ Critical     │ Threshold + 5   │    ██ 11%        │  │
│  └──────────────┴─────────────────┴──────────────────┘  │
│                                                          │
│  Modal outcome: Partial Success                          │
│  (bar widths update live as inputs change)               │
└─────────────────────────────────────────────────────────┘
```

The bars are simple CSS width percentages — no canvas, no SVG charting library. Probabilities are computed from the exact 36-case 2d6 distribution. The "Modal outcome" line updates to whichever band has the highest probability at the current Fit + Threshold combination, giving instant interpretive guidance.

---

## Wireframe (top to bottom)

```
════════════════════════════════════════════════════════════════
TAB NAV (existing pattern):
  [1 Body] [2 Soul] [3 Personality] [4 Carriages] [∞ Chaos & Harmony] [§ Factions] [⚙ The Engine]
════════════════════════════════════════════════════════════════

────────────────────── PART I · THE CORE ROLL ──────────────────────
[sub-part divider · cath-eyebrow + ornament · no anchor needed]

[HERO BLOCK · large]   #engine-hero
  eyebrow: "Reference · the roll that runs the train"
  h2 (Cinzel): THE ENGINE
  lede (prose): 30-second TL;DR of the unified mechanic.
    "Every task, every journey, every event resolves through 
     one grammar: roll 2d6, add your Fit, compare to a Threshold.
     What follows — outcome, yield, clock, event, rest — is all
     downstream of that one throw."
  → jump-link: "See it all fire at once → Marlow's run" (#worked-example)
  → cross-link: none (hero is orientation only)
  Size note: single-column prose block, same width cap as body-intro (1280px max)

[SECTION: The Roll · medium]   #roll
  eyebrow: "Layer 0 · the atomic unit"
  h3: "2d6 + Fit vs Threshold"
  Prose: 2-3 sentences on what the roll is and is not (not a d20, bell curve, why it matters)
  
  Card-style display block:
    FORMULA: [ 2d6 ] + [ Fit ] ≥ [ Threshold ]
    (visual treatment: monospace code card, gold border, like .efr-row pattern)
  
  Bands table (4 rows):
    | Band         | Condition              | Colour tag |
    | Fail         | Roll < Threshold       | ember/rust  |
    | Partial      | Roll = Threshold       | gold        |
    | Success      | Roll ≥ Threshold + 2   | green-good  |
    | Critical     | Roll ≥ Threshold + 5   | cyan        |
  
  → PROBABILITY CALCULATOR WIDGET (see wireframe above)
     Sits below the bands table, inside a .info-panel style container
     with a collapsed-by-default affordance (summary/details or a
     "Show calculator" toggle button) so it doesn't dominate the section.
  
  → cross-link: "What is Fit? →" (#fit, next section)

[SECTION: Fit · medium]   #fit
  eyebrow: "Input · your modifier going in"
  h3: "Fit — how well you match the task"
  Prose: formula derivation (Skill + Trait modifiers + Posture)
  Examples table: 3-4 worked Fit calculations with different character builds
  Range note: typical range −2 to +8; what extreme values mean at table
  → cross-link (Soul tab): "Skills that feed Fit → Soul tab" (#soul-index)

[SECTION: Threshold · medium]   #threshold
  eyebrow: "Input · what you're rolling against"
  h3: "Threshold — how hard the task is"
  Scale card: base values 4 / 6 / 8 / 10 / 12 by difficulty tier
  Modifiers table: terrain, crowd density, faction hostility, time pressure → +/−
  Note on who sets Threshold (GM) and when it is fixed vs variable
  → cross-link (Carriages tab): "Carriage type sets Threshold floor → Carriages" (#engine)

[SECTION: Outcome · large]   #outcome
  eyebrow: "Output · what the roll produces"
  h3: "Four outputs, one roll"
  
  Four-panel card grid (2×2 or 4-column horizontal):
    [Resolution] — pass/fail of the declared intent
    [Yield]      — the tangible gain or resource produced
    [Duration]   — how long the outcome persists / counts on the clock
    [Complication] — what goes sideways even on a success
  
  Each panel: 2-3 prose lines + example.
  Note: on Fail, only Complication fires; on Crit, Complication is suppressed.
  → cross-link (Personality tab): 
    "Trait phases can convert Complication → Yield — see Personality" (#personality-traits)

────────────────────── PART II · THE WORLD IN MOTION ──────────────────────
[sub-part divider · cath-eyebrow + ornament]

[SECTION: Dispatch & Journey Clock · large]   #dispatch
  eyebrow: "Context · rolls inside a journey"
  h3: "Dispatch — the structured journey"
  
  Journey phases prose (ordered list):
    1. Declaration (Player states intent + carriage)
    2. Threshold assignment (GM)
    3. Roll resolution
    4. Clock advance
    5. Segment outcome
  
  Segment/phase table:
    | Journey length | Segments | Clock ticks |
    | Short          | 2        | 2           |
    | Medium         | 3        | 3           |
    | Long           | 5        | 5           |
  
  Outcome ladder card: how segment results stack toward journey resolution
  (3 partial successes = full success on a medium run, etc.)
  
  → cross-link (Carriages tab, ×2): 
    "Each carriage sets its own Threshold floor → Carriages" (#engine)
    "The Driver post modifies Fit on Engine dispatch → Carriages" (#engine)

[SECTION: Events · large]   #events
  eyebrow: "Interrupts · the world pushing back"
  h3: "Events — four ways the world intervenes"
  
  Trigger table (4 rows):
    | Trigger type   | When it fires               |
    | Segment end    | After each clock advance     |
    | Complication   | On any roll Complication     |
    | Faction        | On faction contact           |
    | Rest           | On completing a rest phase   |
  
  Event anatomy (card or .efr-row list):
    Source → Trigger → Roll (if any) → Outcome → Faction/CL shift
  
  2 worked event examples (brief, reference style)
  
  → cross-link (Chaos & Harmony tab):
    "Events can push or pull Chaos Level → Chaos & Harmony" (#cl-ladder)
  → cross-link (Factions tab):
    "Faction relations shift on Complication → Factions" (#faction-relations)

[SECTION: Rest · small–medium]   #rest
  eyebrow: "Recovery · replenish before the next throw"
  h3: "Rest — pools, costs, and doubling up"
  
  Rest pools table:
    | Pool      | Refills on       | Cap          |
    | Short     | Short rest       | (value TBD)  |
    | Long      | Long rest / day  | (value TBD)  |
  
  Wake costs prose: what spending from each pool costs in dispatch capacity
  Double-up rule: brief description of stacking rest types in the same segment
  Note: trait phases reset on Long Rest (cross-ref hook for Personality)

────────────────────── PART III · SYNTHESIS ──────────────────────
[sub-part divider · cath-eyebrow + ornament]

[SECTION: Trait Integration · medium]   #traits
  eyebrow: "Modifier layer · personality in the roll"
  h3: "Traits — how they plug into the roll"
  
  Prose: traits are not a separate system; they are Fit modifiers and 
  Complication modifiers that fire on phase triggers.
  
  Integration map (table or two-column list):
    | Trait phase | Where it fires         | Effect type        |
    | Positive    | On Success / Crit      | Fit +N or Yield ×M |
    | Negative    | On Fail / Complication | Fit −N or extra Complication |
  
  Stacking note (mirrors the system notes in Personality tab: flat ±N first, ×M last, round once)
  Reset note: Long Rest resets all phases.
  
  → cross-link (Personality tab): 
    "Full trait list with phase details → Personality" (#personality-traits)

[SECTION: Worked Example · large]   #worked-example
  eyebrow: "Synthesis · all systems, one run"
  h3: "Marlow's Medium Journey — end to end"
  
  Narrative walkthrough structured as numbered beats:
    Beat 1: Setup — Marlow's Fit calculated (skills + trait modifier + posture)
    Beat 2: Threshold set — medium carriage dispatch, terrain modifier applied
    Beat 3: Roll 1 — result, band, Resolution + Yield + Duration assigned
    Beat 4: Clock advances — segment 1 of 3 complete, event trigger fires
    Beat 5: Event — trigger type, event anatomy resolved, CL shift noted
    Beat 6: Roll 2 — Complication fires, Complication outcome described
    Beat 7: Rest phase (short) — pool partial refill, wake cost deducted
    Beat 8: Roll 3 — trait positive phase fires on success, Yield multiplied
    Beat 9: Journey resolution — 3-segment outcome ladder applied, final result
  
  Format: alternating prose beat + formula callout block (monospace card)
  so the reader can follow the narrative while seeing the mechanical notation.
  
  No cross-links needed here — this is the terminal synthesis section.
  Optionally: a "Back to top →" jump-link to #engine-hero for reference reuse.

════════════════════════════════════════════════════════════════
END OF TAB
Total estimated scroll height: ~3× the Chaos & Harmony tab
Longest sections: Worked Example, Dispatch, Outcome
Shortest sections: Rest, Trait Integration
════════════════════════════════════════════════════════════════
```
