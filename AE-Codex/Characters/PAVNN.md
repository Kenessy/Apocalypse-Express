---
type: character
status: locked-core
last_updated: 2026-04-26
related: [AICore.md, Lucifer.md, ../Factions/A-Tech.md, ../Factions/aSync.md, ../Cosmology/Overreach.md]
---

# PAVNN

> The party's android companion. **A-Tech-built mule-rated cargo android**, found dormant in the basement crypt of the Chapel of Second Chances ("PAVNN Bay"). Lucifer wakes him with a finger-snap (bypassing the activation phrase the chapel staff never knew). Pass-the-baton control across all players; exempt from the Combat Ally cap. Operates as the campaign's emergency-automation NPC across multiple chapters: TPK Reserve print, Marking ritual Witness, Dam-fueling, CRAM targeting. **At the climax, his sulfur accumulator's burst nullifies Lucifer's protective spell — mechanically necessary for the humanity-path final boss fight to be winnable.**
>
> His name is the chess metaphor made flesh: **PAVNN = pawn**. The piece that can promote, the piece that gets sacrificed in classic openings, the piece that never claims any rank for itself.

---

## Origin — LOCKED 2026-04-26

**A-Tech build.** *[T1: Daniel 2026-04-26 + Tier 1 handout `Terminal Log - Mule Workaround Proposal.md`: "A-Tech buried in its spine"]*

A-Tech is a Sombra-Corp-style megacorp that mass-produces most of the world's robotics. PAVNN is a standard product of their **mule-rated** android line — designed for cargo hauling, not frontline combat. *[T1: Daniel 2026-04-26]*

He pre-dates the Pause. Found dormant in the chapel basement crypt by the players in B1.

See [`../Factions/A-Tech.md`](../Factions/A-Tech.md).

---

## Physical description — LOCKED

*[T1: Database/Scene B1 v1.5+]*

When **off**:
- Slumped frame in the basement crypt's "loading chair"
- Bunked next to the piled corpses of A-Tech chapel workers — Mason Harrow's terminal log: *"the one by the bodies"*

When **active**:
- Unfolds from the chair
- Chest panel glows (once, then again, brighter)
- Servos whine softly during motion
- Eyes come up with a **faint amber ring**

Other physical facts:
- **Spine** with A-Tech-buried safeties (anti-tamper / self-defence measures, undefined specifics)
- "**Mule-rated**" classification (cargo-class lifting and hauling)
- **Humanoid bipedal, human-sized.** *[T1: Daniel 2026-04-26]* Engineering rationale: **standardized to fit human-rated equipment** — doorways, vehicles, tool ergonomics, control panels. Anything designed for human use also accommodates him. This is also why the "loading chair" works for him in the basement crypt.

---

## Voice — LOCKED

*[T1: Database/Scene B1.5]*

- **"Flat but clear."**
- First spoken line on waking:
  > *"Acknowledged. Objective: support contracted souls. Destination: Apocalypse Express, then final rendezvous."*
- Speaks in **succinct, professional, datapad-style sentences**
- Lucifer addresses him *"as if addressing a clerk"* — the employer-employee register matches
- Looks at the players **"with the mild curiosity of a machine seeing new cargo"**

Workshop-stage future-direction note (Tier 3, for sacrifice scene only): the synth voice can carry **occasional warmth** ("not as literary as Cicero. Matter-of-fact, with occasional warmth that catches in his synth voice."). *[T3: Workshop/AICore/PAVNN.md — to be re-confirmed when sacrifice speech is written]*

**Pronoun usage** — narration treats him with deliberate ambiguity:
- B1.5 narration: **"it"** ("the android's chest panel… it glances at you")
- B2 GM tips and Workshop docs: **"he"** ("low-key, built for work, voice flat")

This is intentional uncertainty about personhood. GM can lean either way contextually — start dehumanised, accrue personhood as players bond.

---

## Activation — LOCKED

*[T1: Database/Scene B1.5 + Stanza 2 lore handouts]*

