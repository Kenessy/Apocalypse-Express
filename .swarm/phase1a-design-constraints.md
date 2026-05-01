# Phase 1A: Design Constraints + Visual Language

_Extracted by Agent A, 2026-04-30. Source files: Skills & Postures v1.5, Currencies v2.4, Cantos Outline, character-creation.html (~10,759 lines)._

---

## CSS palette (actual values from `:root`)

```
--void:    #05040a   (deepest black, rarely used directly)
--bg:      #0e0c18   (page background)
--bg2:     #15121f   (slightly lighter background layer)
--gold:    #c99c5a   (primary gold — eyebrows, labels, active tab border, hairline rules)
--gold2:   #e6cfa1   (lighter gold — headings, active tab text, strong/em highlights)
--cyan:    #28bdd8   (accent — technical/systems context; rare)
--ember:   #ff7b5c   (accent — hellish/hostile tones; also aliased as --red-bad)
--rust:    #b54a32   (deep red; rare)
--text:    #f8f5f0   (primary body text, near-white warm)
--muted:   #b8b0c6   (secondary prose, tab labels, descriptions)
--dim:     #9b95a8   (disabled/tertiary elements)
```

**Semantic tint tokens (derived):**
```
--green-good: #97c459  / --green-soft: rgba(151,196,89,.10) / --green-line: rgba(151,196,89,.36)
--red-bad:    #ff7b5c  / --red-soft: rgba(255,123,92,.08)   / --red-line: rgba(255,123,92,.40)
--accent:     var(--gold)  (default; per-component override via inline --accent)
```

**Border-radius canonical tokens:**
```
--r-card:  8px   (tier-1 panels: .body-intro, .info-panel, .soul-picker, all altarpiece sections)
--r-pill:  11px  (pills, archetype-tags, badges)
--r-tight: 4px   (small inner elements — tag interior bevels, thumb corners)
```

---

## Typography

**Three fonts in use (loaded from Google Fonts):**

| Role | Font | Weights loaded |
|---|---|---|
| Display headings | Cinzel | 600, 700 |
| Literary "lead" italic | Cormorant Garamond | 300, 400, 500 (roman + italic) |
| Body + UI + mono | IBM Plex Mono | 400, 500, 600 |

**Canonical type scale (T1–T6 + one extra):**

| Token | Size | Used for | Font |
|---|---|---|---|
| T1 / `--fs-display` | 32px | Page title (h1) | Cinzel 700 |
| T2 / `--fs-title` | 20px | Layer/section header (h2 in `.layer-header`) | Cinzel 700 |
| — | 26–28px | Hero blocks (`.bi-headline`, `.race-title`) | Cinzel 700 |
| — | 22px | Sub-section heads (`.cadence-section-title`, `.soul-picker-title`) | Cinzel 700 |
| T3 / `--fs-body` | 15px | Short UI prose, `.cadence-section-sub`, `.meta-value` | IBM Plex Mono 400 |
| — / `--fs-prose-mono` | 16px | Long-form reading blocks (`.race-body`, `.layer-header p`, `.bi-prose`) | IBM Plex Mono 400 |
| — / `--fs-cormorant-lead` | 19px | Single literary "lead" line per race (`.race-subtitle`) | Cormorant Garamond italic |
| T4 / `--fs-label` | 13px | Tab text, stat values, choice text | IBM Plex Mono 500 |
| T5 / `--fs-caption` | 11px | Eyebrows, breadcrumbs, meta-labels (`.bi-eyebrow`, `.race-eyebrow`, `.meta-label`) | IBM Plex Mono 500 |
| T6 / `--fs-ambient` | 10px | Separators, arrows, decorative text | IBM Plex Mono |

**Key typographic rules:**
- Headings: `letter-spacing: 0.08–0.18em` (wide tracking is the house style)
- Eyebrows: `text-transform: uppercase`, `letter-spacing: 0.18–0.22em`, color `--gold`
- Body text opacity often pulled to `.92` rather than full 1.0
- `strong` and `em` in prose render in `--gold2` (not standard bold/italic)
- Line heights: headings 1.1–1.2; body 1.65–1.8

---

## Voice (from canon docs + existing tabs)

