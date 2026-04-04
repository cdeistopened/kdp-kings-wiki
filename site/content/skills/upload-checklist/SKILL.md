---
name: upload-checklist
description: "Walk through the KDP upload process with emphasis on three irreversible decisions (DRM, KDP Select, ISBN) and complete asset checklists per format. Use before uploading any book."
type: decision
source_chapters:
  - ch-08
source_speakers:
  - Sean Dollwet
  - Dale L Roberts
  - Dave Chesson
---

# Upload Checklist

Walk through every decision in the KDP upload process, with special attention to the three choices you cannot reverse after publishing. Produces format-specific asset checklists and a post-upload verification protocol.

## Usage

```
/upload-checklist --format ebook
/upload-checklist --format paperback
/upload-checklist --format all  # ebook + paperback + hardcover
```

---

## The Three Irreversible Decisions

These are the fields that keep experienced publishers up at night. Everything else on the KDP dashboard can be edited after publication. These three cannot.

### 1. Digital Rights Management (DRM)

Once enabled, DRM cannot be removed. Ever. You would have to unpublish and create a new listing.

> "Digital Rights Management is supposed to protect your ebook against piracy. I don't recommend this option but feel free to research if it makes sense for you. Once you select this option you cannot undo it later."
> -- Dale L Roberts, "How to Self Publish a Book Step By Step on KDP in 10 Minutes"

**Consensus from all three practitioners: DECLINE DRM.** The people who pirate books were never going to buy yours. DRM protects nothing and punishes actual customers (no lending, no easy device transfer).

**Decision:** [ ] Enable DRM / [x] Decline DRM (recommended)

### 2. KDP Select Enrollment

Locks your ebook into a 90-day exclusive agreement with Amazon. During that window, you cannot sell or give away the ebook anywhere else.

> "KDP Select is an exclusivity program in which you can put your ebook into the Kindle Unlimited library where people will check out your book and you will be paid per page read. If you are okay with staying on Amazon and Amazon alone then I would recommend that you choose KDP Select."
> -- Dale L Roberts, "How to Publish eBooks on KDP | Step-by-Step Tutorial for Beginners"

> "If you write in fiction I'd highly recommend you really think about using KU and therefore Kindle Select. However though if you're a nonfiction I'd recommend probably not."
> -- Dave Chesson, "KDP Select Review: Is it Worth It?"

**Working rule:**
- Fiction: default to KDP Select (KU reader base skews fiction)
- Nonfiction: consider going wide from the start
- You can opt out before the 90-day period auto-renews

**Decision:** [ ] Enroll in KDP Select / [ ] Skip (go wide)

### 3. Free vs. Purchased ISBN

Free KDP ISBN = your book's imprint is listed as "Independently Published" -- permanently for that edition. Cannot be changed later.

> "When using a free assigned ISBN through a publishing platform you're essentially allowing them to own the imprint of your book. If you're purchasing your own ISBN through sites like Bowker... then you can own the imprint."
> -- Dale L Roberts, "Paid ISBN vs Free ASIN from Amazon - How to Buy ISBNs"

For ebooks, ISBN is optional. Amazon assigns a free ASIN regardless:

> "You don't have to [enter] an ISBN because Amazon will give you a free ISBN."
> -- Sean Dollwet, "How to Upload a Book to Amazon KDP (Complete Step-By-Step Tutorial)"

Print books require one -- free or purchased. ISBNs through Bowker (US) run $125 single or ~$1.50 each at 1,000 units.

**Decision:** [ ] Free KDP ISBN / [ ] Purchased ISBN (imprint: _______)

---

## Pre-Upload Asset Checklists

### Ebook Assets

- [ ] Manuscript file (ePub preferred; DOCX and KPF accepted)
- [ ] Front cover image (JPEG or TIFF)
- [ ] Book description with HTML formatting (up to 3,000 characters)
- [ ] 7 keyword phrases (from `/keyword-fill`)
- [ ] 3 category selections identified and verified non-ghost (from `/listing-optimizer`)
- [ ] Metadata document: title, subtitle, author name, description ready to copy-paste
- [ ] Three irreversible decisions made (DRM, KDP Select, ISBN)

> "I highly recommend ePub over the other options. It's less hassle and mostly honors what you've created for your interior. The other options tend to have formatting issues."
> -- Dale L Roberts, "How to Self Publish a Book Step By Step on KDP in 10 Minutes"

### Paperback Assets (in addition to ebook)

