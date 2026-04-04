---
name: listing-optimizer
description: "Write Amazon KDP book descriptions (HTML-formatted), select categories with ghost/duplicate screening, and build author bios. Use when preparing a book for upload or optimizing an existing listing."
type: decision
source_chapters:
  - ch-09
source_speakers:
  - Sean Dollwet
  - Dave Chesson
  - Zach Diamanti
---

# Listing Optimizer

Write the complete Amazon listing package: 5-part HTML description, 3 category selections (screened for ghosts and duplicates), and author bio. Based on Sean Dollwet's description framework, Dave Chesson's category research, and Zach Diamanti's bio template.

## Usage

```
/listing-optimizer --title "Beekeeping for Beginners" --manuscript "path/to/manuscript.md"
/listing-optimizer --asin B0XXXXXXXX  # optimize existing listing
```

## Prerequisites

- Book manuscript (or detailed summary) available for reference
- Keywords filled via `/keyword-fill`
- Niche validated via `/niche-scout`

---

## Workflow

### Part 1: Book Description (5-Part Framework)

> "The book description has five different parts: you have the hook or the headline, you have the lead section or credibility section talking about who you are, you have the bullet points section talking about what's inside the book -- features, benefits -- and then you have the overcome objection section, and then you have the call to action."
> -- Sean Dollwet, "Amazon KDP MISTAKES"

| Section | Purpose | Length |
|---------|---------|-------|
| **1. Hook/Headline** | Stop the scroll. Bold question or provocative statement. | 1-2 sentences |
| **2. Lead/Credibility** | Who wrote this and why it matters. | 2-3 sentences |
| **3. Bullet Points** | What's inside -- features AND benefits, scannable. | 5-8 bullets |
| **4. Overcome Objections** | "Even if you've never..." / "Whether you're..." | 2-3 sentences |
| **5. Call to Action** | Ask for the sale. Direct and clear. | 1 sentence |

**Writing Rules:**

- **Lead with the reader's benefit**, not the author's story. "Unless you are already famous, no one really cares about your story... People really only care about what's in it for them." -- Sean Dollwet, "Amazon KDP MISTAKES"
- Every word is an algorithm signal -- audit for unintended keyword associations
- Avoid health claims ("heal", "cure") -- blocks Amazon Ads. Use "improve", "discover", "support"
- Study top-selling descriptions in your category and model their structure
- Bold main points, italicize key terms, use bullets -- visual distinction matters

**The split-second test:**

> "If people have to stop and read the title, read the book cover, and take a couple seconds just to understand what the book is about, then that is a failed book cover."
> -- Sean Dollwet, "Amazon KDP MISTAKES"

The same principle applies to descriptions. Scannable beats dense.

### Amazon HTML Reference

Amazon KDP descriptions support a limited set of HTML tags:

| Tag | Purpose |
|-----|---------|
| `<b>text</b>` | Bold |
| `<i>text</i>` | Italic |
| `<br>` | Line break |
| `<p>text</p>` | Paragraph |
| `<h4>text</h4>` | Heading (largest allowed) |
| `<h5>text</h5>` | Subheading |
| `<h6>text</h6>` | Small heading |
| `<ul><li>text</li></ul>` | Bullet list |
| `<ol><li>text</li></ol>` | Numbered list |

**NOT supported:** `<h1>`-`<h3>`, `<img>`, `<a>` (links), `<div>`, `<span>`, CSS, colors, fonts, tables.

**Character limit:** All characters count, including HTML tags.

### Description Template

```html
<h4><b>[HOOK: Bold question or provocative statement]</b></h4>

<p>[LEAD: 2-3 sentences establishing credibility and relevance]</p>

<p><b>Inside you'll discover:</b></p>
<ul>
<li>[Benefit 1 -- specific and reader-focused]</li>
<li>[Benefit 2]</li>
<li>[Benefit 3]</li>
<li>[Benefit 4]</li>
<li>[Benefit 5]</li>
<li>[Benefit 6]</li>
</ul>

<p>[OVERCOME OBJECTIONS: "Whether you're... or..." / "Even if you've never..."]</p>

<p><b>[CTA: "Scroll up and click 'Buy Now' to..."]</b></p>
```

---

### Part 2: Category Selection (3 Picks)

The 2023 overhaul changed everything:

> "Unlike before where you would just select BISACs and then could go and add up to 10 more categories through a form, Amazon now shows you a list of Amazon categories and you can select three and that's it."
> -- Dave Chesson, "INSANE Amazon Category Change"

**The 5-Step Category Selection Process:**

**1. Identify fitting categories** with realistic ranking potential. Check BSR of top books. Categories where leaders sit at BSR 20K-80K offer the best path.

**2. Check for duplicates.** 54% of KDP categories are duplicates:

