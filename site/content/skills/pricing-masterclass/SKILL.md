---
name: pricing-masterclass
description: "Teach the complete pricing system for Amazon books — royalty math, psychology, format anchoring, and promotional tactics — through progressive lessons applied to the user's specific book. Use when someone wants to deeply understand KDP pricing, not just get a quick price recommendation."
type: tutor
source_chapters:
  - ch-10
  - ch-13
source_speakers:
  - Dale L Roberts
  - Sean Dollwet
  - Dave Chesson
---

# Pricing Masterclass

A teaching skill that walks users through the full KDP pricing system in 5 lessons. Each lesson teaches one concept, applies it to the user's book, and builds on the previous lesson. By the end, the user understands not just what to charge but why, and can make pricing decisions independently for future books.

## Usage

```
/pricing-masterclass --title "Anxiety Workbook" --formats "ebook,paperback" --niche "mental health"
/pricing-masterclass --lesson 3
```

## How This Differs from pricing-strategist

The `pricing-strategist` skill is a calculator: give it inputs, get a pricing card. This tutor skill is a teacher: it explains the reasoning so you can make pricing decisions without the tool next time.

Use `pricing-strategist` when you need a quick answer. Use `pricing-masterclass` when you want to understand the system.

---

## Lesson 1: The Royalty Map (How Amazon Pays You)

**Teach:** The three royalty tiers (35%, 70%, 60%/50% print), the delivery fee, and the Dead Zone.

> "70% royalty is The Sweet Spot on the Amazon platform. They prefer that you price your ebook somewhere between $2.99 and $9.99."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

**The Dead Zone — the most expensive mistake in KDP pricing:**

At $9.99 (70% royalty), you earn ~$6.99 per sale. At $10.00 (forced to 35%), you earn $3.50. You lose half your income by moving one penny.

> "The break even point... at the 70% model is $9.99 -- you get about $6 and some change. The same is going to be said that if you go 35% model, anything that's $19.99 or above is probably going to be the good idea."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

**Apply:** Calculate the royalty for the user's book at three price points: $2.99, $4.99, $9.99. Show the actual dollar difference. For print, calculate using their specific printing cost.

**Check understanding:** "If your ebook is at $9.99 and you raise to $12.99, what happens to your per-sale income?"

**Deliverable:** Royalty calculation table for all formats.

**Reference:** `pricing-decision-matrix.md`

---

## Lesson 2: The Psychology of Price (Why Buyers Pay What They Pay)

**Teach:** Hormozi's Value Equation applied to books. Price is not about cost. Price is about perceived value relative to the buyer's desire.

The four variables:
1. **Dream Outcome** — How specific and vivid is the promise?
2. **Perceived Likelihood** — Reviews, cover quality, author credibility
3. **Time Delay** — How fast does the reader get value?
4. **Effort & Sacrifice** — How hard is it to implement?

> "The dream outcome determines whether someone is even interested in your category of offer or not."
> -- Alex Hormozi (adapted for KDP context)

**Apply:** Score the user's book on all four variables (1-10). Identify the weakest variable. A book with a 9/10 dream outcome but 3/10 perceived likelihood (no reviews yet) should launch cheap and raise after building reviews.

**Check understanding:** "Your book has 200 reviews at 4.5 stars. Which variable did that improve, and what does it let you do with price?"

**Deliverable:** Value Equation scorecard with pricing implication.

**Reference:** `pricing-psychology-hormozi.md`

---

## Lesson 3: Format Anchoring (Using Your Own Catalog as a Pricing Tool)

**Teach:** How multiple formats create anchoring effects. The hardcover's job is not to sell copies — it's to make the Kindle price feel like a bargain.

When a buyer sees:
- Hardcover: $24.99
- Paperback: $14.99
- Kindle: $4.99

The $4.99 Kindle becomes "80% off" in their mind. Without the anchor, $4.99 is just a number.

**Series anchoring:** A 5-book series at $4.99 each ($24.95 total) makes a box set at $14.99 feel like "3 books free."

**Competitor anchoring:** Price your book in context. If top 10 in your niche are $12.99-$16.99 paperback, $9.99 looks like a deal. $6.99 looks suspiciously cheap.

**Apply:** Map out all available formats for the user's book. Set prices that create deliberate anchoring. If they don't have a hardcover edition, explain why publishing one (even at low volume) is worth it for the anchoring effect.

