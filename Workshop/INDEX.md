---
type: index
status: living
last_updated: 2026-04-25
---

# Workshop — Index

> Browse-friendly map of all Workshop content. **Start here** if you're a new agent (or Daniel returning to the project after a gap) and want to know what exists.
>
> See [README.md](README.md) for conventions and how to add new content.

---

## How this is organised

- **Top-level reference docs** — used across many topics (Factions, Cosmology)
- **Topic folders** — characters, world locations, climax architecture
- **Templates** — under `_templates/`, for use when adding new content
- **Scratchpad** — chronological idea dump, append-only

---

## Top-level

| Doc | What it is |
|---|---|
| [README.md](README.md) | Conventions for agents working in Workshop |
| [INDEX.md](INDEX.md) | This file — navigable map |
| [Factions.md](Factions.md) | Top-level faction map (humanity / Lucifer / AI Core) and the players as the only true free-will agent |
| [SCRATCHPAD.md](SCRATCHPAD.md) | Dated, append-only idea dump |

---

## Characters

| Doc | What it is | Status |
|---|---|---|
| [Cicero/OVERVIEW.md](Cicero/OVERVIEW.md) | The chronicler-NPC; obsidian quill; commissioned by Lucifer to write the world's record | Architecture locked |
| [Cicero/QUESTIONS.md](Cicero/QUESTIONS.md) | Open decisions about Cicero (book details, voice, etc.) | 4 decided, 5 still open |
| [AICore/OVERVIEW.md](AICore/OVERVIEW.md) | The AI Core / aSync — third orthogonal faction; "I am inevitable" logic | Architecture locked |
| [AICore/PAVNN.md](AICore/PAVNN.md) | The companion robot; sulfur accumulator; sacrifice in Hell | WIP |
| [AICore/QUESTIONS.md](AICore/QUESTIONS.md) | Open decisions about AI Core and PAVNN | 7 open |

> [!todo] Future characters to add
> Lucifer's own dedicated overview doc (currently scattered between A5 references and Climax/LuciferMonologue.md). Other recurring NPCs as they are introduced.

---

## World

| Doc | What it is | Status |
|---|---|---|
| [World/PausedApocalypse.md](World/PausedApocalypse.md) | The double apocalypse held in stasis by Lucifer's chrono machine; visual / cinematic guide; "judder forward" zones | Locked |

> [!todo] Future world docs to add
> - `World/BrokenEarth.md` — geography of the surface, regions the B-arc covers
> - `World/Darkhold.md` — the previous map / origin of the atomic bomb
> - `World/OrbVault.md` — where the Orb is hidden, what guards it
> - `World/HALT.md` — the Null Meridian / cross-realm transit, mechanics
> - `World/Hell.md` — geography of Hell, deepest level (final arena)

---

## Climax

| Doc | What it is | Status |
|---|---|---|
| [Climax/OVERVIEW.md](Climax/OVERVIEW.md) | Full 20-step climax architecture; humanity / robot / Lucifer paths; new hellfire foreshadow | Architecture locked |
| [Climax/LuciferMonologue.md](Climax/LuciferMonologue.md) | The address-to-God monologue verbatim + 7-stage analysis + companion train-reveal line | Locked |
| [Climax/EndingsTable.md](Climax/EndingsTable.md) | Comparison matrix per ending; pre-locked elements; hidden / future paths | Locked |

> [!todo] Future climax docs to add
> - `Climax/PAVNN_FinalSpeech.md` — when written
> - `Climax/Cicero_FinalWords.md` — when written
> - `Climax/LocomotivePuzzle.md` — detailed puzzle mechanics for Phase 2A

---

## Templates (for agents)

| File | Purpose |
|---|---|
| [_templates/CHARACTER_TEMPLATE.md](_templates/CHARACTER_TEMPLATE.md) | Starter for new character architecture docs |
| [_templates/LOCATION_TEMPLATE.md](_templates/LOCATION_TEMPLATE.md) | Starter for new world / location docs |
| [_templates/QUESTIONS_TEMPLATE.md](_templates/QUESTIONS_TEMPLATE.md) | Starter for new open-decisions docs |

---

## Future folders (planned but not yet created)

- `Weavers/` — the Fates / fabric-of-fate weavers; book-repair branch (hidden 4th ending)
- `Lucifer/` — dedicated overview doc for Lucifer himself (currently distributed)
- `Items/` — the Orb, the quill, the book, the chrono machine, the atomic bomb — each as its own doc when fleshed out
- `Foreshadow/` — cross-cutting timeline view; what is planted where, when each anchor lands

---

## Quick browse — by question

**"Who is who?"** → [Factions.md](Factions.md)

**"What is the world like?"** → [World/PausedApocalypse.md](World/PausedApocalypse.md)

**"How does the campaign end?"** → [Climax/OVERVIEW.md](Climax/OVERVIEW.md), [Climax/EndingsTable.md](Climax/EndingsTable.md)

**"Tell me about Cicero."** → [Cicero/OVERVIEW.md](Cicero/OVERVIEW.md)

**"Tell me about the AI Core / PAVNN."** → [AICore/OVERVIEW.md](AICore/OVERVIEW.md), [AICore/PAVNN.md](AICore/PAVNN.md)

**"What does Lucifer say to God at the end?"** → [Climax/LuciferMonologue.md](Climax/LuciferMonologue.md)

**"What's been decided lately?"** → [SCRATCHPAD.md](SCRATCHPAD.md) (most recent entries first when read top-to-bottom — wait, actually entries are appended, so latest is at bottom)

**"What still needs deciding?"** → search for `> [!todo]` callouts across all docs, or check `*/QUESTIONS.md` files

**"How do I add new content?"** → [README.md](README.md) → "Conventions for agents"

---

## Index maintenance

When adding a new doc to Workshop:

1. Place it in the right folder (or create one with a clear name)
2. Add YAML frontmatter (see [README.md](README.md) → "Frontmatter convention")
3. **Add a row to this INDEX.md** under the right section
4. If it's a major architectural addition, also append a SCRATCHPAD entry with the date and rationale

Keep this index lean — link, don't duplicate. Descriptions ≤ one sentence.
