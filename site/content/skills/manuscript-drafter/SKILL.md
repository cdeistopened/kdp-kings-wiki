---
name: manuscript-drafter
description: "Generate book manuscript content section-by-section at 1,250 words per section with anti-AI detection safeguards. Use after book-architect produces an outline."
type: decision
source_chapters:
  - ch-04
source_speakers:
  - Sean Dollwet
  - Dale L Roberts
---

# Manuscript Drafter

Generate a complete book manuscript one section at a time, following Sean Dollwet's 4-step safe publishing workflow. Each section targets 1,250 words, designed to stay within AI context window limits while maintaining quality. Includes the anti-AI detection checklist that separates publishable content from flaggable output.

## Usage

```
/manuscript-drafter --outline "path/to/outline.md" --chapter 1 --section 1.1
/manuscript-drafter --outline "path/to/outline.md" --all
```

## Prerequisites

- Complete book outline from `/book-architect` (8 chapters, 3 subchapters, 3 sections each)
- Pain points list from Phase 1 of [[book-architect|book-architect]]
- Target keyword and title/subtitle finalized

---

## The 4-Step Safe Publishing Workflow

> "You're really only adding two extra steps that might take a little bit of time but it is to ensure that your content does not get blocked and also that your account is safe long-term."
> -- Sean Dollwet, "Do NOT Use ChatGPT To Write a Book in 2026 - Unless You Do THIS"

| Step | Action | Tool |
|------|--------|------|
| 1. Generate | Draft content with AI | ChatGPT / Claude |
| 2. Rephrase + Add Input | Rewrite + add personal knowledge, stories, fact-checking | Manual + QuillBot |
| 3. Check for AI & Plagiarism | Run detection checks | Originality.ai / Grammarly Premium |
| 4. Publish on KDP | Only after steps 2-3 pass | KDP Dashboard |

---

## Workflow

### Step 1: Generate One Section at a Time

Target specifications:
- **Total manuscript:** ~30,000 words (120-150 pages)
- **Per chapter:** ~3,750 words
- **Per section:** ~1,250 words

> "The key to writing non-fiction with AI is you want to break down the chapter in as much subsection as possible so that you can write in as little section as possible."
> -- Sean Dollwet, "How to ACTUALLY Write a Book with ChatGPT - Full Tutorial"

**Section generation prompt:**

```
Please write 1,250 words for Chapter [X] [chapter title],
Section [Y.Z] [section title].
Cover these points: [bullet points from outline].
Don't write in a list style.
Focus on practical advice and use stories to make the information more personal.
```

**Why section-by-section?** The context window problem:

> "Context window is essentially how much AI remembers what it wrote in the past... this is right now the biggest issue when it comes to writing a book with AI because when it comes to shorter outputs it's very easy... but longer outputs when it comes to writing the entire book, 100 page, 200 page content, it becomes tricky because it becomes very repetitive and surface level."
> -- Sean Dollwet, "How to ACTUALLY Write a Book with ChatGPT - Full Tutorial"

AI output quality degrades around 2,000-3,000 words in a single generation. The 1,250-word target stays safely below this threshold.

### Step 2: Heavy Editing (Non-Negotiable)

> "Never just copy paste what you generated from ChatGPT into a book and just publish it with no editing no humanizing nothing because that rarely makes a good book. There's a 99% chance that that book is not good enough."
> -- Sean Dollwet, "How to ACTUALLY Write a Book with ChatGPT - Full Tutorial"

**Editing checklist for every section:**

- [ ] Fact-check every claim, statistic, and reference
- [ ] Replace AI-generated anecdotes with personal stories or verified real-world examples
- [ ] Cut fluff and surface-level generalizations
- [ ] Rewrite sections that read flat or generic
- [ ] Add personal voice, opinions, and lived experience
- [ ] Use iterative prompts to improve weak passages ("Rewrite this to be more [specific/persuasive/practical]")

**What separates a 3-star book from a 5-star book:**

> "If you look at all the bestselling non-fiction books... they do have good tips, but it's often how they delivered that tip inside the book through storytelling. Sharing the author's story on how they used that tip, real life examples of other people using it. That's what separates a five-star quality non-fiction book to a three or four star."
> -- Sean Dollwet, "How to Create an eBook FAST with ChatGPT (Step-By-Step)"

AI gives you the information layer. You supply the human layer.

### Step 3: AI Detection Check

Sean tested 5 methods for making AI content undetectable. Results:

