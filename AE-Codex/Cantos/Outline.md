---
type: campaign-outline
status: seed — partial canon
last_updated: 2026-04-25
---

# Cantos — campaign outline

> The campaign is structured as **a Prelude + a sequence of Chapters/Cantos**. This doc tracks structure and naming.

---

## Structure (clarified 2026-04-25)

**The Prelude** = the Null Meridian "obsidian-setting" content. Players wake dead, sign Lucifer's pact, get printed bodies, exit the chapels, and reach the Apocalypse Express. Currently consists of: *[T1: Daniel 2026-04-25]*

| Scene | Doc location | Content |
|---|---|---|
| A1 Null Meridian Prelude | `Database/40_Scenes/(Scene) A1` | Wake on the obsidian platform, meet Cicero |
| A2 Obelisk, Clock & Postcards | `Database/40_Scenes/(Scene) A2` | The countdown begins, silver postcard |
| A3 Train Arrival & Boarding | `Database/40_Scenes/(Scene) A3` | The AE arrives, players board |
| A4 Gossip Car & Golden Tickets | `Database/40_Scenes/(Scene) A4` | Tickets discovered, social beat |
| A5 Sundown Saloon | `Database/40_Scenes/(Scene) A5` | Lucifer's pitch, sign the pact, Orb mission set |
| B1 Chapel of Second Chances | `Database/40_Scenes/(Scene) B1` | Revival in printed bodies, Lucifer briefing |
| B2 Chapel of the Second Dawn | `Database/40_Scenes/(Scene) B2` | Storage room puzzle, exit toward the AE |

**Chapters** = the actual campaign that happens AFTER the prelude. Sketched in the brainstorm canvas (working/canon names) with parallel earlier Obsidian planning docs (alt names + early structure):

| # | Canon name (brainstorm canvas) | Alt name (Obsidian planning doc) | Detail status |
|---|---|---|---|
| 1 | **The Gauntlet** | "Redline Covenant" (Obsidian Canto 1, baseline-ready v1.7) | sketched + alt detailed; **canon name is "The Gauntlet"** |
| 2 | **As Above so Below** | "Underlines" (Obsidian Canto 2 v0.2) | seed |
| 3 | **MUTATED JUNGLE?** (WIP marker) | "The Verdant Frontier" (Obsidian Canto 3 v0.2) | seed |
| 4 | **Burning Bridges** | — | concept only |
| 5 | **(placeholder, no name)** | — | empty |
| 6 | **Drifting away** | — | concept only |
| 7 | **The World Anchor** | (Obsidian Canto 7 v0.1, name preserved) | seed |
| 8 | **To Hell and Back** | — | concept only |
| 9 | **Siege of DarkHold** | — | concept only |
| 10 | **Gambit for the 9th rank** | — | concept only — likely matches the climax architecture in `Workshop/Climax/` |

**Naming convention locked:** brainstorm canvas names are canon. Obsidian planning docs use alt names but cover the same arcs. *[T1: Daniel 2026-04-25 — "Sval a gauntlet majd lesz ahol az orbot szerzik meg az első nagy arc / könyv"]*

> [!important]
> **The actual chapter content has NOT been written in detail.** The Obsidian planning docs are sketches. Daniel: *"még messze van"* — designing them is far-off work. **Don't over-invest in chapter-internal architecture until they're being actively designed.**

---

## What's locked per canto

### Chapter 1 — The Gauntlet (alt: Redline Covenant)

**Goal:** Secure the Apocalypse Express, fuel it, install the Orb. *[T2: Obsidian/Canto 1 v1.7 planning doc]*

**Critical path (planning):** Station (Offboarder set-piece) → Dam Complex → Ruins/Tunnel Entrance → Tunnels/Temple (Orb retrieval) → Mount Orb in AE locomotive. *[T2: Obsidian/Canto 1 v1.7]*

**Exit condition:** `orb_installed=True` AND `ae_ready=Fueled` *[T2]*

**Daniel's framing:** *"első nagy arc / könyv sok mini locationnel"* — first big arc/book with many mini-locations. *[T1: Daniel 2026-04-25]*

