---
name: pricing-strategist
description: "Set optimal ebook, print, and audiobook pricing using royalty bracket math, dead zone avoidance, price pulsing, hotshotting, and Countdown Deals. Use before upload or when optimizing existing titles."
type: decision
source_chapters:
  - ch-10
source_speakers:
  - Dale L Roberts
  - Sean Dollwet
---

# Pricing Strategist

Set prices across all formats using Amazon's royalty bracket math, the dead zone, and three tactical pricing strategies. Produces a pricing card with royalty calculations for each format.

## Usage

```
/pricing-strategist --title "Beekeeping for Beginners" --formats "ebook,paperback" --print-cost "$3.50"
/pricing-strategist --optimize --asin B0XXXXXXXX
```

## Prerequisites

- Book format(s) determined (ebook, paperback, hardcover, audiobook)
- Print cost known (from KDP's royalty calculator)
- KDP Select enrollment decision made

---

## Workflow

### Step 1: Understand the Ebook Royalty Tiers

> "70% royalty is The Sweet Spot on the Amazon platform. They prefer that you price your ebook somewhere between $2.99 and $9.99."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

| Price Range | Royalty Rate | Delivery Fee | Best For |
|------------|-------------|-------------|----------|
| $0.99 - $2.98 | 35% | None | Launch promos only |
| **$2.99 - $9.99** | **70%** | Yes (file-size based) | **Primary pricing tier** |
| $10.00 - $19.98 | 35% | None | **DEAD ZONE -- AVOID** |
| $19.99+ | 35% | None | Premium/specialized only |

### Step 2: Avoid the Dead Zone

**The Dead Zone: $10.00 to $19.98**

At $9.99 with 70% royalty, you earn ~$6.99. To match that at 35%, you need $19.99 ($19.99 x 0.35 = ~$7.00).

> "The break even point... at the 70% model is $9.99 -- you get about $6 and some change. The same is going to be said that if you go 35% model, anything that's $19.99 or above is probably going to be the good idea."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

**Any price between $10.00 and $19.98 earns you LESS than $9.99 would.** Never price in this range.

### Step 3: Calculate Print Royalties (Post-June 2025)

**Formula:** Royalty = (List Price x Royalty Rate) - Printing Cost

| Print Price | Royalty Rate | Impact |
|------------|-------------|--------|
| At or above $9.99 | 60% | Standard rate |
| Below $9.99 | 50% | 10-point cut effective June 2025 |

> "Starting June 10th, KDP will cut your print royalties from 60% to 50% on any print book price below $9.99 US."
> -- Dale L Roberts, "BREAKING: Amazon KDP Just Made a Brutal Change"

**Hardest hit categories:**
- Children's books (color interiors = high print cost)
- Short nonfiction (workbooks, planners)
- Low-content books (journals, notebooks, puzzle books)

> "This royalty cut doesn't just trim earnings. It pressures entire business models."
> -- Dale L Roberts, "BREAKING: Amazon KDP Just Made a Brutal Change"

**Action:** Run your price through KDP's royalty calculator. Price at or above $9.99 whenever the market supports it.

### Step 4: Check Global Royalty Penalty

If NOT enrolled in KDP Select:

> "Despite pricing your ebook at 70% you will not get that rate in Brazil, Japan, Mexico, or India -- that is unless you enroll your ebook in KDP Select."
> -- Dale L Roberts, "KDP Select Review: Worth It in 2024?"

Other platforms (Apple Books, Kobo, Google Play) pay 70% without geographic restrictions:

> "Platforms like Apple Books for Authors, Barnes & Noble Press, Google Play Books, and of course Kobo Writing Life allow for 70% royalty per sale -- period. No asterisk, no delivery fees, no pricing shenanigans."
> -- Dale L Roberts, "KDP Select Review: Worth It in 2024?"

### Step 5: Audiobook Pricing (ACX/Audible)

You don't set audiobook prices -- Audible sets them based on audio length:

> "ACX pricing is determined based on the book length or audio length. You don't pick the prices."
> -- Sean Dollwet, "How to Make Money Publishing Audiobooks on Audible ACX"

| Audio Length | Approx. Royalty (40% Exclusive) |
|-------------|-------------------------------|
| Under 1 hour | ~$0.90 |
| 1-3 hours | ~$1.80 |
| 3-5 hours | ~$3.60 |
| 5-10 hours | ~$4.60 |
| 10-20 hours | ~$5.60 |

Counterintuitive dynamic: expensive books sell better on Audible because members use their monthly credit on high-value titles:

> "More expensive books sell better on Audible just because Audible members get one free credit to redeem for any book of their choice."
> -- Sean Dollwet, "How to Make Money Publishing Audiobooks on Audible ACX"

The ACX Bounty Program adds $75 per new listener who signs up through your book and stays past trial:

> "Would you rather have $4 to $20 per sale of your audiobook, or would you rather have $75?"
> -- Dale L Roberts, "Get EVEN MORE Money From a Self Published Book"

### Step 6: Apply Pricing Strategies

#### Strategy 1: Price Pulsing (Finding Your Sweet Spot)

> "You have a specific price point and let's say there's very little sales coming through... then you drop that price point."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

The process:
1. Launch at target price (e.g., $7.99)
2. If sales are weak, drop to $2.99
3. As sales pick up, inch back up: $3.99, $4.99, $5.99
4. "Don't make that drastic jump back up to $7.99 because you might scare away the market."

> "If you use price pulsing, do it only to figure out what your buying audience is willing to spend. You're going to find that sweet spot somewhere in the middle."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

#### Strategy 2: Hotshotting (Spiking Sales Velocity)

> "Hotshotting... essentially works like price pulsing but you're not moving the price point up down up down. It's typically a drastic drop to spike sales and you're doing it for a limited time."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

The play: Drop to $0.99, blast your email list with urgency ("going to $9.99 next week"), let the algorithm notice the velocity spike:

> "The Amazon algorithm is going to go 'oh wow this is hot, this is cool, we're going to go ahead and serve this to other people that are buying similar products.' And so then you start to get a snowball effect."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

#### Strategy 3: Kindle Countdown Deals (The 70% Loophole)

**The single most important tactical pricing tool in KDP Select:**

> "The nice part about the countdown deal is KDP will honor the original royalty rate set for your book. Let's say you have a book priced $9.99 at the 70% royalty, then drop it to 99 cents for the countdown deal -- you still get 70%."
> -- Dale L Roberts, "KDP Select Review: Worth It in 2024?"

Without Countdown Deal: $0.99 x 35% = $0.35 per sale
With Countdown Deal: $0.99 x 70% = $0.69 per sale -- nearly DOUBLE.

This is the only mechanism on KDP that preserves your royalty rate during a price promotion.

### Step 7: Avoid the 99-Cent Trap

> "Dropping your book down to 99 cents kind of sucks. Literally you're getting paid 35 cents out of every dollar for each time your ebook sells."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

Amazon's algorithm favors consistency over spikes:

> "It's not enough that you had hundreds of sales within the course of a day or two days or even for that matter a month. What Amazon's algorithm likes to see is consistency."
> -- Dale L Roberts, "Kindle Book Pricing Strategy"

Use 99 cents as a temporary launch/promotional tool -- never as a long-term price.

### Step 8: Build Margins for Platform Risk

> "Amazon isn't your business partner. It's a platform, and platforms protect their margins."
> -- Dale L Roberts, "BREAKING: Amazon KDP Just Made a Brutal Change"

Price at the top of what your market will bear. Build enough margin to absorb future rate cuts.

---

## Output Format

### Pricing Card

```markdown
## [Book Title] -- Pricing Strategy

### Ebook
- **List Price:** $[X.XX]
- **Royalty Rate:** [35% / 70%]
- **Delivery Fee:** ~$[X.XX]
- **Net Royalty:** $[X.XX] per sale
- **Dead Zone Check:** [PASS / FAIL]

### Paperback
- **List Price:** $[X.XX]
- **Printing Cost:** $[X.XX]
- **Royalty Rate:** [50% / 60%] (above/below $9.99)
- **Net Royalty:** $[X.XX] per sale

### Hardcover
- **List Price:** $[X.XX]
- **Printing Cost:** $[X.XX]
- **Net Royalty:** $[X.XX] per sale

### Audiobook (if applicable)
- **Length:** [X hours]
- **Estimated Retail:** $[X.XX] (Audible-set)
- **Royalty (40% exclusive):** ~$[X.XX] per sale
- **Bounty potential:** $75 per new listener

### Break-Even Analysis
- **Total Investment:** $[X]
- **Avg Royalty (blended):** $[X.XX]
- **Units to Break Even:** [X]
- **At [X] sales/day:** [X months] to break even

### Promotional Pricing Plan
| Phase | Price | Duration | Royalty | Purpose |
|-------|-------|----------|---------|---------|
| Free promo | $0.00 | 5 days | $0 | Reviews + discovery |
| 99-cent launch | $0.99 | 1-2 weeks | $0.35 | Volume + BSR |
| Ramp up | $2.99-$4.99 | 2-4 weeks | $2.09-$3.49 | Transition |
| Full price | $[target] | Ongoing | $[target royalty] | Profit |
| Countdown Deal | $0.99 | 7 days | $0.69 (70%!) | Re-ranking |
```

---

## Related Skills

- **[[competitor-reverse-engineer|competitor-reverse-engineer]]** -- Price against competitor comps discovered during reverse-engineering
- **[[upload-checklist|upload-checklist]]** -- Make DRM and KDP Select decisions before finalizing pricing, then apply during upload
- **[[launch-sequence|launch-sequence]]** -- Pricing phases integrated into launch plan
- **[[amazon-ads|amazon-ads]]** -- ACOS benchmarks depend on price/margin

## Related Frameworks

- `pricing-decision-matrix.md` — The complete pricing decision tree covering royalty tiers, dead zone, and format-specific calculations
- `pricing-psychology-hormozi.md` — Hormozi's Value Equation adapted for Amazon book pricing: anchoring, format stacking, perceived value levers
- `offer-naming-for-book-titles-hormozi.md` — Why the book title IS the offer name: Hormozi's naming methodology applied to KDP title/subtitle decisions
- `wide-vs-exclusive.md` — KDP Select vs. going wide: the strategic tradeoff that affects pricing, royalties, and promotional tools