- **Formal-procedural rules language with in-world flavor injected at chapter breaks.** The rules text (Skills, Currencies) uses compact tables, icon prefixes, and a clipped telegraphic style: "Gate → Hard Override → Soft Override → d20 → Offsets → Bands." No filler words. Think ops manual, not textbook.
- **Gothic-mythic flavor in lore passages.** The Sparkplug lore block uses present-tense declarative sentences with poetic repetition: "It sounds like hope. It works like hunger." The Leverage lore uses near-biblical register ("Then the tickets appeared"). Lore sections are clearly marked and offset from rule text.
- **Train-and-dispatch idioms throughout.** "Read the rails, find your post." "Pick a race in the Body tab to see your sub-type archetype bonuses here." The train is both literal vehicle and organizing metaphor. Dispatch, posting, carriages, fuel cost per journey — the vocabulary is consistently railway-operational.
- **Pact/debt register from Lucifer's world.** Characters are damned souls. The body is "the form Lucifer dresses that soul in." Reviving costs PLUGs ("distilled from what used to be someone"). The tone treats death as bookkeeping and mercy as arithmetic, never softening or apologizing.
- **In-world flavor in tutorial copy, not neutral.** Even the character creation tutorial uses in-world language: "Every PC begins as a damned human soul." The sub-header on the page: "Learn what kind of being you can become — and who'll ride the rails with you." Neutral rules-text and in-world flavor are woven together, not separated into different pages.

---

## Recurring visual idioms

1. **`.cath-eyebrow` / `.bi-eyebrow`** — Small-caps gold label above every heading, often with an SVG ornament (`#orn-arch-small`, `#orn-quatrefoil`, `#orn-rose-petal`) replacing the default hairline. Format: `[ornament] Category · subcategory`. Always uppercase, `letter-spacing: 0.18–0.22em`, color `--gold`.

2. **`-altarpiece` containers** — Each tab has a root container named `[tab]-altarpiece` (`.body-altarpiece`, `.soul-altarpiece`, `.cadence-altarpiece`, `.carriage-altarpiece`, `.factions-altarpiece`). These are `display: flex; flex-direction: column; gap: 24px` wrappers that hold all the sections of a tab in a continuous vertical column.

3. **`.layer-header` hero opener** — Every numbered chargen tab (Body, Soul, Personality, Carriages) opens with a `.layer-header` block: eyebrow (`Layer N of 4 · Name`) → `h2` (Cinzel gold) → prose paragraph (`--fs-prose-mono`, line-height 1.8). Max-width 920px. This is the canonical tab-opening beat.

4. **`.cadence-section-header` / `.soul-picker-header`** — Shared section sub-header treatment used across multiple tabs: eyebrow → `h3` (Cinzel, 22px, `--gold2`) → descriptive paragraph (`--fs-body`, color `--muted`). Max-width 980px. The same HTML pattern appears in Soul, Personality, Carriages, Chaos & Harmony, and Factions.

5. **Stained-glass panel** — Key content blocks (Soul picker, Race Distribution, Archetype Bonus, Faction Affiliation, Cadence Hero) use a shared background treatment: `linear-gradient(180deg, rgba(14,12,24,.88), rgba(14,12,24,.94))` with two radial gradient accent blobs (gold at top-left, ember at bottom-right), `border: 0.5px solid rgba(201,156,90,.30)`, `border-radius: var(--r-card)`, `box-shadow: inset 0 0 0 0.5px rgba(201,156,90,.12), 0 8px 28px rgba(0,0,0,.45)`.

6. **`.fac-section-divider`** — Ornamental section divider used in Factions (and adaptable elsewhere): flex row with `[ornament] · TEXT · [ornament]`, hairline rule extending to edges via `::before`/`::after`. Color `rgba(201,156,90,.35)`, font-size 10px, uppercase.

7. **Key-value rule rows** — `.efr-row` / `.psn-row` / `.meta-row` pattern: `display: grid; grid-template-columns: 130px 1fr; gap: 12px`. Key in gold/uppercase/caption size; value in muted body text with `strong` highlighted in `--gold2`. Used for engine fuel rules, personality system notes, race metadata.

8. **`.zone-card` / `.subrace-card`** — Interactive selection cards with image + text overlay. Zone cards use per-type CSS custom property `--zc-glow` for accent color; active state adds gold border glow. Cards that are not selected in an active group get `opacity: .38` dimming.

9. **`.cadence-stage-placeholder`** — Placeholder panel for JS-rendered content that isn't ready: `border: 0.5px dashed rgba(201,156,90,.25)`, `border-radius: 8px`, centered `--muted` mono text. Used when a cross-tab dependency isn't yet fulfilled.

