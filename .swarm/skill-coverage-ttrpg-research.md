# TTRPG Multi-Skill Coverage Research

> Research by Agent A — May 2026. Focus: how TTRPGs handle multi-skill task requirements, crew pooling, and skill-bar coverage. Targeted to Apocalypse Express's existing 2d20(d20)+skill vs DC system.

---

## Summary Table

| Game | Mechanic Name | How It Works (1 line) | Best For | Weakness |
|---|---|---|---|---|
| Burning Wheel | Linked Tests + FoRKs + Help | Chain of obstacle-gated rolls; each fail adds +1 Ob to next; related skills donate bonus dice pre-roll | Sequential task chains with meaningful failure cost | Dice-math overhead; FoRK cataloguing gets fiddly |
| Blades in the Dark | Group Action + Set Up + Assist | Best result counts for whole group; leader eats stress for teammates' poor rolls; setup improves position | Fast crew cooperation, shared consequences | All must roll the same action — poor fit for diverse-skill tasks |
| Shadowrun 5e | Teamwork Test | Assistants roll first; each hit adds 1 die to leader's pool (capped at leader's skill rating) | Granular "expertise transfer" with a natural ceiling | Critical glitch from any assistant breaks the whole roll; cap punishes expert leaders |
| Traveller (Mongoose 2e) | Task Chain | Linked rolls where one result feeds next as DM bonus/penalty; any crew member can contribute their skill | Crew dispatch on a ship — different roles, different skills | Rules-light on what happens when the chain's middle link fails catastrophically |
| Spire | Skill + Domain dice assembly | Binary: have skill = +1d10, have domain = +1d10, mastery = +1d10; keep highest; GM removes dice for difficulty | Fast multi-axis qualification check | No numeric skill levels — can't represent "very good at Systems vs barely knows Rigging" |
| Heart: The City Beneath | Dice Pool (same engine as Spire) | 1d10 base + skill + domain + mastery; highest die wins; difficulty removes dice | Dangerous high-stakes rolls with binary skill qualification | Group cooperation is not formalized; each PC acts individually |
| Forged in the Dark (BitD family) | Position/Effect + Set Up | One action sets position or effect level for a follow-up action by a different PC using a different skill | Multi-skill sequential coverage without requiring same-skill rolls | Set Up timing is sequential, not simultaneous |
| Numenera / Cypher System | Asset Reduction | Each helper or complementary action lowers task difficulty by 1 step (max 2 steps from assets) | Simple, fast group effort that doesn't outscale the challenge | Hard cap of 2 steps means big crews don't matter beyond the first two helpers |
| Forbidden Lands / Year Zero Engine | Help Dice | Only one PC rolls; others may help by adding extra Skill dice before the roll; leader alone takes push risk | Focused crew effort where the expert drives and others boost | Help restricted in some actions (Scouting, Lead the Way); no per-skill differentiation |
| Apocalypse World 2e | Hold + Spend | Single stat roll gives "hold" points spent later for specific outcomes; gigs work as async resources | Resource-banking from skill use, deferred coverage | Hold is per-move, not a general multi-skill frame |
| Lancer | Skill Triggers | Each pilot has triggers that grant flat bonus (+2 to +6) to narrative checks; only one trigger per roll | Flexible narrative skill application; player-driven framing | Single trigger cap; no crew pooling — individual-only |
| Stars Without Number | Aid Another | Helper rolls a separate check vs the same DC; if they pass, lead character gets +1 (but max +1 total) | Low-overhead help with fiction-justified skill swaps | Only +1 max regardless of how skilled or how many helpers |

---

## Per-Game Deep Dives

### Burning Wheel — Linked Tests, FoRKs, and Help

**How it works:**
Burning Wheel uses three layered mechanics for multi-skill tasks. First, **Linked Tests**: a chain of rolls where each test's outcome feeds the next. If a test in the chain fails, subsequent tests gain +1 Obstacle. The chain frames a single large goal as a sequence of sub-tasks, each gated by a separate skill. Second, **FoRKs (Fields of Related Knowledge)**: before rolling, a player may add +1d per related skill their character possesses. A skill rated 7+ gives +2d instead. FoRKs are self-help — one character brings multiple competencies to bear. Third, **Help from allies**: another PC can donate +1d or +2d (if their skill is 5+) by describing how they assist, effectively transferring part of their skill pool to the roller. Help adds dice before the roll; the roller still needs to meet or exceed the Obstacle.

