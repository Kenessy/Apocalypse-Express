# Digital Multi-Skill Coverage Research

> Research Agent B — May 2026. Covers 12 games across Tiers 1-4 with 2+ sources each.

---

## Summary Table

| Game | Mechanic name | How it works (1 line) | UI pattern | Decision space |
|---|---|---|---|---|
| Citizen Sleeper 1 | Dice Placement | Pre-rolled dice pool assigned to per-skill action slots; skill level adds +0 to +2 to die value | Drag die to slot; live probability shown immediately | ~6 viable placements per cycle from 5 dice |
| Citizen Sleeper 2 | Crew Dice Pool | Sleeper + crew each roll 2 dice; crew skills provide Advantage/Disadvantage per action | Same drag-slot UI extended across multiple characters | Combinatorial: 4+ crew means 8+ dice covering ~8-10 slots |
| Lobotomy Corporation | Virtue-Matched Work | 4 stats (Fortitude/Prudence/Temperance/Justice) each govern a specific work type; success rate = stat level * modifier, capped 95% | Containment unit click reveals work options; agent stats shown with color-coded numbers | Low — one optimal agent per work type, limited by availability |
| Frostpunk 1 | Worker/Engineer Gating | Binary type gate: Workers vs. Engineers; buildings require a specific type; staffing level scales efficiency 0-100% | Building info panel shows slots + assigned count; arrows to assign | Very low per-building; strategic at macro resource level |
| FTL: Faster Than Light | Station Manning | One crew per station; presence applies skill bonus; skills are station-specific, no overlap | Ship map shows crew position; colored room icons change with manning | 4-6 crew, 6-8 key stations; daily triage is central |
| Sunless Sea / Skies | Officer Stat Bonus | Officers passively add to captain stats (Iron/Mirrors/Veils/Pages/Hearts); events check a single stat with pass/fail probability | No live preview — stat total shown in captain sheet; events show required stat | Hiring choice (which officer); no per-event assignment |
| Disco Elysium | Passive/Active Skill Voices | 24 skills each constantly check passively; active checks use 2d6+skill vs. difficulty; multiple skills can comment on same scene | Skill voices appear in dialogue; difficulty and probability shown before roll | Build-time (stat investment); minor in-scene (clothing, drugs) |
| RimWorld | Work Priority + Passion | Colonists assigned to work types by priority 1-4; skill level determines output quality/speed; passion doubles XP gain | Work tab grid: brightness = skill, flame icon = passion | Per-colonist: assign to multiple works; emergent from task queue |
| Dwarf Fortress | Labor Specialization | Enabled labors determine task eligibility; more skilled dwarves get priority; no priority number in vanilla | Units screen: checkboxes per labor per dwarf; Steam version adds work detail groups | Each dwarf can hold all labors; specialist vs. generalist tradeoff |
| Oxygen Not Included | Skills Board / Job System | Skill points spent on skill tree unlock tasks; morale cost per tier; interests reduce morale cost; task execution independent of job title | Skills board shows tree with cost/morale impact; duplicant panel shows interests | Constrained by morale ceiling; deep planning space per duplicant |
| Spirit Island | Elemental Threshold | Power cards grant elements; innate powers have tiered thresholds (e.g., 2 Fire + 1 Earth = base; add 2 Water = enhanced); elements not consumed | Card layout shows element icons; spirit board shows innate with threshold brackets | Draft-like: card selection determines element combos achieved per turn |
| Pandemic | Role Ability Coverage | Fixed roles cover different disease-management functions; team assignment decides who acts where | Role card with specific ability text; no live preview beyond knowing the board state | Low individual (fixed abilities); high team-composition |

---

## Per-Game Deep Dives

---

### Citizen Sleeper 1 — Dice Placement on Skill-Tagged Slots