10. **SVG ornament sprites** — Decorative glyphs inlined in the `<head>` SVG `<defs>` block and referenced via `<use href="#orn-arch-small"/>`, `#orn-quatrefoil`, `#orn-rose-petal`. The ornament `<svg>` wrapper in eyebrows is always `aria-hidden="true"`.

---

## Section structure patterns

**Tab open:** Every numbered chargen tab opens with a `.layer-header` (eyebrow → h2 → prose). The `.layer-header` is inside the tab's `[name]-altarpiece` flex column and comes first before any content sections.

**Reference tabs (∞ / §):** Open with a custom hero block instead of `.layer-header`. Chaos & Harmony uses `.cadence-altarpiece` with a `layer-header` followed immediately by a `.cadence-hero` stained-glass panel. Factions uses a `.fac-hero` two-column block (text + icon). These tabs use `class="tab tab-reference"` on the nav button.

**Content sections within a tab:** Each section has a `.cadence-section-header` (or equivalent: `.soul-picker-header`) as its opener — eyebrow → h3 → sub-paragraph — then the content (grid of cards, meters, floor plan, etc.). Sections are separated by vertical `gap: 24px` from the altarpiece flex layout, and important dividers use `.fac-section-divider` ornament rows.

**Card grids:** Content that presents multiple options uses CSS grid with `auto-fill / minmax()` columns. Cards use consistent border, background, border-radius patterns. Interactive cards highlight with gold border glow on hover/active.

**Max-widths:** The layer header caps at 920px. Section headers cap at 980px. Full-width grids can reach 1280px max.

**Tab padding:** `.tab-panel { padding: 32px 40px 60px }`.

---

## Tab navigation

**Markup:**
```html
<nav class="tab-nav" id="tabNav">
  <button class="tab active" data-tab="test"><span class="num">1</span>Body</button>
  <button class="tab" data-tab="lelek"><span class="num">2</span>Soul</button>
  <button class="tab" data-tab="szem"><span class="num">3</span>Personality</button>
  <button class="tab" data-tab="vagon"><span class="num">4</span>Carriages</button>
  <button class="tab tab-reference" data-tab="cadence"><span class="num">∞</span>Chaos &amp; Harmony</button>
  <button class="tab tab-reference" data-tab="factions"><span class="num">§</span>Factions</button>
</nav>
```

**Tab IDs and panel IDs:**

| `data-tab` | `<section id>` | Class | Number |
|---|---|---|---|
| `test` | `tab-test` | `.tab.active` | 1 |
| `lelek` | `tab-lelek` | `.tab` | 2 |
| `szem` | `tab-szem` | `.tab` | 3 |
| `vagon` | `tab-vagon` | `.tab` | 4 |
| `cadence` | `tab-cadence` | `.tab.tab-reference` | ∞ |
| `factions` | `tab-factions` | `.tab.tab-reference` | § |

**Note:** Tab keys use Hungarian words (`lelek` = soul, `szem` = eye/personality, `vagon` = carriage). A new tab should follow this pattern — use a short Hungarian or thematic key for `data-tab` and match it as `id="tab-[key]"`.

**JS switching:** Single event listener on `#tabNav`, delegates to `.tab`. Removes `.active` from all tabs and panels, adds `.active` to clicked tab + matching panel. Side effects: switching to `lelek` fires `refreshSoulLayer()` and `renderSideTrackPips()`.

