---
type: research
status: source-material
last_updated: 2026-04-26
agent: opus general-purpose, 2026-04-26
purpose: Combat resolution patterns for AE's HTML dice-driven VN
---

# Research — Combat Resolution Patterns in Dice-Driven Narrative Games

> Agent-produced survey of how successful narrative-priority dice games handle combat, with a synthesis of 7 design patterns and 3 top recommendations for the Apocalypse Express HTML VN format.
>
> **This is research source material**, not Codex canon. The Codex doc derived from it lives at [`AE-Codex/Mechanics/Combat.md`](../../AE-Codex/Mechanics/Combat.md).

---

## Per-game findings

### Citizen Sleeper (2022) + Citizen Sleeper 2 (2025)

- **Mechanic**: 1–5 d6 dice pool per cycle; player slots dice into action nodes; each slot has 3 outcome bands (1–2 / 3–4 / 5–6) modified by skill
- **Body matters**: *Condition* caps dice pool size; CS2 *stress* permanently breaks dice until repaired
- **Time**: ~30 sec per decision; combat is multi-cycle contracts
- **Steal**: **Risk-tiered slots with three outcome bands** — leaves prose room for partial-success/cost narration

### Disco Elysium (2019)

- **Mechanic**: 2d6 + skill vs. DC. White Checks (retryable), Red Checks (one-shot, story-locking)
- **Modifier transparency**: Shows full stack ("Logic +2, Hangover −1, Pride of Office +1, you wear the disco shirt +1, DC 12 — 58%")
- **Time**: 1–3 checks across a 2–8 minute conversation
- **Steal**: **The transparent modifier stack** — every contributing factor laid out makes a single die feel earned

### Roadwarden (2022)

- **Mechanic**: Hidden rolls behind text choices; preparation-as-modifier
- **Steal**: **Preparation-as-modifier** — every consumable, item, or in-fiction prep step prints onto the modifier list, making combat feel like consequence of earlier scenes

### Cultist Simulator (2018)

- **Mechanic**: No dice. Card-and-timer. Slot Reason/Passion/Health/Funds cards into verb slots. Failure spawns Dread/Fascination cards that propagate
- **Steal**: **Slot-the-character-as-card** — treat each AE party member as a "card" with attributes; combat nodes have slot requirements (e.g., "needs HUM + Wrath")

### Sunless Sea / Sunless Skies

- **Mechanic**: Storylet quality-checks with **percentage success preview shown to player**
- **Sunless Skies facets**: instead of "+1 to Iron," player picks story snippet from captain's past — every stat increase is backstory
- **Steal**: **Show the percentage before the click, label every option with the stat it uses** — gold-standard UX for choice-driven dice combat

### Reigns (2016)

- **Mechanic**: Binary swipe (Tinder-style)
- **Steal**: **Hidden state machine + binary swipe** — useful for AE's quick non-boss encounters (random horrors on the rail line) where mechanical depth would distract

### Pathologic 2 (2019)

- **Mechanic**: Real-time melee; *stamina shares a bar with thirst*
- **Steal**: **Body resources are combat resources** — HUM bleeds, CYB overheats, SYN loses coherence; combat *consumes the body* in tag-specific ways

### Slay the Princess (2023)

- **Mechanic**: Dialogue trees only; internal "Voices" (Hero, Skeptic, Stubborn, etc.) act as quasi-stats — a chorus speaking different options
- **Steal**: **The chorus of voices as soul-archetype combat** — closest existing model to AE's Soul Index. During combat, each Soul archetype whispers a different option ("Wrath: break his jaw"; "Pride: name him a coward"); player picks which voice to obey

### Secondary references

- **80 Days**: Time-as-currency
- **ChoiceScript**: 3–6 round rhythm of named verbs, each a stat check
- **Tales of Maj'Eyal**: Talent trees with category-mastery multipliers
- **Twine combat**: Descriptive prose with stat-checks gating which choices are available

---

## Seven distinct patterns

**P1. Slot-the-Die** (Citizen Sleeper) — Each combat node is a card with named slots; player drags dice from a per-character pool into slots. 3 outcome bands (1–2 / 3–4 / 5–6). Body Tag and Soul Index print modifiers onto each slot.

