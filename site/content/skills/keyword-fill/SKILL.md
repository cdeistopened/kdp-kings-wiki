---
name: keyword-fill
description: "Fill Amazon's 7 backend keyword boxes using the hybrid strategy from Chesson's 121-author experiment. Use after validating a niche with niche-scout."
type: decision
source_chapters:
  - ch-03
source_speakers:
  - Dave Chesson
  - Sean Dollwet
  - Jacob Rothenberg
---

# Keyword Fill

Fill all 7 Amazon KDP keyword boxes using the hybrid strategy proven across 121 authors. This skill takes a validated niche and produces copy-paste-ready keyword boxes optimized for maximum indexing with minimum dilution.

## Usage

```
/keyword-fill "mediterranean diet meal prep"
/keyword-fill --title "Keto for Beginners" --subtitle "A Simple Guide to Losing Weight with the Ketogenic Diet"
```

## Prerequisites

- Niche validated via `/niche-scout` (BSR confirmed, competition beatable)
- Book title and subtitle finalized (or near-final)
- Amazon autocomplete research completed (or will be done in Step 1)

---

## Workflow

### Step 1: Gather Keyword Candidates

**Amazon Autocomplete + Alphabet Technique:**

> "The alphabet technique -- type in [your keyword] and then type 'a' and now you have a set of new keywords. 'B' and now you have a new set of keywords. Then you just keep going."
> -- Sean Dollwet, "Find Profitable Keywords FAST"

1. Open Amazon in an incognito window
2. Select the Kindle Store department
3. Type the seed keyword
4. Append each letter a-z and record all relevant autocomplete suggestions
5. Target 50-100 candidate phrases

**Shortcut:** Use the Amazon Search Suggestion Expander Chrome plugin to automate the alphabet process. "This chrome plugin will basically spit out so many more keywords that you can go and check." -- Sean Dollwet

**Competitor title mining:** Search the seed keyword on Amazon and note every word/phrase used in the titles and subtitles of page-one results -- especially self-published books selling well.

### Step 2: Validate Demand for Top Candidates

For each keyword candidate, search it on Amazon and check:

- **BSR of page-one books:** At least 3 books under 30,000 Kindle BSR
- **Search results count:** Under 3,000 is ideal

> "If you can find keywords where the search results is below 3,000, that is typically good. Even if you have to go over it a little bit, that is fine."
> -- Sean Dollwet, "Find Profitable Keywords FAST"

Cut any keyword that fails both tests. Narrow to your top 15-20 validated phrases.

### Step 3: Check for Exact-Match Title Opportunities

> "If nobody else is actually using this keyword [in their title] and if you use it, that is why it's that much easier to rank for it."
> -- Sean Dollwet, "HOW TO DO KEYWORD RESEARCH for Kindle Publishing"

Note which phrases have few or no exact-match titles on page one. These are high-value targets for your keyword boxes (and potentially your title/subtitle).

### Step 4: Remove Words Already in Title/Subtitle

List every word that appears in your book's title and subtitle. These words are EXCLUDED from your keyword boxes.

> "Putting the same word more than once inside of those boxes or your title or subtitle does not help. We saw no indication that somebody would rank that or index better if they had it more often."
> -- Dave Chesson, "7 Kindle Keywords: Use all 50 Characters or Not?"

### Step 5: Apply the Hybrid 7-Box Strategy

Split your 7 boxes into two groups based on Chesson's 121-author experiment:

> "The real answer to this is you should actually do both... Use three to four of the boxes and use those particular phrases inside of it. Now once you've done the three to four boxes, use the rest of them to fill in with other words or phrases that are generally descriptive of what your book is about."
> -- Dave Chesson, "7 Kindle Keywords: Use all 50 Characters or Not?"

**Boxes 1-3 (or 1-4): Exact Target Phrases**
- Your highest-intent, highest-volume search phrases
- Complete phrases shoppers actually type
- These are the terms you want to rank for directly

