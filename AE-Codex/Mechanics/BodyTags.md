---
type: mechanic
status: locked-core (VN-format) — D&D-version still TBD
last_updated: 2026-04-26
related: [../Cosmology/SoulIndices.md, ../Characters/PAVNN.md]
applies_to: VN-relevant — D&D version not yet locked
---

# Body Tags

> The physical-form axis of character creation. Three tags — **HUM**, **CYB**, **SYN** — gate which characters can do which tasks in the world. Used heavily in the VN format for **task-assignment puzzles** ("send the cyborg to hack, the human to make deals, the robot to guard"). Orthogonal to Soul Index (cosmic temperament).

---

## The three tags — LOCKED

*[T1: Daniel 2026-04-26]*

| Tag | Meaning | Body composition |
|---|---|---|
| **HUM** | Human | Pure organic |
| **CYB** | Cyborg | Hybrid — partial mechanical augmentation, partial organic substrate |
| **SYN** | Synthetic | Pure mechanical (e.g., PAVNN-class android) |

**Resolution chosen for the VN format:** 3 tags. Reasoning:
- **Binary FLESH/STEEL** would lose the cyborg middle-ground — the most interesting category for partial-access situations
- **4+ tags** would over-granularize without clear gameplay benefit
- **3 = natural triad** of pure-organic / hybrid / pure-mechanical, each with distinct gating implications

---

## Core gating principle — LOCKED

*[T1: Daniel 2026-04-26]*

The Body Tag determines **what tasks a character can attempt and at what effectiveness**. Tag-specific gates appear frequently in the world:

| Capability | HUM | CYB | SYN |
|---|---|---|---|
| Social deals / persuasion / fitting in | **Full** | Partial | Often blocked |
| Hacking / robot-only locks | **None** | **Partial (~50%)** | **Full** |
| Sleep requirements | Yes | Reduced | None |
| Long-watch guard duty | Tires | Tolerable | Indefinite |
| Sleep-cycle-bound activities | Yes | Reduced | No |
| Industrial-strength labour | Limited | Augmented | Full |
| Eating organic food | Required | Optional | Forbidden / inert |
| Eating "robot food" / charge-cells | None | Optional | Required |
| Pure-organic / pure-mechanical environment access (e.g., bio-sealed lab vs. high-EM environment) | Tag-specific lockouts apply | Often penalized in both directions | Locked out of organic, free in mechanical |

**The exact percentages are illustrative**, not hard-locked yet — Daniel's working example: *"cyborg meg tudja hackelni 50% hatásfokkal, robot 100%, ember nem tudja"*. The pattern is: **HUM = pure organic gating, SYN = pure mechanical gating, CYB = partial both ways**.

---

## Why this matters for the VN format

**Body-tag-gating is one of the central gameplay loops** of the VN. *[T1: Daniel 2026-04-26]*

The player builds a party (3+ characters), each with their own Body Tag. When a scene requires a specific tag-capability, the player **chooses which party member to send**. Different members' tags unlock different narrative branches. Tag-mismatched assignments either fail outright or proceed at reduced effectiveness.

Examples:
- **Negotiation scene** → send the HUM (full diplomatic capability) or risk the CYB (partial; might unsettle the negotiator)
- **Surveillance / overnight watch** → send the SYN (no sleep needed) so the rest of the party can rest
- **Hack a robot-locked door** → send the SYN (full success) or the CYB (50% — might trip alarms)
- **Bio-sealed area** → send the HUM only

This gameplay loop **rewards diverse party composition** — a party of all-HUMs or all-SYNs would be hard-locked out of half the campaign.

---

## Game-design intent — preventing exploit

*[T1: Daniel 2026-04-26 — see also `Characters/PAVNN.md`]*

Body Tags also explain why the campaign **doesn't let players recruit unlimited random A-Tech robots** they encounter. The activation phrases (PIN-style aSync security; see [PAVNN.md](../Characters/PAVNN.md#how-lucifer-knows-the-phrase--locked-2026-04-26)) are unknown to the players, so dormant robots stay dormant. This **caps SYN access** to specifically authored party members (PAVNN being the canonical one).

---

## Soul Index × Body Tag = 12 archetype combos

*[T1 — derived from `Cosmology/SoulIndices.md` lock + this lock]*

Character creation is a 2-axis grid:

| | HUM | CYB | SYN |
|---|---|---|---|
| **Boiler** (Wrath) | 1 | 2 | 3 |
| **Crown** (Pride) | 4 | 5 | 6 |
| **Maw** (Greed) | 7 | 8 | 9 |
| **Mirror** (Envy) | 10 | 11 | 12 |

12 base archetype combos before customization or class. Each combo has a distinct flavor (e.g. *"Crown-SYN"* = pride-driven cosmic temperament expressed through a synthetic body — likely an authoritarian android leader-figure). Plus customization on top.

---

## D&D version — DEFERRED

The exact mechanical resolution (skill-check modifiers, gating math, percentages) is **not yet locked for the D&D ruleset version** of the campaign. When/if D&D-version is built, Body Tags will need:

- Specific OFS modifiers on tag-relevant skill checks
- Hard-DC vs Soft-DC distinctions for tag-locked vs tag-modified gates
- Possibly skill-imprint-style passives per tag (similar to Soul Index Skill Imprints)
- Body-Tag interaction with class features (e.g., a SYN Wizard's spellcasting source — robot brain interpretation needed)
- Sleep-cycle / Long-Rest interactions per tag

> [!todo] D&D-version body tag mechanics
> Defer until either (a) the VN proves the gating loop works, then we port; or (b) Daniel decides to build the D&D version in parallel.

---

## Open questions

> [!todo]
>
> - **Tag-vs-tag interactions** — do CYB characters partially-trip both HUM and SYN gates, or do they get the better of the two?
> - **Hidden tags / passing** — can a CYB character pass for HUM or SYN in social situations?
> - **PAVNN's exact tag** — locked as SYN per his android nature, but worth confirming
> - **Player character body-tag changes mid-campaign** — Revival prints (per Database/Rule 1) potentially allow body-tag changes between deaths; how does that interact?
> - **The "robot food" question** — what do SYN characters consume? Sparkplug-equivalents? Fuel cells? Hellfire residue?

---

## Cross-references

- [`../Cosmology/SoulIndices.md`](../Cosmology/SoulIndices.md) — the orthogonal cosmic-temperament axis
- [`../Characters/PAVNN.md`](../Characters/PAVNN.md) — canonical SYN (mule-rated A-Tech android)
- [`../Mechanics/Hellstatic.md`](Hellstatic.md) — D&D-only mechanic; body-tag interaction TBD when D&D version is built
- Source: `AE - Campaign Resources/Character Creation/Ancestry Layer - Soul Indices + Body Tags v2.md` (referenced but does not define HUM/CYB/SYN — they are referenced as undefined there)