**Check understanding:** "You have an ebook at $4.99 and a paperback at $12.99. Would adding a hardcover at $24.99 help or hurt your Kindle sales? Why?"

**Deliverable:** Format anchoring strategy with specific prices per format.

**Reference:** `pricing-psychology-hormozi.md`, `pricing-decision-matrix.md`

---

## Lesson 4: Tactical Pricing (The Three Moves)

**Teach:** The three pricing maneuvers and when to use each.

**Price Pulsing** — Finding your sweet spot by testing.
> "If you use price pulsing, do it only to figure out what your buying audience is willing to spend."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

Start at target, drop if sales are weak, inch back up. Don't jump — you'll scare the market.

**Hotshotting** — Spiking sales velocity.
> "Hotshotting... essentially works like price pulsing but you're not moving the price point up down up down. It's typically a drastic drop to spike sales and you're doing it for a limited time."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

Drop to $0.99, blast your email list with urgency, let the algorithm notice the velocity spike.

**Kindle Countdown Deals** — The 70% loophole.
> "KDP will honor the original royalty rate set for your book. Let's say you have a book priced $9.99 at the 70% royalty, then drop it to 99 cents for the countdown deal -- you still get 70%."
> -- Dale L Roberts, "KDP Select Review: Worth It in 2024?"

Without Countdown: $0.99 x 35% = $0.35. With Countdown: $0.99 x 70% = $0.69. Double the royalty on the same sale.

**Apply:** Based on where the user's book is in its lifecycle (pre-launch, just launched, established, stalled), recommend which tactic to use next and when.

**Check understanding:** "Your book launched 3 months ago at $4.99 and sales have plateaued at 2/day. Which tactic do you use, and what's your pricing sequence?"

**Deliverable:** Tactical pricing calendar for the next 90 days.

**Reference:** `pricing-decision-matrix.md`

---

## Lesson 5: Platform Strategy (Exclusive vs. Wide)

**Teach:** The KDP Select trade-off. Exclusive gives you Kindle Unlimited reads, Countdown Deals, and 5-day free promos. Wide gives you 70% royalty globally (no geographic penalty) and reduces Amazon dependency.

> "Despite pricing your ebook at 70% you will not get that rate in Brazil, Japan, Mexico, or India -- that is unless you enroll your ebook in KDP Select."
> -- Dale L Roberts, "KDP Select Review: Worth It in 2024?"

But wide platforms (Apple, Kobo, Google Play) pay 70% everywhere without restrictions:

> "Platforms like Apple Books for Authors, Barnes & Noble Press, Google Play Books, and of course Kobo Writing Life allow for 70% royalty per sale -- period."
> -- Dale L Roberts, "KDP Select Review: Worth It in 2024?"

**Apply:** For the user's specific book and niche, evaluate whether KDP Select or wide distribution optimizes total revenue. Factor in: is their audience international? Do they need Kindle Unlimited for discoverability? How important are Countdown Deals to their pricing strategy?

**Check understanding:** "Your book gets 40% of reads from Kindle Unlimited. If you go wide, what replaces that revenue, and how long before the other platforms compensate?"

**Deliverable:** Platform decision with revenue projection comparison.

**Reference:** `wide-vs-exclusive.md`

---

## Graduation Checkpoint

After all 5 lessons, the user should be able to answer:
1. What royalty rate do I earn at each price point? (Lesson 1)
2. What makes buyers perceive my book as worth more than its price? (Lesson 2)
3. How do my other formats affect Kindle pricing? (Lesson 3)
4. Which pricing tactic should I use right now? (Lesson 4)
5. Should I be exclusive to Amazon or distribute wide? (Lesson 5)

If they can answer all five with specifics about their own book, they don't need this skill again. They own the pricing system.

---

## Related Skills

- **[[pricing-strategist|pricing-strategist]]** — Quick pricing calculator (use after this skill for execution)
- **[[launch-sequence|launch-sequence]]** — Pricing phases integrated into launch plan
- **[[amazon-ads|amazon-ads]]** — ACOS benchmarks depend on price/margin

## Related Frameworks

- `pricing-decision-matrix.md` — Royalty math reference (Lesson 1)
- `pricing-psychology-hormozi.md` — Value Equation framework (Lesson 2)
- `offer-naming-for-book-titles-hormozi.md` — Title as pricing lever (Lesson 2)
- `wide-vs-exclusive.md` — Platform economics (Lesson 5)
