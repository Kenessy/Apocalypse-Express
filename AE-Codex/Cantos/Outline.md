---
type: campaign-outline
status: seed — partial canon
last_updated: 2026-04-25
---

# Cantos — campaign outline

> The campaign is structured as a series of Cantos. This doc tracks the canon-name mapping, status of each canto's design, and where the source-of-truth lives.

---

## Canon name vs brainstorm name

The brainstorm canvas (`Assets/Canvas/(Canvas) Ideas brainstorming.canvas`, `[T3]`) listed 10 chapter names that were an **earlier iteration**. The **current canonical names** come from the **Obsidian Canto X.md docs** in `Brainstorming, Drafts and ideas/Chapter (Canto) High level brainstorming/`.

| # | Brainstorm name (T3, may be retired) | Canonical name (T2 from Obsidian Canto doc) | Doc status |
|---|---|---|---|
| I | The Gauntlet | **The Redline Covenant** | baseline-ready v1.7 |
| II | As Above so Below | **Underlines** (subtitle "As Above, So Below") | seed v0.2 |
| III | MUTATED JUNGLE? | **The Verdant Frontier** | seed v0.2 |
| IV | Burning Bridges | TBD — no Obsidian doc found | TBD |
| V | (placeholder, no name) | TBD | TBD |
| VI | Drifting away | TBD — no Obsidian doc found | TBD |
| VII | The World Anchor | **The World Anchor** (name preserved) | seed v0.1 |
| VIII | To Hell and Back | TBD — no Obsidian doc found | TBD |
| IX | Siege of DarkHold | TBD — no Obsidian doc found | TBD |
| X | Gambit for the 9th rank | TBD — no Obsidian doc found | TBD |

> [!todo] OPEN — see [../Questions.md](../Questions.md)
> Are Cantos IV, V, VI, VIII, IX, X currently undesigned, or do their docs exist somewhere I haven't found? If undesigned: are the brainstorm names still aspirational targets, or have those been retired too?

---

## What's locked per canto

### Canto I — The Redline Covenant

**Goal:** Secure the Apocalypse Express, fuel it, install the Orb. *[T2: Obsidian/Canto 1 v1.7]*

**Critical path:** Station (Offboarder set-piece) → Dam Complex → Ruins/Tunnel Entrance → Tunnels/Temple (Orb retrieval) → Mount Orb in AE locomotive. *[T2: Obsidian/Canto 1 v1.7]*

**Exit condition:** `orb_installed=True` AND `ae_ready=Fueled` *[T2: Obsidian/Canto 1 v1.7]*

**This means: the Orb is acquired and mounted in Canto I. NOT in the climax.** *[T2 — corrects an earlier Workshop assumption]*

> [!todo] OPEN
> Read the full Canto 1 doc and extract every additional locked fact (set pieces, NPCs Kassad / Sorrel / Voss, evidence cards, flag dependencies, etc.) into per-canto / per-character codex docs.

---

### Canto II — Underlines (As Above, So Below)

**Goal:** Escape the collapsing Gauntlet with the Orb, traverse the Underlines (Metro → Ossuary/Catacombs → Natural Caves), surface on the far side. *[T2: Obsidian/Canto 2 v0.2]*

**Read flags:** `orb_installed=True`, `ae_ready ∈ {Secured, Fueled}` *[T2: Obsidian/Canto 2 v0.2]*

**Set piece:** Ghost-Train Interchange (timed gap-leap via wind-up booster) *[T2: Obsidian/Canto 2 v0.2]*

**Level range:** 3-5 *[T2]*

---

### Canto III — The Verdant Frontier

**Goal:** Traverse the **mutated jungle**; at the **overgrown SABRE/A-Tech military station**, **salvage the armored carriage** housing the **'Clear-Sky' CRAM** (if possible). *[T2: Obsidian/Canto 3 v0.2]*

**Set piece:** Overgrown SABRE/A-Tech military station — armored carriage with 'Clear-Sky' CRAM. *[T2]*

**Sets flag:** `cram_installed ∈ {False, True}` *[T2]* — used in Canto VII

**Level range:** 5-7 *[T2]*

---

### Canto VII — The World Anchor

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