**P2. Transparent Stack Check** (Disco Elysium + Sunless Skies) — Single 2d6 + modifier vs. visible DC, with every modifier laid out on screen. Pick option, click, see prose.

**P3. Voice-Chorus Combat** (Slay the Princess + Cultist) — No dice at all. Each Soul archetype offers one tonally-distinct line/action; player picks which voice to obey.

**P4. Card-Slot Party Tactics** (Cultist Simulator) — Each combat node demands a party member with specific Body Tag / Soul tags. Player decides *who* to send into the slot before any dice are rolled.

**P5. Body-as-Resource Attrition** (Pathologic + Citizen Sleeper) — Combat consumes a tag-specific body resource: HUM bleeds, CYB overheats, SYN loses coherence.

**P6. Storylet-Round Verbs** (ChoiceScript / Failbetter) — Combat lasts 3–5 named "rounds." Each round shows 3–4 verbs ("Press," "Hold," "Bait," "Withdraw"), each gated to a stat with shown odds.

**P7. Single-Swipe Tonal Combat** (Reigns) — Non-boss / atmospheric encounters: one-paragraph horror beat with two binary choices that adjust party-state meters.

---

## Top 3 recommendations for AE

### Recommendation 1 — Hybrid: P4 + P1 for primary boss/major encounters

Combat is presented as a sequence of 3–6 "moments." Each moment is a card with 1–3 slots. Each slot reads in English: "Hold the breach (needs HUM or CYB; consumes 1 die; 1–2 → wound, 3–4 → hold + minor cost, 5–6 → hold clean)." The player first picks *which party member* fits the slot (P4 — Body Tag gate makes the choice meaningful), then assigns dice from that character's pool (P1).

**Why it fits AE**: HTML-native, 5–10 min/scene budget, Body Tag is structural, Soul Index plugs in as per-slot modifier, D&D-port-friendly (each "moment" → D&D round, dice slots → attack rolls/saves, outcome bands → partial success structure).

### Recommendation 2 — P2 (Transparent Stack Check) for skill-driven and "internal" confrontations

For Disco-Elysium-style scenes where the conflict is *interpersonal or internal* (a sermon, a stand-off, a mind-touch with an Outside thing), use a single 2d6 + visible-stack check. Every Soul Index, Body Tag, Cicero-companion-bonus, and prior-choice modifier prints visibly above the die.

**Why it fits AE**: 30–90 second resolution inside a longer scene, lets cosmic-horror scenes be combat-without-combat, Soul Index temperaments differentiate (Pride wins commands that Wrath can't), maps to D&D as straight skill check / saving throw.

### Recommendation 3 — P5 (Body-as-Resource Attrition) as the connective tissue

Layer this *under* recommendations 1 and 2. Every character has a Body Tag-specific small reservoir (HUM = Blood/Stamina, CYB = Heat/Charge, SYN = Coherence/Echo) and a shared Soul-degradation meter (analogous to Sleeper Condition or Sunless Terror). Combat doesn't kill — it *drains*. Drained characters can't slot into the next encounter without a rest beat.

**Why it fits AE**: Makes combat consequential without being lethal, gives the multi-character party real teeth, slow-burn D&D pacing, cosmic horror tone, body tags differentiate visibly in fiction.

### Combined architecture (one-paragraph spec)

> A combat scene is 3–5 "moments." Each moment is either a Stack-Check (P2, ~45 sec) or a Slot-Card with 1–2 dice slots (P1+P4, ~90 sec). Slots are Body-Tag-gated and Soul-modified, with three outcome bands and visible odds. Win/lose, every roll drains a tag-specific body pool plus 1 point of party-wide Soul-degradation. Scenes end when the encounter resolves narratively, never when an HP bar empties. Total combat budget: 4–7 minutes inside a 5–10 minute scene, leaving prose room. Future D&D port: each moment becomes a round; slots become actions; pools become HP + exhaustion + sanity.

---

## Sources

(Full reference list preserved in agent's original report — 37+ links to dev blogs, GDC talks, postmortems, Reddit / Codex discussions, official wikis. Available on request.)
