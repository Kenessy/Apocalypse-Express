---
type: codex-root
status: living
last_updated: 2026-04-25
---

# AE-Codex

**The single converging-truth database for the Apocalypse Express campaign.** Built incrementally, fact by fact, only with verified content. When this codex contains everything, the story is done.

---

## Philosophy

This codex is **distinct from `Workshop/`**:

- **`Workshop/`** = brainstorm, drafts, design conversation traces, speculation, things-to-try
- **`AE-Codex/`** = **only what we know for sure** — facts confirmed against canonical sources or explicitly locked by Daniel

If a claim cannot be traced to a Tier 1 or Tier 2 source (see below), it does not belong in AE-Codex. It belongs in Workshop, or in the question backlog.

The asymptotic goal: when every cosmological, mechanical, character, canto, and item question has been answered and entered here, the Apocalypse Express story is complete.

---

## Source ladder

Every fact in AE-Codex carries a provenance citation. The four tiers:

### Tier 1 — Locked Canon
- Daniel explicitly confirmed in conversation, OR
- Documented in a baseline-ready Canto doc (e.g. Canto 1 Redline Covenant v1.7), OR
- Documented in a published rule in `Database/20_Rules/`

Cite as: `[T1: <source>]` e.g. `[T1: Daniel 2026-04-25]` or `[T1: Database/Rule 1 Revival]` or `[T1: Obsidian/Canto 1 v1.7]`

### Tier 2 — Vault Existing Content
- Present in the working Obsidian vault or `Database/` but not explicitly re-confirmed in this session
- Internally consistent and matches surrounding context

Cite as: `[T2: <source>]` e.g. `[T2: Obsidian/Canto 7 v0.1]`

### Tier 3 — Brainstorm Aspiration
- Found in brainstorm canvas or marked as draft
- May be superseded by later iterations
- **Does NOT enter AE-Codex.** Lives in Workshop or as an open question.

### Tier 4 — Speculation
- My extrapolations or pattern-matching
- **Does NOT enter AE-Codex.** Lives only as an open question.

If a Tier 1 fact contradicts a Tier 2 fact, Tier 1 wins; the Tier 2 source gets corrected or annotated.

---

## How to add a fact

1. Verify the source (Tier 1 or Tier 2)
2. Open the relevant doc in AE-Codex/ (or create one if no fit yet — match the existing folder taxonomy)
3. Write the fact concisely with provenance citation
4. Update [INDEX.md](INDEX.md) if a new doc was created
5. If the fact answers an open question, mark it resolved in [Questions.md](Questions.md)
6. Commit with message format: `AE-Codex: <topic> — <one-line summary>`

## How to add a question

1. Identify the gap — something needed to advance the story or design
2. Open [Questions.md](Questions.md) (or a topic-specific question file if very localised)
3. Write the question with: prompt, context, candidate answers (only as seeds, not assumed answers), priority (CORE / IMPORTANT / NICE-TO-HAVE)
4. Commit

When Daniel answers, the answer becomes a Tier 1 fact and gets entered in the right Codex doc.

---

## Folder layout

```
AE-Codex/
├── README.md              ← this file
├── INDEX.md               ← browseable map of all Codex content
├── Questions.md           ← prioritised open question backlog
├── Cosmology/             ← world-state, the spark, factions, the pause
├── Cantos/                ← one doc per chapter / canto
├── Characters/            ← NPCs, recurring figures
├── Mechanics/             ← rules-relevant systems (Hellstatic, Drift, etc.)
└── Items/                 ← Orb, quill, book, chrono machine, World Anchor, etc.
```

Empty folders (created here for taxonomy) get populated as facts arrive. Don't create files speculatively.

---

## Workshop vs AE-Codex — the relationship

- **Workshop/** continues to exist for design conversations, speculation, Lucifer monologue drafts, the iteration trail
- **AE-Codex/** is the distillation — only the verified residue

When a Workshop draft becomes locked-in (Daniel confirms), the relevant fact migrates from Workshop → AE-Codex with a Tier 1 citation. The Workshop doc may keep the fuller draft, but AE-Codex gets the single sentence of truth.

---

*Created 2026-04-25 — the converging-truth phase begins.*
