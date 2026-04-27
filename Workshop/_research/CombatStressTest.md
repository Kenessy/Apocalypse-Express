---
type: research
status: source-material
last_updated: 2026-04-26
agents: 3 × opus general-purpose, 2026-04-26
purpose: Adversarial / edge-case / simulation stress-test of v0.1 combat system
---

# Research — Combat System Stress Test (3-agent swarm)

> Three parallel opus agents adversarially tested the v0.1 combat proposal from `CombatPatterns.md`. This doc preserves their findings as source material.
>
> The synthesis (v0.2 refined system) is locked at [`AE-Codex/Mechanics/Combat.md`](../../AE-Codex/Mechanics/Combat.md).

---

## Agent 1 — Exploit Hunter

**Top critical/high exploits found:**

1. **Save-Scum Roulette** (CRITICAL) — Visible % on Red checks invites reload-until-success. Browser save-state in HTML VN is muscle memory. Fix: hide % → bands; sealed pre-rolls on Red checks at scene entry.
2. **Mirror Mono-Party Universal Solvent** (CRITICAL) — Three Mirrors covers all slots, all Soul bonuses. Fix: Mirror requires category declaration before roll + costs +1 SD per wildcard.
3. **Overboil Snowball** (HIGH) — Boiler chains Pressure d4→d6→d8 if pressure carries between moments. Fix: pressure resets per moment OR carries SD tick.
4. **Rest Treadmill** (HIGH) — If rest refills body pools cheaply, attrition is cosmetic. Fix: rest is narrative resource (limited per chapter, advances doom-clock, costs SD).
5. **One-PC Workhorse** (HIGH) — Best-synergy character does everything; others become tag-fillers. Fix: slot caps per character per encounter (max 2).
6. **Tag-Stack Bypass via Revival** (HIGH) — If Revival lets player re-pick Body Tag, deliberate death = respec. Fix: revival preserves tag OR tag-change carries permanent stat penalty.
7. **White-Check Grind to Mod-Stack Infinity** (HIGH) — Patient retries inflate stacks. Fix: White-check successes give narrative benefit, not stacking mods (or expire end-of-scene).
8. **Crown Grid Multi-Stack Loophole** (MEDIUM) — Anti-stack rules leak via uncovered slot categories. Fix: anti-stack must be categorical (any Crown nullifies any other).
9. **Maw Hidden-Pocket Loot Pre-Stash** (MEDIUM) — Hoard everything for boss. Fix: Pocket cap (3-5 items); items "cool" — can't use same scene as stashed.
10. **Mod-Stack Auto-Success Floor** (MEDIUM) — Stacked +6 makes every check 90%+. Fix: DC scales with stack OR mods cap at +3 visible OR very-high stacks trigger SD.
11. **Encounter Skip via Layer-2 Dominoes** (MEDIUM) — Skip-checks become always-best path. Fix: skip-checks are Red and require worse outcomes (lose loot/relationship).
12. **Soul-Degradation Avoidance Build** (MEDIUM) — Lowest-degradation playstyle = meter never moves. Fix: Degradation rises on scene-tick (every scene +1) regardless of action.

**Critical concerns about the design:**

- Three-layer load may be too heavy for 5-10 min scene
- Visible modifier transparency conflicts with VN re-read culture (save-scumming)
- Body Tag as ONLY hard gate creates binary slot logic
- Soul-Degradation has no fail-state defined
- No defined economy for dice pools

**5 design fixes (consolidated):** Hide exact %, show bands · Mirror requires category declaration · SD ticks on scene-entry not action · Cap white-check carryover · Slot caps per character per encounter.

**What works (defensive validation):**

- No HP bar / narrative termination
- Three outcome bands prevent all-or-nothing UX
- Body Tag separate from Soul Index makes mono-builds harder

---

## Agent 2 — Edge Case Mapper

**28 edge cases catalogued.** Top 5 urgent (Critical):

1. **EC-1/18 — Unfillable slots.** No defined fallback if no party member has the required tag. Hard softlock. **Fix: every Tag-gated slot must define a "Force" or "Off-Tag" option (slot at +1 die penalty, wound-band floor, SD tick).**
2. **EC-5/7/11 — Drained = unslottable softlock.** In forced combat with no rest, all PCs unslottable = hard wall. **Fix: Drained PCs CAN still slot but at degraded outcomes + SD tick instead of body drain.**
3. **EC-6 — Soul-Degradation MAX undefined.** Meter exists but ceiling state undefined. **Fix: At MAX, Fracture event fires — one PC's Soul Index inverts (Wrath bonus becomes liability), authored bad-branch chapter.**
4. **EC-19/20 — Drained vs Broken vs Dead vocabulary.** Player's emotional read depends on knowing what states mean. **Fix: Drained = compromised but conscious; Broken = sits out until authored recovery; Dead = authored only.**
5. **EC-12 — Red check failure with story dependency.** **Fix: Every Red check ships with authored failure branch (worse outcome, scene continues).**

