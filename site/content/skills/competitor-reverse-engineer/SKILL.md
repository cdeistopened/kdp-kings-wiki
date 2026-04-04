---
name: competitor-reverse-engineer
description: "Mine successful self-published author catalogs to discover validated niches and keyword opportunities. Use when exploring new niches or expanding an existing series."
type: decision
source_chapters:
  - ch-02
source_speakers:
  - Sean Dollwet
  - Dale L Roberts
  - Dave Chesson
---

# Competitor Reverse Engineer

Discover validated niches and keyword ideas by reverse-engineering successful self-published author catalogs on Amazon. This is the highest-ROI niche research method -- every title in a profitable indie publisher's catalog represents a keyword they already validated through real sales.

## Usage

```
/competitor-reverse-engineer "ketogenic diet"
/competitor-reverse-engineer --asin B0XXXXXXXX
/competitor-reverse-engineer --author "Author Name"
```

## Why This Works

> "You want to find what is already working. You're not trying to reinvent a wheel here. You want to just do what is already working, and what is already working is what is profitable."
> -- Sean Dollwet, "HOW TO DO KEYWORD RESEARCH for Kindle Publishing" (2020)

Every book title from a profitable self-published author is a pre-validated keyword. Their catalog is a map of proven demand.

---

## Workflow

### Step 1: Find Self-Published Winners

Search a broad niche keyword on Amazon (Kindle Store). Scan the first 2-3 pages of results.

**How to spot self-published books:**

> "To tell if it's a real author or a self-published author: if the title is just the keyword, if the price is between $2.99 to $4.99, that's usually the price range for a self-published book. And the cover image -- you can tell it's a stock image instead of a professionally done cover."
> -- Sean Dollwet, "HOW TO DO KEYWORD RESEARCH for Kindle Publishing 2019"

**Additional signals:**
- Publisher field says "Independently Published"
- Author has multiple titles in similar niches
- Keyword-heavy title that matches the search term exactly
- BSR under 100,000 (confirms the book is actually selling)

### Step 2: Check the Self-Published Litmus Test

> "If there's other self-published books on page one making money, that means their sole traffic source is from Amazon. And if they are able to compete in this keyword, then I should be able to come in and compete as well."
> -- Sean Dollwet, "HOW TO DO KEYWORD RESEARCH for Kindle Publishing 2019"

For each self-published book found, verify:
- [ ] BSR under 100,000
- [ ] Price between $2.99-$9.99 (confirms real revenue)
- [ ] Publisher: "Independently Published"
- [ ] No major platform or media presence (pure organic Amazon)

### Step 3: Mine the Author Catalog

Click through to the author's Amazon page. Browse ALL their titles. Each title represents a keyword they have validated.

**Real example from the manuscript:**

Starting from "ketogenic diet" (5,000+ search results, too competitive), Sean followed an author page to discover "keto meal prep" (BSR ~174, self-published, $5.99). That same author's catalog revealed:
- "Mediterranean diet"
- "Paleo diet for beginners"
- "Anti-inflammatory diet"
- "Keto whole food diet"

All validated niches with room for new entries.

### Step 4: Record the Data

For each title in the catalog, capture:

| Field | What to Record |
|-------|---------------|
| Title | Exact title (this IS the keyword) |
| BSR (Kindle) | Current best seller rank |
| BSR (Paperback) | Check paperback too -- some niches perform better in print |
| Price | Ebook and paperback |
| Review Count | Low reviews + good BSR = beatable |
| Review Rating | Below 4.0 = quality gap you can fill |
| Publish Date | Older books with steady BSR = evergreen niche |
| Cover Quality | Poor cover = improvement opportunity |

### Step 5: Validate Each Discovered Niche

For every keyword extracted from the catalog, run the 3-Step Validation Framework:

> "In order to find, validate, and improve our book idea, we need to do three things. Number one: what are people actually looking for on Amazon? Number two: will people pay for that book? Number three: is the competition too great?"
> -- Dave Chesson, "How to Find Profitable Book Ideas That Make You Money on Amazon"

