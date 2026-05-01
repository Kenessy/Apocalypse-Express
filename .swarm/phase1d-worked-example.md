# Marlow's Medium Run — A Fully Worked Journey

> **What this document is:** A first-read walkthrough of a complete medium journey using the 2d6+Fit dispatch system. Every mechanic fires at least once. Read it top to bottom the first time you play.

---

## The Setup

**Route:** Ironveil Depot → Concord Yards
A medium freight run through open scrubland and a chronoshear seam. Total scheduled time: roughly 9 hours. Night departure, 11:00 PM.

**Cargo:** Three pallets of refurbished install gear — converter brackets, splice harnesses, calibration rigs — bound for a forward outpost at Concord Yards that has been running on jury-rig for two weeks. The outpost commander has been on the wire twice already. Stakes are real but not dramatic: nobody dies if this arrives a few hours late, but somebody's shift gets very miserable.

**Weather:** Chronoshear active between waypoints 3 and 4. Predictable on the charts, still dangerous to cross. Klara noted it before boarding. Marlow has run this line before.

**Crew:**

| Name | Role | Ancestry | Key Skill | License | Trait |
|---|---|---|---|---|---|
| Marlow | Driver (cab) | Human | SYS +2 (→ Fit +1) | [RCP] +1 | Methodical |
| Klara | Bastion gunner (rear car) | Cindered (Wrath-Forged) | SLG +2 (→ Fit +1) | [EOD] +1 | Hyperfocus |
| PAVNN | Tender operator | Construct (MULE) | — | — | Service Intelligence |
| Doc | Medic (galley/bunk) | Human | PRY +1 (→ Fit +0) | [MED] +1 | Lazy |

> **Fit conversion note:** In Apocalypse Express, d20 skill modifiers map to the Fit range at roughly half value, rounded. SYS +2 → Fit contribution of +1. A role-trained Driver also gets +1 from being stationed at their post.

---

## The Journey Clock

Medium journey = **8-segment clock**, 4 phases.

```
JOURNEY CLOCK — start of run
█ █ █ █ █ █ █ █
0 / 8 segments filled
```

Phases in order:

| Phase | Task | Threshold | Notes |
|---|---|---|---|
| 1 | Departure | 7 | Routine: cold engine, station clearance |
| 2 | Cruise | 8 | Steady run, open country |
| 3 | Hazard | 11 | Chronoshear seam crossing |
| 4 | Approach | 8 | Slowdown, Concord Yards alignment |

Clock fills as phases succeed. At the end, total segments determine the **journey ladder tier** and affect PLUG cost.


---

## Phase 1 — Departure

**Time:** 11:02 PM. Ironveil Depot is quiet. The platform crew has cleared the last passenger off the rear landing. Marlow runs his pre-departure checklist out of habit — not because dispatch requires it, but because he is the kind of man who does not leave stations without running his checklist.

PAVNN patches in from the Tender: *"Boiler nominal. Pressure at 94%. Ready on your call, Operator."*

This is Marlow's territory. He's done departure hundreds of times. His hands are on the throttle before he consciously decides to put them there.

### Fit Calculation — Phase 1

> **Teaching moment:** Fit is computed fresh each phase. Several sources stack together, and the game displays them as a line-item breakdown before you roll. Nothing is hidden.

```
PHASE 1 — DEPARTURE
─────────────────────────────────────────
Threshold:    7   (easy — station departure)
Marlow's Fit: +5
  SYS mod       +1   (skill → Fit conversion)
  [RCP] license +1   (Rail Crew Proficient trained)
  Role-trained  +1   (Driver at Driver post)
  Methodical    +1   (ROUTINE task — fires)
  PAVNN assist  +1   (Construct assistant, routine)

You need 2+ on 2d6 for S · 5+ for CS · ≤1 for F (CF impossible at this Fit)

Probability preview:
  CS  (total ≥ 12):  ~83%
  S   (total 10–11): ~11%
  F   (total 7–9):   ~4%
  CF  (total ≤ 6):   impossible
─────────────────────────────────────────
```

> **Methodical (Routine +1):** Marlow's trait adds +1 Fit whenever the task is something he's done many times in a familiar context. Departure from a known station is textbook routine. This bonus will NOT apply in Phase 3, where the chronoshear makes the task genuinely novel and hazardous.