- [ ] Interior manuscript (PDF preferred -- DOCX gets "a little wonky")
- [ ] Full wrap cover (PDF only -- front, spine, and back)
- [ ] Trim size selected (6x9 most common for nonfiction)
- [ ] Cover finish chosen (matte preferred by ~90% of publishers)
- [ ] Print-specific category selections (different from ebook categories)
- [ ] ISBN decision made (free KDP or purchased)

### Hardcover Assets

- [ ] Same interior as paperback (reuse works fine)
- [ ] Different cover dimensions than paperback (PDF, full wrap)
- [ ] Separate ISBN (free KDP or purchased -- different from paperback)
- [ ] Note: expanded distribution NOT available for hardcovers

> "Since the hard cover book is a different publication type you'll need to assign a new ISBN."
> -- Dale L Roberts, "How to Self Publish a Book Step By Step on KDP in 10 Minutes"

### Account Prerequisites

- [ ] KDP account created at kdp.amazon.com
- [ ] Tax information submitted (W-9 for US, W-8BEN for international)
- [ ] Bank account linked for royalty deposits

> "The very first thing you want to do is click on your account here and make sure you enter your tax information and bank account so that you can get paid."
> -- Sean Dollwet, "How to Upload a Book to Amazon KDP (Complete Step-By-Step Tutorial)"

---

## Upload Walkthrough: Key Fields

### Page 1: Book Details

| Field | Notes |
|-------|-------|
| Language | Select book's language |
| Title/Subtitle | Keywords in subtitle, but don't stuff |
| Series | Create if applicable (ordered or unordered) |
| Description | Use HTML. Don't paste plain text. |
| Categories | Select 3 -- verified non-ghost |
| Keywords | 7 slots, 50 chars each -- from `/keyword-fill` |
| Pre-order | Up to 1 year in advance for ebooks |

> "If you just copy and paste your words into this, your book description will look like a giant block of text."
> -- Dave Chesson, "How to Upload a Book To Amazon"

### Page 2: Content

| Field | Notes |
|-------|-------|
| DRM | IRREVERSIBLE. Decline recommended. |
| Manuscript | Upload ePub (preferred) |
| Cover | Upload JPEG/TIFF (ebook) or PDF wrap (print) |
| AI disclosure | Declare AI-generated vs AI-assisted honestly |
| Previewer | ALWAYS launch. Check all device views. Fix flagged errors. |
| ISBN | Optional for ebook. Required for print. |

### Page 3: Pricing

| Field | Notes |
|-------|-------|
| KDP Select | IRREVERSIBLE for 90 days. Decide before uploading. |
| Territories | All territories (worldwide) unless rights are sold |
| Royalty/Price | 70% tier: $2.99-$9.99. Avoid dead zone $10-$19.98. |
| Expanded distribution | Enable for paperback (unless using IngramSpark) |

---

## Print-Specific Options

| Option | Common Choices |
|--------|---------------|
| Paper type | Black & white / premium color / standard color |
| Trim size | 5"x8" (fiction), 6"x9" (nonfiction), 8.5"x11" (children's) |
| Bleed | No bleed for standard text books |
| Cover finish | Matte (preferred) or glossy |

> "I recommend you select expanded distribution which is basically allowing Amazon to sell your books outside of Amazon. So once a month you can get some extra sales from here."
> -- Sean Dollwet, "How to Upload a Book to Amazon KDP (Complete Step-By-Step Tutorial)"

> "Expanded distribution is not available for hard cover books right now."
> -- Dale L Roberts, "How to Self Publish a Book Step By Step on KDP in 10 Minutes"

---

## Post-Upload Checklist (Within 72 Hours)

- [ ] Verify product page -- title, subtitle, description, cover display correctly
- [ ] Check categories are active and not ghost categories
- [ ] Confirm 7 keywords are entered (they occasionally drop during upload)
- [ ] Order a proof copy for any print edition before promoting
- [ ] Link ebook and print editions on same product page (usually automatic -- verify)
- [ ] Set up Author Central at author.amazon.com -- add bio, photo, editorial reviews
- [ ] Save proof copy review notes for any formatting corrections

---

## Related Skills

- **[[listing-optimizer|listing-optimizer]]** -- Description, categories, bio (run BEFORE upload)
- **[[keyword-fill|keyword-fill]]** -- 7 keyword boxes (run BEFORE upload)
- **[[pricing-strategist|pricing-strategist]]** -- Set optimal price and make KDP Select/DRM decisions BEFORE uploading
- **[[launch-sequence|launch-sequence]]** -- Plan launch timeline (run AFTER upload)

## Related Frameworks

- `upload-checklist.md` — Extended guidance on the upload process, including the three irreversible decisions and format-specific asset requirements
