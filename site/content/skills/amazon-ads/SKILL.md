---
name: amazon-ads
description: "Set up and optimize Amazon Sponsored Product ad campaigns using the 4-campaign system, bidding strategies, ACOS benchmarks, keyword harvesting, and troubleshooting matrix. Use after launch or to revive stalled books."
type: decision
source_chapters:
  - ch-12
source_speakers:
  - Sean Dollwet
  - Dale L Roberts
  - Rick Wong
  - Dave Chesson
---

# Amazon Ads

Set up and optimize Amazon Sponsored Product ad campaigns using the 4-campaign architecture, proper bidding, ACOS benchmarks, keyword harvesting from search term reports, and a diagnostic troubleshooting matrix. Based on Chapter 12 of Kings of Kindle.

## Usage

```
/amazon-ads --setup --title "Beekeeping for Beginners" --format paperback
/amazon-ads --optimize --campaign "Keto Manual Keyword Down PB 022026"
/amazon-ads --troubleshoot "high impressions, no clicks"
```

## Core Principle

> "Ads do not sell books, it only shows your books to more people. If the book is fundamentally bad, it's unattractive, the cover is bad, it's in a niche that nobody's looking for, no matter how many people you show the book to, if nobody wants it then you're not going to get sales."
> -- Sean Dollwet, "Full Beginner Amazon Ads Tutorial for Amazon KDP"

Fix the book first (cover, description, reviews, price). Then run ads.

---

## The Organic Ranking Flywheel

> "The way the Amazon algorithm works is it doesn't really matter whether you make the sales organically or whether you make the sales through ads -- a sale is a sale. And every time you make a sale you basically move up in the organic ranking."
> -- Sean Dollwet, "Full Beginner Amazon Ads Tutorial for Amazon KDP"

Every ad-driven sale improves organic rank. The goal: reach a point where organic sales sustain themselves and ad spend becomes optional.

---

## Which Ad Type to Use

| Ad Type | Verdict | Why |
|---------|---------|-----|
| **Sponsored Products** | USE THIS | Appears in search results, product pages, "also bought" carousels |
| **Lock Screen Ads** | AVOID | Interest-based only, far too broad. ACOS "well over 400 percent." |
| **Sponsored Brand Ads** | Advanced only | Requires 3+ titles. For authors with a "deeper backlog." |

Until you have 3+ titles and a proven workflow, run Sponsored Products exclusively.

**Which format to advertise:**

> "You really should just advertise for your paperback only if you have an option between ebook or paperback, because a lot of times paperback in my experience has a lot better ROI and lower ACOS... mainly because the average order value of the paperback is much higher."
> -- Rick Wong, "Amazon Ads for KDP: Step-by-Step Tutorial for Beginners"

Higher sale price = wider margin = more forgiving ACOS threshold.

---

## The 4-Campaign System

Sean Dollwet's architecture gives each book four campaigns:

| Campaign | Type | Timing | Targeting | Starting Bid |
|----------|------|--------|-----------|-------------|
| 1. Manual Keyword | Sponsored Product, manual | Day 1 | Broad match | $0.30 (low content) / $0.65 (high content) |
| 2. Manual Product | Sponsored Product, manual | Day 1 | ASIN targeting, expanded | $0.30 / $0.65 |
| 3. Automatic | Sponsored Product, auto | Week 3 | Amazon-chosen | $0.30 |
| 4. Scale (Exact) | Sponsored Product, manual | Week 3+ | Exact match, proven winners | $0.60+ |

### Why Manual First, Automatic Later

> "When you initially publish a book, Amazon has very limited data on what your book is about... Instead what we want to do is to train Amazon what your book is about by manually choosing keywords and manually choosing products that is relevant to your book."
> -- Sean Dollwet, "Full Beginner Amazon Ads Tutorial for Amazon KDP"

After 2 weeks of manual data, automatic campaigns target far more relevant audiences.

### Alternative: Start with Auto

> "I kind of like likening it to the auto campaign as more of your Hunter because it allows the algorithm to go out, find additional keywords, and basically your manual campaign is more of your Farmer because you know what your good keywords are, you're constantly trying to farm for sales."
> -- Rick Wong, "Amazon Ads for KDP: Step-by-Step Tutorial for Beginners"

Either approach works. Key principle: **never bundle multiple books into one campaign.**

### Nonfiction vs. Fiction Targeting

> "Non-fiction books really do well with keywords. And for fiction books, using product targeting more might give you a better ROI."
> -- Rick Wong, "Amazon Ads for KDP: Step-by-Step Tutorial for Beginners"

- **Nonfiction:** Weight toward keyword campaigns (readers search for topics)
- **Fiction:** Weight toward product/ASIN campaigns (readers browse similar titles)

---

## Campaign Setup: Step by Step