**Critical distinction:** Skills are never summed into a combined pool against a single number. Each roll tests one primary skill at one Obstacle. Surplus in a helper's skill doesn't compensate for the lead roller's deficiency beyond the bonus dice it grants.

**When triggered:** Whenever a task has clearly sequential phases (plan a heist, navigate a journey, repair a ship system), the GM decides it's a Linked Test. FoRKs apply any time a player can justify a related skill.

**Designer rationale:** Luke Crane designed Linked Tests explicitly as a pacing tool — resolve a journey or complex operation with a few rolls and coloring narration, then move to the emotional core of the story. The +1 Ob failure cascade means early mistakes compound, modeling how real-world failure chains work.

**Weakness:** The FoRK inventory becomes bookkeeping-heavy. Players must track which skills apply to which tests, and GMs must adjudicate plausibility in real time. Forums note that players sometimes FoRK dubiously-related skills, creating friction.

**Sources:** [Burning Wheel In-Depth — Cannibal Halfling](https://cannibalhalflinggaming.com/2020/07/29/burning-wheel-in-depth/) · [RPGnet Linked Tests thread](https://forum.rpg.net/index.php?threads/burning-wheel-linked-tests-confuse-me.553675/) · [BW Procedural Guide v2.2](http://questingblog.com/wp-content/uploads/2015/02/Burning-Wheel-Procedural-Guide-V2.pdf) · [Help and FoRKs with Beginner's Luck — brehaut.net](https://brehaut.net/blog/2021/help_and_forks_with_beginners_luck/)

---

### Forged in the Dark / Blades in the Dark — Group Actions, Set Up, Assist

**How it works:**
Blades in the Dark separates multi-skill crew work into three mechanics that can combine. **Group Action**: all PCs roll the same action (same skill); the single best result counts for the whole group; the leader takes 1 stress per PC who rolled 1–3. **Assist**: one PC takes 1 stress to give +1d to another PC's roll. Only one assist per roll is allowed. **Set Up**: a PC rolls a different action/skill to improve the **position** (risk level) or **effect** (impact level) for a follow-up action by a teammate who uses a *different* skill. This is how multi-skill sequential coverage is achieved — not pooling but chaining.

**Critical distinction for AE:** Group Action forces everyone to roll the same stat. Multi-skill coverage is achieved through Set Up: character A uses Wreck to break down a door (sets position), then character B uses Finesse to slip through. They used different skills for different phases, each determining the other's conditions.

**Position and Effect framing:** Before any roll, the GM assesses position (Controlled/Risky/Desperate) and effect level (Limited/Standard/Great). These two axes determine what a success actually achieves. A Set Up can shift either axis for the follow-up action. This means a strong performer in one skill can "donate" a better position to a weak performer in another skill.

**Weakness:** All members of a group action must use the same action, so a crew with diverse skills cannot truly pool. The stress cost mechanic on the leader is punishing for large groups. Assist is limited to +1d and one person.

**Sources:** [Blades in the Dark Teamwork SRD](https://bladesinthedark.com/teamwork) · [Action Roll SRD](https://bladesinthedark.com/action-roll) · [G+ Archive Group Action discussion](https://bitd.gplusarchive.online/2015/08/08/question-about-on-point-group-action-rolls/)

---

### Heart: The City Beneath — Dice Pool by Qualification

**How it works:**
Heart uses the Resistance system: 1d10 base + 1d10 if you have the relevant **skill** + 1d10 if you have the relevant **domain** + 1d10 if you have **mastery**. Keep the highest. Results: 1 = critical failure, 2–5 = failure, 6–7 = success at cost, 8–9 = success, 10 = critical success. Difficulty is handled by the GM removing dice *after* assembly (Risky = remove best die; Dangerous = remove two best dice), which is mechanically brutal and creates tension even for qualified characters.

Skills and domains are binary — you either have them or you don't. There is no numeric skill rating. This means a character with Systems does not have "Systems 3" vs "Systems 1" — they simply have Systems or they do not. Coverage is all-or-nothing per qualifier.

**Group coverage:** Heart does not formalize group pooling or crew coordination at a mechanical level. Characters act individually. The game is more about personal consequence (stress tracks, fallout) than collective resource management.

**Weakness for AE:** The binary skill qualification means it cannot express "Marlow has Systems 3, Rigging 0" — you'd either have Systems or not. The model is best for checking whether someone is qualified, not for expressing degrees of expertise. Also, no mechanism for one character's surplus in one skill to compensate for another's deficit.

**Sources:** [RPG Writeups — Heart](https://writeups.letsyouandhimfight.com/lazyangel/heart-the-city-beneath/) · [Ponderings on Games — Heart](https://ponderingsongames.com/2023/01/30/heart-the-city-beneath/) · [Dice Pool review](https://thedicepool.com/2024/07/15/heart-the-city-beneath/)

---

### Spire: The City Must Fall — Skill + Domain Dice Assembly

**How it works:**
Spire uses the same dice-pool engine as Heart (they share the Resistance System). Skills are what you do; Domains are where or to whom you do it. Both are binary. Roll 1–4d10 keep highest. Nine skills: Compel, Deceive, Fight, Fix, Investigate, Pursue, Resist, Sneak, Steal. Nine domains: Academia, Crime, Commerce, High Society, Low Society, Occult, Order, Religion, Technology.

The intersection of skill and domain creates specificity: a thief who has Steal + Crime domain is well-suited to stealing in criminal environments but has no domain bonus stealing from a High Society vault. A character with Fix + Technology repairs tech gear; Fix + Crime repairs criminal-world equipment or tools.

Multi-skill requirements: a task that requires both Investigate and Technology domain would ideally require one character who has both. If they don't have one, they lose that die. There's no mechanism to compensate a missing skill with surplus in another.

**Weakness:** Since skills have no numeric ratings, there's no "how good" — only "do you have it." The system works beautifully for quick qualification checks but cannot represent a crew where one character partially covers a requirement.

**Sources:** [Cannibal Halfling — The Independents: Spire](https://cannibalhalflinggaming.com/2018/03/21/the-independents-spire/) · [Fantasy Faction review](https://fantasy-faction.com/2020/spire-rpg-review-part-one-core-book) · [RPG Writeups — Spire](https://writeups.letsyouandhimfight.com/lazyangel/spire/)

---

### The Sprawl — Mission Clocks and Legwork Resources

**How it works:**
The Sprawl (a Cyberpunk PbtA game) splits task resolution into phases. During **Legwork**, characters gather abstract resources: **Intel** (spend for a roll bonus during the mission) and **Gear** (spend to produce equipment). Both are accumulated through skill-appropriate moves, but each piece of Intel or Gear is generated by a single-skill roll against a 2d6+stat result. The **Legwork Clock** tracks exposure — every Legwork roll risks advancing a 6-segment clock, alerting the target.

The design insight: intel and gear act as deferrable skill coverage. If your crew lacks a tech specialist, you gather Tech Intel during Legwork and spend it during the mission to offset the gap — a retcon-friendly abstraction. The actual mission rolls still use individual stats, but the pre-banked resources can bridge coverage gaps.

**Multi-skill handling:** The Sprawl does not pool skills or check skill-by-skill against requirements. It uses the PbtA pattern: one move, one stat. Coverage gaps are bridged indirectly through the intel/gear banking system.

**Weakness:** The retcon abstraction distances fiction from mechanics. The system doesn't natively answer "what happens when nobody in the crew can meet a specific technical requirement" — it just says "if you gathered enough Intel, you can."

**Sources:** [Creative Game Life — The Sprawl overview](https://www.creativegamelife.com/the-sprawl-tabletop-rpg) · [Age of Ravens — The Sprawl Hard Moves](http://ageofravens.blogspot.com/2017/09/the-sprawl-cyberpunk-hard-moves.html)

---

### Powered by the Apocalypse (General) — Moves and Single-Stat Design

**How it works:**
PbtA games are built around the principle that each **move** is triggered by fiction and uses exactly one stat. Stats typically range −2 to +3. Roll 2d6+stat: 10+ is a strong hit, 7–9 is a mixed hit, 6− is a miss. The move's text determines consequences at each tier. There is no standard multi-stat mechanic; each move owns its stat.

Some PbtA hacks have experimented with "use the lower of X or Y" (seen in Monster of the Week variants and some Dungeon World hacks), but the canonical Apocalypse World design avoids this. Apocalypse World 2e's "Hold + Spend" mechanic (e.g., Read a Sitch gives hold 3 on 10+, spend hold to ask GM questions) is a form of skill-result banking — you generate value with one stat and deploy it in fictional moments.

**For crew coverage:** PbtA does not have a crew-pooling mechanic. Each character acts with their own stats. Help is typically modeled as one character setting up a situation (via their own move) to give another character better fictional positioning for their move.

**Weakness:** The single-stat-per-move design is intentionally narrow. It's excellent for character expression but explicitly unsuited to "crew pooling skill requirements" as a core mechanic.

**Sources:** [lumpley.games — PbtA part 11](https://lumpley.games/2024/04/29/powered-by-the-apocalypse-part-11-dice/) · [Troy Press — Skill Mechanics for PbtA](https://troypress.com/skill-mechanic-for-pbta-games/) · [Apocalypse World basic moves preview](http://apocalypse-world.com/previews/BasicMoves2Epreview.pdf)

---

### Lancer — Skill Triggers (Narrative Mode)

**How it works:**
Lancer's narrative (out-of-mech) resolution uses **Triggers** — named areas of exceptional expertise (e.g., "Blow Something Up," "Get Somewhere Quickly," "Lead"). Each trigger grants a flat bonus from +2 to +6. When a character faces a challenge, they roll 1d20 + any one applicable trigger bonus. Only **one trigger can apply per roll**, regardless of how many could be argued to be relevant.

The game explicitly reverses the GM-calls-skill convention: the GM presents a situation; the player decides how to approach it and declares which of their triggers applies (subject to GM arbitration). This makes triggers descriptive of character concept rather than exhaustive skill lists.

**No crew pooling:** Lancer's narrative mode is individually-resolved. Crew collaboration at the fiction level is expected but there's no mechanical expression for "both pilots contribute their triggers to one task."

**Weakness for AE:** Triggers cannot be stacked or combined, which makes the system excellent for individual character expression but unable to model a work-station where multiple crew members pool different competencies toward a shared requirement.

**Sources:** [Forst Stories — Skill Triggers in Lancer](https://forststories.com/skill-triggers-lancer/) · [Lancer FAQ & Errata](https://lancer-faq.netlify.app/) · [RPG PUB — Wild Words SRD](https://www.rpgpub.com/threads/lancer-wild-words-srd-a-more-robust-narrative-mode-for-lancer.11291/)

---

### Coriolis: The Third Horizon — Year Zero Dice Pool + Pray to the Icons

**How it works:**
Coriolis uses the Year Zero Engine: roll a pool of d6s equal to (Skill + Attribute). Each 6 counts as a success; one success typically suffices. Extra successes unlock bonus effects; three or more = Critical Success. If you fail, you may **Pray to the Icons** (YZE's "push" mechanic): reroll all non-6 dice, but give the GM a **Darkness Point** (a GM resource for complications). The prayer reroll captures the "try harder at personal cost" design.

**Extended Actions:** Coriolis handles multi-round tasks by accumulating successes over multiple rolls until a threshold is met. The same skill is typically used throughout. Multiple characters may each roll their own pools and add successes — this is the closest the system comes to crew pooling, though it's still parallel individual rolls rather than a unified pool.

**Weakness:** No mechanism for different skills to contribute to the same extended action requirement. Two characters with different skills both rolling their own pools against the same task both need the same applicable skill — surplus from one doesn't transfer to the other's deficit.

**Sources:** [Stargazer's World — Coriolis review](https://stargazersworld.com/2017/07/17/review-coriolis-the-third-horizon/) · [Phil Gamer — Let's Study Coriolis](https://philgamer.wordpress.com/2017/02/03/lets-study-coriolis-part-3-systems-combat/)

---

### Numenera / Cypher System — Asset Steps and Complementary Actions

**How it works:**
Cypher System frames all tasks as difficulty levels 1–10 (target number = difficulty × 3). Characters reduce difficulty by: training (−1 step), specialization (−2 steps from the same skill), assets (−1 step per asset), or Effort (spend pool points for −1 step each). A helper character can serve as an **asset** by taking a relevant action — each helper who passes a check against the same difficulty provides −1 step, capped at 2 total asset steps. Complementary actions (different characters doing different but related things) provide +2 flat bonus to the primary roll.

This means: if a task requires Skill A and Skill B, character A's expertise reduces difficulty, and character B's complementary action gives a +2 bonus, even though they used different skills. The system absorbs multi-skill coverage through the asset/difficulty-reduction abstraction.

**Weakness:** The 2-step asset cap means four skilled helpers are no better than two. Also, the "complementary action" bonus applies to the same roll rather than qualifying separate skill requirements — it doesn't check whether each skill requirement is met individually.

**Sources:** [Obsidian Portal — Skills, Assets and Effort](https://numenera-tales.obsidianportal.com/wikis/rule-skills-assets-and-effort) · [Monte Cook — Beyond the Book: Asset Limits](https://www.montecookgames.com/beyond-the-book-asset-limits/)

---

### Forbidden Lands / Year Zero Engine — Help Dice

**How it works:**
Year Zero Engine (used in Forbidden Lands and Mutant Year Zero) consolidates crew effort into a single roll. When facing a group challenge, the group decides who is best suited (highest skill) and that character rolls. Other PCs may **help**: each helper adds extra Skill Dice to the roller's pool before the roll. The lead character alone may **push** (reroll at personal cost — injury/attribute damage). Help is explicitly forbidden in some actions (Scout, Lead the Way) where it would be unrealistic.

This is a clean dispatch model: the best-qualified character drives; others augment. However, all helpers add generic dice — there's no differentiation between "Marlow helps with Systems expertise" vs "Kenji helps with Rigging expertise." Help is help.

**Weakness for AE:** Year Zero's help model doesn't track what skill each helper is contributing. It answers "can this crew attempt this task?" with a combined dice pool but doesn't model "this task requires Systems 2 AND Rigging 3 — who covers which?"

**Sources:** [Year Zero Engine SRD — Free League](https://freeleaguepublishing.com/wp-content/uploads/2023/11/YZE-Standard-Reference-Document.pdf) · [SBRPG — Forbidden Lands Dice Pools](http://sbrpg20.blogspot.com/2022/03/forbidden-lands-dice-pools.html)

---

### Shadowrun 5e — Teamwork Tests (the most granular system found)

**How it works:**
Shadowrun's Teamwork Test is the most explicit multi-skill coordination mechanic found in the research. The team selects a **leader** (rolls the primary test). All **assistants** roll the same skill first; each hit (success) they score adds +1 die to the leader's pool. The cap: the leader cannot receive more bonus dice than their own skill rating. Additionally, each assistant who scores at least one hit increases the relevant **Limit** for the leader's roll by 1 (Limits cap the number of successes that count on a roll).

This means: a highly skilled leader benefits from many assistants; a barely-skilled leader hits the cap quickly. The Limit bonus from helpers is uncapped, which is significant.

**Critical glitch rule:** If any assistant rolls a critical glitch (roughly half the dice showing 1s), the Limit benefit is lost — a single unskilled helper can sabotage the whole effort.

**Why it's relevant to AE:** Shadowrun's model proves the general case that "assistants contribute skill-weighted dice, capped by the lead's skill" is a workable formal design. It doesn't handle multi-skill requirements (each assistant still uses the same skill as the leader), but the capping mechanic prevents trivial stacking.

**Sources:** [Shadowrun 5th SRD — Tests and Limits](https://shadowrun-5th-srd.fandom.com/wiki/Tests_and_Limits) · [Obsidian Portal — Teamwork Tests](https://shadowrun-throw-back.obsidianportal.com/wikis/teamwork-tests) · [Shadowrun 5e blog — Teamwork + Extended Tests](http://shadowrun20.blogspot.com/2016/04/how-to-use-teamwork-with-extended-test.html)

---

### Traveller (Mongoose 2e) — Task Chains

**How it works:**
Traveller models multi-step crew operations through **Task Chains**: a series of linked skill checks where the result of one roll becomes a DM (die modifier) for the next. A roll that scores Effect 0 (barely passed) gives no bonus to the next check; Effect 2+ gives +1 DM; Effect 4+ gives +2 DM. Failures penalize the next check. Different crew members can perform different links in the chain, each using their own skill.

This is the game closest to AE's "work station" concept: "the Engineer patches the power conduit (Engineering roll → Effect 2), which helps the Pilot stabilize the flight controls (Pilot roll at +1 DM)." Each skill in the chain is checked separately; the chain outcome depends on all links.

**Weakness:** Traveller's task chain doesn't have a formal "coverage determination" step. There's no notion of "this task requires Engineering 2 — does our crew meet that?" The system assumes narrative assignment (if nobody has Engineering, the relevant crew slot is empty and that chain link cannot be attempted). The formal mechanics only activate once the appropriate character is rolling.

**Sources:** [Take on Rules — Traveller Skills & Tasks](https://takeonrules.com/2020/09/28/lets-read-traveller-core-rulebook-skills-and-tasks/) · [Demiplane Nexus — Task Chains](https://app.demiplane.com/nexus/traveller/rules/task-chains)

---

### Stars Without Number — Aid Another (simplified group help)

**How it works:**
SWN uses 2d6 + Skill vs target number (6/8/10/12/14). One PC leads; others may aid by rolling the same or a related skill against the same difficulty. If the helper passes, the lead character gets +1 to their roll. **Maximum +1 total bonus regardless of how many help.** Importantly, the helper's skill does not need to match — if you can justify how your different skill helps, the GM may allow it.

**Weakness:** The hard +1 cap means expertise is essentially irrelevant for helpers — a master engineer helping vs a novice helping both give the same +1. The uncapped leader-skill bonus in Shadowrun is a significant improvement.

**Sources:** [Take on Rules — Group Rolls for SWN](https://takeonrules.com/2020/12/21/thinking-through-group-rolls-for-stars-and-worlds-without-number/) · [RPG Workshop — SWN modifications](https://rpgworkshop.wordpress.com/stars-without-number/stars-without-number-modifications-and-clarifications/)

---

## Cross-Cutting Patterns

Across all researched games, five structural patterns recur:

### Pattern 1: "Best Die Counts" (BitD family, Heart/Spire)
Roll everyone; take the single best result; leader absorbs stress/cost for failures. Simple, fast. Breaks down when different tasks require different skills — forces all participants to use the same action.

### Pattern 2: "Dice Donation" (Burning Wheel Help, Year Zero Help, Shadowrun Teamwork)
Others contribute dice to the primary roller before the roll. The primary character's skill rating often caps how many bonus dice are meaningful. Surplus in the helper's skill doesn't compensate for the lead's deficiency — it only adds dice to the primary pool. The Shadowrun cap-by-leader's-skill is the most elegant version.

### Pattern 3: "Difficulty Reduction / Asset Steps" (Cypher System, some PbtA)
Instead of adding dice, helpers reduce the number needed. Cap typically applies (2 steps from assets in Cypher). Complementary actions from different skills contribute to the same roll. Loses granularity on who covers what requirement.

### Pattern 4: "Sequential Chain / Linked Tests" (Burning Wheel Linked Tests, Traveller Task Chains, BitD Set Up)
Different characters use different skills in sequence; each result influences the next. This is the pattern that most naturally handles "task requires multiple distinct skills" — each link in the chain is checked separately. Failure in one link costs something (harder Ob, negative DM, worse position).

### Pattern 5: "Resource Banking" (The Sprawl, Apocalypse World Hold, BitD downtime)
Skills are used ahead of time to generate abstract resources (Intel, Gear, Hold) that are spent during execution to offset coverage gaps. Elegant for fiction but disconnects the moment of skill use from the moment of coverage determination.

### Where dice roll relative to coverage determination:
- **BW, YZE, Shadowrun:** Coverage is determined first (assign character, assemble dice), *then* roll.
- **BitD Group Action:** Everyone rolls simultaneously; coverage is the aggregate.
- **Cypher:** Difficulty is assessed first; helpers reduce it before the single primary roll.
- **Traveller Task Chain:** Coverage is narrative ("assign your Engineer to this link"); roll happens per link.

No surveyed game checks skill requirements per-skill and then rolls separately for each deficiency/surplus. The closest is **Burning Wheel Linked Tests** where each skill in a sequence is checked discretely at its own Obstacle.

---

## Recommendation for Apocalypse Express

AE's existing core: `d20 + skill modifier vs DC`, with Bands (CS/S/F/CF), Keyed/Open Locks, and a clearly structured check-block format. The research points to three patterns that fit without requiring a rebuild:

---

### Recommended Pattern 1: Per-Skill Coverage Check with Position Feed-Forward (Priority: HIGH)

**Closest analog:** Burning Wheel Linked Tests + BitD Set Up combined.

The work station has N skill requirements listed. Each requirement is a separate check. Assign one crew member per requirement (or leave it unassigned). Each assigned character rolls their skill vs the requirement's DC. Results feed into an aggregate "coverage score" that determines the final outcome:
- Full coverage (all checks S or CS): mission goes as planned.
- Partial coverage (some F, none CF): complications arise, costs are incurred.
- Critical gap (any CF, or an unassigned requirement): serious degradation or failure.

**Why it fits AE:** AE already uses the check-block format with multiple checks per scene. The per-requirement structure simply means a work station is a scene with multiple mandatory checks, each assigned to a crew member. It integrates with the existing Locks/Bands system without modification. The feed-forward from each check's Band into a composite outcome is novel but straightforward: sum CS=+1, S=0, F=-1, CF=-2 and read a coverage table.

**Design notes:** Surplus in one skill does NOT compensate for deficit in another — this is intentional and narratively meaningful. Marlow's Systems 3 doesn't fix the Rigging 0 problem. Each requirement stands.

---

### Recommended Pattern 2: Dice Donation with Skill-Capped Ceiling (Priority: MEDIUM)

**Closest analog:** Shadowrun Teamwork Test (most granular found), adapted to d20.

When a character assists on a specific skill check, they roll their own version of that skill. Each band of their result donates a modifier to the lead roller: CS grants +3, S grants +1, F grants 0, CF grants -1. The total bonus donated is capped at the lead character's own skill rank × 2 (prevents unskilled characters from trivially covering skilled requirements).

This handles the "crew pools skill points" framing cleanly. A high-skill helper provides meaningful benefit; a low-skill helper provides marginal benefit; the cap prevents the crew from trivially covering a Keyed R3 requirement by ganging up on it.

**Why it fits AE:** AE's Open Lock already gives Advantage (at-or-over rung) or Disadvantage (under rung) — this extends the same logic to assistance rolls. The Bands-based donation (+3/+1/0/-1) slots directly into AE's existing Offset system. No new resolution layer needed.

---

### Recommended Pattern 3: Upfront Coverage Declaration as Difficulty Dial (Priority: MEDIUM-HIGH)

**Closest analog:** Cypher System Asset Steps, reframed as a pre-roll coverage assessment.

Before any work-station roll, the GM (or the fictional framing) declares how many skill requirements the station has. The crew declares how many they can cover (assign characters who meet each requirement). Each uncovered requirement adds +2 to the work station's effective DC. Each covered requirement at R1-below adds +0. Each covered requirement at R-met adds +0. Each covered at R-above adds -1 (surplus mastery).

This is fast, fiction-forward, and integrates cleanly with AE's dial-based DC modifiers (already used in the Stealth matrix). It models "skill coverage determines difficulty, dice determines execution" — the exact dispatch pattern the prompt describes. It answers the coverage question before the roll, not after.

**Why it fits AE:** AE already uses modular DC construction (Scene DC + dials). "Uncovered requirement = +2 DC dial" is the same pattern as "Hostile NPC = +2 DC dial" in the Influence rules. No structural change required; just a new dial category for work-station scenes. The dice roll comes AFTER coverage is assessed, which is the cleanest design: determine your situation, then test your execution.

---

### What NOT to adopt

- **Binary skill qualification (Heart/Spire):** AE's existing rank system (R1–R4) already has numeric granularity. Flattening to binary would be a regression.
- **Same-action group roll (BitD Group Action):** Requires all crew to use the same skill. Inappropriate for multi-skill dispatch.
- **Uncapped dice stacking:** Any help system needs a ceiling to prevent trivial coverage. The Shadowrun cap-by-leader-skill or AE's Keyed Lock concept both provide this.
- **Resource banking as primary coverage model (The Sprawl):** Too much abstraction for a train-based scene-by-scene game where real-time skill application is the core fiction.

---

*Research cutoff: May 2026. 11 game systems covered. 25+ sources consulted.*