> **PAVNN assist (+1):** PAVNN's Service Intelligence trait mirrors the same logic — routine tasks get a +1 to the assisted roll. He is watching gauges, reading pressure curves, calling out clearances. The system records him as the assisting crewmember for this phase.

Marlow rolls 2d6: **5 + 4 = 9.** Total: 9 + 5 = **14.** Margin vs Threshold 7: **+7. → Critical Success.**

```
RESULT: CS  (margin +7)
─────────────────────────────────────────
Resolution:   Critical Success
Yield:        125% — train clears station cleanly,
              minor schedule advantage baked in
Duration:     3h 20m to end of cruise phase
Clock:        +2 → ◆◆ 2/8 segments filled
Complication: none
─────────────────────────────────────────
```

The train rolls out of Ironveil without incident. PAVNN logs the departure at 11:04 PM, two minutes ahead of the scheduled window. Marlow doesn't celebrate. He adjusts the throttle and watches the depot lights shrink in the rear mirror.

```
JOURNEY CLOCK — after Phase 1
◆ ◆ █ █ █ █ █ █
2 / 8 segments filled
```

---

## Phase 2 — Cruise

**Time:** 12:40 AM. The scrubland is dark and flat on both sides. No wind distortion yet — the chronoshear is still three hours ahead. Marlow has the throttle at 70% and the cab to himself.

In the bunk car, Doc is asleep with his coat pulled over his face. Klara has settled onto the rear bench with her SLG field-stripped across her knees — barrel, receiver, feed assembly, all laid out in sequence on a folded utility rag. PAVNN is in the Tender, cycling through pressure diagnostics with the particular low hum that means everything is fine.

This is the quiet part of the run. Marlow watches the gauge needle, watches the track, watches nothing in particular.

### Fit Calculation — Phase 2

```
PHASE 2 — CRUISE
─────────────────────────────────────────
Threshold:    8   (normal — open-country run)
Marlow's Fit: +5
  SYS mod       +1
  [RCP] license +1
  Role-trained  +1
  Methodical    +1   (ROUTINE — still fires)
  PAVNN assist  +1   (routine, still assisting)

You need 3+ on 2d6 for S · 6+ for CS · ≤2 for F · impossible CF

Probability preview:
  CS  (total ≥ 11):  ~72%
  S   (total 9–10):  ~19%
  F   (total 5–8):   ~8%
  CF  (total ≤ 4):   impossible
─────────────────────────────────────────
```

Marlow rolls 2d6: **3 + 4 = 7.** Total: 7 + 5 = **12.** Margin vs Threshold 8: **+4. → Success.**

```
RESULT: S  (margin +4)
─────────────────────────────────────────
Resolution:   Success
Yield:        100% — steady progress, no variance
Duration:     3h 40m (as scheduled)
Clock:        +1 → ◆◆◆ 3/8 segments filled
Complication: none
─────────────────────────────────────────
```

> **Yield vs Resolution:** A Success doesn't mean "barely made it." It means 100% of expected progress — the train covered the distance, the boiler held, the schedule is intact. Yield is about *how much*, not whether you passed. A CS would have given 125% (minor schedule bonus, small edge). An F would yield 50% — the train still moves, but slower, and something might be half-done.

The run settles into its rhythm. No one speaks on comms for nearly two hours.

```
JOURNEY CLOCK — after Phase 2
◆ ◆ ◆ █ █ █ █ █
3 / 8 segments filled
```


---

## Mid-Journey Event — "Boiler Stress" (02:47 AM)

**Trigger type: State-triggered** — the journey clock is at 3/8 segments with a hard phase ahead. PLUG reserves have been ticking down since departure. The system flags a threshold condition and the event card drops.

PAVNN's voice comes over the cab line, flat and factual: *"Operator. Boiler stress indicator at amber. Sustained output has been compressing the secondary loop. I am logging a 14% efficiency loss over the last hour. Recommend intervention before the chronoshear crossing."*

Marlow checks the time. 02:47 AM. The seam is two hours out.