**Boxes 4-7 (or 5-7): Broad Descriptive Fill**
- Individual words and modifiers Amazon can recombine
- 1-2 boxes dedicated to category-reinforcing terms
- Related topic words that expand reach

**Why this split matters:**

> "The more phrases you put inside that box, the lower your rankings will be. Basically, if you put more words into that box you diminish your argument that you should show up for that particular phrase."
> -- Dave Chesson, "7 Kindle Keywords: Use all 50 Characters or Not?"

Exact-phrase boxes concentrate ranking power. Broad boxes maximize indexing breadth. The hybrid approach gives you both.

### Step 6: Apply Formatting Rules

Hard rules for every keyword box:

- **No commas.** "Some people say adding in a comma is a good idea -- no, man. Not a comma." -- Jacob Rothenberg, "KDP Keywords: How to Use the 7 Keyword Slots"
- **No quotation marks.** "If you put into one of your seven KDP boxes 'epic adventure hot romance' with quotations, then Amazon system will only show for that exact phrase and nothing else." -- Dave Chesson, "Amazon Keyword Rules: New Update!"
- **No words from your title or subtitle** (already ranking)
- **No brand names** you don't own
- **No Amazon program names** (Kindle Unlimited, KDP Select, etc.)
- **No subjective claims** ("best," "amazing," "#1")
- **No time-sensitive statements** ("new for 2024")
- **No spelling variants or plurals** (Amazon handles these automatically)
- **No category words** already covered by your category selections (2024 rule update)

### Step 7: Category Reinforcement

> "I now recommend that authors use one or two of their seven Kindle keyword boxes for their category keywords."
> -- Dave Chesson, "INSANE Amazon Category Change"

Dedicate 1-2 boxes to terms that reinforce your chosen categories. Use additional boxes for terms from categories you did NOT select -- Amazon may add you automatically.

---

## Output Format

Present the filled keyword boxes as a table:

| Box | Strategy | Keywords (max 50 chars) |
|-----|----------|------------------------|
| 1 | Exact phrase | [high-intent phrase] |
| 2 | Exact phrase | [high-intent phrase] |
| 3 | Exact phrase | [high-intent phrase] |
| 4 | Category reinforcement | [category terms] |
| 5 | Broad descriptive | [descriptive words] |
| 6 | Broad descriptive | [descriptive words] |
| 7 | Broad descriptive | [related topic words] |

Also output:
- **Words excluded** (already in title/subtitle)
- **Character count** for each box (max 50)
- **Estimated indexing reach** (total unique 2-3 word combinations Amazon will generate)

---

## Post-Launch Optimization

After the book is live with ads running, keywords should evolve:

> "Have Amazon ads running. Pay attention to your ads campaign -- see what keywords are bringing you impressions, clicks, and sales. I would say you want to optimize for keywords that are bringing you in the most sales."
> -- Jacob Rothenberg, "KDP Keywords: How to Use the 7 Keyword Slots"

- **Monthly for first 3 months:** Check Amazon Ads search term reports. Promote converting terms to exact-phrase boxes. Replace non-converting terms.
- **Quarterly thereafter:** Refresh broad boxes with new related terms.

---

## Related Skills

- **[[niche-scout|niche-scout]]** -- Validate the niche before filling keywords (run FIRST)
- **[[competitor-reverse-engineer|competitor-reverse-engineer]]** -- Mine competitor titles and subtitles for keyword ideas you'd never find through autocomplete alone
- **[[listing-optimizer|listing-optimizer]]** -- Write description + select categories (run AFTER keywords)
- **[[amazon-ads|amazon-ads]]** -- Set up campaigns that feed keyword optimization data

## Related Frameworks

- `keyword-research-pipeline.md` — The 7-box keyword system and full research methodology this skill implements
- `amazon-listing-seo-neil-patel.md` — Neil Patel's SEO methodology adapted for Amazon: semantic keyword clusters, search intent matching, and keyword density principles applied to KDP backend boxes and listing copy