**Reference tabs:** Distinguished by `.tab-reference` class, which overrides `.num` to use Cinzel font at 16px (vs the numeric tabs' IBM Plex Mono). Numbers `∞` and `§` signal non-chargen reference status.

---

## Cross-link patterns

**No explicit in-page anchor links (`href="#..."`) are used between tabs.** Cross-references are done through:

1. **Prose text mentions** — e.g., in Factions: _"The DNA-tags (HUM / SYN / HELLISH / DIVINE) cross-reference the Body tab; here we focus on who, not what."_ In Soul tab: _"Pick a race in the Body tab to see your sub-type archetype bonuses here."_ Just plain text naming the other tab.

2. **JS state dependency** — The Soul tab's content dynamically reads from Layer 1 (Body) state. The Soul tab registers a hook via `refreshSoulLayer()` on tab-switch. The cross-tab dependency is encoded in JS, not in the HTML markup.

3. **Placeholder panels for unfulfilled dependencies** — When a JS-rendered section depends on another tab's state not yet set, it renders a `.cadence-stage-placeholder` with descriptive text like "Pick a race in the Body tab to see your sub-type archetype bonuses here."

4. **In-prose `§Factions` notation** — The faction tab is referenced inline in body copy using the `§` sigil that matches its tab number: "Your faction ties" / "§Factions tab has the full faction roster." This sigil notation creates a visual shorthand without needing actual hyperlinks.

---

## Canonical vocabulary (from rules docs)

### Skill abbreviations (full list)

| Code | Full name | Ability |
|---|---|---|
| PRY | Pry (Prying) | STR |
| RGG | Rigging | STR |
| TNK | Tinker | DEX |
| ACR | Acrobatics | DEX |
| RES | Resilience | CON |
| SLG | Soul Grit | CON |
| SYS | Systems | INT |
| STL | Stillsense | INT |
| GDS | Godsight | WIS |
| RDL | Riddlecraft | WIS |
| IFC | Influence | CHA |
| GIL | Guile | CHA |

### Discipline brackets (binary; gate safety-critical steps)
- **[MED]** — MedTech
- **[EOD]** — Demolitions
- **[RCP]** — Railcraft & Power

_Discipline tags gate eligibility for safety-critical steps; the roll still uses the listed skill (e.g., [EOD] steps use TNK)._

### Band names (roll outcomes vs DC)

| Code | Full name | Threshold |
|---|---|---|
| CS | Critical Success | DC +5 or more |
| S | Success | DC … DC +4 |
| F | Failure | DC −4 … DC −1 |
| CF | Critical Failure | DC −5 or worse |

### Beltline (resolution order)
**Gate → Hard Override → Soft Override → d20 → Offsets → Bands**

_"Beltline" is the canonical name for the full resolution sequence._

### Lock types
- **Keyed R#** — Must have that rank or higher to attempt. Help cannot grant eligibility.
- **◇ Open R#** — Anyone can try; at/over rung = Soft Advantage; under rung = Soft Disadvantage.

### Rank gates
- R1 appears at Act I; R3 appears in Act II; R4 appears only in Act III ("legend gate").

### PLUG / Sparkplug language

**Canonical idiom:** _"One canister will wake a Hellfire boiler and shove a steam train through purple haze."_

Key vocabulary:
- **PLUG** — The code/abbreviation. "Sparkplug" is the full name.
- **"Exotic fuel & second chances"** — The subtitle from the canon doc.
- **Cost-per-journey framing:** 1 PLUG short hop · 2 PLUG medium · 3 PLUG long haul.
- **Weight:** TNY / 1 pBL in pockets; 1 BL outside. Not legal tender. No public LEV↔PLUG market.
- **Lore register:** PLUGs are charged by what lingers after death ("distilled from what used to be someone"). The device "sounds like hope. It works like hunger." Moon-jars, ghost batteries — street names exist.
- **Fallback without PLUGs:** Reserve print (8h + 2d4); Train goes Low-Energy; sequential 1×1; +1 Major injury.

### Currency denominations (LEV / Leverage)
- **gr** = Gray Ticket (10 gr = 1 LEV)
- **rd** = Red Ticket, the workhorse (1 rd = 1 LEV; "rd" and "LEV" are synonyms)
- **gd** = Gold Ticket (1 gd = 10 LEV)
- **ST** = Spin-Time tokens (5 per Long Rest; expire; no carry-over)

### World vocabulary
- **The Halt** / **the Pause** — The apocalyptic event that froze time into pockets.
- **Surgefronts** — Phenomenon from the Halt; can unsitch metal and flesh.
- **Trueflow** — Safe, uninterrupted, real time under normal causality.
- **αSync / aSYNC** — Lucifer's operational unit; sometimes styled α-SYNC.
- **The Gauntlet** — Canon name for Chapter 1.
- **Null Meridian** — The obsidian platform / Prelude setting.
- **CDR** — Chaos Drift meter/scan system.
- **Hellfire boiler** — The engine technology the train runs on (PLUG-powered).

---

## Design constraints summary

1. **Font trinity is fixed.** New content must use only Cinzel (headings), IBM Plex Mono (body/labels/UI), and Cormorant Garamond (literary italic lead line only, one per section maximum). No other fonts.

2. **Color must stay within the palette.** `--gold` and `--gold2` for all highlights/headings; `--text` / `--muted` / `--dim` for body copy hierarchy. Accent colors (`--cyan`, `--ember`) only for specific semantic purposes (technical/systems = cyan; hellish/hostile = ember). Never invent new colors.

3. **Every new tab must open with a `.layer-header` OR a custom hero block matching the tab's role.** Numbered chargen tabs use `.layer-header`. Reference tabs use a bespoke hero matching the Factions or Cadence hero patterns.

4. **The `data-tab` / `id="tab-[key]"` pairing is mandatory.** New tabs must follow the existing JS tab-switch pattern — add a `<button class="tab" data-tab="[key]">` to `#tabNav` and a matching `<section class="tab-panel" id="tab-[key]">` in `<main>`.

5. **All section sub-headers use the `.cadence-section-header` / `.soul-picker-header` pattern.** eyebrow (`.cath-eyebrow` with SVG ornament) → h3 (`.cadence-section-title` or `.soul-picker-title`, Cinzel 22px, `--gold2`) → descriptive paragraph (mono, `--muted`, `--fs-body`).

6. **Stained-glass panel background is mandatory for featured content sections** (not for lightweight info rows). The dark radial-gradient + gold border + inset shadow combo is the canonical "important panel" signal.

7. **Key-value information must use the `.efr-row` / `.meta-row` grid pattern** — 2-col grid (label ~120–130px, value 1fr), label in gold uppercase caption size, value in muted body text.

8. **All canonical skill names, abbreviations, and discipline brackets must match exactly.** PRY not "Pry", RGG not "Rigging" (in code contexts), [EOD] not "[eod]". Band names: CS/S/F/CF, never "crit success" etc.

9. **Voice must mix in-world flavor with rules precision.** Body copy can and should use Lucifer-pact, railway-operational, and Halt-mythology idioms. Neutral tutorial language alone is not enough — the "damned soul" register should appear at least in opening/transition copy.

10. **Cross-tab references use prose text + sigil notation (`§Factions`, `Body tab`, `Layer 2`), not hyperlinks.** Dynamic cross-tab dependencies (JS-rendered) should degrade gracefully with a `.cadence-stage-placeholder` fallback message.

---

## Open questions for synthesis

1. **Which tab number/slot does the new Skills tab occupy?** The existing nav has tabs 1–4 (Body, Soul, Personality, Carriages) plus two reference tabs (∞, §). Does the new tab insert as a new numbered chargen step (e.g., "5 · Skills"), or is it a reference tab (like ∞/§)? This affects whether it gets a `.layer-header` or a bespoke hero, and whether it's `tab-reference` styled.

2. **What is the new tab's `data-tab` key?** Following the pattern of Hungarian-adjacent or thematic short keys (`test`, `lelek`, `szem`, `vagon`, `cadence`, `factions`). Suggest `kepesseg` (Hungarian for "skill/ability") or `dispatch` — but this needs an authorial decision.

3. **Does the Skills tab need JS reactivity?** The Soul tab re-renders when Body tab state changes. Does the Skills tab need to read from Body or Soul state (e.g., to show race-based skill bumps)? If yes, the JS hook pattern from `refreshSoulLayer()` needs to be replicated.

4. **Discipline bracket display:** The three disciplines ([MED], [EOD], [RCP]) gate specific skills. Is the intent to show them as tags on skill cards, as a separate discipline section, or woven into the skill descriptions? The rules doc treats them as binary licenses — the visual treatment needs a design decision.

5. **Rank gate display:** Beltline resolution order and the Keyed vs Open lock distinction are dense rules content. Does the Skills tab focus on the 12 skill descriptions for chargen purposes, or does it also need to present the full Bands table and Beltline? Knowing the scope will determine whether this is a simple 12-card grid or a full mechanics primer like the Chaos & Harmony tab.

6. **Posture sections (Stealth, Influence):** The rules doc includes Stealth and Influence as extended posture subsystems with their own tables. Should these appear in the Skills tab or are they deferred to another reference section?

7. **Soul Grit and Strain:** These are defined under Skills in the rules doc but are more character-resilience mechanics than skill descriptions. Should they appear in the Skills tab or stay in the Soul tab?

8. **Image/icon assets:** The Body and Soul tabs use per-race portrait images (`img/races/...`) and faction icons. Does the Skills tab need icons per skill (12 icons, one per skill code)? The rules doc assigns emoji to each skill — are full icon assets available or should the tab use text/emoji only?
