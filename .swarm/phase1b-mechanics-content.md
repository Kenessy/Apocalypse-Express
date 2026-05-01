# Apocalypse Express — Rules & Mechanics Content
### Draft for Character-Creation Tutorial Tab · AGENT B Output · Phase 1b

---

## Quick Start (30 Seconds)

Here is how a roll works, start to finish.

You have a **Fit** number — your character's combined edge on the task. The task card shows a **Threshold** — the difficulty target. You roll **2d6, add your Fit, and compare the total to the Threshold**.

Four things can happen: a **Critical Success (CS)**, a **Success (S)**, a **Failure (F)**, or a **Critical Failure (CF)**. The gap between your total and the Threshold decides which band you land in. Beat it by 3 or more? CS. Meet it up to +2? S. Miss it by 1–3? F. Miss by 4 or more? CF.

Before you even pick up the dice, the task card tells you your Fit, the Threshold, and the probability of each band — so you always know what you're rolling for and what to roll to hit it.

From there, four separate fields come out of the roll: what happened (Resolution), how much you got done (Yield), how long it took (Duration), and whether anything extra went sideways (Complication). These are tracked separately — not collapsed into a single "outcome." That distinction matters, and it will make more sense in a few sections.

---

## The Roll

### What you're rolling: 2d6 + Fit vs. Threshold

Every check in Apocalypse Express follows the same structure:

> **Roll 2d6, add your Fit. Compare the result to the Threshold.**

The four result bands are defined by the *margin* — how far your total lands above or below the Threshold:

| Band | Label | Margin |
|---|---|---|
| Critical Success | **CS** | Total ≥ Threshold + 3 |
| Success | **S** | Total = Threshold to Threshold + 2 |
| Failure | **F** | Total = Threshold − 1 to Threshold − 3 |
| Critical Failure | **CF** | Total ≤ Threshold − 4 |

### What the player sees before rolling

The task card displays everything you need before you touch the dice:

```
TASK: Reroute boiler feed line
Fit:       +2   (your number)
Threshold: 11   (the task's difficulty)

To hit CS → roll 9+ on 2d6   (probability: 28%)
To hit S  → roll 6–8 on 2d6  (probability: 44%)
To hit F  → roll 3–5 on 2d6  (probability: 25%)
To hit CF → roll 2   on 2d6  (probability:  3%)
```

You can see your odds before committing. If something about the situation has changed — a trait applies, a crewmate can assist — now is when you account for it.

### A beat-by-beat example

Mira is patching a cracked coupling on the boiler feed line. The task card reads: **Fit +2, Threshold 11**.

She rolls 2d6: a 4 and a 5, total 9. She adds her Fit: 9 + 2 = **11**.

Her total equals the Threshold exactly — that's a margin of 0, which puts her in the **S (Success)** band (Threshold to Threshold + 2).

The task card reads out the four fields for an S result:
- **Resolution:** Success
- **Yield:** 100% — the line is fully patched
- **Duration:** 20 minutes (set by the task card, unmodified)
- **Complication:** none

If her roll had been 9 + 2 = 11... wait, she rolled 9 total, plus Fit +2, equals 11. That hits Threshold on the nose — Success. Had the dice shown 3+5=8, plus Fit +2 = 10 — that's Threshold − 1, a **Failure**, partial repair only. Had she rolled 4+4=8, she'd still have hit 10 — same Failure. The dice and Fit together determine everything. Simple, visible, no hidden math.

---

## Fit

**Fit** is your character's total modifier for a given task. It represents skill, preparation, equipment, and support — everything stacked into one number before you roll.

### The formula

```
Fit = Skill mod + License bonus + Trait modifiers + Gear/Prep + Assistant
```

- **Skill mod** — derived from your canon d20 skill rank: `floor(d20_mod / 2) + role_trained_bonus (0 or 1)`. A character with a +4 d20 modifier and role training gets `floor(4/2) + 1 = +3`.
- **License bonus** — +1 if you hold the relevant discipline license: `[MED]` for medical tasks, `[EOD]` for explosive ordnance, `[RCP]` for railcraft and power systems. No license? No bonus.
- **Trait modifiers** — some traits add or subtract Fit depending on context (more on this in the Traits section).
- **Gear/Prep** — having the right tools or having prepared ahead of time can add +1.
- **Assistant** — a crewmate actively helping you adds their assist die, which translates to a bonus.