### 1. Find Keywords and ASINs

- **Amazon search bar + alphabet technique** -- note autocomplete suggestions
- **AMZ Suggestion Expander** (free Chrome plugin) -- captures all suggestions
- **ASIN Fetcher** (free Chrome plugin) -- scrapes competitor ASINs from search results
- **Publisher Rocket** ($97 one-time) -- searches AMS keyword data, ASINs, author names

**Target count:** 15-30 per campaign.

> "You never want to add more than 30 targets per campaign."
> -- Sean Dollwet, "Full Beginner Amazon Ads Tutorial for Amazon KDP"

### 2. Choose Bid Strategy

| Strategy | Behavior | Best For |
|----------|----------|----------|
| **Dynamic Bids Down Only** | Amazon lowers bid when conversion unlikely; never exceeds max | Beginners, conservative |
| Dynamic Bids Up and Down | Amazon raises/lowers based on conversion (up to 100% increase) | Experienced, proven books |
| Fixed Bids | Bid stays exactly as set | Steady impressions |

> "We're always going to do down only. Dynamic bids down only. This is the most conservative and you won't overspend by doing this."
> -- Sean Dollwet, "Full Beginner Amazon Ads Tutorial for Amazon KDP"

Dave Chesson offers a nuance:

> "Amazon can actually limit your impressions if you do [down only]. So if you want to stay safe it's better to just choose fixed bids."
> -- Dave Chesson, "How to do Amazon Book Ads in 2024"

### 3. Set Bid Amount (The Penny Trick)

> "When selecting a bid number never go with a number like that, those that end with zero or five. That's because most authors just put those in... I like to go 1 cent or 2 cent above this. So say I want to select 50 cents then I'll make it 51 cents."
> -- Dave Chesson, "How to Do Amazon Book Ads - in 2020!"

| Book Type | Starting Bid |
|-----------|-------------|
| Low/medium content (journals, word search) | $0.30-$0.31 |
| High content (nonfiction, fiction) | $0.65-$0.66 |
| Scale campaigns (proven winners) | $0.60+ |

### 4. Set Daily Budget

| Level | Amount | Notes |
|-------|--------|-------|
| Minimum viable | $3/day | Sean's floor for tight budgets |
| Recommended start | $5-$10/day | Campaigns "rarely spend the daily budget" |
| For significant data | $10/day+ | Dale's minimum for meaningful results |

### 5. Add Negative Keywords

> "I enter in words like free, free book, free ebook. I believe this is important because if people are typing into Amazon 'free anything' and Amazon shows my book, they may click on it costing me the money, but are going to be harder to convince to buy something."
> -- Dave Chesson, "How to Do Amazon Book Ads - in 2020!"

**Negative keyword checklist:**
- [ ] "free," "free book," "free ebook"
- [ ] Misleading topic associations
- [ ] Your own author name (exact match negative)
- [ ] Your own book titles

### 6. Name Campaigns Clearly

Convention: `[Book] [Type] [Targeting] [Bid Strategy] [Format] [Date]`

Example: `Keto Cookbook Manual Keyword Down PB 022026`

---

## Match Types

| Match Type | Behavior | Use Case |
|-----------|----------|----------|
| **Broad** | Any word order, includes synonyms | Discovery -- maximum reach |
| Phrase | Exact sequence preserved, words before/after allowed | Mid-funnel control |
| **Exact** | Only this phrase plus plurals | Scale -- proven converters only |

> "I personally like to make all my keywords broad phrases so as to give Amazon the best chance to show my book. Because remember you don't pay Amazon until a shopper clicks on it."
> -- Dave Chesson, "How to Do Amazon Book Ads - in 2020!"

**Avoid category targeting:**

> "It's been mine and many other authors' observation that targeting through categories is very fruitless and has poor returns."
> -- Dave Chesson, "How to Do Amazon Book Ads - in 2020!"

Target specific ASINs instead.

---

## Optimization: The Weekly Rhythm

Check campaigns twice per week, 20-30 minutes each session (~1 hour/week total). Wait for sufficient data: at least 1,000 impressions per campaign and 10 clicks per target.

### ACOS Benchmarks

> "If your ACOS is above break even, so typically break even is above 40%... if it's over 40% you're most likely losing money... and if you're below 40% ACOS then you're profiting."
> -- Sean Dollwet, "Full Beginner Amazon Ads Tutorial for Amazon KDP"

| ACOS | Status | Action |
|------|--------|--------|
| Below 40% | Profitable (paperback) | Increase bid 3-5 cents above current CPC |
| ~40% | Break even | Hold steady |
| Above 40% | Losing money | Lower bid below CPC |
| 400%+ | Disaster | Pause campaign immediately |

### Keyword Harvesting: Discovery to Scale