Standard A-Tech androids of this class **require an activation phrase** to boot. The chapel staff (per Mason Harrow's GateLinq Advisory terminal log) **knew the phrase was needed but did not know what it was**, so PAVNN sat dormant in the basement until the apocalypse hit.

**Lucifer activates him with a finger-snap** in B1.5 — bypassing the phrase requirement entirely. This is a privileged authentication channel: Lucifer has authorization that the standard A-Tech crew didn't. *[T1: Database/Scene B1.5]*

**The activation phrase itself is never quoted in any vault source.** Mason Harrow's "Mule Workaround Proposal" memo describes a possible alternative — a **"maintenance hot-start"** (partial activation, not a full boot, just enough to get him upright and carrying) — but the GM-note on the handout flags this as **"non-actionable for players (no steps)."** It's flavor lore, not a player puzzle.

> [!todo] OPEN
> Was the activation-phrase backstory intended to be a **playable puzzle** (players have to find the phrase), or **only flavor** (the handouts establish that the phrase exists, but players never need it because Lucifer handles it)? Daniel-confirm.

---

## Mechanical roles — LOCKED

PAVNN is the campaign's **emergency-automation NPC**: every system that needs an "in case the players fail / forget / aren't here" backup falls to him.

### 1. TPK Reserve print auto-start *[T1: Database/Rule 1 Revival]*

If all PCs die and no Sparkplugs are inserted, **PAVNN auto-starts one Reserve print** (8h + 2d4) and locks the Train until it completes. First PC decants with +1 Major. He is the **only entity** with this authority. As long as he is alive, the campaign cannot end via TPK.

### 2. Combat Ally exemption *[T1: AE_CC_Master §0.4.4]*

PAVNN is a **"Train system / crew asset, not a summoned soul."**
- Does **NOT count** toward any PC's 1-Combat-Ally cap
- **Pass-the-baton control**: any player can drive him in combat, swappable per scene
- Not bonded to any single PC — he is the party's shared asset

### 3. Aspects of Chaos Witness fallback *[T1: Database/Procedure Aspects of Chaos]*

If no PC volunteers as Witness for Lucifer's Marking ritual, PAVNN can serve so the ceremony proceeds and play does not stall.

### 4. Canto 1 — AE water-fueling automation *[T2: Obsidian/Canto 1 v1.7]*

When the Dam Complex objective is completed (any of three solution paths), PAVNN **autonomously detects the coupled AE and runs the fill sequence**. The party's success at the Dam translates mechanically as "Dam done → water flows → AE fills." PAVNN handles all the pumping logic.

### 5. Canto 7 — CRAM Carriage targeting AI *[T2: Canto 7 + Gear-CRAM Carriage]*

Canto 7's CRAM Barrage Defense set-piece **requires PAVNN present** (`pavnn_present` flag is a precondition).
- PAVNN has **two assist modes** the GM picks per barrage window:
  - **Targeting** (live engagement)
  - **Forecast** (predictive)
- Mechanics still TBD; the role is locked, the specific dice/resolution is not.

### Combat behavior baseline

Per B1.5: **"Not built for frontline combat; in fights it tends to hunker down or follow simple orders."** *[T1]*

So while he occupies a Combat Ally slot, he is **not a heavy hitter** — he carries gear, opens doors, runs basic repairs, and follows player commands. The Code rule says "supporting voice, not a second GM."

---

## The chess metaphor — LOCKED

**PAVNN = pawn (literal).** *[T1: Daniel 2026-04-25, captured in `../Cosmology/Overreach.md` and previously in ChessGame.md]*

His name was chosen deliberately to invoke the chess piece. The pawn:
- Is the lowest-rank piece
- Can promote on reaching the 8th rank
- Is the piece classically **sacrificed in opening gambits**
- Never claims any rank for itself

This name-anchors PAVNN's role in the climax sacrifice (see below). Per [`../Cosmology/Overreach.md`](../Cosmology/Overreach.md), the chess metaphor is one of several overlapping framings for the **9th rank / Overreach** cosmology — PAVNN is its visual cornerstone.

> [!important]
> "PAVNN's pawn-sacrifice should feel mechanically and narratively like a pawn promotion that doesn't go through — he doesn't ascend; he stays a pawn but gives his life so the game can continue." — `../Cosmology/ChessGame.md` (now folded into `Overreach.md`)

---

## Climax role (humanity path) — LOCKED

**Steps 17-18 of the 20-step humanity-path climax sequence** *[T2: AE-Codex/Climax/Overview.md, derived from Workshop/Climax/]*

After the locomotive crashes into Hell, PAVNN's **internal sulfur accumulator** bursts. Sulfur is unique to "this side" (Hell / the otherworld); it **nullifies Lucifer's sustained protective spell** that protects his true form. As the accumulator's sulfur acid leaks, the spell dies. Without it, the quill (now sword in otherworld physics) can wound Lucifer's true form.

**PAVNN's sacrifice is mechanically necessary for the humanity-path final boss fight to be winnable.** Without him, the quill bounces off Lucifer.

He delivers a **final speech** before passing — Workshop draft notes: not as literary as Cicero, more matter-of-fact, with occasional warmth catching in his synth voice. Themes (per Workshop): what he was, who built him, why he was on the train; that he was always doing what he was told but he chose to actually care along the way; the "free will inside obedience" theme; a line connecting digital and organic mortality. *[T3: Workshop/AICore/PAVNN.md — final speech text not yet drafted]*

---

## Per-ending fate

*[T2: AE-Codex/Climax/Overview.md]*

| Path | PAVNN's fate |
|---|---|
| **Humanity** | Sacrifice in Hell (sulfur accumulator burst) |
| **Robots (AI Core ascendance)** | Becomes part of the gamma'd robot ascendance |
| **Lucifer (compliance)** | Dies with the world in the firestorm |

---

## Loyalty chain

*[T1 confirmed: he serves the party; T2/T3 derived: the chain]*

Per Workshop's working architecture (consistent with locked surrounding facts):
1. **Lucifer** commanded him: "serve AI Core" (i.e., follow the train's mainframe)
2. **AI Core** commands him: "help the party"
3. **PAVNN** does what he was told: helps the party

He has free will at the **tactical** level (how to help, what jokes, when to volunteer info) but the foundational **why** (helping the party at all) was decided for him before the campaign began.

This is the **simpler structural mirror of Cicero's chain** — both are commissioned servants whose execution-level autonomy doesn't extend to questioning their commission. Cicero believes his work is his own life-ambition; PAVNN believes his orders are his job. PAVNN is *less* to grieve about than Cicero in one sense (he never thought he was an artist), but *equally* tragic in another (he never had the chance to choose something else). *[T3: Workshop/AICore/PAVNN.md — character-architecture parallel pending Daniel confirmation]*

---

## Recurring on-train interactions

PAVNN appears in **chess-in-mirror scenes** opposite Lucifer's hologram throughout the campaign — Lucifer playing chess in the reflection, with PAVNN on the player-visible side. *[T1: Daniel 2026-04-25, captured in `Lucifer.md`]*

Open Q18: do Cicero and PAVNN **see Lucifer themselves** in those mirror scenes (commissioned-agent privilege), or do the players see them looking at a mirror that contains a third figure only the players perceive?

---

## Cross-references

- [`AICore.md`](AICore.md) — PAVNN's commanding system; sibling-faction product (aSync R&D, A-Tech post-acquisition)
- [`Lucifer.md`](Lucifer.md) — PAVNN's ultimate employer; the snap that wakes him
- [`Cicero.md`](Cicero.md) — structural mirror; the parallel commissioned servant
- [`../Factions/A-Tech.md`](../Factions/A-Tech.md) — the corp that built him
- [`../Factions/aSync.md`](../Factions/aSync.md) — the absorbed sister-corp that built the AI Core that commands him
- [`../Cosmology/Overreach.md`](../Cosmology/Overreach.md) — the chess metaphor that names him
- [`../Climax/Overview.md`](../Climax/Overview.md) — his climactic sacrifice in context
- [`../Items/ApocalypseExpress.md`](../Items/ApocalypseExpress.md) — the train that may "mistrust" him (per train-as-loyalty-being lock) if AI Core's agenda manifests too clearly

---

## Workshop reference

The fuller architecture, including foreshadow timeline and final-speech stub, lives in [`../../Wo