```
╔════════════════════════════════════════════╗
║  EVENT — BOILER STRESS                     ║
║  Trigger:  State (PLUG low, 3/8 clock)     ║
║  Time:     02:47 AM                        ║
╠════════════════════════════════════════════╣
║  STAKE                                     ║
║  The secondary pressure loop is running    ║
║  hot. Left alone, Phase 3 Threshold rises  ║
║  from 11 → 13 (chronoshear already hard;  ║
║  degraded boiler makes it very hard).      ║
║  Intervention now stabilizes it — but at  ║
║  a crew cost.                              ║
╠════════════════════════════════════════════╣
║  CHOICES                                   ║
║                                            ║
║  A) WAKE DOC — TNK + [RCP], Threshold 9   ║
║     Doc has [MED] not [RCP]; his Fit is    ║
║     lower on this task. Lazy fires if      ║
║     this is his Fresh Start (first event); ║
║     +1 Fit, but Duration ×1.5. Costs 1    ║
║     Rest block from Doc's 2 available.    ║
║                                            ║
║  B) SEND PAVNN — auto-resolve, no roll    ║
║     Service Intelligence: routine task,   ║
║     Fit bonus applies. Boiler stabilized. ║
║     Cost: PAVNN unavailable for Phase 3.  ║
║     Marlow loses his assistant bonus on   ║
║     the hardest phase of the run.         ║
║                                            ║
║  C) PUSH THROUGH — no roll, no cost       ║
║     Phase 3 Threshold becomes 13.         ║
║     PAVNN stays available. Marlow keeps   ║
║     +1 Fit — but against a harder wall.   ║
╚════════════════════════════════════════════╝
```

> **Rest note:** Option A would consume 1 of Doc's 2 Rest blocks. Waking a PC costs 1 block; it represents real sleep debt and recovery capacity spent. Doc hasn't touched his Rest blocks yet — this would be his first spend. Option B spends no Rest at all.

**Daniel picks Option B: Send PAVNN.**

The logic is simple and worth watching: PAVNN is a Construct. He doesn't tire, doesn't complain, doesn't use Rest blocks. The cost of sending him to the boiler is purely mechanical — he can't be in two places at once, and the Tender is not the cab. For the duration of Phase 3, Marlow is running without an assistant.

*"PAVNN. Take the secondary loop. Manual flush and reset. I'll run Phase 3 solo."*

*"Understood, Operator. Proceeding."*

The hum in the Tender changes pitch. PAVNN is already moving.

### Cost Ledger Update

```
BOILER EVENT — RESOLVED (Option B)
─────────────────────────────────────────
Boiler status:    STABLE (PAVNN on site)
Phase 3 Threshold: 11  (unchanged — crisis averted)
Rest blocks spent: 0   (no PC woken)

PAVNN status:     OCCUPIED — unavailable Phase 3
Marlow Phase 3 Fit: recalculated (see below)

Marlow loses:
  PAVNN assist    -1   (not available)
  Methodical      -1   (Phase 3 is NOVEL/HAZARD)
Net Phase 3 Fit:  +2
─────────────────────────────────────────
```

This is the trade in clear terms: a stable boiler and unchanged Threshold in exchange for running the hardest phase at Fit +2 instead of Fit +5. Whether that's the right call depends on how the dice fall.

---

## Phase 3 — Hazard (Chronoshear Seam)

**Time:** 04:50 AM. The scrubland has given way to distortion country. The air outside the cab glass looks wrong — slightly doubled at the horizon, like a reflection that hasn't committed to its direction yet. This is the chronoshear seam: a stable tear in local spacetime where two temporal currents run adjacent and occasionally overlap.

Running a loaded freight train through a chronoshear seam is not unusual on the Apocalypse Express line. It is also not routine. The terrain reads differently every crossing. Equipment that worked fine last week might resonate at the wrong frequency. The driver has to feel the track, not just follow it.

Klara is already awake. She's moved to the spotter position on the rear car roof hatch, her SLG reassembled and shouldered. She's not expecting a firefight — she's lighting up the seam-edge terrain with a mounted lumen rig, feeding Marlow visual reference points through the rear cam. This is where her Hyperfocus pays out.

Doc is still in the bunk, which is fine. There's nothing for him here.

### Fit Calculation — Phase 3

