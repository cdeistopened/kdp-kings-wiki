---
name: launch-bootcamp
description: "Teach the complete book launch process through 4 progressive lessons — review collection, free promo strategy, paid ads basics, and the content amplification engine. Use when someone wants to understand WHY each launch phase works, not just follow a checklist."
type: tutor
source_chapters:
  - ch-11
  - ch-12
source_speakers:
  - Sean Dollwet
  - Dale L Roberts
  - Dave Chesson
---

# Launch Bootcamp

A teaching skill that builds launch competence through 4 lessons. Each lesson teaches the strategic logic behind one launch phase, applies it to the user's actual book, and creates a plan for that phase. Unlike the `launch-sequence` skill (which outputs a checklist), this skill teaches the user to think about launches so they can adapt when things don't go to plan.

## Usage

```
/launch-bootcamp --title "Container Gardening for Small Spaces" --publish-date 2026-05-01
/launch-bootcamp --lesson 2
/launch-bootcamp --relaunch --asin B0XXXXXXXX
```

## Why a Launch Bootcamp Exists

Most first-time publishers either skip the launch entirely or follow a checklist without understanding why each step matters. When something goes wrong (reviews don't come, ads burn cash, social media gets no traction), they can't diagnose the problem because they never learned the system — they just followed instructions.

This skill teaches the system.

---

## Lesson 1: The Review Engine (T-28 to Day 5)

**Teach:** Why reviews matter more than any other launch variable. Amazon's algorithm treats review count and velocity as the primary trust signal for new books. A book with 25 reviews in its first month gets dramatically different algorithmic treatment than a book with 3 reviews.

> "You sign up, you start reviewing other people's books, collect some points, and then whenever you're ready, you use those points to get reviews for your book."
> -- Sean Dollwet, "The EASIEST Way to Get 100s of Reviews for Amazon KDP"

**The three review sources:**

| Source | Setup Time | Expected Reviews | Compliance Risk |
|--------|-----------|-----------------|----------------|
| Review exchange services (PubBy, Bookbite) | 4 weeks of banking points | 15-30 per launch | Low (Amazon-compliant) |
| ARC readers (email list, Facebook groups) | 2 weeks of outreach | 5-15 per launch | Low if worded correctly |
| Organic readers | Ongoing | 1 per 100 sales (typical) | None |

**The compliance boundary:**

> Reviews must be voluntary. You can offer free copies for "consideration" of leaving a review. You cannot require a review, pay for a review, or specify a rating.

**Key insight:** Review exchange services are a grind. You review other people's books for weeks before you can request reviews for yours. This is why you start 4 weeks before launch — not the week of.

**Apply:** Based on the user's timeline and existing audience:
1. Recommend which review services to join
2. Calculate how many points they can bank before launch
3. Draft ARC reader outreach language
4. Set a realistic review target for launch week

**Check understanding:** "You have 15 PubBy points and your book launches in 10 days. Is that enough? What should you have done differently?"

**Deliverable:** Review collection plan with service signups, point targets, and outreach scripts.

**Reference:** `30-day-launch-sequence.md` (Phase 1)

---

## Lesson 2: The Free Promo + 99-Cent Engine (Days 1-20)

**Teach:** The economics of launching cheap. The first two weeks are an investment in rank, not a revenue period. Every free download and every 99-cent sale tells Amazon's algorithm that readers want this book.

> "You're probably not going to be making profit in the first one to two weeks because your book is priced very low and you're making very little royalties, and that's okay because it's normal. You're investing in your book's future success by ranking your book higher."
> -- Sean Dollwet, "Complete, No BS Guide to Book Launch"

**The math that makes it work:**

| Phase | Price | Royalty | Algorithm Signal |
|-------|-------|---------|-----------------|
| Free promo (5 days) | $0.00 | $0 | Downloads count for category ranking |
| 99-cent period (1-2 weeks) | $0.99 | $0.35/sale | Sales velocity drives BSR down |
| Post-launch | $2.99-$4.99 | $2.09-$3.49 | Organic rank holds from momentum |

**The 30-day window:**

> "When you first launch your book on Amazon it has a 30-day new book boost... Amazon will place your book in more categories, more keywords, just have people view your books more than usual in the first 30 days."
> -- Sean Dollwet

You get one shot at this window per book. Waste it by launching at full price with no strategy and the algorithm stops paying attention.

**The free promo + review intersection:** During the free window, every download is a potential review. This is why you deploy review service points on Day 1, not Day 15.

> "Have people download your book on Amazon during the free promotion and leave a review which will show up as verified reviews."
> -- Sean Dollwet

**Apply:** Map out the user's pricing trajectory from Day 1 through Day 30. Calculate expected royalty at each phase. Set BSR targets for each transition.

**Check understanding:** "Your book has been at $0.99 for 10 days and you've sold 45 copies. BSR is at 35,000. Do you raise price now or wait? What signals would tell you it's time?"

**Deliverable:** Phase pricing schedule with BSR milestones and transition triggers.

**Reference:** `30-day-launch-sequence.md` (Phases 2-4), `pricing-decision-matrix.md`

---

## Lesson 3: Amazon Ads for Launch (Days 6+)

**Teach:** The minimal viable ad strategy for a first launch. Auto campaign at $5/day to harvest keywords. The relationship between ads and organic rank.

> "The way the Amazon algorithm works is it doesn't really matter whether you make the sales organically or whether you make the sales through ads -- a sale is a sale. And every time you make a sale you basically move up in the organic ranking."
> -- Sean Dollwet

**The launch ad strategy (simplified for first-timers):**

**Week 1 of ads (Days 6-12):**
- 1 Auto campaign, $5/day, default bids
- Purpose: let Amazon find keywords that convert for your book
- Expected: high ACOS, low efficiency — this is keyword research, not profit

**Week 2+ (Days 13+):**
- Pull search term report from auto campaign
- Create 1 manual keyword campaign targeting terms that actually converted
- Reduce auto campaign budget to $2/day (keep it running for discovery)
- Raise manual campaign budget to $5-8/day

**The ACOS reality check:**

> "Ads do not sell books, it only shows your books to more people. If the book is fundamentally bad, it's unattractive, the cover is bad, it's in a niche that nobody's looking for, no matter how many people you show the book to, if nobody wants it then you're not going to get sales."
> -- Sean Dollwet

If ACOS is above 100% after Week 2, the problem is not the ads. The problem is the book (cover, description, price, or niche). Fix the book before spending more on ads.

**Apply:** Set up the user's first auto campaign. Define the search term review schedule. Set ACOS thresholds for kill/scale decisions.

**Check understanding:** "Your auto campaign spent $35 and made 3 sales at $4.99 each. What's your ACOS? Is this campaign working? What do you do next?"

**Deliverable:** Week 1 ad campaign settings + Week 2 optimization plan.

**Reference:** `amazon-ads-setup.md`, `amazon-ads` skill

---

## Lesson 4: The Content Amplification Engine (Ongoing)

**Teach:** Free traffic through content extraction. The book is 30,000 words of structured content. Instead of creating social media from scratch, extract it from what you've already written.

**GaryVee's Content Pyramid applied to books:**

| Layer | What | Volume |
|-------|------|--------|
| Pillar | The book (30,000 words) | 1 |
| Derivative | Blog posts, threads, email sequences | 8-12 |
| Micro | Quote graphics, tips, short videos | 48-64 |

**8 chapters x 8 micro pieces = 64 posts = 32 days at 2/day.**

This maps directly onto the 30-day launch window. You have enough content to post twice daily for the entire launch without creating anything new.

**Sean Dollwet's 7 video formats:**

1. ASMR-style reading with text overlay (no talking)
2. Teaching something from the book
3. Showcasing the cover
4. Flipping through pages (no talking)
5. Reading aloud
6. Coloring page time-lapse (for activity books)
7. AI-generated carousels

> "The videos that did the best for him are the easiest ones to create."
> -- Sean Dollwet

**The batch method:** 2 hours filming + 2 hours Canva + 1 hour scheduling = 64 pieces of content. Compare to ad-hoc posting, which produces maybe 10 posts with triple the total time.

**Apply:** Map the user's 8 chapters to derivative and micro content. Build a 30-day posting calendar. Identify which platforms match their comfort level (video-comfortable: TikTok/YouTube Shorts; text-comfortable: X threads/LinkedIn).

**Check understanding:** "You've published your book and have zero social media following. Which 3 content formats from the list should you start with, and why?"

**Deliverable:** 30-day content calendar with specific pieces mapped to chapters and platforms.

**Reference:** `content-pyramid-book-launches-garyvee.md`, `30-day-launch-sequence.md`

---

## Bootcamp Graduation

After all 4 lessons, the user should be able to:
1. Build a review pipeline before any future book launch
2. Structure pricing phases that trade short-term revenue for long-term rank
3. Run a basic Amazon Ads campaign and interpret the data
4. Extract 64+ pieces of social content from a single book

They should also understand this:

> "It's not like your book will forever fail if you don't do a book launch or if you don't do it successfully."
> -- Sean Dollwet

The launch gives you a head start. The ongoing work — ads, content, catalog building — determines whether you keep it.

---

## Related Skills

- **[[launch-sequence|launch-sequence]]** — Quick launch checklist (use after this skill for execution)
- **[[amazon-ads|amazon-ads]]** — Full ad campaign setup
- **[[pricing-strategist|pricing-strategist]]** — Pricing calculator for each phase
- **[[first-book-walkthrough|first-book-walkthrough]]** — If the user hasn't published yet, start there instead

## Related Frameworks

- `30-day-launch-sequence.md` — The tactical timeline this skill teaches (all 4 lessons)
- `amazon-ads-setup.md` — Full ad campaign reference (Lesson 3)
- `content-pyramid-book-launches-garyvee.md` — Content extraction method (Lesson 4)
- `pricing-decision-matrix.md` — Royalty math for pricing phases (Lesson 2)
