# Workshop

Work-in-progress design space — character architectures, story drafts, foreshadow chains, world-state notes, and brainstorm scratchpads.

**Workshop is intentionally separate from `Database/`.** The Database is the canonical, structured rulebook the GM brings to the table. Workshop is the unstructured WIP space where ideas get worked out *before* (sometimes) being promoted into Database.

---

## Start here

→ **[INDEX.md](INDEX.md)** — browse all current content.

→ **[SCRATCHPAD.md](SCRATCHPAD.md)** — chronological log of what was decided when, and why.

If you're a new agent (Claude or otherwise), read INDEX first to know what exists. Then this README for conventions. Then dive into the topic the user is asking about.

---

## Conventions for agents

### Read before writing

Check what's already here. Don't duplicate, don't quietly overwrite. INDEX.md is the fastest way to scan.

### Append, don't overwrite

Unless explicitly asked to replace something, **add a dated section** rather than overwriting. The user wants to see how thinking evolved. Specifically:

- **In OVERVIEW docs**: amend or add new sections; don't destroy old ones unless they are wrong
- **In QUESTIONS docs**: when a question is decided, change the heading to `## Question N — DECIDED YYYY-MM-DD` and replace options with the decision + rationale. Keep the heading.
- **In SCRATCHPAD**: append a new dated entry. Never edit old ones.
- **In INDEX**: update the relevant table when adding a new doc. Keep entries to one sentence.

### Frontmatter convention

Every doc should start with YAML frontmatter:

```yaml
---
type: [character | location | climax | world-state | mechanic | reference | questions | index | scratchpad]
status: [stub | wip | locked | living]
related: [list of related doc paths]
canonical_sources: [list of Database paths if applicable]
last_updated: YYYY-MM-DD
---
```

Status meanings:
- **stub** — placeholder, mostly empty
- **wip** — work in progress, expect changes
- **locked** — major architecture decided; updates should be additions, not rewrites
- **living** — meant to be continuously updated (INDEX, SCRATCHPAD, QUESTIONS)

This frontmatter is **machine-parseable**. Future agents (or scripts) should be able to query Workshop by type, status, related, etc.

### Templates

When adding a new doc, **start from a template** in `_templates/`:

- `_templates/CHARACTER_TEMPLATE.md` — for new NPCs, companions, antagonists
- `_templates/LOCATION_TEMPLATE.md` — for new world locations, scenes' physical settings
- `_templates/QUESTIONS_TEMPLATE.md` — for any new "open decisions" file

Copy the template, rename it, fill it in. This keeps structure consistent across the database.

### Mark uncertainty

Use Obsidian-style callouts:

- `> [!todo] heading` — for unresolved questions or open work
- `> [!important] heading` — for load-bearing facts
- `> [!summary]` — for the doc's TL;DR (usually at the top)
- `> [!warning] heading` — for things that conflict with canonical Database content

### Folder discipline

- **Don't create empty folders speculatively.** Wait until there's content to put in them.
- **Use clear folder names** that match the topic (e.g. `Cicero/`, `Climax/`, `World/`)
- **Avoid hyphens or spaces** in folder names — keep them simple identifiers

### Linking within Workshop

Use **Obsidian-friendly relative paths**: `[Cicero](Cicero/OVERVIEW.md)`. Markdown links work in both Obsidian and standard markdown viewers.

### Linking to canonical Database

Use full paths from repo root: `Database/40_Scenes/(Scene) A1 Null Medirian Prelude.md`. Don't rely on relative paths to Database from Workshop, because the file structure in Database may move and Workshop should not be brittle to it.

**Important:** do not link from `Database/00 Master Index.md` or any canonical Database file *back to Workshop*. Workshop must not pollute canonical navigation.

### Promoting Workshop content to Database

When something is finished and ready to be table-facing rules / scenes, **ask the user before moving it**. Do not promote on your own initiative. The Database has its own structure and conventions; promotion is a translation step, not a copy.

---

## Current top-level structure

```
Workshop/
├── README.md           ← this file
├── INDEX.md            ← browseable map
├── SCRATCHPAD.md       ← dated idea dump
├── Factions.md         ← top-level faction map
├── Cicero/             ← character: the chronicler-NPC
├── AICore/             ← faction: AI Core / aSync / PAVNN
├── Climax/             ← campaign endgame architecture
├── World/              ← world state, locations
└── _templates/         ← starter templates for new content
```

See [INDEX.md](INDEX.md) for everything inside.

---

## What does NOT belong in Workshop

- Final, table-facing rules → `Database/20_Rules/`
- Final, run-ready scenes → `Database/40_Scenes/`
- Compiled player/GM books → `Database/Compiled/`
- Image assets for the public site → `docs/`
- Code or build scripts → `Tools/`

---

## When in doubt

- The **user** is the final source of truth on creative decisions
- The **Database** is the canonical reference for rules and scenes already written
- **Workshop** is the conversation space where ideas live before they earn a permanent home

If a Workshop doc disagrees with Database, **the Database wins** unless the user explicitly says otherwise. Mark the conflict with `> [!warning]` and surface it.

---

*This README and the surrounding structure was set up 2026-04-25 during the Cicero / climax / cosmology design conversations. Maintain it; improve it; treat the next agent (which might be you) with the courtesy of clear conventions.*