**6 edges-as-features:**

- Fracture event = authored "shadow chapter" with inverted PC
- All-Mirror = "Hollow Train" challenge run (Mirrors pay SD per wildcard = self-imposed challenge)
- Suppressing Soul Index = "Restrained" tag unlocks alternate dialogue
- Intentional grief run = authored "rock bottom" branch
- Tag suspension via wound = natural escalating pressure
- Multi-combat as one extended encounter = pacing-strength reframing

**20 rule clarifications proposed.** Most critical:

- Slot fallback rule (Force option always available)
- Tag-only gating; Soul is modifier never gate
- Drained-but-active rule (degraded outcomes + SD instead of body)
- Broken/Dead/Drained vocabulary
- SD MAX = Fracture event
- Red check failure clause
- White check retry framing rule
- Soul Index opt-in toggle (per-slot suppression)
- Mid-slot drain resolution (assigned dice resolve before drain)
- Mid-encounter revival (only between moments, pool at 1)
- Multi-combat consolidation rule
- Solo-encounter scaling (1-2 slots, halved drain)
- Sub-3 party slot doubling (one PC fills two slots at -1 die penalty)
- Mod-stack UI cap (display 6 max + expander)
- Soft pity / Resolve (3 consecutive wound bands → +1 next die)
- Tag suspension flag (only when wound explicitly carries it)
- Scaling by complexity not numbers
- Soul Index per-encounter recharge (1× per Layer-1 encounter)
- Greyed portrait UX with hover tooltips
- Brace choice before known multi-combat

---

## Agent 3 — Gameplay Simulator

**5 encounters simulated:**

| # | Encounter | Time | Verdict |
|---|---|---|---|
| 1 | Tutorial — depot shamble | ~3 min | Under target — needs more weight |
| 2 | Mid-game — drift drone, attrition pressure | ~6.5 min | **System sings; ad-copy moment** |
| 3 | Lucifer hologram Stack Check | ~2 min | **Highest engagement per minute** |
| 4 | Canto 7 boss — Archon-Auditor | ~7 min combat / 12-13 min scene | **Over target** — 5 moments too many |
| 5 | Solo combat — saboteur | ~3 min | Solo rules carve distinct texture |

**Cross-sim design observations:**

1. **Slot-type vocabulary too narrow** — 4 types (Attack/Defend/Command/Exploit) repeats by Moment 3. Add 2-3 more (Probe, Brace, Subvert) OR add slot modifiers (Loud / Quiet variants).
2. **Bands UI undermined by visible dice** — once player sees [5,3,6] they reverse-engineer math; bands become decorative. Either hide raw dice OR commit to bands fully (show "Best: 6 → CLEAN").
3. **Compromised vs Broken needs unambiguous mechanical statement** — agent had to guess across 3 sims whether Compromised cuts dice or downgrades bands.
4. **Unfilled-slot auto-wound is feature not bug** — but only if previewed before commit. Players who learn it post-hoc reload.
5. **Soul-Degradation as scene meter (not encounter) is design's strongest invention** — Encounter 2 only worked because SD pressure had built across the scene.
6. **PAVNN-assist / CRAM Carriage auto-fill saves boss pacing** — without it Encounter 4 would hit 18 min. Carriage upgrades = quietly the system's most valuable currency.
7. **Mirror is load-bearing class** — answers coverage gaps in 3/5 sims. Risk: too essential. Need second-best wildcard for non-Mirror parties.

**3 NEW design suggestions from sim:**

1. **"Strained" composite status** — replace off-tag triple-penalty (extra die + wound floor + SD tick) with single named status whose tooltip lists all three. Reduces UI noise.
2. **PAVNN-assist tier as Carriage progression axis** — Carriage upgrades explicitly buy auto-fills per scene (CRAM tier 2 = 2 auto-fills/scene). Gives upgrades felt mechanical impact.
3. **"Coverage Preview" before scene-start** — show player which slot-types party covers natively. Frontloads planning so unfilled-slot wound feels earned not surprise-tax.

**Bottom line:** "the proposed system plays the way the agents claim in 4 of 5 sims. Encounter 2 is the proof-of-concept. Encounter 4 reveals slot-vocabulary repetition risk at boss length. The remaining gaps are UX-density and rule-clarity issues, not architecture flaws — the bones are sound."