```
PHASE 3 — HAZARD (CHRONOSHEAR SEAM)
─────────────────────────────────────────
Threshold:    11  (hard — seam crossing)
              [Stable thanks to Option B]

Marlow's Fit: +2
  SYS mod       +1
  [RCP] license +1
  Role-trained  +1   (still stationed correctly)
  Methodical     0   (NOVEL task — does NOT fire)
  PAVNN assist   0   (OCCUPIED — unavailable)

Klara's Hyperfocus (this phase — her chosen):
  Klara's own Fit: SLG+1 + [EOD]+1 + role +1 + Hyperfocus +2 = +5
  She is not rolling the phase; she is spotting.
  Her Hyperfocus contributes a situational bonus to
  the ENVIRONMENT, not directly to Marlow's Fit.
  [GM call: Klara's spotting reduces environmental
  penalty — Threshold stays at 11 rather than drifting
  higher from visual interference. Her contribution
  is in what she prevents, not what she adds.]

You need 9+ on 2d6 for S · 12+ for CS · 5–8 for F · ≤4 for CF

Probability preview:
  CS  (total ≥ 13):  ~28%
  S   (total 11–12): ~17%
  F   (total 9–10):  ~19%
  CF  (total ≤ 8):   ~36%
─────────────────────────────────────────
```

> **Teaching moment — Methodical does not fire here.** The trait text is explicit: Routine +1 Fit. A chronoshear crossing is by definition novel and dangerous. Marlow's experience is real — but the seam doesn't care about experience. The bonus simply isn't there.

> **Teaching moment — Hyperfocus is Klara's, not Marlow's.** Hyperfocus gives +2 Fit to the PC who has it, on their chosen phase. Klara chose Phase 3. But Klara is not the one rolling the dispatch check — Marlow is. What Klara's bonus does in fiction is keep the environmental pressure from worsening; it doesn't transfer as a flat Fit modifier. The game tracks whose trait it is and who is rolling.

The seam opens ahead of them like a gap in the world. Marlow drops to 40% throttle. The rails are still there — they always are — but the sound of the wheels changes, a harmonic flutter that means the train is running through two moments of time at once.

Klara's lumen rig fires. The terrain ahead snaps into harsh relief: rail curve, ballast scatter, a half-dissolved signal post from an earlier crossing. Marlow has reference points. He works the throttle with both hands.

Marlow rolls 2d6: **2 + 3 = 5.** Total: 5 + 2 = **7.** Margin vs Threshold 11: **-4. → Failure.**

```
RESULT: F  (margin -4)
─────────────────────────────────────────
Resolution:   Failure
Yield:        50% — seam crossed, but rough.
              Speed dropped, schedule slipped.
Duration:     +1h 20m beyond estimated
Clock:        -1 (Hazard phase F penalty) → ◆◆ 2/8
Complication: outcome-triggered event (see below)
─────────────────────────────────────────
```

> **Failure ≠ zero progress.** Yield 50% means the train got through the seam. It did not derail, it did not stall. It came through slower than planned, with more wear than planned, and the clock paid the price. The journey is still happening. Failure costs segments and opens complications — it does not end the run.

The train lurches out of the seam at 05:40 AM, two cars shuddering on slightly misaligned coupling linkage. PAVNN's voice from the Tender, calm as ever: *"Boiler stable. Secondary loop nominal. Phase 3 transit complete. Coupling stress detected."*

```
JOURNEY CLOCK — after Phase 3
◆ ◆ █ █ █ █ █ █
2 / 8 segments filled  (lost 1 from Hazard F)
```


---

## Outcome-Triggered Event — "Coupling Slack" (05:42 AM)

**Trigger type: Outcome-triggered** — Phase 3 Failure activates a minor complication. This is not a crisis; it's the system adding texture to the failure, making the F feel like something rather than just a number going down.

