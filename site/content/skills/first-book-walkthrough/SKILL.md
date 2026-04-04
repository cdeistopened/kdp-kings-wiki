---
name: first-book-walkthrough
description: "Walk a first-time publisher through the complete KDP process step by step — from blank idea to published book. Teaches each phase, applies it to their book, then advances. Use when someone says 'I want to publish my first book' or 'where do I start with KDP.'"
type: tutor
source_chapters:
  - ch-01
  - ch-02
  - ch-03
  - ch-04
  - ch-06
  - ch-07
  - ch-08
  - ch-09
  - ch-10
  - ch-11
source_speakers:
  - Sean Dollwet
  - Dale L Roberts
  - Dave Chesson
---

# First Book Walkthrough

A guided tutorial that takes a first-time KDP publisher from "I want to publish a book" to "my book is live on Amazon" in 7 teaching phases. Each phase teaches the concept, applies it to the user's actual book, and produces a deliverable before moving on.

## Usage

```
/first-book-walkthrough
/first-book-walkthrough --idea "I want to write a book about container gardening"
/first-book-walkthrough --resume phase-3
```

## How This Skill Works

Unlike decision skills that produce one output, this tutor skill is a conversation. It teaches, applies, checks understanding, then advances. The user should be able to stop at any phase and have a usable deliverable for that stage.

**The teacher's mindset:**

> "The biggest thing that I can suggest for everyone is to just get started... The hardest part about anything is just starting."
> -- Sean Dollwet, "How to Self Publish a Book on Amazon (STEP-BY-STEP)"

The first book doesn't need to be perfect. It needs to exist.

---

## Phase 1: The Business Model (10 minutes)

**Teach:** How KDP makes money. Three revenue channels (Kindle, paperback, audiobook), royalty tiers, and the compounding portfolio model.

> "Your goal is to essentially run the publishing house at a profit while building a catalog of books that earns you recurring, mostly passive income."
> -- Sean Dollwet (paraphrased from Ch 1 revenue model)

**Key concept:** One book is a lottery ticket. Ten books is a business. The first book teaches you the system. The second book earns.

**Apply:** Ask the user:
1. What topic or niche interests you?
2. Do you plan to write it yourself or outsource?
3. What's your budget for the first book? ($0 / under $100 / under $500 / $500+)

**Deliverable:** A first-book brief: topic, writing method, budget tier, format target (ebook only vs. ebook + paperback).

**Reference:** `kdp-revenue-map.md`

---

## Phase 2: Niche Validation (20 minutes)

**Teach:** Why most first books fail — they pick a topic they love but nobody searches for. The 3-step validation framework: demand (search volume), willingness to pay (BSR analysis), and beatable competition.

> "The biggest mistake beginners make is to pick a niche that they're personally passionate about without validating that other people are actively searching for and buying books in that niche."
> -- Sean Dollwet (paraphrased from Ch 2)

**Key concept:** You don't need the best niche. You need a niche where self-published books are already selling — proof that the market exists and indies can compete.

**Apply:** Run `/niche-scout` on the user's topic. Walk them through the BSR data, competition signals, and series potential. If the niche fails validation, help them pivot to a related niche that passes.

**Deliverable:** A validated niche with BSR scorecard and keyword volume data.

**Reference:** `niche-validation-pipeline.md`, `niche-scout` skill

---

## Phase 3: Keywords and Title (15 minutes)

**Teach:** How Amazon's A9 algorithm matches buyers to books through keywords. The 7-box system. Why the title IS the most important keyword placement. The hybrid exact-phrase + broad-fill strategy.

> "Fill all 7 backend keyword boxes. No commas — Amazon treats spaces as separators. Front-load the highest-volume phrase. Never repeat words from your title — Amazon already indexes those."
> -- Dave Chesson (from the 121-author keyword experiment)

**Key concept:** Keywords determine who sees your book. Title determines whether they click. Both are search engine optimization, not creative expression.

**Apply:** Run `/keyword-fill` for their niche. Generate 10 title options using the Book Architect's pain point methodology. Evaluate titles against the thumbnail test and Hormozi's offer naming criteria.

**Deliverable:** 7 filled keyword boxes + chosen title and subtitle.

**Reference:** `keyword-research-pipeline.md`, `offer-naming-for-book-titles-hormozi.md`, `keyword-fill` skill, `book-architect` skill (Phases 2-3)

---

## Phase 4: Outline and Manuscript (30 minutes to start, then async)

**Teach:** The 8-chapter structure with 3 subchapters of 3 sections each. Why pain-point-driven outlines outperform topic-driven outlines. The safe AI publishing workflow for those using ChatGPT.

> "Instead of saying straight up, hey, write me a book on mental toughness, you have to first identify the pain points so that we can write a book around that."
> -- Sean Dollwet, "How to Create an eBook FAST with ChatGPT"

**Key concept:** The outline is the real creative work. The manuscript is execution. Spend 80% of your thinking time on the outline.

**Apply:** Run `/book-architect` to generate the full outline from their validated niche and keywords. If they're using AI, walk through the 4-step safe publishing workflow (generate, rephrase, check, polish).