Fit ranges from **−2** (an untrained rookie in a crisis) to **+5** (a legendary specialist in peak conditions).

### Three examples

**Example 1 — Rookie medic, wrong job.**
Sable has Heal +1 on her sheet (d20 mod +1). She's assisting with a railcraft repair, which is outside her training. No [RCP] license, no relevant gear, no assistant.
`Fit = floor(1/2) + 0 + 0 + 0 + 0 = 0`
She's rolling at flat, no modifier. The dice carry her alone.

**Example 2 — Trained crewmate, right job.**
Rook is a mechanic. His TNK (Tinkering) mod is +3 from his d20 sheet, he holds an [RCP] license, and he's got his full toolkit (Gear +1).
`Fit = floor(3/2) + 1 + 0 + 1 + 0 = 1 + 1 + 1 = +3`
He's rolling comfortably above average.

**Example 3 — Specialist with assistance.**
The same Rook, but this time Mira is actively assisting (she's a trained helper, counts as +1 assist), and his Trait — Methodical — gives +1 Fit on routine tasks.
`Fit = floor(3/2) + 1 + 1 (trait) + 1 + 1 = +5`
That's the ceiling. On a Threshold 11 task, he only needs to roll a 6 on 2d6 for a Success.

---

## Threshold

**Threshold** is the task's difficulty number. It's set by the task card and is always visible before you roll. Think of it as the target the dice and Fit need to reach.

### The five-tier scale

| Difficulty | Threshold | What this looks like |
|---|---|---|
| Easy | 7 | Routine maintenance, a path you've walked a hundred times |
| Normal | 9 | Standard field repair, competent work under mild pressure |
| Hard | 11 | Critical system under load, unfamiliar terrain at night |
| Very Hard | 13 | Jury-rigged fix mid-derailment, emergency surgery in a moving car |
| Heroic | 15 | One shot at a cascading boiler failure with borrowed tools |

Most checks in a standard journey sit at 9 or 11. You'll see 13 when things are genuinely going wrong. 15 means the situation has become a crisis moment.

### Modifiers to Threshold

The base difficulty is modified by two factors, which are folded into the Threshold value shown on the card before you roll — you never calculate them yourself mid-session.

**Environment** pushes the Threshold up or down depending on conditions: working in howling ashfall, in zero-visibility steam, or on a shaking coupling between cars adds +1 or +2. Sheltered, stationary, good lighting subtracts 1 from the base.

**Time pressure** increases Threshold when the clock is tight. If the task must be completed before the next phase ticks over and you're behind, the GM may apply a +1 or +2 time-pressure modifier. The task card reflects this — you will not be surprised by a hidden modifier at resolution.

> **Example:** Fixing a burst pressure valve has a base Threshold of 9. Working during a Chronoshear Flare (visibility near zero, instruments unreliable) adds +2. The card shows Threshold 11. That's what you roll against.

---

## Outcome — Four Fields, Not One

This is the most important structural thing to understand about how Apocalypse Express resolves tasks.

Most games give you one "outcome": you succeed or fail, and the GM narrates what that means. Apocalypse Express splits the result of every roll into **four separate fields**, each tracked independently:

| Field | What it answers |
|---|---|
| **Resolution** | Which band did you land in? (CF / F / S / CS) |
| **Yield** | How much of the task's value did you get? |
| **Duration** | How long did the task take? |
| **Complication** | Did something extra go wrong (or unexpectedly right)? |

### Why four fields?

Because traits and gear and circumstances affect these differently — sometimes in opposite directions.

Here's the problem that four fields solves: imagine a trait that makes you thorough but slow. If "outcome" were a single track, you'd have to pick whether the trait makes you better or worse overall. With four fields, the trait can be precise: it improves one field while penalizing another, without muddying the resolution.

### The Methodical trait — a live example

The **Methodical** trait card reads:

```
TRAIT: Methodical
On a ROUTINE task:   +1 Fit
On a NOVEL task:     Yield ×0.75
```

Notice what it does NOT say: it doesn't give you +1 Fit AND Yield ×0.75 at the same time. Each condition triggers a different field:

- Routine task: your **Fit** goes up (you're in your groove — better chance of the S or CS band)
- Novel task: your **Resolution** is unaffected — but whatever you produce is worth 25% less (**Yield** drops). You're less efficient outside your comfort zone, but the roll itself isn't penalized.

This matters in play: a Methodical mechanic attempting a routine boiler check gets +1 Fit — he's more likely to succeed. The same mechanic trying a novel emergency jury-rig gets no Fit bonus, and even if he succeeds (S or CS), the Yield is reduced — the improvised solution is less effective. Two different fields. Two different interventions. Neither contaminates the other.

### Yield reference

| Band | Yield |
|---|---|
| CS | 125% — extra progress, bonus loot, or superior result |
| S | 100% — full task value |
| F | 50% — partial result; task incomplete or less effective |
| CF | 0–25% — minimal or no result; complication likely |

### Duration note

Duration is set by the **task card**, not by the roll result. Rolling a CS does not mean the task took less time — unless a trait or gear modifier explicitly targets the Duration field. This keeps time management predictable and allows traits that do modify duration (like Service Intelligence's Duration ×0.5 on routine tasks) to be meaningfully distinct from raw skill bonuses.

---

## Dispatch and the Journey Clock

### What dispatch is

A single roll covers one task in one moment. **Dispatch** wraps a whole journey's worth of work into a structured sequence of rolls, aggregating their results into a single outcome for the journey.

Every journey is divided into **phases**. Each phase is one 2d6 + Fit roll against a Threshold. The result of each phase advances (or retreats) a **Journey Clock**, which tracks how close the train is to a smooth arrival.

### Journey length and clock size

| Journey | Phases | Clock segments |
|---|---|---|
| Short | 1–2 | 4 |
| Medium | 3–4 | 8 |
| Long | 5 | 12 |

### How the clock ticks

Each phase resolution moves the clock:

| Phase result | Clock movement |
|---|---|
| CS | +2 segments |
| S | +1 segment |
| F | 0 (or −1 on a hazard phase) |
| CF | −2 segments + complication triggers |

> **Example:** You're on a Medium journey — 8-segment clock, 4 phases. Phase 1 goes CS (+2), Phase 2 is S (+1), Phase 3 is F (0), Phase 4 is S (+1). Clock ends at 4 of 8 — 50% filled.

### The journey outcome ladder

At journey's end, compare filled segments to maximum:

| Clock fill | Journey result | Effect |
|---|---|---|
| 75–100% | **Smooth run** | PLUG cost ×0.5, +1 minor reward |
| 50–74% | **On time** | PLUG cost at base rate, no extras |
| 25–49% | **Rough arrival** | PLUG cost ×1.5, 1 minor wear on installs |
| 0–24% | **Limped in** | PLUG cost ×2, major complication on arrival |

The clock's final state is what the crew brought the train home with. A single bad phase hurts but rarely destroys a journey — the multi-phase structure means one CF can be recovered from if the crew adapts.

> **Note:** The Journey Clock only applies to **journey work-slots** — the ongoing crew assignments during travel. Combat encounters and social scenes have their own resolution structures and do not tick the journey clock.

---

## Events

Events are interruptions that fire during a journey — things that demand the crew's attention now, while the train is moving and the clock is ticking.

### The four trigger sources

Events fire from four sources, and the crew will usually know which kind is hitting them:

**1. Authored / scripted** — The GM wrote this event into the journey as a specific narrative beat. It fires at a predetermined moment regardless of how the rolls are going. A stowaway reveals herself during the mountain pass. A contact makes contact.

**2. Outcome-triggered** — A phase resolves as F or CF, and that result automatically fires an event. The failure didn't just lose clock segments — it woke something up. A missed rail coupling triggers a pressure spike. A botched navigation choice brings a hazard fauna encounter.

**3. State-triggered** — Something about the train's current condition crosses a threshold. PLUG reserves drop below a critical level, fauna pressure reaches maximum, a key install takes too much wear. These events fire when the state condition is met, not on a roll result.

**4. Random** — Each phase has a 1-in-6 chance of spawning a mini-event, a small complication or opportunity that the GM rolls for behind the screen. Random events are lower stakes but keep the journey unpredictable.

### Anatomy of an event card

Every event has the same structure:

```
TITLE:    What this is called (one-line narrative hook)
TRIGGER:  Why it fired (which of the four sources)
STAKE:    What's at risk if the crew ignores it
CHOICES:  2–4 options, each listing:
          - Cost (PLUG / clock segments / Rest / Duration / item wear)
          - Optional Roll (skill + Threshold)
          - Outcome (immediate state changes)
```

### Three example events

---

**EVENT: Boiler Stress** *(state-triggered)*

```
TITLE:    Boiler Stress
TRIGGER:  State — PLUG reserves fell below 20%
STAKE:    Continued operation degrades the boiler lining;
          CF on next phase adds permanent install wear

CHOICE A: Emergency vent
  Cost:    −1 clock segment
  Roll:    none
  Outcome: Boiler stress cleared; PLUG burn rate normalized

CHOICE B: Push through and ration
  Cost:    −1 PLUG per remaining phase
  Roll:    TNK vs. Threshold 11 each phase
  Outcome: On S/CS, no further degradation; on F/CF, boiler lining takes wear

CHOICE C: Wake the engineer
  Cost:    1 Rest block (from engineer's pool)
  Roll:    TNK vs. Threshold 9
  Outcome: On S/CS, stress cleared and PLUG burn rate reduced for 2 phases
```

---

**EVENT: Stowaway** *(authored / scripted)*

```
TITLE:    Stowaway
TRIGGER:  Scripted — fires on Phase 2 of the Ashfall Crossing run
STAKE:    Unregistered passenger creates faction risk (Hellfire Authority
          inspection at destination); if discovered by a CF, escalates to
          custody demand

CHOICE A: Report immediately
  Cost:    −1 faction relation (Underside contacts)
  Roll:    none
  Outcome: Stowaway detained; faction relation loss logged; no further risk

CHOICE B: Hide them in the cargo hold
  Cost:    Duration +10 minutes at destination (thorough unload cover)
  Roll:    STL vs. Threshold 9
  Outcome: On S/CS, stowaway hidden; on F, +1 complication charge at inspection

CHOICE C: Negotiate passage fee
  Cost:    none (if stowaway has PLUG — roll to determine)
  Roll:    GIL vs. Threshold 11
  Outcome: On CS, +2 PLUG gained; on S, break even; on F/CF, faction rumor spreads
```

---

**EVENT: Chronoshear Flare** *(environmental)*

```
TITLE:    Chronoshear Flare
TRIGGER:  Random — rolled on Phase 3 of any Long journey through the Ashen Belt
STAKE:    Temporal distortion causes navigation instruments to lag;
          next phase Threshold increases by +2 unless mitigated

CHOICE A: Reduce speed and wait it out
  Cost:    −1 clock segment
  Roll:    none
  Outcome: Threshold penalty for next phase cancelled; clock takes the cost instead

CHOICE B: Navigate by landmarks (manual override)
  Cost:    none
  Roll:    RDL vs. Threshold 13
  Outcome: On S/CS, flare navigated without clock loss; on F, Threshold penalty stands;
           on CF, −1 clock segment AND Threshold penalty

CHOICE C: Use PAVNN-assisted routing (if a PAVNN unit is aboard)
  Cost:    −1 PLUG
  Roll:    SYS vs. Threshold 9
  Outcome: On S/CS, full correction — no penalty, no clock loss; on F, same as Choice A
```

---

## Rest

Every PC on the crew starts each journey with a **Rest pool** — a small reserve of recovery capacity that represents their ability to be woken mid-journey for urgent tasks without burning out.

### Pool sizes by journey length

| Journey | Rest blocks per PC |
|---|---|
| Short | 1 |
| Medium | 2 |
| Long | 3 |

### The wake cost

Certain events — particularly state-triggered ones like Boiler Stress — can wake a sleeping crew member, pulling them into an unscheduled task. When this happens, the woken PC spends **1 Rest block**.

What happens to their Rest total matters:

| Rest state | Effect |
|---|---|
| Rest 1+ available | No penalty — they're fine |
| Rest 0 (just spent their last block) | −1 Fit for the rest of the journey |
| Rest −1 (woken a second time, same journey) | −2 Fit, and CF chance increases on their rolls |
| Rest below −1 | PC cannot be assigned to additional tasks except mandatory events |

Rest degradation is cumulative. A PC woken three times on a Long journey is functionally compromised by the final phase.

### Making it tangible

Wake your medic at 03:00 to handle the boiler pressure spike. She spends her last Rest block — Rest pool hits 0. From that point on, every roll she makes takes a −1 Fit penalty. If the boiler fails again at Phase 4 and you wake her a second time, she's at −2 Fit and rolling with an elevated CF chance. By arrival, she's barely functional.

Was it worth it? That's the crew's call — and it's a real call, with real consequences.

### The Double-up option

Two crew members can **share a wake event**, splitting the cost:

- Each PC spends **0.5 Rest blocks** (round up to 1 if they're already at 0)
- The pair gains **+1 Fit** on the resolution roll for that event

Double-up works well when the event requires a skill neither PC has at full competence, or when one PC is already resting on their last block. Two tired people cooperating can outperform one exhausted person working alone — and the Fit bonus makes the better resolution band more reachable.

---

## Traits — How They Plug In

Every character in Apocalypse Express carries one or more **Traits** — personality and background qualities that mechanically interact with the four outcome fields (Fit, Yield, Duration, Complication, Threshold).

The key thing to understand: **traits don't just make you better or worse in general.** Each trait card explicitly states which field it targets and under what condition. When you read a trait, you're reading a precise modifier instruction, not a vague flavor note.

### How to read a trait card

A trait card always has:
- A **condition** — when does this apply?
- A **field** — which of the four outcome fields (or Fit, or Threshold) does it modify?
- A **modifier** — the numeric or proportional change

### Three traits, walked through

---

**TRAIT: Methodical**

```
On a ROUTINE task:
  → +1 Fit

On a NOVEL task:
  → Yield ×0.75
```

*Condition splits by task familiarity, not by roll result.* When the task is something your character has done many times — a routine inspection, their standard check — the Methodical trait improves their roll odds (+1 Fit). When the task is unfamiliar, it doesn't hurt the roll, but whatever they produce is less effective (Yield reduced to 75%). The message: Methodical characters are most valuable when deployed on work they know well.

---

**TRAIT: Hyperfocus**

```
Before Phase 1 of any journey, choose one phase.

On the chosen phase:
  → +2 Fit

On all other phases:
  → −1 Fit
```

*Player declares the chosen phase before the journey begins — no changing it mid-run.* Hyperfocus is a high-variance trait: devastating if the chosen phase lines up with a critical moment, punishing if the journey doesn't go where you expected. A Hyperfocus character planned for Phase 3 who faces a brutal CF on Phase 1 can't redirect. This trait rewards journey planning and punishes improvisation.

---

**TRAIT: Service Intelligence (PAVNN)**

```
On a ROUTINE task:
  → +1 Fit
  → Duration ×0.5

On a NOVEL task:
  → −1 Fit
  → Duration ×1.5
```

*This trait modifies two fields simultaneously — Fit and Duration — and it flips direction based on familiarity.* The PAVNN unit is blazingly efficient at catalogued work (routine: better roll, faster execution) and significantly slower on tasks outside its knowledge base (novel: worse roll, longer task). Duration ×0.5 matters on a journey clock where every phase counts — a PAVNN crew member working routine tasks is genuinely valuable as a clock-segment protector. Working novel tasks, they cost you in both resolution quality and clock time.

---

### A note on field targeting

When you pick your character's traits during creation, consider which fields each trait affects and how those interact with your intended role. A character primarily assigned to routine maintenance slots benefits enormously from Methodical or PAVNN. A character expected to handle novel crises or emergency decisions will find those same traits actively detrimental. Traits are not simple bonuses — they're field-specific bets on how your character will be deployed.

---

*End of Agent B content draft — Rules & Mechanics, Phase 1b.*