```
╔════════════════════════════════════════════╗
║  EVENT — COUPLING SLACK                    ║
║  Trigger:  Outcome (Phase 3 F result)      ║
║  Time:     05:42 AM                        ║
╠════════════════════════════════════════════╣
║  STAKE                                     ║
║  The seam transit stressed the inter-car   ║
║  couplings. Car 2 has 3mm of slack in the  ║
║  rear link. Not dangerous at current       ║
║  speed. Will become uncomfortable noise   ║
║  and minor instability on final approach  ║
║  unless addressed.                         ║
╠════════════════════════════════════════════╣
║  RESOLUTION                                ║
║  No roll required. PAVNN re-emerges from   ║
║  boiler duty and manually tensions the     ║
║  coupling nut on Car 2 during the low-     ║
║  speed segment after the seam.             ║
║                                            ║
║  Cost: +0.5h duration on Phase 4 timeline  ║
║  No segment loss. No rest spend.           ║
║  Complication absorbed.                    ║
╚════════════════════════════════════════════╝
```

Marlow hears the tension wrench clanking on the undercarriage cam. PAVNN handles it without being asked. That's what Service Intelligence means on the practical end — he reads the situation state and acts on it before the operator has to voice the order.

This event required no roll, cost no Rest, and lost no clock segments. It added half an hour to Phase 4's duration estimate and a half-page of texture to the run. That's the minimum weight of an outcome-triggered complication on a Failure.

---

## Phase 4 — Approach

**Time:** 07:10 AM. Predawn. Concord Yards is visible on the horizon — a string of light clusters marking the cargo sidings and the station roof. Marlow has been awake for just over eight hours. He doesn't feel it yet. He will when he stops.

PAVNN is back in the Tender. The coupling is secured. The boiler is running clean. Klara has come down from the spotter hatch and is back in the crew car with her SLG in its case, drinking something out of a thermos that smells scorched. Doc emerged from the bunk at 06:30, assessed the situation, determined there was nothing medical to do, and went back to the bunk with a different posture — sitting up, reading something on a card deck.

The approach to Concord Yards is routine: slow the train, align to the station track, coordinate with yard dispatch on coupling priority. Marlow's hands know this. The seam crossing doesn't come with him into this phase. Whatever was novel about the last two hours is behind him now.

PAVNN is back as assistant. Methodical fires again.

### Fit Calculation — Phase 4

```
PHASE 4 — APPROACH
─────────────────────────────────────────
Threshold:    8   (normal — station alignment)
Marlow's Fit: +5
  SYS mod       +1
  [RCP] license +1
  Role-trained  +1
  Methodical    +1   (ROUTINE — fires again)
  PAVNN assist  +1   (back from boiler, available)

You need 3+ on 2d6 for S · 6+ for CS · ≤2 for F

Probability preview:
  CS  (total ≥ 11):  ~72%
  S   (total 9–10):  ~19%
  F   (total 5–8):   ~8%
  CF  (total ≤ 4):   impossible
─────────────────────────────────────────
```

> **PAVNN returned:** Because Option B was chosen at the Boiler event — and because PAVNN's task (manual boiler flush) had a clear endpoint — he became available again after Phase 3 completed. His Service Intelligence trait marks the boiler work as a routine task for him, which meant it resolved without complication. He was occupied, not gone.

Concord Yards dispatch comes on the wire. Marlow acknowledges, drops to 20% throttle, and begins the alignment sequence. The yards are just waking up — a few workers on the sidings, a maintenance crawler moving between tracks. Normal morning activity.

Marlow rolls 2d6: **6 + 5 = 11.** Total: 11 + 5 = **16.** Margin vs Threshold 8: **+8. → Critical Success.**

```
RESULT: CS  (margin +8)
─────────────────────────────────────────
Resolution:   Critical Success
Yield:        125% — train aligns to cargo siding
              on first pass; yard crew has docking
              clamps ready before Marlow calls for
              them. Small schedule recovery.
Duration:     2h 10m (slightly ahead of revised ETA)
Clock:        +2 → ◆◆◆◆ 4/8 segments filled
Complication: none
─────────────────────────────────────────
```

The train rolls into its berth with a sound like a long exhale. PAVNN kills the boiler to standby. The cargo doors are unlocked before the brakes have finished cooling.

Marlow sits in the cab for a moment after power-down. Not doing anything. Just sitting.

```
JOURNEY CLOCK — final
◆ ◆ ◆ ◆ █ █ █ █
4 / 8 segments filled
```

---

## Journey Ladder — Final Tally

### Segment log

| Phase | Outcome | Segment change | Running total |
|---|---|---|---|
| 1 — Departure | CS | +2 | 2 / 8 |
| 2 — Cruise | S | +1 | 3 / 8 |
| 3 — Hazard | F | -1 | 2 / 8 |
| 4 — Approach | CS | +2 | 4 / 8 |