**This means: the Orb is acquired and mounted in Chapter 1. NOT in the climax.** *[corrects earlier Workshop assumption — climax design needs revisiting]*

> [!todo] DEFERRED
> Daniel: *"még messze van"*. Don't over-design until actively being built. Obsidian planning doc has lots of sketched detail (Kassad / Sorrel / Voss NPCs, evidence cards, flag dependencies, set pieces) — preserved for reference but not extracted into Codex until Daniel reactivates this chapter.

---

### Chapter 2 — As Above so Below (alt: Underlines)

**Goal:** Escape the collapsing Gauntlet with the Orb, traverse the Underlines (Metro → Ossuary/Catacombs → Natural Caves), surface on the far side. *[T2: Obsidian/Canto 2 v0.2]*

**Read flags:** `orb_installed=True`, `ae_ready ∈ {Secured, Fueled}` *[T2: Obsidian/Canto 2 v0.2]*

**Set piece:** Ghost-Train Interchange (timed gap-leap via wind-up booster) *[T2: Obsidian/Canto 2 v0.2]*

**Level range:** 3-5 *[T2]*

---

### Chapter 3 — MUTATED JUNGLE? (alt: The Verdant Frontier)

**Goal:** Traverse the **mutated jungle**; at the **overgrown SABRE/A-Tech military station**, **salvage the armored carriage** housing the **'Clear-Sky' CRAM** (if possible). *[T2: Obsidian/Canto 3 v0.2]*

**Set piece:** Overgrown SABRE/A-Tech military station — armored carriage with 'Clear-Sky' CRAM. *[T2]*

**Sets flag:** `cram_installed ∈ {False, True}` *[T2]* — used in Canto VII

**Level range:** 5-7 *[T2]*

---

### Chapter 7 — The World Anchor (name preserved across both)

**Goal:** Neutralize the **World Anchor's Trueflow projection** so it stops unfreezing legacy ordnance and the AE can pass. *[T2: Obsidian/Canto 7 v0.1]*

**Reads flags:** `cram_installed=True` (acquired in Canto III), `pavnn_present`, `party_mark_state` *[T2]*

**Sets flags:** `trueflow_radius_final=Zero`, `cram_state=Ejected`, `ordnance_fallout`, `glass_severity`, `ae_stress`, `heaven_attention=True` *[T2]*

**Set pieces:**
- **Twin-Towers Split** (Above: Celestial / Archon-Auditor · Below: Mirror-Hell / Chain-Warden) *[T2]*
- **CRAM Barrage Defense** (PAVNN-assisted) *[T2]*
- **Lucifer Chain-Melt** (finale) *[T2]*

**Lucifer materializes physically for the first time** in this canto, melting the final two chains. *[T2: Obsidian/Canto 7 v0.1]* This bends the rules — sets flag `heaven_attention=True`.

**Celestials are extermination-minded utilitarians** — PCs bearing infernal marks (from A5 pact) are executed on sight. No parley. *[T2]*

**Doctrine source: "Order 7/Delta — Purge Protocol"** — mark-class Infernal = terminate *[T2]*

> [!todo] OPEN — many
> What is the World Anchor physically? What is Trueflow, mechanically and cosmologically (relation to the chrono machine)? What does the Project TRUEFLOW evidence card reveal? Where does Chapter 7 sit chronologically in the train route? Is Lucifer's appearance here the same Lucifer the players met in A5, or a different aspect?

---

## What's NOT yet locked

- Cantos IV, V, VI, VIII, IX, X (whether they have docs / their actual canon names)
- The Gambit for the 9th rank concept (was Canto X in brainstorm; may still be the climax title — needs confirmation that the climax architecture in `Workshop/Climax/` matches Canto X's intended shape)
- The Siege of DarkHold concept (was Canto IX; brings the atomic bomb — may still be canon)
- Travel structure (does the train cover Cantos I → X linearly, or with branches / side excursions?)
- Pacing (sessions per canto)

→ [../Questions.md](../Questions.md) for the question backlog.
