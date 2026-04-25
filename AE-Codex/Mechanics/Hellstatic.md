---
type: mechanic
status: full
last_updated: 2026-04-25
---

# Hellstatic — Soul-Shell Desync

> Death-residue mechanic that triggers when a player has accumulated 3 Major injuries. The soul and the printed body lose alignment with each repeated death.

**All facts in this doc come directly from `Database/20_Rules/(Rule) 1. Revival.md`.** *[T1: Database/Rule 1 Revival]*

---

## When it activates

- **Active only** while the character has **3 Major injuries**
- **Dormant** below 3 Major injuries (no HS checks rolled)
- **HS persists as a value** even when dormant — it doesn't reset when injuries drop

---

## How it accumulates

- Each time the character **dies while at 3 Majors**, **HS +3**
- **Tracked unbounded** internally
- For check rolls, use **effective HS = min(HS, 20)**
- **−3 HS per Long Rest** (decays during recovery)

---

## How it triggers in play

When **Active** (character at 3 Majors), before each **declared** test:

1. Player declares the specific action / test (incl. reactions)
2. Roll a **Hellstatic d20**
3. If the roll is **≤ effective HS**, the declared test is at **HARD Disadvantage**
4. If **effective HS = 20**, the character has **constant Disadvantage** (skip step 2)

---

## Override semantics

HS is a **Hard Override**:
- It **ignores any Soft Advantage**
- **HARD vs HARD = Normal** (cancels out), then resolve **SOFT**, then roll
- The chosen state **persists through rerolls of the same test**

---

## Character lore frame

The mechanic represents **Soul-Shell Desync** — the soul and the printed body losing alignment after multiple deaths and reprints. With each death-while-injured, the new printed body fits the soul slightly less well, until physical attempts begin to fail unpredictably. Long rests recover some alignment.

---

## Cross-references

- **Rule 1 Revival** — the parent system; Hellstatic is its section §7
- **Devil's Mercy** procedure — does NOT cancel HS checks (HS is Hard Override) *[T1: Database/Procedure Devil's Mercy]*
- **Ancestry / Soul Indices** — Major injuries deferred via certain ancestries don't count toward HS while deferred *[T1: Database/Ancestry Layer Soul Indices + Body Tags v2]*

---

## What this is NOT

- **Not the Spark word** (the cosmological term Lucifer uses for what he gave humanity). Daniel explicitly clarified 2026-04-25: *"jah hellstatic egy mechanika amikor sokszor meghalt a player vagy valami"* — Hellstatic is a death mechanic only.

The "Hellstatic rename?" note in the brainstorm canvas referred to renaming **this mechanic** (or possibly something else mechanical), not the cosmological spark. *[Workshop note]*