The most valuable optimization -- graduate winners from broad/auto into exact match:

1. Open campaign > Search Terms report
2. Filter for keywords with 3+ orders
3. Copy winners into a new exact match campaign
4. Set bids higher ($0.60+) -- proven conversion data justifies it
5. Consider switching from "down only" to "up and down" bidding

---

## Troubleshooting Matrix

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| **No/low impressions** | Bids too low | Raise bids |
| | Keywords irrelevant | Amazon favors relevance -- realign |
| | Outbid by competition | Raise bid or target less competitive terms |
| **Impressions but no clicks** | Cover not compelling at thumbnail size | Fix cover (Ch 6) |
| | Title doesn't communicate benefit | Improve title clarity |
| | Not enough reviews (aim for 15+) | Collect reviews before spending on ads |
| | Wrong audience seeing your ad | Check targeting relevance |
| **Clicks but no sales** | Weak description / A+ content | Rewrite with 5-part framework (Ch 9) |
| | Reviews negative or too few | Address review gaps |
| | Price too high vs competition | Adjust pricing (Ch 10) |
| **Sales but high ACOS** | Bids too high | Lower bid below current CPC |
| | Book price too low for margin | Consider raising price |
| | Broad match eating budget | Move winners to exact; pause underperformers |

---

## Billing and Account Protection

Amazon uses tiered billing for new accounts: pennies > $50 > $250 > ~$500 > monthly. Keep payment current -- bounced payment freezes all campaigns.

### Invoice Audit Warning

> "Essentially the issue is that Amazon might be overcharging you when you're running Amazon ads."
> -- Sean Dollwet, "Amazon Ads May Be Stealing Money from You"

**Protect yourself:** Compare dashboard click counts against invoice line items monthly. If discrepancies found, contact Amazon support with screenshots.

---

## When to Outsource

> "Ads are all about constant testing and tweaking. It's very simple work but it's time-consuming. It should be one of the first tasks you outsource."
> -- Sean Dollwet, "Full Beginner Amazon Ads Tutorial for Amazon KDP"

Outsource once you clear $500/month in revenue.

| Option | Cost | Notes |
|--------|------|-------|
| Train a general VA (Upwork) | Lowest | Requires your time to train |
| Hire a PPC specialist (Upwork) | Mid-range | Verify KDP experience |
| Dedicated service (e.g., Backed By ~$550/mo) | Highest | Specialized in book ads |

**Critical:** FBA ad managers are NOT the same as KDP ad managers. Book margins are thinner. Always hire someone who specializes in publishing.

---

## Output Format

### Campaign Setup Card

```markdown
## [Book Title] -- Amazon Ads Plan

### Campaign 1: Manual Keyword (Day 1)
- Type: Sponsored Product, Manual
- Match: Broad
- Bid: $[X.XX] (down only)
- Budget: $[X]/day
- Keywords (15-30):
  1. [keyword]
  2. [keyword]
  ...
- Negative keywords: free, free book, free ebook, [author name], [book title]

### Campaign 2: Manual Product (Day 1)
- Type: Sponsored Product, Manual
- Targeting: ASIN + expanded
- Bid: $[X.XX]
- Budget: $[X]/day
- ASINs (15-30):
  1. [ASIN] -- [competitor title]
  2. [ASIN] -- [competitor title]
  ...

### Campaign 3: Automatic (Week 3)
- Type: Sponsored Product, Auto
- Bid: $0.31
- Budget: $[X]/day
- Note: Launch after 2 weeks of manual data

### Campaign 4: Scale/Exact (Week 3+)
- Type: Sponsored Product, Manual
- Match: Exact
- Bid: $0.61+
- Keywords: [graduated from Campaigns 1-3 search term reports]
- Threshold: 3+ orders before graduation

### Optimization Schedule
- [ ] Check 2x/week (Mon + Thu), 30 min each
- [ ] Review ACOS against 40% benchmark
- [ ] Pause targets with high spend + zero orders
- [ ] Graduate 3+ order keywords to Campaign 4
- [ ] Audit first invoice against dashboard
```

---

## Related Skills

- **[[launch-sequence|launch-sequence]]** -- Ads start in Phase 3 of launch (coordinate timing)
- **[[pricing-strategist|pricing-strategist]]** -- Price determines ACOS breakeven threshold
- **[[keyword-fill|keyword-fill]]** -- Same keyword research feeds both backend boxes and ad campaigns
- **[[competitor-reverse-engineer|competitor-reverse-engineer]]** -- Find competitor ASINs to target in Manual Product campaigns
- **[[listing-optimizer|listing-optimizer]]** -- Strong description/categories improve click-to-sale conversion

## Related Frameworks

- `amazon-ads-setup.md` — The complete 4-campaign architecture with bid strategies, match types, and optimization schedule