**How it works:**
Each cycle the Sleeper rolls 1-5 d6s (count determined by current health Condition). Actions on the station map each belong to one of five skills: Engineer, Interface, Endure, Intuit, Engage. Each action slot accepts one die. Your skill level in the matching skill adds 0, +1, or +2 to the die value placed there before resolving. Outcome categories are typically: 4-6 = full success, 2-3 = partial/mixed, 1 = failure. Some actions are tagged Safe (no downside on low), Risky (some downside on low), or Dangerous (serious downside on low). Players receive between 6 and ~15 accessible action slots per cycle but only 5 dice to distribute.

**The key coverage insight:** This is not multi-skill coverage of a single task — each task uses a single skill slot. The multi-skill challenge emerges because players need to spread dice across multiple distinct skill-tagged tasks in a single cycle, and a roll of 2 wasted on a Risky slot is a meaningful negative. Decision space collapses around: which task gets my worst die? Where do I accept failure?

**UI:**
Drag a die to a slot and the game immediately displays branching outcome probabilities next to the die. Players see exact % odds before committing. This live preview is the critical feedback mechanism.

**Design intent:**
Developer Gareth Damian Martin described the system as inspired by tabletop RPGs (explicitly Ironsworn and similar Powered by the Apocalypse games). The pre-rolled dice pool creates a daily "hand" of resources — players must plan around what they got, not just what they want. The intent was to make failure interesting rather than punishing, with the narrative branching differently rather than ending.

**Community reception:**
Broadly praised as the best mechanical integration of dice into narrative RPG since Disco Elysium. Primary complaint: low condition states (few dice, low values) feel punishing and reductive. The "safe action as low-die sink" mechanic was considered an elegant pressure valve.

