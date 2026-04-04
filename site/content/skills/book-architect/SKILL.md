---
name: book-architect
description: "Generate pain-point-driven book outlines with 10 title/subtitle options and 8-chapter structures. Use after niche and keyword research is complete."
type: decision
source_chapters:
  - ch-04
source_speakers:
  - Sean Dollwet
---

# Book Architect

Transform a validated niche into a complete book blueprint: reader pain points, 10 title options, 10 subtitle options, and a detailed 8-chapter outline with 3 subchapters and 3 sections each. Based on Sean Dollwet's ChatGPT drafting pipeline from Chapter 4.

## Usage

```
/book-architect --niche "beekeeping for beginners" --keyword "beekeeping for beginners"
/book-architect --niche "anxiety management" --keywords "anxiety relief" "stress management" "calm mind"
```

## Prerequisites

- Niche validated via `/niche-scout`
- Primary keyword identified via `/keyword-fill` or niche research
- Target audience understood

---

## Workflow

### Phase 1: Reader Pain Point Discovery

Start by understanding the reader, not by writing.

> "Instead of saying straight up, hey, write me a book on mental toughness, you have to first identify the pain points so that we can write a book around that."
> -- Sean Dollwet, "How to Create an eBook FAST with ChatGPT (Step-By-Step)"

**Prompt to use:**

```
I'm writing a book about [NICHE/TOPIC]. Please help me list the biggest pain points
of the reader that needs to be solved. Tell me what they feel and think and what they want.
```

**Review the output critically:**
- Are these real problems readers face, or generic filler?
- Cross-reference against negative reviews of competitor books (what do readers complain about?)
- Add pain points from your own knowledge/experience
- Rank pain points by severity and frequency

**Output:** A ranked list of 8-12 reader pain points that the book will solve.

### Phase 2: Title Generation (10 Options)

Generate title ideas that incorporate the primary keyword AND address the pain points from Phase 1.

**Prompt:**

```
Based on these reader pain points: [PASTE PAIN POINTS]

Generate 10 short title ideas for a book about [TOPIC].
The title should incorporate the keyword "[PRIMARY KEYWORD]".
Keep titles simple and instantly clear.
```

**Title rules from Sean Dollwet:**

> "If people have to stop and read the title, read the book cover, and take a couple seconds just to understand what the book is about, then that is a failed book cover. You want people to know instantly, without even thinking, without even observing carefully, what the book is about in a split second."
> -- Sean Dollwet, "Amazon KDP MISTAKES"

> "Just call it 'Robots Fighting Dinosaurs Coloring Book.' You don't have to do this whole 'first high quality cool premium coloring book.'"
> -- Sean Dollwet, "Amazon KDP MISTAKES"

**Output:** 10 title options ranked by clarity and keyword integration.

### Phase 3: Subtitle Generation (10 Options)

The subtitle carries the SEO weight. Your main keyword belongs here if it's not already in the title.

**Prompt:**

```
Please give me 10 long subtitle ideas about [CHOSEN TITLE].
It should clearly describe the benefits of reading the book.
Use power words and numbers to make it attractive.
Add the keyword "[TARGET KEYWORD]" to it.
```

**Subtitle rules:**

> "Explain what the book is in the subtitle... it could be as simple as 'sci-fi superhero thriller' or 'sci-fi superhero adventure for kids.'"
> -- Sean Dollwet, "Amazon KDP MISTAKES"

For nonfiction, frame the benefit with a concrete promise. Sean rewrites a meditation subtitle from "The Simple Guide to Mindfulness and Improved Mental Health" to: "A simple guide to discover inner peace, develop mindfulness, and improve mental health in 30 days or less."

**Avoid health claims:** Words like "heal" or "cure" will block Amazon Ads. Use "improve," "discover," or "support" instead.

**Output:** 10 subtitle options ranked by benefit clarity and keyword integration.

### Phase 4: Detailed Book Outline

This is the structural backbone. Generate a full outline with specific constraints.

**Prompt:**

```
Create a detailed 8 chapter book outline with three subchapters
that have three sections for a book on [TOPIC].
The title is [CHOSEN TITLE]. The subtitle is [CHOSEN SUBTITLE].

Additional requirements:
- Avoid repeating the same information throughout the book
- Start each chapter with a hook -- relevant quote, interesting facts, statistics
- Focus on novel ideas rather than basic information
- Focus on actionable steps rather than just facts
- Break each chapter into 3 sub-chapters
- Expand each subchapter with 3 bullet points
- Use markdown formatting
```

**Outline validation checklist:**
- [ ] Does every chapter solve a real pain point from Phase 1?
- [ ] Is there progression (beginner concepts first, advanced later)?
- [ ] No repeated information across chapters?
- [ ] Each chapter has actionable takeaways, not just information?
- [ ] Chapter hooks are specific and engaging?
- [ ] Total structure supports ~30,000 words (3,750 words/chapter)?

### Phase 5: Word Count Planning

Target specifications from Sean Dollwet:

| Level | Target |
|-------|--------|
| Total manuscript | ~30,000 words (120-150 pages) |
| Per chapter | 30,000 / 8 = ~3,750 words |
| Per subchapter | 3,750 / 3 = ~1,250 words |

This structure directly feeds the `/manuscript-drafter` skill, which generates content one 1,250-word section at a time.

---

## Output Format

### Complete Book Blueprint

```markdown
## Pain Points Addressed
1. [Pain point] -- addressed in Chapter [X]
2. [Pain point] -- addressed in Chapter [X]
...

## Title: [Chosen Title]
## Subtitle: [Chosen Subtitle]
## Primary Keyword: [keyword]

## Outline

### Chapter 1: [Title]
Hook: [Quote, fact, or statistic]

#### 1.1 [Subchapter Title]
- [Section 1.1.1]: [Description + key points]
- [Section 1.1.2]: [Description + key points]
- [Section 1.1.3]: [Description + key points]

#### 1.2 [Subchapter Title]
...

#### 1.3 [Subchapter Title]
...

### Chapter 2: [Title]
...

[Repeat for all 8 chapters]

## Word Count Targets
| Chapter | Subchapters | Target Words |
|---------|------------|-------------|
| Ch 1    | 3 x 3 sections | 3,750 |
| Ch 2    | 3 x 3 sections | 3,750 |
| ...     | ...        | ...         |
| Total   | 72 sections | 30,000 |
```

### Title/Subtitle Options (All 10)

| # | Title | Subtitle | Keyword Coverage | Notes |
|---|-------|----------|-----------------|-------|
| 1 | [title] | [subtitle] | [keywords hit] | Recommended |
| 2 | [title] | [subtitle] | [keywords hit] | |
| ... | | | | |

---

## Related Skills

- **[[niche-scout|niche-scout]]** -- Validate niche before architecting (run FIRST)
- **[[keyword-fill|keyword-fill]]** -- Identify keywords for title/subtitle integration
- **[[competitor-reverse-engineer|competitor-reverse-engineer]]** -- Study competitor TOCs and chapter structures to identify content gaps and reader expectations
- **[[manuscript-drafter|manuscript-drafter]]** -- Generate content section-by-section from this outline
- **[[cover-brief|cover-brief]]** -- Create cover design brief using the chosen title

## Related Frameworks

- `low-content-creation-pipelines.md` — If creating journals, planners, or activity books instead of high-content manuscripts, use this framework instead of the 8-chapter outline approach
- `offer-naming-for-book-titles-hormozi.md` — Hormozi's naming methodology applied to book titling: the title IS the offer name, name the dream outcome, not the topic