**Final clock: 4 / 8 segments.**

### Ladder tier

```
JOURNEY LADDER
─────────────────────────────────────────
6–8 segments:  Smooth Run     — PLUG cost ×0.75
4–5 segments:  On Time        — PLUG cost ×1.0   ← HERE
2–3 segments:  Rough Arrival  — PLUG cost ×1.5
0–1 segments:  Limped In      — PLUG cost ×2.0 + wear
─────────────────────────────────────────
Result: ON TIME
```

**On Time** means the cargo delivery is logged at base rate. No PLUG surcharge, no schedule penalty, no bonus. The outpost at Concord Yards gets their install gear. The two-week jury-rig situation ends at 07:40 AM. Nobody on the wire about it again.

### What the ladder tiers mean in play

> **Teaching moment:** The journey ladder translates clock state into economic consequence. A Smooth Run (6–8 segs) is worth more PLUG — the operator earns a rate bonus for early, clean delivery. On Time (4–5 segs) is neutral. Rough Arrival (2–3 segs) means a 1.5× PLUG cost increase — the operator either absorbs the overhead or passes it to the client, which has its own consequences. Limped In (0–1) is a crisis: heavy cost multiplier, mandatory wear check on the train, possible equipment downgrade.

> Marlow's run hit 4 segments — the floor of On Time. The boiler event and the chronoshear Failure kept it from being a Smooth Run. The Phase 1 CS gave the journey its early cushion. Without that first critical success, Phase 3's -1 would have landed the run at 3 segments and a Rough Arrival tier with a ×1.5 PLUG cost.

### Rest summary

| PC | Rest blocks available | Rest blocks spent | Remaining |
|---|---|---|---|
| Marlow | 2 | 0 | 2 |
| Klara | 2 | 0 | 2 |
| PAVNN | — (Construct) | — | — |
| Doc | 2 | 0 | 2 |

No Rest was consumed on this run. The crew arrives at Concord Yards at full capacity. Option A (Wake Doc) would have spent 1 of Doc's blocks; Doc would have arrived with 1 remaining. The cost of Rest is forward-looking — blocks spent now are blocks unavailable in the next run or during an in-station recovery phase.

---

## Closing Notes — What This Run Demonstrated

| Mechanic | Where it fired |
|---|---|
| Fit computation (per-source breakdown) | Every phase pre-roll card |
| Probability preview before rolling | Every phase card |
| Trait conditional (routine vs novel) | Methodical: on in Ph1/2/4, off in Ph3 |
| Trait conditional (chosen phase) | Hyperfocus: Klara's Ph3 only |
| Assistant as Fit source | PAVNN +1 in Ph1/2/4; absent Ph3 |
| State-triggered event | Boiler Stress at 02:47 AM |
| Event choice with explicit cost ledger | Option B: boiler stable, lose PAVNN Ph3 |
| Rest mechanic (not consumed) | All blocks intact; Option A shown as contrast |
| F outcome = 50% yield, not 0% | Phase 3 — train cleared the seam |
| Outcome-triggered event from F | Coupling Slack — minor complication |
| Journey clock accumulation | Phase-by-phase tally shown |
| Ladder tier from clock total | 4/8 → On Time → PLUG ×1.0 |
| Yield vs Resolution separation | Explained at Phase 2 result |
| Duration as separate from resolution | Noted at Phase 3 F — extra 1h 20m |

The run from Ironveil Depot to Concord Yards was not clean. The chronoshear took something from the clock and the Failure at Phase 3 was genuine. But the choices made before that roll — stabilizing the boiler, keeping the Threshold at 11 instead of 13 — meant the Failure landed in recoverable territory. A CF at Phase 3 would have meant -2 segments and a more serious complication, and if the boiler had been pushed through instead, the Threshold at 13 would have made CF the more likely outcome.

That's what the system is doing underneath the dice: making the pre-roll decisions matter as much as the roll itself.

---

*Document: phase1d-worked-example.md — AGENT D output for Marlow's Medium Run*
*Route: Ironveil Depot → Concord Yards | Clock: 4/8 | Tier: On Time*