**Sources:**
- [The Gamer — How The Dice System Works In Citizen Sleeper](https://www.thegamer.com/citizen-sleeper-dice-explained-guide/)
- [UNCG 237 Blog — In-Depth Explanation of Dice Roll Mechanic](https://uncg237publications.wordpress.com/2024/12/20/the-dice-roll-mechanic-in-citizen-sleeper-an-in-depth-explanation/)
- [Game Design Library — Citizen Sleeper Game Design Analysis](https://www.gamedesignlibrary.com/post/citizen-sleeper-game-design-adding-a-twist-to-visual-novels-with-clever-mechanics)

---

### Citizen Sleeper 2: Starward Vector — Crew Pool + Skill Coverage

**How it works:**
CS2 extends the original system from single character to crew. The Sleeper plus recruited crew members each roll 2 action dice per cycle. Crew provide their dice to the same pool used at Contract locations. Each crew member has specific skill affinities: their affinity grants Advantage (+1 to any die used on a matching skill action) or Disadvantage (-2 on a non-matching action used badly). Contracts have a Derelict Stress meter — negative outcomes on any action add Stress. Reaching Stress thresholds triggers Crisis events. Time is bounded by Cycle Clocks that count down to forced outcomes.

**Multi-skill coverage:** Contracts have multiple action types (move/repair/negotiate/etc.) and player must cover all of them with the combined dice pool. A crew member with Engineering affinity makes your Engineering dice more effective but does nothing for the Engage actions. This is much closer to the "multiple skill bars, crew pool to cover" pattern described in the brief.

**UI:**
Same drag-to-slot UI as CS1 with extended crew portrait bar showing whose dice are whose. Skill advantage/disadvantage is visualized as a +1 or -2 modifier shown on hover before placement. Players can see which crew dice will get the bonus before committing.

**Developer intent:**
Martin cited Firefly, Cowboy Bebop, and Farscape as narrative inspiration — "ragtag crew" stories. The mechanic mirrors how crew members cover each other's skill gaps. He noted that balance is deliberately imperfect; the player may have broken dice or absent crew, and the design embraces that asymmetry as part of the survival narrative.

**Community reception:**
CS2 improved on CS1 by making shortfall survivable — Stress meters rather than binary failure. The crew system was praised for making recruiting decisions meaningful. Criticism: dice-break RNG felt arbitrary, and some contracts required specific crew skill combos unavailable early in the game.

**Sources:**
- [Magic Game World — Contracts, Crew, and Hazards Explained](https://www.magicgameworld.com/citizen-sleeper-2-starward-vector-contracts-crew-and-hazards-explained/)
- [Game Rant — Interview with Gareth Damian Martin](https://gamerant.com/interview-citizen-sleeper-2-gameplay-story/)
- [The Gamer — Complete Dice Mechanic Guide CS2](https://www.thegamer.com/citizen-sleeper-2-starward-vector-dice-complete-guide/)

---

### Lobotomy Corporation — Virtue-Matched Work Assignment

**How it works:**
Agents have four Virtues: Fortitude (HP), Prudence (Sanity), Temperance (Work Success/Speed), Justice (Movement/Resistance). Each Abnormality has four work types: Instinct (red, trains Fortitude), Insight (white, trains Prudence), Attachment (black, trains Temperance), Repression (pale, trains Justice). Work Success Rate is calculated as: each point of the relevant stat grants +0.2% success rate, stacking with the agent's base Work Success stat, capped at 95%. Qliphoth Overload (the "containment integrity" system) imposes stacking failure rate penalties (-4% to -6% per overload level depending on Abnormality tier).

**Multi-stat relevance:** Different Abnormalities strongly favor specific work types. Some Abnormalities require multiple types to be performed in sequence, meaning a manager needs an agent with coverage across Temperance (Attachment) AND Fortitude (Instinct) — either a well-rounded agent or two separate specialists.

**UI:**
Clicking an Abnormality's containment unit opens a work type selection wheel with the four options color-coded. Selecting a work type then shows available agents with their relevant stat displayed. Stats display as base number + blue bonus from training, with red penalties shown separately. There is limited live preview — the player sees agent stats but must calculate expected success rates mentally.

**Design intent:**
The four-virtue system mirrors the four cardinal virtues (Fortitude, Prudence, Temperance, Justice) and is deeply narrative-integrated. The panic system (where an agent's dominant stat determines which violent/self-destructive behavior they perform when they break) creates a counterintuitive risk: over-training a stat can make an agent's panic worse.

**Community reception:**
Considered punishingly opaque for new players — the connection between work types and stat training, and between stat dominance and panic type, is not clearly explained in-game. The "More Detailed Info" mod on NexusMods was downloaded extensively to surface this hidden information. The system rewards mastery but has a high friction barrier.

**Sources:**
- [Lobotomy Corporation Wiki — Stats](https://lobotomycorp.fandom.com/wiki/Stats)
- [LP Archive — Mechanics Talk 2: Agent Growth](https://lparchive.org/Lobotomy-Corporation/Update%20125/)
- [Steam Guide — Lobotomy for Beginners](https://steamcommunity.com/sharedfiles/filedetails/?id=2538065805)

---

### Frostpunk 1 — Worker/Engineer Binary Type Gating

**How it works:**
Citizens are one of two labor types: Workers or Engineers. Buildings have type requirements: medical posts, infirmaries, workshops, and research buildings require Engineers only. Most extractive/production buildings accept Workers. When a building is staffed, each additional worker adds to efficiency linearly, with full staffing = 100% efficiency. The game uses a health-priority auto-assignment when the player clicks to add workers: healthiest available citizens of the required type fill first.

**Multi-skill element:** This is the simplest possible multi-skill gating — two types, hard walls on certain buildings. The decision space is resource allocation (how many Engineers do you have total, and which buildings compete for them?), not per-task skill matching.

**UI:**
Building info panel shows total slots, current occupancy, and a simple + / - control. Worker/Engineer distinction shown by icon. No live outcome preview — production rate scales with headcount, shown as production-per-cycle stat.

**Reception:**
Considered well-understood and rarely criticized for complexity. The binary type system creates macro-level tension (should I educate more children to Engineer status?) without individual worker micromanagement. The main critique is that it undersimulates specialized skill — an engineer with 10 years of medical experience is identical to one fresh from school.

**Sources:**
- [Frostpunk Wiki — People](https://frostpunk.fandom.com/wiki/People)
- [Advanced Guide to Frostpunk Worker Mechanics](https://gamestoday.info/pc/frostpunk/advanced-guide-to-frostpunk-worker-mechanics/)
- [Twinfinite — How to Assign Workers in Frostpunk](https://twinfinite.net/guides/frostpunk-assign-workers-how/)

---

### FTL: Faster Than Light — Station Manning Coverage

**How it works:**
Ship systems (Weapons, Shields, Engines, Piloting, Medbay, etc.) each have an optional manning slot. A crew member physically standing in the room applies a skill bonus: Piloting improves evasion, Engines improves FTL charge and evasion, Shields speeds recharge, Weapons boosts fire rate. Skills are station-specific and don't cross-apply. Crew level in each skill increases through use (each weapon fired = +1 Weapons XP). Racial abilities modify some bonuses (Zoltan give free power to their room; Mantis fight faster).

**Multi-skill coverage challenge:** The central tension is that combat demands multiple stations simultaneously, but each crew member can only be in one place. A crisis (fire, breach, system damage) means someone must leave their station to repair, creating cascading shortfalls. Player must preplan who covers which station at rest AND who reassigns under pressure.

**UI:**
Ship interior view shows crew portraits on the floor plan. Each room changes icon/color when manned (highlighted). No explicit "skill coverage" bar — player must know which rooms benefit from manning. Crew assignment panel shows current position and skill levels numerically.

**Reception:**
Widely considered the best real-time crew coverage puzzle design. Praised for emergent complexity without explicit "skill bar" UI. The lack of per-skill preview (you must know the system from experience or documentation) is a barrier but creates mastery satisfaction.

**Sources:**
- [FTL Wiki — Crew Skills](https://ftl.fandom.com/wiki/Crew_skills)
- [Vigaroe — FTL Analysis: Crew Overview and Experience](https://www.vigaroe.com/2022/10/ftl-analysis-crew-overview-and.html)
- [Steam Guide — Practical FTL](https://steamcommunity.com/sharedfiles/filedetails/?id=266502670)

---

### Sunless Sea / Sunless Skies — Officer Stat Accumulation + Single-Axis Checks

**How it works:**
Captain has five stats (Iron, Mirrors, Veils, Pages, Hearts). Officers each provide a fixed bonus to one or more captain stats when hired. Events at ports use StoryNexus's quality-based narrative engine: each option has a required stat level or a probability-based challenge (0-100%). Officers effectively "purchase" stat coverage permanently. No per-event assignment of officers — all hired officers contribute simultaneously.

**Multi-skill element:** There is no per-event crew allocation decision. The coverage decision is made at hiring time: which combination of officers gives you the stat profile you need for the events you'll encounter? Partial success states (success with a drawback, or failure with a consolation) exist in some events, making outcomes graded rather than binary.

**UI:**
Captain sheet shows total stats; officer bonuses stack additively. Events show stat requirement or challenge rating before you commit to the option. No live preview of additional officer effects.

**Reception:**
The indirect coverage model (buy stat permanently through officer hiring) reduces friction but removes the moment-to-moment crew assignment puzzle. Praised for narrative integration; occasionally criticized for stats feeling interchangeable rather than strategic.

**Sources:**
- [Sunless Sea Wiki — Officers](https://sunlesssea.fandom.com/wiki/Officers)
- [Sunless Sea Wiki — Captain Statistics](https://sunlesssea.fandom.com/wiki/Captain_statistics)
- [Failbetter Forums — Stat Bonus Stacking](https://community.failbettergames.com/t/stat-bonus-stacking/19415)

---

### Disco Elysium — Passive Skill Chorus + Active Single-Stat Checks

**How it works:**
24 skills are organized across four attributes (Intellect, Psyche, Physique, Motorics). Skills make constant passive checks, injecting their "voice" into dialogue when they pass. Active checks roll 2d6 + relevant skill vs. difficulty (DC), with probability shown to the player. Skills interact narratively — Logic and Encyclopedia both comment on intellectual puzzles, often from different angles. The Thought Cabinet provides permanent skill buffs/debuffs via internalized "thoughts."

**Multi-skill relevance:** Disco Elysium doesn't stack skills on a single check mechanically, but creates the *illusion* of multi-skill coverage through overlapping passive checks. High Perception AND high Visual Calculus both fire on the same crime scene, giving richer information from multiple angles — coverage as narrative depth rather than mathematical bonus.

**UI:**
Skill voices appear as interjections mid-dialogue. Active check shows die icon with probability before roll; white checks (retryable) vs. red checks (permanent). Clothing and items can modify active checks — visible as a modifier breakdown in the check preview.

**Reception:**
Celebrated as the most innovative skill system in RPG design for treating skills as characters rather than stats. The multi-voice chorus created emergent character personality. Criticism: skill investment in later chapters felt less meaningful because many checks had already fired.

**Sources:**
- [Disco Elysium Wiki — Skills](https://discoelysium.fandom.com/wiki/Skills)
- [Gabriel Chauri — Disco Elysium RPG System Analysis](https://www.gabrielchauri.com/disco-elysium-rpg-system-analysis/)
- [ScreenRant — Disco Elysium Dice Guide](https://screenrant.com/disco-elysium-dice-guide-uses/)

---

### RimWorld — Work Priority Grid + Passion Modifier

**How it works:**
Colonists have 12 skills (0-20 scale). A Work tab grid lets players assign each colonist to each work type with priority 1-4 (4 = lowest). Tasks within a work type have internal priority order. Skill level determines output quality, speed, and failure risk. Colonists have 0-2 Passions per skill: Passion doubles XP gain and provides a mood buff while performing that work. At skill 0, a colonist can still attempt most tasks but at significantly reduced speed and with elevated failure rates (cooking causes food poisoning; construction causes structure collapses).

**Multi-skill element:** RimWorld tasks are not truly multi-skill, but the team coverage challenge is identical — you have a colony of specialists with gaps, and tasks need to be distributed across available pawns. The strategic depth comes from managing coverage across a wide portfolio of task types simultaneously, not from per-task multi-stat resolution.

**UI:**
Work tab is a matrix grid. Each cell shows skill level as outline brightness (dim = low skill, bright yellow = high skill) with small flame icons for passion. Hovering shows tooltip with exact skill level. No per-task live preview of outcome quality — players must know the relationship between skill and output from documentation or experience.

**Reception:**
The work tab is considered one of RimWorld's most important UI innovations for colony management games. The Work Tab mod (most downloaded of all RimWorld mods) extended the grid format with additional sorting. The passion/skill visual shorthand is praised as scannable; the lack of outcome preview is considered acceptable because outcomes are probabilistic and emergent over time rather than single decisive checks.

**Sources:**
- [RimWorld Wiki — Work](https://rimworldwiki.com/wiki/Work)
- [RimWorld Wiki — Skills](https://rimworldwiki.com/wiki/Skills)
- [Steam Guide — Understand Skills](https://steamcommunity.com/sharedfiles/filedetails/?id=935337774)

---

### Dwarf Fortress — Labor Enable + Skill Priority Dispatch

**How it works:**
Each dwarf has every possible labor either enabled or disabled. When a job is created (by designation, workshop queue, or work order), an idle dwarf with that labor enabled is assigned it. Since the Steam version (2022), more skilled dwarves get priority for jobs in their specialty. Dwarves can hold all labors simultaneously but gain skills faster by specializing. DFHack's autolabor and labormanager tools extend the system with automatic skill-based assignment.

**Multi-skill element:** DF has no per-task multi-stat check — tasks are single-skill and single-dwarf. The coverage challenge is again at the portfolio level: with 40 dwarves and 60 labor types, which dwarves cover which labors without over-spreading skill growth?

**UI:**
Vanilla DF: Units screen with a large checkbox grid (dwarf × labor). Steam version adds Work Details groups. No per-task preview; the relationship between skill and output quality is referenced via the Wiki rather than surfaced in-game.

**Reception:**
Notorious for UI friction — third-party tools (Dwarf Therapist) existed for years to replace the checkbox grid with a more scannable matrix. The Steam version improved but still relies heavily on player mental model.

**Sources:**
- [Dwarf Fortress Wiki — Labor](https://dwarffortresswiki.org/index.php/Labor)
- [DFHack autolabor docs](https://docs.dfhack.org/en/stable/docs/tools/autolabor.html)
- [Steam Community — Work Details guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2920669655)

---

### Oxygen Not Included — Skill Tree + Morale-Gated Job Assignment

**How it works:**
Duplicants earn Skill Points by working. Points are spent on a skill tree at a Printing Pod or Mini-Pod. Each skill tier has a morale cost — higher tier skills increase the duplicant's morale need. If their morale need exceeds their morale (from food quality, recreation, etc.), they suffer debuffs. Interests (1-3 per duplicant) reduce morale cost for related skills by 1 and increase XP rate. Critically, job assignment ("jobs" in the UI) is separate from task permission — jobs only affect skill acquisition; task eligibility is controlled by which skills have been unlocked.

**Multi-skill element:** Individual tasks (e.g., operating an Oil Refinery) require specific skills to be unlocked. A single duplicant can have the entire skill tree unlocked eventually, but morale constraints mean specialization is optimal. The coverage problem: which duplicants spec into which skills to cover all needed tasks while managing morale budgets?

**UI:**
Skills board shows each duplicant's tree with unlocked nodes highlighted, morale cost shown per skill, and interests shown as icons. The overall morale balance is visualized with a threshold bar. No per-task live assignment preview; players must cross-reference task requirements with skill trees mentally.

**Reception:**
Considered one of the most sophisticated simulation skill systems in the genre. The morale cost as a resource cap on specialization depth is widely praised as a clever constraint. Main criticism: the disconnect between "job assignment" (for XP gain) and "task permission" (from skill tree) confuses new players.

**Sources:**
- [ONI Wiki — Skills](https://oxygennotincluded.wiki.gg/wiki/Skills)
- [ONI Wiki — Skills Board](https://oxygennotincluded.wiki.gg/wiki/Skills_Board)
- [Gamepressure — ONI Attributes and Assigning Jobs](https://guides.gamepressure.com/oxygen_not_included/guide.asp?ID=40261)

---

### Spirit Island (Digital + Tabletop) — Elemental Threshold Coverage

**How it works:**
Eight elements (Sun, Moon, Fire, Air, Water, Earth, Plant, Animal). Each turn, spirits gain elements from the power cards they play plus progression track bonuses. Innate powers (unique per spirit, printed on the spirit board) have tiered threshold requirements: e.g., Tier 1: 2 Fire = "deal 1 damage"; Tier 2: 2 Fire + 1 Earth = "deal 1 damage AND push 1 explorer"; Tier 3: 3 Fire + 1 Earth + 1 Air = full effect. Elements are not consumed — they're a "check" at resolution. Players may choose to satisfy a lower tier even if a higher one is available.

**Multi-skill coverage as design foundation:** Spirit Island's entire strategic engine is built around element coverage. Card selection is a drafting problem of "which elements can I generate consistently across multiple turns?" Cooperative play adds inter-player element sharing (some powers grant elements to other spirits). The decision space is exceptionally rich — 10-15 cards to choose from per game, each card a different element profile, each spirit needing a specific profile to fire its innate powers.

**UI (digital version):**
Cards display element icons prominently. Spirit board shows innate power tiers with element requirements in brackets. During the Spirit Phase, current element totals are shown as a running tally. Threshold brackets glow when met.

**Reception:**
Considered one of the most elegant multi-resource threshold systems in modern games, digital or analog. The "non-consuming" nature of thresholds (checking rather than spending) removes analysis paralysis around whether to "save" elements. Community discussion around element-combo optimization is extensive and positive.

**Sources:**
- [Spirit Island Wiki — Elements](https://spiritislandwiki.com/index.php?title=Elements)
- [Greater Than Games Forums — Strategy: Drawing for Elements](https://forums.greaterthangames.com/t/strategy-drawing-for-elements/16901)
- [Querki — Elemental Thresholds FAQ](https://querki.net/raw/darker/spirit-island-faq/Elements+and+Elemental+Thresholds)

---

### Pandemic (Tabletop/Digital) — Role Ability Coverage

**How it works:**
Each player draws a random Role card at game start. Five base roles (Medic, Scientist, Researcher, Dispatcher, Operations Expert) each provide a unique mechanical exception to standard rules. Roles don't have "skill levels" — they provide binary exceptional abilities. Team coverage challenge: the combination of roles determines which parts of the problem space (treatment, curing, logistics, distribution) are made easier. No per-event assignment of roles — each player's role is fixed and active at all times.

**Multi-skill relevance:** Pandemic is the purest expression of "role coverage determines team viability." If the team has neither Medic nor Scientist, cube management and curing are both harder. The mechanic models skill coverage as team composition at setup, not in-session assignment.

**UI:**
Role card is fixed; abilities listed in text. No assignment UI. No preview. The coverage decision is made once (role dealing) and its implications unfold through play.

**Reception:**
Role asymmetry in Pandemic is considered a gold standard for cooperative design. The simplicity (one role, a few exceptions) means new players can understand their role immediately. Expansions added more roles (Contingency Planner, Quarantine Specialist) to increase coverage variety.

**Sources:**
- [Pandemic Wikipedia](https://en.wikipedia.org/wiki/Pandemic_(board_game))
- [Board Game Geek — All Available Pandemic Roles](https://boardgamegeek.com/geeklist/47148/all-available-pandemic-roles)
- [The Gamers' Guides — Pandemic Strategy Guide](https://www.thegamersguides.com/pandemic-board-game-strategy-guide/)

---

## Cross-Cutting Patterns

### UI Patterns Common Across the Genre

1. **Live die/modifier preview before commit** (Citizen Sleeper 1 & 2): Showing exact outcome probabilities before a die is locked is the strongest player-trust mechanism. It shifts player frustration from "the game cheated me" to "I made a calculated risk."

2. **Grid/matrix for team-level skill overview** (RimWorld Work Tab, Dwarf Fortress Units screen, Fallout Shelter SPECIAL assignment): When the coverage challenge is portfolio-level (many tasks, many workers), a scannable 2D grid is the dominant UI pattern. Column = worker/task; Row = task/worker; cell content = skill level or assignment state.

3. **Color-coding for quality tiers** (RimWorld brightness, Lobotomy Corp blue/red numbers, FTL room states): Almost all systems use hue/brightness to communicate skill adequacy without requiring number reading. Green/yellow/red or dim/bright are universal.

4. **Element icon sets as compact vocabulary** (Spirit Island, Citizen Sleeper skill icons, Lobotomy Corp work type colors): When there are 4-8 distinct skill types, dedicated icons become the "alphabet" players learn. Players eventually read icon patterns faster than text.

5. **Shortfall as Stress/meter vs. immediate failure** (CS2 Derelict Stress, Oxygen Not Included Morale, FTL hull integrity): Modern designs favor accumulated-pressure failure (meter fills over multiple shortfall events) over binary pass/fail. This allows players to recover and makes shortfalls feel like tactical setbacks rather than arbitrary endings.

### Math Patterns

1. **Additive flat bonus** (Citizen Sleeper +0/+1/+2 to die; Sunless Sea officer stat stacking; FTL piloting skill = % evasion per level): Most common. Simple, legible, easy to tune.

2. **Binary gate with graded coverage** (Frostpunk Worker/Engineer: type gate is binary, but headcount is continuous): Two-tier: pass the type gate first, then more bodies = more output. Clean for macro management games.

3. **Probability success rate** (Lobotomy Corporation: stat * 0.2% per point, capped 95%; Sunless Sea: 0-100% challenge): Creates graded coverage where any team can attempt any task but specialists dramatically outperform generalists.

4. **Threshold check with tiered rewards** (Spirit Island: 2 Fire = Tier 1, 4 Fire + 1 Earth = Tier 2): Coverage above minimum generates bonus effects rather than just reducing failure risk. Creates incentive to over-invest in coverage for rewards, not just to avoid failure.

5. **Per-individual vs. pool-aggregate math**: All games reviewed resolve individual skill-action pairs (one worker does one task) rather than pooling all skill points into one check. The "pool to cover" pattern is more common in tabletop (FFG Star Wars dice pools, Blades in the Dark position/effect) than digital.

### Decision-Space Patterns

- **At-setup coverage** (Pandemic roles, Sunless Sea officer hiring): Decision made once; implications last entire game. Highest strategic weight, lowest tactical friction.
- **Per-cycle assignment** (Citizen Sleeper dice placement, FTL station manning, Lobotomy Corp work dispatch): Decision made every cycle/round. Highest tactical friction, highest player agency. Scales poorly with roster size > 8.
- **Priority + autonomy** (RimWorld, Dwarf Fortress, ONI): Player sets priority rules; agents execute autonomously. Best for large rosters (10-40 units). Player's role is strategic configuration, not tactical direction. Creates satisfying "system running itself" moments.
- **Tree-constrained coverage** (Oxygen Not Included, Two Point Hospital training): Player shapes coverage by investing in skill trees over time. Long-term planning game within the coverage system.

---

## Recommendation for AE — TTRPG Context

**Context:** AE uses 2d6+Fit-vs-Threshold as its core resolution. We are considering a multi-skill coverage layer for "work-station" tasks like the Driver Post, where multiple skill requirements must be met by crew assignment.

### Pattern 1: Spirit Island Elemental Threshold — directly translatable

**Why:** The threshold model (2 Rigging + 1 Systems = partial; 2 Rigging + 2 Systems + 1 Tinkering = full) maps perfectly to AE's tabletop context. Requirements are printed on station cards. Coverage is checked, not consumed. Players see their crew's skill totals, check against the card, and know their tier before rolling. The tiered-reward structure (shortfall = degraded outcome, full coverage = bonus die) avoids binary failure while rewarding optimization. Physical station cards as the "spirit board" equivalent are already native to tabletop play.

**Implementation note:** Create Station Cards with a two- or three-tier threshold bracket printed prominently. Crew assign by placing their character card or a token at the station. Count skills contributed; resolve at the matched tier.

### Pattern 2: Citizen Sleeper Skill-Advantage Modifier — live preview feedback

**Why:** CS2's +1 Advantage / -2 Disadvantage system is the simplest way to model skill coverage as a die modifier in a 2d6 system. A station that "needs Systems 2" could grant +1 per level of Systems coverage above the minimum, and impose -1 or -2 when the crew is below minimum. This produces graded outcomes from existing 2d6 rolls rather than requiring a new subsystem. The principle of showing the modifier before the roll (live preview) maps to tabletop as "count your crew skills, announce the modifier, then roll."

**Implementation note:** Crew tile cards showing skill levels face-up at the station provide the same "live preview" function as CS's drag-to-slot UI. The modifier is computed openly by the table before dice are thrown.

### Pattern 3: RimWorld Work Grid as Physical Assignment Board — scales to crew management

**Why:** For AE sessions with 4-6 stations requiring simultaneous coverage each shift, a physical assignment matrix — a laminated card or dry-erase grid with crew names on one axis and station names on the other — gives the GM and players a scannable "team coverage map" at a glance. This directly mirrors RimWorld's work tab, which players found solved the cognitive load of managing many workers across many tasks. The visual shorthand (filled = assigned, colored dot = skill match quality) can be implemented with simple marker or tokens.

**Implementation note:** A "Shift Planning Phase" where all crew cards are placed on the assignment grid before the shift begins (rather than resolved ad hoc) gives players the deliberate pre-commitment feel of Pandemic's role assignment combined with RimWorld's grid legibility.