**Quick validation checklist for each keyword:**
- [ ] Search results under 3,000
- [ ] At least 3 books on page one with BSR under 30,000
- [ ] No more than 5 books under 5,000 BSR in top 20
- [ ] At least 2-3 self-published books selling well on page one
- [ ] Beatable covers, titles, or descriptions visible

### Step 6: Check All Three Platforms

> "Some topics do well on one platform and not the other. Just because Kindle is not profitable doesn't mean that keyword is bad. Some keywords literally, the Kindle BSR is terrible, but if you look at the paperback they're all selling really well."
> -- Sean Dollwet, "HOW TO DO KEYWORD RESEARCH for Kindle Publishing" (2020)

For each promising keyword, search on:
- Kindle eBooks (BSR target: under 50,000)
- Paperback (BSR target: under 100,000)
- Audiobook/Audible (target: under 100 search results)

### Step 7: Assess Series Potential

> "If a book is self-published, that means the publisher is someone like us. So if they are profitable with publishing in that keyword, that's a very good sign that if we do the same thing, the keyword is also going to be profitable for us."
> -- Sean Dollwet, "The Easiest Amazon KDP Keyword Research Method You've Ever Seen"

Can you identify 5-10 related keyword variations from the catalog for a book series? A catalog of 8-12 related titles from one author = a proven series blueprint.

---

## Output Format

### Competitor Profile

| Field | Value |
|-------|-------|
| Author/Pen Name | [name] |
| Publisher | Independently Published |
| Total Titles | [count] |
| Niche Cluster | [primary topic area] |
| Estimated Monthly Revenue | [based on BSR-to-sales conversion] |

### Keyword Opportunities Extracted

| Keyword (from title) | BSR (Kindle) | BSR (Paperback) | Reviews | Beatable? | Notes |
|----------------------|-------------|----------------|---------|-----------|-------|
| [keyword 1] | [bsr] | [bsr] | [count] | Yes/No | [weak cover, old, etc.] |
| [keyword 2] | [bsr] | [bsr] | [count] | Yes/No | |

### Competition Weakness Analysis

For each beatable competitor, identify:

> "A prime example I look for is when books are doing well but it's obvious I can beat them with a better cover, a catchier title, and a better description. This proves there is a market willing to buy even if the current options are subpar."
> -- Dave Chesson, "How to Find Profitable Book Ideas That Make You Money on Amazon"

- [ ] Unprofessional covers among top sellers
- [ ] Poor titles that don't target the keyword
- [ ] Descriptions that are giant blocks of unformatted text
- [ ] Old publish dates (you get a 30-day new release boost)
- [ ] Low or negative reviews revealing content gaps

### Series Blueprint

If 5+ related keywords validated, output a series plan:

| Book # | Target Keyword | Estimated Demand | Competition Level |
|--------|---------------|-----------------|-------------------|
| 1 | [keyword] | [BSR range] | [low/med/high] |
| 2 | [keyword] | [BSR range] | [low/med/high] |
| ... | | | |

---

## Related Skills

- **[[niche-scout|niche-scout]]** -- Deep-dive validation on any keyword discovered here
- **[[keyword-fill|keyword-fill]]** -- Fill keyword boxes after selecting your niche
- **[[book-architect|book-architect]]** -- Build the outline once niche is confirmed
- **[[pricing-strategist|pricing-strategist]]** -- Price your book against the competitor comps you found here
- **[[amazon-ads|amazon-ads]]** -- Target competitor ASINs discovered during reverse-engineering
- **[[listing-optimizer|listing-optimizer]]** -- Study competitor descriptions before writing yours
- **[[cover-brief|cover-brief]]** -- Find reference covers from top sellers in your category to include in the design brief

## Related Frameworks

- `niche-validation-pipeline.md` — The 3-step validation framework applied to each keyword extracted from competitor catalogs