| Method | Technique | Originality.ai Result |
|--------|-----------|----------------------|
| 1 | QuillBot + Grammarly rewrite | 100% AI |
| 2 | Pre-training ChatGPT with "human-like" prompt | 100% AI |
| 3 | Asking ChatGPT to "write like a human" | 100% AI |
| 4 | Asking ChatGPT to rewrite its own output | 100% AI |
| **5** | **Manual rewrite in your own words (~5 min per section)** | **99% Original, 1% AI** |

> "Method number five... essentially accepting that you have to put in the work and manually rewrite the content... I took about five minutes maybe to rewrite the whole thing in my own words... it came back as 99% original, 1% AI."
> -- Sean Dollwet, "How I Use AI for Self Publishing"

**No shortcut beats manual rewriting.** Every other method failed completely.

### Step 4: Plagiarism Check

Run every section through:
1. **Grammarly Premium** plagiarism checker, OR
2. **Originality.ai** for combined AI + plagiarism detection

If outsourcing, also run the encoding detection check (see Chapter 5) -- invisible characters between letters can fool standard plagiarism tools.

---

## Amazon's AI Content Classification

> "KDP officially came out with a statement regarding AI content and they basically classified AI content in two different ways. The first one is AI generated... compared to that AI assistant is something like you write the book yourself or you create the images yourself and then you use AI to edit that later on."
> -- Sean Dollwet, "COMPLETE ChatGPT Tutorial for Amazon KDP"

| Classification | Definition | Disclosure Required? |
|---------------|------------|---------------------|
| AI-Generated | Content created by AI, even with substantial modification | Yes |
| AI-Assisted | You write, AI edits/improves/polishes | No |

The more human input you layer in, the stronger your position with both Amazon and readers.

---

## Section Generation Template

For each of the 72 sections (8 chapters x 3 subchapters x 3 sections):

```markdown
## Section [X.Y.Z]: [Title]

**Chapter context:** [What this chapter covers]
**Section goal:** [What the reader should know/be able to do after reading]
**Pain point addressed:** [From Phase 1 pain point list]
**Key points to cover:**
- [Point 1 from outline]
- [Point 2 from outline]
- [Point 3 from outline]

**Word count target:** 1,250 words
**Stories/examples needed:** [Specific real-world examples to include]

---

[GENERATED CONTENT]

---

**Post-generation checklist:**
- [ ] Word count: _____ / 1,250 target
- [ ] Facts verified
- [ ] AI anecdotes replaced with real examples
- [ ] Fluff cut
- [ ] Personal voice added
- [ ] AI detection score: ___% original
- [ ] Plagiarism check: PASS / FAIL
```

---

## Production Timeline Estimate

| Task | Time Per Section | Total (72 sections) |
|------|-----------------|---------------------|
| AI generation | 2-3 min | 2.5-3.5 hours |
| Manual rewriting | 5-10 min | 6-12 hours |
| Fact-checking | 3-5 min | 3.5-6 hours |
| AI/plagiarism checks | 2 min | 2.5 hours |
| **Total** | **12-20 min** | **14.5-24 hours** |

This is spread across multiple sessions. A realistic timeline for a complete manuscript: 2-4 weeks working 1-2 hours per day.

---

## AI as Assistant, Not Ghostwriter

Dale L Roberts uses AI for the tasks that drain time without requiring creativity:

> "It was kind of crazy, it was like a friendly conversation with someone who shared a common interest. And I was able to bounce some ideas off of AI and AI would shoot it back to me."
> -- Dale L Roberts, "How I Use AI for Self Publishing"

> "I'll still hire a professional human editor or an experienced professional cover designer. I'll probably still lean on my peers to audit my book descriptions or ad copy. There are some aspects to business that still require human interaction."
> -- Dale L Roberts, "How I Use AI for Self Publishing"

You do not have to use AI for the entire manuscript. Many successful publishers use it only for outlines, descriptions, and brainstorming.

---

## Related Skills

- **book-architect** -- Produces the outline this skill consumes (run FIRST)
- **[[listing-optimizer|listing-optimizer]]** -- Write description after manuscript is complete
- **[[cover-brief|cover-brief]]** -- Can run in parallel with manuscript drafting

## Related Frameworks

- `manuscript-formatting-workflow.md` — Format the completed manuscript for KDP upload (ePub, PDF, trim size)
- `safe-ai-publishing-workflow.md` — The 4-step AI content workflow (generate, rewrite, check, publish) that this skill follows