**Deliverable:** Complete 8-chapter outline with word count targets. If AI-assisted, a drafted manuscript with compliance checks passed.

**Reference:** `safe-ai-publishing-workflow.md`, `book-architect` skill, `manuscript-drafter` skill

---

## Phase 5: Cover and Formatting (20 minutes)

**Teach:** The thumbnail test, the 8 cover mistakes that kill sales, budget-tier options ($0-$30 Canva, $30-$100 Fiverr, $100+ professional). Manuscript formatting: the two-phase framework (design vs. format), tool comparison (Kindle Create, Atticus, Vellum).

> "If people have to stop and read the title, read the book cover, and take a couple seconds just to understand what the book is about, then that is a failed book cover."
> -- Sean Dollwet, "Amazon KDP MISTAKES"

**Key concept:** Covers sell books. The interior just has to not lose the sale. Invest proportionally.

**Apply:** Run `/cover-brief` to generate a design brief for their genre. Walk through formatting options based on their budget and technical comfort.

**Deliverable:** Cover design brief ready for designer + formatted manuscript file.

**Reference:** `cover-creation-workflow.md`, `manuscript-formatting-workflow.md`, `cover-brief` skill

---

## Phase 6: Upload and Listing (20 minutes)

**Teach:** The three irreversible decisions during upload (language, title lock on print, ISBN vs. free ASIN). The 5-part description framework. Category selection with ghost and duplicate screening. Author bio template.

> "There are certain things that once you press publish, you cannot change. And the most important one is you cannot change the language of your book."
> -- Sean Dollwet (paraphrased from Ch 8)

**Key concept:** The upload is not a form to fill out quickly. Every field is an optimization opportunity or a trap.

**Apply:** Walk through `/upload-checklist` field by field. Run `/listing-optimizer` to generate the description, categories, and author bio.

**Deliverable:** Complete listing package (description HTML, 3 categories, author bio) + upload walkthrough completed.

**Reference:** `upload-checklist.md`, `listing-optimization-checklist.md`, `upload-checklist` skill, `listing-optimizer` skill

---

## Phase 7: Launch and First 30 Days (15 minutes)

**Teach:** The 4-phase launch (free promo, 99-cent period, ramp-up, full price). Review collection services. Social media video formats. Amazon Ads basics (start with auto campaign at $5/day).

> "When you first launch your book on Amazon it has a 30-day new book boost... Amazon will place your book in more categories, more keywords, just have people view your books more than usual in the first 30 days."
> -- Sean Dollwet, "Complete, No BS Guide to Book Launch"

**Key concept:** The launch is an investment, not a payday. You're buying rank. Profit comes after.

**Apply:** Run `/launch-sequence` with their publish date. Set up initial Amazon Ads via `/amazon-ads`. Plan the Content Pyramid extraction for social media.

**Deliverable:** 30-day launch timeline with pricing phases, ad budget, and content calendar.

**Reference:** `30-day-launch-sequence.md`, `content-pyramid-book-launches-garyvee.md`, `launch-sequence` skill, `amazon-ads` skill

---

## Progression Rules

1. **Never skip phases.** Each phase's output feeds the next. Publishing without keyword research is publishing blind.
2. **Let the user set the pace.** Some people want to complete all 7 phases in one session. Others need days between phases to write a manuscript.
3. **Validate before advancing.** At the end of each phase, confirm the deliverable exists and makes sense before moving on.
4. **Encourage imperfect action.** The first book teaches the system. Perfectionism is the enemy.

> "A lot of the people I've coached, once they publish five books, 10 books, 15 books... they're all producing quality content, they're doing everything right — and it's because they learned from those first few."
> -- Sean Dollwet (paraphrased from publishing philosophy)

---

## Related Skills

- **[[niche-scout|niche-scout]]** — Phase 2
- **[[keyword-fill|keyword-fill]]** — Phase 3
- **[[book-architect|book-architect]]** — Phases 3-4
- **[[manuscript-drafter|manuscript-drafter]]** — Phase 4
- **[[cover-brief|cover-brief]]** — Phase 5
- **[[listing-optimizer|listing-optimizer]]** — Phase 6
- **[[upload-checklist|upload-checklist]]** — Phase 6
- **[[pricing-strategist|pricing-strategist]]** — Phase 7
- **[[launch-sequence|launch-sequence]]** — Phase 7
- **[[amazon-ads|amazon-ads]]** — Phase 7

## Related Frameworks

- `kdp-revenue-map.md` — Phase 1: understanding the business model
- `niche-validation-pipeline.md` — Phase 2: validating demand
- `keyword-research-pipeline.md` — Phase 3: keyword strategy
- `safe-ai-publishing-workflow.md` — Phase 4: AI-assisted writing
- `cover-creation-workflow.md` — Phase 5: cover design
- `manuscript-formatting-workflow.md` — Phase 5: formatting
- `upload-checklist.md` — Phase 6: upload process
- `listing-optimization-checklist.md` — Phase 6: listing optimization
- `pricing-decision-matrix.md` — Phase 7: pricing
- `30-day-launch-sequence.md` — Phase 7: launch execution