> "Over 54 percent of these KDP categories are actually duplicates of each other."
> -- Dave Chesson, "How to Choose Amazon Book Categories in 2023"

Use duplicates strategically -- one pick that maps across multiple browse paths = maximum coverage.

**3. Screen for ghost categories.** 27% are ghosts:

> "Over twenty-seven percent of categories listed on KDP are what I call a ghost category. These are categories where if your book is listed in it you can't get a bestseller tag for it."
> -- Dave Chesson, "INSANE Amazon Category Change"

**Ghost detection:** Visit the actual Amazon page. If it lacks a category name and browsable tree in the sidebar, it's a ghost. Never select it.

> "If you select all three [ghost categories], you're basically wasting two of your three choices and are just being put into the Paranormal and Urban subcategory above it and that's it."
> -- Dave Chesson, "How to Choose Amazon Book Categories in 2023"

**4. Make your 3 selections** with full knowledge of the duplicate map and ghost list.

**5. Reinforce with keywords.** Dedicate 1-2 keyword boxes to category-specific terms.

> "I now recommend that authors use one or two of their seven Kindle keyword boxes for their category keywords."
> -- Dave Chesson, "INSANE Amazon Category Change"

**Watch for misclassification:** Amazon reads everything -- title, subtitle, keywords, description, author name. Careless language causes misclassification:

> "The words in your book description absolutely affect what Amazon sees. They read your book description."
> -- Dave Chesson, "Discovering How Amazon Treats Your Book"

---

### Part 3: Author Bio (5-Key Template)

> "Unless you're a household name, you have to build credibility with the reader."
> -- Zach Diamanti, "How to Write an Author Bio"

**Length:** 50-100 words. That's it.

> "We're talking 50 to 100 words. Almost every bio I've been asked to write... fell into two categories: either a 50-word bio or a 100-word bio."
> -- Zach Diamanti, "How to Write an Author Bio"

| Key | Purpose |
|-----|---------|
| **1. Punchy opener** | Name your books/genre, set expectations |
| **2. Expertise** | Nonfiction: credentials. Fiction: voice/personality. |
| **3. Credibility** | Awards, features -- state simply, don't brag |
| **4. Personal touch** | Humanize -- hobby, family, location |
| **5. CTA** | Website, freebie, social handle |

**Tailor to the audience.** Same author, different books = different bios.

---

## Output Format

### Complete Listing Package

```markdown
## Book Description (HTML)
[Full HTML-formatted description using 5-part framework]

## Category Selections
| # | Category Path | Ghost Check | Duplicate Coverage | BSR of #1 Book |
|---|-------------|------------|-------------------|---------------|
| 1 | [path] | Verified active | [duplicate mapping] | [bsr] |
| 2 | [path] | Verified active | [duplicate mapping] | [bsr] |
| 3 | [path] | Verified active | [duplicate mapping] | [bsr] |

## Author Bio
[50-100 word bio using 5-key template]

## Listing Audit Checklist
- [ ] Subtitle displays fully in search results
- [ ] Description uses 5-part framework
- [ ] No health claims blocking ads
- [ ] Description leads with reader benefit, not author biography
- [ ] Category selections verified as non-ghost
- [ ] Keywords don't duplicate title/subtitle words
- [ ] Author bio is 50-100 words with all 5 keys
- [ ] Title is instantly clear at thumbnail size
```

---

## Common Listing Mistakes (Red Flags)

From Sean Dollwet's reviews of real publisher submissions:

- **Subtitle gets cut off** -- Keep it short enough to display fully
- **Thin description** -- "Your book description is very very sad here because it's just like five sentences." Use the 5-part framework.
- **No A+ Content** -- Should have 3-5 modules minimum
- **Health claims blocking ads** -- "heal"/"cure" prevents Amazon Ads entirely
- **The autobiography trap** -- Lead with reader benefit, not your personal journey
- **Poor category fit** -- If the #1 bestseller has BSR above 400,000, demand is too low

---

## Related Skills

- **[[niche-scout|niche-scout]]** -- Validate niche + get BSR data for category selection (run FIRST)
- **[[keyword-fill|keyword-fill]]** -- Fill keyword boxes, including category reinforcement terms
- **[[competitor-reverse-engineer|competitor-reverse-engineer]]** -- Study competitor descriptions before writing yours to identify what works and what to beat
- **[[cover-brief|cover-brief]]** -- Design brief for the cover (can run in parallel)
- **[[upload-checklist|upload-checklist]]** -- Final pre-upload verification

## Related Frameworks

- `listing-optimization-checklist.md` — The complete listing audit checklist covering description, categories, keywords, and A+ Content
- `amazon-listing-seo-neil-patel.md` — Neil Patel's SEO methodology adapted for Amazon listings: keyword density, semantic clusters, search intent matching applied to KDP descriptions and backend keywords
