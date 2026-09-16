# Day 04 — Section 6: Full SEO Content Generation System

**Date:** 16 Sep 2026 | **Lectures:** 6.31–6.60 (30 lectures) | **Section:** 6 of 8

---

## Table of Contents

1. [What You're Building — The Big Picture](#1-what-youre-building)
2. [Reverse-Engineering OutRank — Studying the Best](#2-reverse-engineering-outrank)
3. [SEO Fundamentals You Must Know](#3-seo-fundamentals)
4. [System Architecture — Data Flow Diagram](#4-system-architecture)
5. [Airtable Database Design — All 5 Tables](#5-airtable-database-design)
6. [Workflow 1 — ICP Generator](#6-workflow-1-icp-generator)
7. [DataForSEO Setup — Authentication & API](#7-dataforseo-setup)
8. [Workflow 2 — Seed Keywords (URL → Keywords)](#8-workflow-2-seed-keywords)
9. [Workflow 3 — Long-Tail Keywords (Keyword → Sub-keywords)](#9-workflow-3-long-tail-keywords)
10. [Workflow 4 — Subtopics Generator](#10-workflow-4-subtopics-generator)
11. [Workflow 5 — Blog Content Generation Pipeline](#11-workflow-5-blog-content-generation)
12. [The Context Loop — Writing Long-Form Articles](#12-the-context-loop)
13. [Airtable Interface — V1 Front-End](#13-airtable-interface)
14. [What's Next — V2 Migration Plan](#14-whats-next)
15. [Tips, Tricks & Warnings (Full List)](#15-tips-tricks-and-warnings)
16. [Quick Recall Test](#16-quick-recall-test)

---

## 1. What You're Building

In Section 6 you build a **complete AI-powered SEO content generation system** — an end-to-end pipeline that:

1. Takes a company's **website URL + LinkedIn page** as the only inputs
2. Automatically generates an **Ideal Customer Profile (ICP)**
3. Finds **seed keywords** your competitors are ranking for
4. Expands those into hundreds of **long-tail keywords** (cheaper to rank for)
5. Generates **subtopic ideas** per keyword
6. Writes **full, cited, SEO-optimised blog articles** in Markdown
7. Stores everything in **Airtable** with a visual front-end for clients

**Why this matters for you professionally:**
- OutRank charges $99/month for this exact service
- Their output is 90-100% AI-detected (you can do the same or better)
- You can build this for clients as a white-labelled SaaS or freelance project
- Total running cost per company: roughly $1–$5 in API calls (vs $99/month)

---

## 2. Reverse-Engineering OutRank

**OutRank** is a real $1M+/year SaaS that generates SEO blog content for businesses. The instructor studied it by signing up and going through the onboarding. Here's exactly what OutRank takes as inputs and what it outputs — so you know what to build.

### OutRank's 6-Step Onboarding (Inputs)

**Step 1 — Business Info**
- Website URL
- Business name (auto-filled by AI from website)
- Business description (auto-filled by AI)
- Target audience description

> **Your equivalent:** The `Companies` table in Airtable, with the ICP generator filling all fields automatically.

**Step 2 — Competitor URLs**
- List of 3–5 competitor website URLs
- OutRank scrapes what keywords they're already ranking for

> **Your equivalent:** The `Competitors` table, where you add competitor URLs and n8n calls DataForSEO to find their keywords.

**Step 3 — Blog Inputs (existing content)**
- Sitemap URL (so it can avoid writing about pages that already exist)
- Best article examples (1–3 URLs) — teaches it your writing style
- It scans existing blogs to prevent **keyword cannibalisation** (two of your articles competing for the same keyword — bad for SEO)

> **Your equivalent:** The `Blog Inputs` table. You fill in sitemap URL, article examples, and it uses that as context.

**Step 4 — Branding & Style**
- Language (default: English)
- Tone and style (informative vs listicle)
- Number of internal links per article (default: 3)
- Global article instructions (e.g. "always include practical examples")
- Image style (brand + text realism OR watercolor realism)
- Brand colour (hex code)

> **Your equivalent:** Fields in `Blog Inputs` table — tone, style, internal links, instructions, image style, brand colour.

**Step 5 — Enhancement Options** (yes/no toggles)
- Include YouTube video embeds
- Include call-to-actions (CTAs)
- Include infographics
- Include emojis

> **Your equivalent:** 4 single-select fields (Yes/No) in the `Blog Inputs` table.

**Step 6 — Keyword Strategy**
- Manual entry OR auto-generate keywords
- OutRank generates ~30 long-tail keywords based on competitor analysis

> **Your equivalent:** Automated via DataForSEO — you run workflows to get keywords with actual search volume, difficulty, and CPC data.

### OutRank's Outputs

```
Content Repository View
┌───────────────────────────────────────────┐
│ Keyword            │ Difficulty │ Volume  │
│ digital transform..│ Low        │ 390/mo  │
│ AI automation tool.│ Medium     │ 1,200   │
│ workflow automation│ Low        │ 480     │
└───────────────────────────────────────────┘
  ↓ Click into any row
  ↓ See full blog content

Content Schedule View  
┌───────────────────────────────────────────┐
│ Calendar showing which article publishes  │
│ which day. Drag to rearrange schedule.    │
│                                           │
│ Mon: "What is API Integration?"           │
│ Wed: "Top 10 Workflow Tools"              │
│ Fri: "How to Automate Invoice Processing" │
└───────────────────────────────────────────┘
```

> **Key insight the instructor shared:** OutRank's own blog articles score 90–100% AI-detected on AI-detector tools. So you're building something equivalent to a $99/month SaaS, at a fraction of the cost. The prompt engineering is what you'll optimise over time to make it sound more human.

---

## 3. SEO Fundamentals You Must Know

These concepts came up throughout the 30 lectures. You need all of them.

### Why Ranking on Google Matters
- **93% of users never go past page 1** of Google search results
- **Content is the #1 ranking factor** — Google rewards consistent, high-quality content
- Ranking on page 1 = free organic traffic every month, forever

### Short-Tail vs Long-Tail Keywords

```
Short-Tail (Hard to rank):              Long-Tail (Easier to rank):
┌─────────────────────────────┐         ┌─────────────────────────────────────────┐
│ "cars"                      │         │ "cars for sale that are red in           │
│ Volume: 1,000,000/month     │         │  Chippenham under £2,000"               │
│ Competition: Extremely high │         │ Volume: 50/month                        │
│ Ranking chance: Near zero   │         │ Competition: Very low                   │
│ (AutoTrader, etc dominate)  │         │ Ranking chance: High                    │
└─────────────────────────────┘         └─────────────────────────────────────────┘
```

**Strategy:** Target long-tail keywords first. As you accumulate multiple articles about related long-tail topics, Google begins to trust your site and you start climbing for the short-tail terms too.

### Topic Clusters (Hub & Spoke Model)

```
                    [HUB ARTICLE]
                  "AI Automation Tools"
                  (seed keyword — hard)
                        │
          ┌─────────────┼──────────────┐
          │             │              │
   [SPOKE 1]       [SPOKE 2]      [SPOKE 3]
"AI automation   "Best no-code  "How to automate
 for beginners"  tools 2025"    invoice processing"
 (long-tail)     (long-tail)    (long-tail)
```

- **Hub** = main article targeting the seed keyword
- **Spokes** = individual articles each targeting one long-tail keyword
- All spokes **link back to the hub** and to each other (internal links)
- This cluster structure signals to Google that you're an authority on the topic

### Keyword Cannibalisation — CRITICAL Warning
> If you write TWO articles that both target the keyword "AI automation tools", they will compete against each other in Google's rankings and both rank lower. **One keyword = one article, maximum.**

This is why OutRank scans your existing sitemap — to avoid writing about things you've already covered.

### Keyword Metrics (from DataForSEO)

| Metric | What it means | What you want |
|--------|--------------|---------------|
| **Volume** | Average monthly searches | HIGH |
| **Competition Index** | 0.0–1.0 (1.0 = very hard) | LOW (< 0.3) |
| **Keyword Difficulty** | Low / Medium / High | LOW |
| **CPC (Cost Per Click)** | What advertisers pay per click | Use as proxy for difficulty |

> **Rule of thumb:** Target keywords with **low difficulty + high volume + highly relevant to your service**. A keyword like "Zapier" has huge volume but you'll never rank for it against Zapier's own site. Focus on niche terms.

### Internal Links
- **Internal link** = a link from one of YOUR blog articles to another one of YOUR blog articles
- Recommended: **3 internal links per article**
- Helps Google understand how your content is related
- Passes "link authority" between pages

---

## 4. System Architecture — Data Flow Diagram

Here's the complete data flow you're building across all 6 workflows:

```
INPUT (from Airtable)
     │
     ├─► [Company URL + LinkedIn]
     │         │
     │         ▼
     │   ┌─────────────────────────────────────────────┐
     │   │  WORKFLOW 1: ICP Generator                  │
     │   │  AI Agent + Perplexity → fills ICP fields   │
     │   └─────────────────┬───────────────────────────┘
     │                     │ (ICP: who is your customer?)
     │
     ├─► [Company URLs + Competitor URLs]
     │         │
     │         ▼
     │   ┌─────────────────────────────────────────────┐
     │   │  WORKFLOW 2: Seed Keywords                  │
     │   │  DataForSEO keywords-for-site endpoint      │
     │   │  → 10 seed keywords per URL                 │
     │   └─────────────────┬───────────────────────────┘
     │                     │ (e.g. "AI automation tools")
     │
     │                     ▼
     │   ┌─────────────────────────────────────────────┐
     │   │  WORKFLOW 3: Long-Tail Keywords             │
     │   │  DataForSEO × 4 endpoints:                  │
     │   │  1. Related keywords                        │
     │   │  2. Keyword suggestions                     │
     │   │  3. Keyword ideas                           │
     │   │  4. Autocomplete                            │
     │   │  → ~19 long-tail keywords per seed keyword  │
     │   └─────────────────┬───────────────────────────┘
     │                     │ (e.g. "AI workflow automation tools free")
     │
     │                     ▼
     │   ┌─────────────────────────────────────────────┐
     │   │  WORKFLOW 4: Subtopics Generator            │
     │   │  DataForSEO content generation endpoint     │
     │   │  → 10-12 subtopic ideas per keyword         │
     │   └─────────────────┬───────────────────────────┘
     │                     │ (e.g. "Introduction to AI workflow tools")
     │
     │                     ▼
     │   ┌─────────────────────────────────────────────┐
     │   │  WORKFLOW 5: Blog Content Pipeline          │
     │   │                                             │
     │   │  Stage A: Content Planner                  │
     │   │  (Gemini 1.5 Pro — reasoning model)         │
     │   │  → Article structure + research questions   │
     │   │                                             │
     │   │  Stage B: Research Agent                   │
     │   │  (Gemini Flash + Perplexity sonar)          │
     │   │  → Facts + citations for each section       │
     │   │                                             │
     │   │  Stage C: Content Writer (loop)             │
     │   │  (Claude 3.5 Sonnet — writing model)        │
     │   │  → One section at a time, with context      │
     │   │  → Temporary Airtable field stores progress │
     │   └─────────────────┬───────────────────────────┘
     │                     │
     │                     ▼
OUTPUT: Full blog article (Markdown, 2000+ words) stored in Airtable Blog Content table
```

**Scale reality check (important!):**
- 1 company → ~5 URLs (own + competitors)
- 5 URLs × 10 seed keywords = **50 seed keywords**
- 50 seed keywords × 19 long-tail = **950 long-tail keywords**
- 950 × 10 subtopics = **9,500 potential article topics**

> That's why you use buttons in Airtable to control WHICH keywords you process. You don't run everything at once — you choose strategically.

---

## 5. Airtable Database Design — All 5 Tables

### Table 1: Companies

This is the master table. Everything links back here.

| Field Name | Field Type | Notes |
|------------|-----------|-------|
| Company Name | Single line text | Primary field |
| Website URL | URL | e.g. `https://automake.io` |
| Company LinkedIn | URL | e.g. `https://linkedin.com/company/...` |
| Generate ICP | **Button** | Triggers Workflow 1 via webhook |
| Product Description | Long text | Filled by ICP Generator |
| Ideal Customer Profile | Long text | Filled by ICP Generator |
| Pain Points & Challenges | Long text | Filled by ICP Generator |
| Key Goals | Long text | Filled by ICP Generator |
| How They Currently Solve Problems | Long text | Filled by ICP Generator |
| Status | Single select | `Incomplete` / `Processing` / `Complete` |

**Button formula (critical — learn this):**
```
= "<YOUR_WEBHOOK_URL>?record_id=" & RECORD_ID()
```
- Replace `<YOUR_WEBHOOK_URL>` with your n8n production webhook URL
- The `RECORD_ID()` function appends this row's unique Airtable ID to the URL
- When clicked, it opens the URL in a new tab, which fires the n8n webhook
- The webhook receives the record ID as a query parameter: `?record_id=recXXXXXXXX`

> **Step by step — how to create a Button field:**
> 1. Add new field → choose field type **Button**
> 2. Name it (e.g. "Generate ICP")
> 3. Choose action: **Open URL**
> 4. In the URL formula field, type: `= "https://your-n8n-webhook-url?record_id=" & RECORD_ID()`
> 5. Make sure there's a `?` before `record_id=` (that's the query string separator)
> 6. Choose a colour for the button (optional)
> 7. Save

### Table 2: Competitors

| Field Name | Field Type | Notes |
|------------|-----------|-------|
| Competitor URL | URL | Primary field |
| Competitor Of | Link to Companies | Links back to which company this competes with |
| Keyword Status | Single select | `Incomplete` / `Processing` / `Complete` |
| Get Keywords | **Button** | Triggers Workflow 2 |

> **Tip:** Add your OWN company URL here as well as competitors. This way Workflow 2 finds keywords you're already ranking for too.

### Table 3: Blog Inputs

One row per company. Stores all branding/style preferences.

| Field Name | Field Type | Default |
|------------|-----------|---------|
| Company | Link to Companies | — |
| Sitemap URL | URL | — |
| Blog Root URL | URL | e.g. `https://automake.io/blog` |
| Best Article Example 1 | URL | An article you want to emulate |
| Best Article Example 2 | URL | — |
| Best Article Example 3 | URL | — |
| Tone and Style | Single select | Options: `Informational`, `Listicle` |
| Number of Internal Links | Number | Default: `3` |
| Global Article Instructions | Long text | e.g. "Always include practical examples" |
| Image Style | Single select | `Brand + Text Realism`, `Watercolor Realism` |
| Brand Colour | Single line text | Hex code, e.g. `#FF6B35` |
| YouTube Videos | Single select | `Yes` / `No` (default: Yes) |
| Call To Action | Single select | `Yes` / `No` (default: Yes) |
| Infographics | Single select | `Yes` / `No` (default: Yes) |
| Emojis | Single select | `Yes` / `No` (default: Yes) |

### Table 4: Keywords

This is the core table. One row per keyword (both seed and long-tail).

| Field Name | Field Type | Notes |
|------------|-----------|-------|
| Seed Keyword | Single line text | The top-level keyword (from URL research) |
| Keyword | Single line text | The long-tail keyword |
| Date Added | Date | When this keyword was found |
| Competition Index | Number | 0.0–1.0 (from DataForSEO) |
| Volume | Number | Monthly search volume |
| CPC | Currency | Cost per click in USD |
| Keyword Difficulty | Single select | `Low` / `Medium` / `High` |
| Company | Link to Companies | Which company this keyword relates to |
| URL | Link to Competitors | Which URL this keyword came from |
| Subtopics | Long text | Array of 10–12 topic ideas |
| Temporary Article | Long text | Stores in-progress article (cleared after done) |
| Keyword Status | Single select | `Incomplete` / `Processing` / `Complete` |
| Long Tail Status | Single select | `Incomplete` / `Processing` / `Complete` |
| Subtopic Status | Single select | `Incomplete` / `Processing` / `Complete` |
| Article Status | Single select | `Incomplete` / `Processing` / `Complete` |
| Get Long Tail Keywords | **Button** | Triggers Workflow 3 |
| Get Subtopics | **Button** | Triggers Workflow 4 |
| Generate Article | **Button** | Triggers Workflow 5 |

> **Why so many status fields?** Each status tracks one workflow stage independently. You can see at a glance what's been done for each keyword across all workflows.

### Table 5: Blog Content

| Field Name | Field Type | Notes |
|------------|-----------|-------|
| Blog ID | Auto number | Unique ID |
| Keyword | Link to Keywords | Which keyword this article targets |
| Date Created | Date | When article was generated |
| Title | Single line text | Article title |
| Blog Content | Long text | Full Markdown article |
| Blog Content (Rich) | Long text (rich) | Enable rich formatting to preview rendered Markdown |
| Date Scheduled | Date | When to publish |

> **Rich text tip:** You can create two versions of the content field — one plain text (for sending to APIs) and one with rich formatting enabled (for human review). The rich text version renders Markdown headings, bold, tables, etc. inside Airtable.

---

## 6. Workflow 1 — ICP Generator

### What It Does
Takes a company's name, website URL, and LinkedIn page → uses an AI Agent with Perplexity to research the company → fills in the ICP fields in your Companies table.

### Step-by-Step Build

**In Airtable:**
1. Make sure the Companies table has all fields from Table 1 above
2. Add a **Button** field called "Generate ICP"
3. Set the URL formula: `= "<your-webhook-url>?record_id=" & RECORD_ID()`
4. Activate your n8n workflow FIRST before testing the button (otherwise nothing happens)

**In n8n — workflow structure:**
```
[Webhook] → [Get Record] → [If: Status = Incomplete?]
                │
         TRUE branch:
                │
         [Update Record: Status = Processing]
                │
         [AI Agent + Perplexity Tool]
                │
         [Update Record: Fill ICP fields + Status = Complete]
```

**Node 1: Webhook (trigger)**
- Type: Webhook
- Method: GET
- Path: auto-generated (copy the Production URL)
- The record ID arrives as: `{{ $json.query.record_id }}`

**Node 2: Get Record (Airtable)**
- Table: Companies
- Operation: Get Record
- Record ID: `{{ $json.query.record_id }}`

**Node 3: If (check status)**
- Condition: `{{ $json.Status }}` equals `Incomplete`
- This prevents re-running if already complete

**Node 4: Update Record (set to Processing)**
```
Table: Companies
Operation: Update Record
Record ID: {{ $('Get Record').item.json.id }}
Fields:
  Status = "Processing"
```
> **Critical UX tip:** This "Processing" status update must happen IMMEDIATELY when the button is clicked, BEFORE the AI research runs. This gives visual feedback to the user that something is happening. Without this, the user stares at an unchanged screen for 30+ seconds and thinks it's broken.

**Node 5: AI Agent**
- Type: AI Agent (not Basic LM Chain — you need the tools feature)
- Model: Gemini 2.5 (cheap, excellent at web research)
- Tools: Add Perplexity tool

**Why Gemini 2.5 for ICP?**
- It's cheap (much cheaper than GPT-4)
- It handles structured information from websites well
- The task isn't creative — it's research and extraction

**AI Agent System Prompt:**
```
You are an expert research analyst. Use perplexity to research and analyze 
companies to develop detailed customer personas, pain points, and market 
positioning insights for strategic business development.

You MUST research all three provided inputs:
1. The company name
2. The website URL  
3. The LinkedIn URL

Thoroughly focus on B2B customer characteristics and pain points.
Ensure ALL sections are completed with detailed, research-backed information.
Do NOT make assumptions about company operations without supporting evidence.
```

**AI Agent User Message:**
```
Company Name: {{ $('Get Record').item.json['Company Name'] }}
Website URL: {{ $('Get Record').item.json['Website URL'] }}
LinkedIn URL: {{ $('Get Record').item.json['Company LinkedIn'] }}
```

**Structured Output Parser (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "product_description": { "type": "string" },
    "ideal_customer_profile": { "type": "string" },
    "pain_points_and_challenges": { "type": "string" },
    "key_goals": { "type": "string" },
    "how_they_currently_solve_problems": { "type": "string" }
  }
}
```

**Node 6: Update Record (write ICP data + set Complete)**
```
Table: Companies
Operation: Update Record
Record ID: {{ $('Get Record').item.json.id }}
Fields:
  Product Description = {{ $json.output.product_description }}
  Ideal Customer Profile = {{ $json.output.ideal_customer_profile }}
  Pain Points & Challenges = {{ $json.output.pain_points_and_challenges }}
  Key Goals = {{ $json.output.key_goals }}
  How They Currently Solve Problems = {{ $json.output.how_they_currently_solve_problems }}
  Status = "Complete"
```

### What Good ICP Output Looks Like

The instructor tested this with his company **Automake** and got:

> *"Automake offers custom automation solutions powered by n8n. They design and implement automated workflows that reduce manual effort for businesses. Their ICP is businesses of various sizes that experience challenges with manual multi-system workflows leading to inefficiencies. Key pain points: manual repetitive tasks, poor system integration, limited scalability, lack of visibility, insufficient resources."*

The instructor's verdict: **"Hit the nail on the head. Really happy with this — with a limited prompt and a cheap model."**

### Label this workflow in n8n
- Add a sticky note label: **"ICP Generator"**
- Colour it purple
- This keeps things organised as you add more workflows

---

## 7. DataForSEO Setup

### What is DataForSEO?
DataForSEO is a **cheap SEO data API** that gives you:
- Keywords a website is ranking for
- Search volume, competition, CPC for any keyword
- Long-tail keyword suggestions, related keywords, autocomplete
- Content subtopic ideas

Cost: approximately **$0.001–$0.075 per API call** (vs $99/month for OutRank).

### Authentication — Base64 Encoding

DataForSEO uses **HTTP Basic Auth** but in a slightly unusual way. You must Base64-encode your credentials before using them.

**Step-by-step:**
1. Sign up at `dataforseo.com`
2. Go to **API Access** page
3. You'll receive an email with your **API password**
4. Open a **Base64 encoder** (search "base64 encoder" on Google)
5. Type in your credentials in this exact format: `youremail@example.com:yourAPIpassword`
6. Click **Encode**
7. Copy the resulting Base64 string (it will look like `dGVzdEBleGFtcGxlLmNvbTpwYXNzd29yZA==`)

**Example:**
```
Input:  ranak0501@gmail.com:MySecretAPIPassword123
Output: cmFuYWswNTAxQGdtYWlsLmNvbTpNeVNlY3JldEFQSVBhc3N3b3JkMTIz
```
(Not real — just an example of the format)

### Setting Up Credentials in n8n — Header Auth (IMPORTANT SECURITY TIP)

**DO NOT** put your Base64 credentials directly inside the HTTP Request node's body parameters. If you share your workflow JSON file with someone, they'll see your credentials.

**Instead, use Generic Credential → Header Auth:**

1. In your HTTP Request node, click **Authentication**
2. Select **Generic Credential Type**
3. Select **Header Auth**
4. Click **Create New Credential**
5. Set:
   - **Name:** `Authorization`
   - **Value:** `Basic <your-base64-encoded-credentials>`
   - (The word "Basic" followed by a space, then your Base64 string)
6. Save the credential
7. Now in the HTTP Request node, you'll see the Header Auth credential is selected
8. **Remove any `Authorization` header you had in the Headers section** — it's now handled by the credential

> **Why this matters:** When you export your n8n workflow as JSON and share it in the community or with a client, the credentials stored in the Header Auth system are **encrypted and not exposed**. Credentials in headers/body ARE exposed in the JSON export.

### Importing DataForSEO curl requests into n8n

DataForSEO's documentation shows every endpoint with a ready-made **curl command**. Here's how to use it:

1. Go to `dataforseo.com` → API Documentation
2. Find the endpoint you want (e.g. "Keywords Data → Google Ads → Keywords for Site → Live")
3. On the right side, you'll see a **curl request**
4. Copy it
5. In n8n, add an **HTTP Request** node
6. Click the **...** menu → **Import from cURL**
7. Paste the curl command
8. n8n auto-fills: URL, method (POST/GET), body parameters
9. Remove any `Authorization` header it imported — you're using Header Auth credential instead
10. Set your credential in the Authentication section

### Cost Tracking Dashboard

DataForSEO has a dashboard at `app.dataforseo.com` where you can:
- See exactly how much each endpoint has cost you
- Track usage per endpoint
- Optimise which endpoints you're using

> Tip: Always top up your DataForSEO account before running bulk tests. You'll get errors if you run out of credit mid-flow.

---

## 8. Workflow 2 — Seed Keywords (URL → Keywords)

### What It Does
Takes a URL (your site or a competitor's) → calls DataForSEO's "Keywords for Site" endpoint → returns 10 seed keywords with search volume, competition, and CPC data → stores them in the Keywords table.

### The DataForSEO Endpoint

**Endpoint:** `Keywords Data → Google Ads → Keywords for Site → Live`
**URL:** `https://api.dataforseo.com/v3/keywords_data/google_ads/keywords_for_site/live`
**Method:** POST
**Cost:** ~$0.075 per task (one URL = one task)

**Request body (after importing curl):**
```json
[{
  "target": "automake.io",
  "location_code": 2826
}]
```

> Remove `location_code` if you want global results (not just UK/specific location). The instructor did this for broader data.

**Rename** this HTTP Request node to: `Get Keywords`

**Limit to 10 items:** Use a **Limit** node after the HTTP Request to cap at 10 seed keywords. This prevents being overwhelmed with data at later stages.

**DataForSEO result returns:** Up to 1,215 keywords (for a well-established site). You only want 10 — the highest-relevance ones.

### Workflow Structure

```
[Webhook] → [Get Record (Competitors table)] → [If: Keyword Status = Incomplete?]
                    │
              TRUE branch:
                    │
              [Update Record: Keyword Status = Processing]
                    │
              [HTTP Request: Get Keywords]
                    │
              [Limit: 10 items]
                    │
              [Create Records in Keywords table × 10]
                    │
              [Update Record (Competitors): Keyword Status = Complete]
```

### Airtable Button for this workflow

In the **Competitors** table, add a Button field:
- Name: `Get Keywords`
- URL formula: `= "<webhook2_url>?record_id=" & RECORD_ID()`
- Colour: Blue

### Mapping DataForSEO data to Airtable fields

DataForSEO's response structure:
```
tasks[0].result[0].items[0] = {
  keyword: "workflow automation",
  competition: 0.47,           ← Competition Index (number)
  competition_level: "MEDIUM", ← Keyword Difficulty (text: LOW/MEDIUM/HIGH)
  search_volume: 1600,         ← Monthly volume
  cpc: 3.52,                   ← Cost per click in USD
  monthly_searches: [...]      ← Historical volume data
}
```

> **Data path tip:** Navigate to the data with: `tasks` → first index → `result` → first index → `items`. In n8n expression syntax that's `{{ $json.tasks[0].result[0].items }}`.

**In the Airtable Create Record node, map fields like this:**
```
Seed Keyword = {{ $json.keyword }}
Date = {{ $now }}  (with typecast enabled)
Competition Index = {{ $json.competition }}
Volume = {{ $json.search_volume }}
CPC = {{ $json.cpc }}
Keyword Difficulty = {{ $json.competition_level }}
Company = ["{{ $('Get Record').item.json.fields['Competitor Of'][0] }}"]
URL = ["{{ $('Get Record').item.json.id }}"]
Keyword Status = "Complete"
```

> **Array format for linked records:** When linking to another Airtable record, the value MUST be passed as an array of record IDs, even if it's just one: `["recXXXXXXXX"]`. Passing it as a plain string will error with "expecting an array but received a string".

> **Date typecast:** Enable "Typecast" in the Airtable node for date fields. Without this, n8n's date format may not match what Airtable expects, causing errors.

### Result you should see

After clicking "Get Keywords" for a competitor URL, you should see ~10 rows appear in your Keywords table with:
- Keywords like: "workflow automation", "workflow automation tools", "AI workflow automation", "automation software"
- All linked back to the company and the URL

---

## 9. Workflow 3 — Long-Tail Keywords (Keyword → Sub-keywords)

### What It Does
Takes one seed keyword → calls 4 different DataForSEO endpoints → gets ~19 long-tail keyword variations → stores them all in the Keywords table linked to their parent seed keyword.

### The 4 Endpoints (and why you need all of them)

| Endpoint | What it finds | Example output |
|----------|--------------|----------------|
| **Related Keywords** | Keywords from Google search results related to your term (searches Google's "related searches" section) | "Zapier", "n8n", "Make.com" |
| **Keyword Suggestions** | Search phrases CONTAINING your keyword — focuses on long-tail expansion | "AI workflow automation tools", "best AI workflow automation tools" |
| **Keyword Ideas** | Keywords in the same product/service CATEGORY — semantically related | "character AI", "humanize AI" (same space) |
| **Autocomplete** | What Google's autocomplete suggests when you type your keyword | "AI automation tools examples", "AI automation tools open source" |

> Use all 4 because they use different algorithms. Together they give a well-rounded view of what's worth targeting.

### Costs for this workflow

- Each endpoint costs approximately **$0.001 per item** returned
- You're limiting to **3 items per endpoint** = $0.003 per keyword per endpoint
- 4 endpoints × $0.003 × 20 seed keywords = **~$0.24 total** for long-tail keywords
- Well within a dollar

**Finding pricing:** In DataForSEO docs, each endpoint page has a pricing section. For "live" mode, it shows cost per task or per item.

### Setting Up Each HTTP Request

Copy the first HTTP Request node (your "Get Keywords" node) and paste it 4 times. Then:

1. **Get Related:** Import curl from `Keywords Data → Google Related Keywords → Live`
2. **Get Suggestions:** Import from `Keywords Data → Google Keyword Suggestions → Live`
3. **Get Keyword Ideas:** Import from `Keywords Data → Google Keyword Ideas → Live`
4. **Get Autocomplete:** Import from `Keywords Data → Google Autocomplete → Live`

For each, after importing curl:
- Remove the `Authorization` header
- Set credential to `Header Auth → DataForSEO Header Auth`
- Set the keyword input to 3 (limit results)
- Rename the node clearly (Get Related, Get Suggestions, etc.)

**Example body for each (keyword is dynamic later):**
```json
[{
  "keyword": "AI workflow tools",
  "limit": 3
}]
```

### Autocomplete Special Case

The autocomplete endpoint does NOT return historical data (search volume, competition, CPC). It only gives you keyword strings.

**Solution:** Use an additional DataForSEO endpoint to bulk-get historical data for those autocomplete keywords:
- Endpoint: `Keywords Data → Google Ads → Keywords for Keywords → Live`
- Pass in the autocomplete keywords as an array
- This returns the missing metrics

```json
[{
  "keywords": ["AI automation tools examples", "AI automation tools open source", "AI automation tools free"],
  "location_code": 2826
}]
```

> Some autocomplete keywords won't have any data — that's normal. Use what you have.

### Edit Fields / Set Node — Standardising Output

After each of the 4 HTTP Request nodes, add an **Edit Fields** node to extract just what you need:

```
For each keyword item:
  keyword       = {{ $json.keyword }}
  competition   = {{ $json.competition }}     (number, 0–1)
  volume        = {{ $json.search_volume }}
  cpc           = {{ $json.cpc }}
  difficulty    = {{ $json.competition_level }}  (LOW/MEDIUM/HIGH)
```

> **Why:** Each endpoint returns slightly different JSON structures. Standardising here means the Airtable node downstream can map fields consistently regardless of which endpoint the data came from.

### Workflow Structure (all 4 run in parallel)

```
[Webhook] → [Get Record (Keywords table)] → [If: Long Tail Status = Incomplete?]
                    │
              TRUE branch:
                    │
              [Update: Long Tail Status = Processing]
                    │
              ┌─────┼──────────────────────────────────────┐
              │     │                │                      │
         [Get    [Get           [Get Keyword    [Get Autocomplete]
         Related] Suggestions]  Ideas]                │
              │     │                │            [Get Bulk Data]
              │     │                │                      │
         [Edit  [Edit          [Edit Fields]    [Edit Fields]
         Fields] Fields]
              └─────┴────────────────┴──────────────────────┘
                                    │
                             [Create Records in Keywords table × 19]
                                    │
                      [Update Record (Keywords): Long Tail Status = Complete]
```

### Airtable Button for Workflow 3

In the **Keywords** table, add a Button field:
- Name: `Get Long Tail Keywords`
- URL formula: `= "<webhook3_url>?record_id=" & RECORD_ID()`
- Colour: different from the seed keyword button (green works)

### Scale warning

With the default settings:
- 10 seed keywords × 4 endpoints × 3 results = **~120 long-tail keywords**
- 120 × subtopics (next workflow) = potentially **1,200+ topic ideas**

> You may want to reduce the limit from 3 to 1 or 2 per endpoint when working with many seed keywords. The goal is a manageable backlog, not thousands of articles.

### After running Workflow 3

Group your Keywords table by the `Seed Keyword` field to visually see:
- Under "AI automation" → all long-tail variations
- Under "workflow automation tools" → all long-tail variations
- etc.

Each keyword row also has buttons for "Get Subtopics" and "Generate Article" — so you decide keyword by keyword what to do next.

---

## 10. Workflow 4 — Subtopics Generator

### What It Does
Takes one long-tail keyword → calls DataForSEO's content generation endpoint → returns 10–12 topic ideas (subtopics) you could write blog articles about → stores them in the `Subtopics` field of that keyword row.

### The DataForSEO Endpoint

**Endpoint:** `Content Generation → Generate Subtopics`
**Method:** POST
**Input:** a topic (your long-tail keyword)
**Output:** list of blog article topic ideas

**Example request:**
```json
[{
  "topic": "AI workflow tools"
}]
```

**Example output for "AI workflow tools":**
```
1. Introduction to AI Workflow Tools
2. Key Features of AI Workflow Tools
3. Popular AI Workflow Tools in 2025
4. Challenges in Implementing AI Workflow Tools
5. AI Workflow Tools for Small Businesses
6. Comparing AI Workflow Tools: Pros and Cons
7. How to Choose the Right AI Workflow Tool
8. Future of AI Workflow Tools
9. Case Studies: Successful AI Workflow Tool Implementations
10. AI Workflow Tools vs Traditional Automation Software
```

### Workflow Structure

```
[Webhook] → [Get Record (Keywords table)] → [If: Subtopic Status = Incomplete AND Keyword exists?]
                    │
              TRUE branch:
                    │
              [Update: Subtopic Status = Processing]
                    │
              [HTTP Request: Generate Subtopics]
                    │
              [Aggregate: collect all subtopics into array]
                    │
              [Update Record (Keywords):
                Subtopics = [aggregated array]
                Subtopic Status = "Complete"]
```

### Aggregate Node

The Generate Subtopics endpoint returns multiple items (one per subtopic). You need to combine them into one array before storing in Airtable.

Use an **Aggregate** node:
- Mode: **Aggregate All Item Data (into a Single List)**
- This takes all 10–12 individual items and bundles them into one array
- Then the Airtable Update node stores this array in the `Subtopics` (Long text) field

### Airtable Button for Workflow 4

In the **Keywords** table:
- Name: `Get Subtopics`
- URL formula: `= "<webhook4_url>?record_id=" & RECORD_ID()`
- Colour: Light purple

### Why you don't write about all subtopics

For the keyword "AI automation course", you might get 12 subtopics. You should pick **1 or 2** to write about. Writing about all 12 would be keyword cannibalisation — you'd be competing with yourself.

> Think of subtopics as a content backlog. You schedule one, write it, publish it, then come back and write the next one months later.

---

## 11. Workflow 5 — Blog Content Generation Pipeline

This is the most complex part. The workflow runs three AI models in sequence.

### The Three-Stage Architecture

```
STAGE A: CONTENT PLANNER
Model: Gemini 1.5 Pro (reasoning)
Input: keyword + subtopic + ICP + style inputs
Output: article structure (headers, key points, research questions, semantic keywords)

          ↓

STAGE B: RESEARCH AGENT
Model: Gemini Flash + Perplexity sonar tool
Input: research questions from Stage A
Output: facts + citations for each section

          ↓  

STAGE C: CONTENT WRITER (runs in a LOOP — one section at a time)
Model: Claude 3.5 Sonnet (creative writing)
Input: one section at a time + all research + what's been written so far
Output: one section of the article (200–500 words)
       + running tally of full article so far (stored in Airtable temp field)

          ↓

Final output: Full Markdown blog article (2000+ words) → Blog Content table
```

### Why Three Separate Models?

| Stage | Task | Best Model Type | Why |
|-------|------|----------------|-----|
| Planning | Structure the article | **Reasoning model** | Needs chain-of-thought to create a logical, flowing structure |
| Research | Find facts with citations | **Search-capable model** | Needs web access + consolidation |
| Writing | Creative, human-like prose | **Creative writing model** | Claude 3.5 Sonnet excels here |

> **Key insight:** You CAN'T use one model for everything if you want quality. A reasoning model writes dry, structured prose. A creative writing model doesn't think deeply enough to plan a 2000-word article. Separating them maximises output quality.

### Inputs to Pull Before Writing

When the "Generate Article" button fires, the first thing n8n does is gather inputs from multiple Airtable tables:

1. **From Keywords table** (the row you clicked): keyword, subtopics, article status
2. **From Companies table** (via linked record): company name, website URL, ICP data
3. **From Blog Inputs table** (via Companies link): tone, internal links target, brand colour, image style, yes/no toggles

Use a **Get Record** node for each table, and then an **Edit Fields** (Set) node to standardise all inputs into one clean object:

```
standardised_inputs = {
  seed_keyword: "AI automation",
  keyword: "AI automation course",
  subtopics: [...array of 12 topics...],
  company_name: "Automake",
  company_url: "https://automake.io",
  icp: "B2B businesses struggling with manual workflows...",
  tone_style: "Informative",
  internal_links_count: 3,
  image_style: "Brand + Text Realism",
  brand_colour: "#FF6B35",
  include_youtube: "Yes",
  include_cta: "Yes",
  include_infographics: "Yes",
  include_emojis: "Yes",
  article_instructions: "Always include practical examples"
}
```

> **Tip on linking tables:** The Keywords table is linked to Companies, and Companies is linked to Blog Inputs. So when you get the Keywords record, you can get the Company record ID from it, then use that to get the Blog Inputs record. This chain-linking is exactly how relational databases work — and why using Linked Record fields (not plain text) matters.

### Stage A — Content Planner (Gemini 1.5 Pro)

**Why Gemini 1.5 Pro for planning:**
- Strong reasoning capability
- Low-medium cost
- Large context window (handles all ICP + keyword data easily)
- Can output structured JSON reliably

**How to select an AI model in n8n:**
- Use **OpenRouter** as the provider
- This gives you access to ALL models (GPT, Claude, Gemini, etc.) through one API key
- In the model dropdown, type the model name

**System Prompt (simplified version of what the instructor used):**

```
You are an expert blog article planner specializing in creating detailed, 
research-driven content outlines. Your purpose is to develop comprehensive 
article structures that balance SEO optimisation with reader value.

CONSTRAINTS:
- Always create outlines that match the specified content style (Informative or Listicle)
- 2-3 supporting points for each header
- Create structures that support 2,000-4,000 word articles
- Never create thin content outlines — each section must add unique value
- Incorporate plans for tables, statistics, and multimedia elements

CONTENT STYLES:
<informative_style>
  - Opening section: current state / problem
  - Foundation concepts clearly explained
  - Progressive depth into specific strategies
  - Real-world examples and case studies
  - Conclusion with practical next steps
</informative_style>

<listicle_style>
  - Brief introduction
  - 7-12 numbered items
  - Each item as a self-contained mini lesson
  - 2-3 implementation points per item
  - Conclusion with summary and CTA
</listicle_style>

RESEARCH QUESTION GUIDELINES:
- Focus on finding recent statistics (last 12 months)
- Look for expert quotes and case studies
- Identify tools, platforms or resources to mention
- Find 5-10 semantic keyword variations to incorporate naturally
```

**User Message (dynamic inputs):**
```
Content Style: {{ $json.tone_style }}
Target Keyword: {{ $json.keyword }}
Subtopics Available: {{ $json.subtopics }}
ICP: {{ $json.icp }}
```

**Structured Output Parser — JSON Schema:**
```json
{
  "type": "object",
  "properties": {
    "article_title": { "type": "string" },
    "content_style": { "type": "string" },
    "target_keyword": { "type": "string" },
    "semantic_keywords": {
      "type": "array",
      "items": { "type": "string" }
    },
    "article_structure": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "section_type": { "type": "string" },
          "header": { "type": "string" },
          "supporting_points": {
            "type": "array",
            "items": { "type": "string" }
          },
          "research_questions": {
            "type": "array",
            "items": { "type": "string" }
          },
          "supporting_elements": { "type": "string" },
          "estimated_words": { "type": "number" }
        }
      }
    },
    "total_estimated_words": { "type": "number" }
  }
}
```

**Example output from Content Planner:**
```
Article Title: "How to Choose the Right AI Automation Course for Your Business"
Content Style: Informative
Target Keyword: "AI automation course"
Semantic Keywords: ["online AI automation course", "learning AI automation", 
                    "career in AI automation", "AI automation tools training"]
Article Structure:
  [0] Section Type: Introduction
      Header: "The Growing Need for AI Automation Skills"
      Supporting Points:
        - Highlight increasing demand for AI automation professionals
        - Discuss business benefits of AI automation
        - Emphasise importance of choosing the right course
      Research Questions:
        - What are latest statistics on growth of AI automation?
        - What are top in-demand skills in AI automation field?
      Estimated Words: 200
  [1] Section Type: Body
      Header: "Key Criteria for Evaluating AI Automation Courses"
      ...
  [5] Section Type: Conclusion
      Header: "Next Steps: Starting Your AI Automation Journey"
      ...
Total Estimated Words: 1,850
```

### Stage B — Research Agent (Gemini Flash + Perplexity)

The Content Planner outputs `research_questions` for each section. The Research Agent's job is to go out and find answers.

**Process:**
1. Split out the article structure (each section becomes a separate item)
2. Merge research questions from all sections together
3. Pass ALL research questions to the Research Agent in one go
4. Research Agent sends multiple queries to Perplexity (aim for 5–10 queries minimum)
5. Returns all findings in one consolidated research block

**Why one bulk research call (not per-section):**
- If you research per-section (6 sections × 3 questions = 18 API calls), costs add up
- The Content Writer can select which facts are relevant to each section
- Simpler flow to maintain

**Research Agent prompt (key parts):**
```
You are a comprehensive research analyst. 

Inputs you'll receive:
- Research questions (from the content plan)
- Supporting points they're trying to answer

Your task:
1. Analyse the incoming research questions
2. Consolidate them where there's overlap  
3. Send relevant queries to Perplexity (use the tool — minimum 5 calls, up to 10)
4. Return relevant information that supports the supporting points
5. Always include working links to sources
6. Return the research question, the answer, and the citation URL
```

**Model settings:**
- Primary: Gemini 1.5 Flash (cheap, fast)
- Fallback: Gemini 1.5 Pro (better if Flash struggles)
- Tool: Perplexity sonar model

**Perplexity tool setup in n8n:**
1. In the AI Agent node, add a tool
2. Search for "Perplexity" in the tools list
3. Add your Perplexity API key as a credential
4. Use the **sonar** model (not sonar-deep-research) to start — it's cheaper
5. The model itself decides what to search based on your instructions

**Output schema for Research Agent:**
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "question": { "type": "string" },
      "answer": { "type": "string" },
      "citation": { "type": "string" }
    }
  }
}
```

**Troubleshooting the Research Agent (what the instructor tried):**
- Problem: Returns too few results → Solution: Explicitly say "ask minimum 5 queries"
- Problem: Summaries too vague → Solution: Change field name to "answer" not "summary"; ask it to return all content from perplexity
- Problem: Good research but poor output format → Solution: Use JSON schema with question + answer + citation fields
- Problem: Gemini Flash struggles with instructions → Solution: Upgrade to Gemini 1.5 Pro for research stage

### Stage C — Content Writer (Claude 3.5 Sonnet, in a LOOP)

**Why Claude 3.5 Sonnet for writing?**
- Claude Sonnet is widely considered the best creative writing model available
- The instructor: *"Claude 3.5 Sonnet has always been really, really good at creating content for me"*
- Fallback: Gemini 1.5 Pro (cheaper but slightly less creative)

**Why a LOOP (not one big call)?**
When you try to write a full 2,000-word article in one call, the model consistently produces only 600–700 words. The context is too large; it tries to be concise.

Solution: Write one section at a time. The Split Out node splits the article structure into 6 individual items (intro + 4 body sections + conclusion), and the loop processes one per iteration.

**Content Writer System Prompt (key elements):**
```
You are an expert blog content writer specialising in creating valuable, 
human-centered articles that educate and inform readers while naturally 
incorporating SEO elements. Your writing style mirrors authentic social 
media voices while delivering comprehensive information.

WRITING STYLE:
- Third-grade reading level (simple, clear language)
- Avoid technical jargon where possible
- Avoid em dashes (–) — these are AI tells
- Short sentences
- Use markdown formatting (headers, bold, bullet points, tables)
- Avoid keyword stuffing — use semantic variations naturally
- Include natural CTAs where contextually appropriate

INPUTS YOU WILL RECEIVE:
- Article title and target keyword
- Content style (informative/listicle)  
- Semantic keywords to weave in naturally
- The specific section to write (header + supporting points)
- All research findings with citations
- What has already been written (for context/flow)
- ICP information (for CTA targeting)

OUTPUT:
- new_article_content: The new section you're writing (complete Markdown)
- article_so_far: Everything previously written PLUS the new section
```

**Why include article_so_far in the output?**
This is the clever trick to maintain context. Each loop iteration:
1. Receives what's been written so far
2. Writes the new section
3. Outputs the new section AND appends it to what was already written
4. That combined output goes into the Airtable `Temporary Article` field
5. Next loop iteration reads the temp field and has full context

```
Iteration 1: writes Introduction → saves to temp field
Iteration 2: reads temp field (Introduction), writes Section 1 → saves to temp field  
Iteration 3: reads temp field (Intro + Section 1), writes Section 2 → saves to temp field
...
Iteration 6: reads temp field (everything), writes Conclusion → saves to temp field
Final step: copy temp field to Blog Content table
```

### The Context Loop — Full n8n Structure

```
[Merge: sections + research] → [Loop] → [Get Record (read temp article from Airtable)]
                                             │
                                    [Content Writer (Claude 3.5)]
                                             │
                                    [Update Record: Temp Article = article_so_far]
                                             │
                                    [Loop back for next section]
                                             │
                              [After loop: Create Blog Content record]
                              [Update Keywords: Article Status = Complete]
                              [Clear Temp Article field]
```

### Content Writer User Message (dynamic)

```
Article Title: {{ $json.article_title }}
Target Keyword: {{ $json.target_keyword }}
Semantic Keywords: {{ JSON.stringify($json.semantic_keywords) }}
Content Style: {{ $json.content_style }}

CURRENT SECTION TO WRITE:
Section Type: {{ $json.section_type }}
Header: {{ $json.header }}
Supporting Points: {{ JSON.stringify($json.supporting_points) }}
Estimated Words: {{ $json.estimated_words }}

RESEARCH FINDINGS (use these for facts and citations):
{{ JSON.stringify($('Research Agent').item.json.output) }}

ARTICLE SO FAR (write the next section to flow naturally from this):
{{ $('Get Record').item.json.fields['Temporary Article'] }}

ICP CONTEXT (use for CTA and audience alignment):
{{ $json.icp }}
```

---

## 12. The Context Loop

### The Problem
Writing an article section by section in a loop creates isolated paragraphs — each section doesn't know what was written before. The article has no flow or continuity.

### Solutions the Instructor Tried

| Approach | Problem |
|----------|---------|
| Edit Fields node to carry context | Lost data between loop iterations |
| Code node to maintain a variable | Unreliable across n8n workflow executions |
| Static workflow data | Too complex, still lost context |
| **Temporary Airtable field** | ✅ Works reliably — simple and effective |

### The Winning Pattern — Temporary Airtable Field

1. Add a `Temporary Article` Long text field to your **Keywords** table
2. At the START of each loop iteration, GET the Keywords record (reads the temp field)
3. At the END of each loop iteration, UPDATE the Keywords record (writes to the temp field)
4. The update sets `Temporary Article = article_so_far` (everything written so far)

This works because:
- Airtable is the persistent store — it doesn't lose data between n8n nodes
- Each loop iteration reads the latest state of the article
- The content writer always has the full context of what's been written

> **The instructor's comment:** *"You could use something like Redis for populating data inside there, and I'm sure there's a way to use the code node to push the data back into the start of the loop, but this was the easiest way to find right now, and we're not pushed for time."*

### What the Final Article Looks Like

The instructor tested this and got:
- **2,161 words** (vs 659 words with a single call)
- Proper Markdown formatting (headers, bullet points, tables)
- Internal structure that flows between sections
- External links to cited sources embedded inline
- A reference to the n8n Academy inside the body (relevant to the keyword)
- Topic: "How to Choose the Right AI Automation Course for Your Business Needs"

Pasting into a Markdown editor showed: headings, statistics, a comparison table, bullet points, and properly formatted links.

### AI Content Detection Reality Check

The instructor tested the article on **AI Detector Zero** and got **100% AI-written** detection score.

**Why this matters:**
- Google allegedly penalises or down-ranks AI-generated content (though this is debated)
- Human readers are more likely to engage with and share content that sounds human
- The instructor's own LinkedIn posts are AI-generated but read as 100% human — because the prompt is tuned for it

**How to improve humanisation:**
- Add a **tone of voice document** (e.g. your LinkedIn posts) to the Content Writer's system prompt
- Avoid em dashes (`–`) — a classic AI tell
- Keep sentences short
- Use "third grade reading level" in the prompt
- You can also use a **Humanise step** (pass the article to an LLM specifically trained to rewrite AI content to sound human — available as API services)

---

## 13. Airtable Interface — V1 Front-End

### Why Build a Front-End in Airtable?

The raw Airtable grid view is too confusing for a client. They'd see all your status columns, all your button fields, linked records — it's overwhelming.

Airtable has a built-in **Interface Designer** (click "Interfaces" in the left panel) that lets you create clean, app-like pages on top of your existing data.

### What the Interface Should Look Like

**Replicate OutRank's interface as closely as possible in V1:**

**Page 1 — Company Setup**
- Form to enter company name, URL, LinkedIn URL
- Button to generate ICP
- Display the generated ICP once complete

**Page 2 — Keywords View**
- Filtered to show only THIS company's keywords
- Shows: keyword, difficulty, volume, CPC
- Colour-coded by difficulty (green = low, amber = medium, red = high)
- Button next to each keyword to get long-tail keywords / subtopics

**Page 3 — Blog Content Schedule**
- Calendar-style view using the `Date Scheduled` field
- Shows which article is planned for which date
- Click into any article to read the full content

**Page 4 — Blog Content Repository**
- List of all written articles
- Click to expand and read any article in rich text format

### V1 Limitations (and V2 Plan)

**V1 (Airtable):**
- No user authentication — anyone with the base can see everything
- One set of data for one account
- Buttons are tied to hardcoded webhooks

**V2 Migration Plan (covered in future videos):**
- Move database from Airtable to **Supabase** (free, PostgreSQL, supports row-level security)
- Build front-end with **Lovable** or **Retool** (proper web app with login)
- Add **user authentication** — each user only sees their own company's data
- Charge users per month or per article generated
- **This is the actual SaaS product you can sell**

> **Key insight:** The instructor's workflow is: build V1 with Airtable to validate the concept and show clients → migrate to Supabase + Lovable for V2 to make it a sellable product.

---

## 14. What's Next

After Section 6, the remaining next steps are:

1. **Remove hardcoded values** from the blog pipeline:
   - Subtopic selection (currently hardcoded — should pick the best subtopic automatically)
   - Content style (currently hardcoded as "Informative" — should be chosen by AI or pulled from Blog Inputs table)

2. **Upload final blog content** to the Blog Content table (linked to keyword, with date, title, rich text)

3. **Image generation** — generate images using **Flux** (image generation model) and embed them into the article Markdown

4. **Scheduling** — add date-based scheduling logic to determine when each article should be published

5. **Airtable Interface** — build the V1 front-end as described above

6. **Connect to CMS** — push articles directly to **WordPress**, **Webflow**, or **Shopify** using their APIs (so clients never have to copy-paste)

7. **Humanisation step** — add a post-processing step to make articles sound more human

8. **V2 migration** — Supabase + Lovable/Retool front-end with auth

---

## 15. Tips, Tricks & Warnings (Full List)

These were spread across all 30 lectures. Collected here for easy revision.

### n8n Tips

1. **Always label workflows clearly** — use sticky note labels with colours (ICP Generator = purple, Keyword Research = blue, etc.) so you can navigate when you have many workflows

2. **Use fallback models** — every AI node should have a backup model. If Claude goes down, fall back to Gemini. This prevents workflows failing in production.

3. **Deactivate nodes during testing** — when testing one section of a workflow, deactivate downstream nodes so you don't accidentally write test data to your database. Re-activate when ready.

4. **Pin execution data** — when testing, pin data from an earlier run so you don't have to rerun the whole workflow just to test one node. Click the output of a node → "Pin Data".

5. **Copy to editor** — instead of viewing pinned data in the small panel, click "Copy to Editor" for a full-screen JSON view. Much easier to read and debug.

6. **Use the log panel** — in AI Agent nodes, expand the log panel (bottom of the output) to see every individual API call the agent made, including what it sent to Perplexity and what came back.

7. **Pop-out log panel** — click the pop-out icon on the log panel to open it in a new window. Essential for reading long research outputs.

8. **OpenRouter for model access** — use OpenRouter as the provider in n8n to access any model (GPT, Claude, Gemini, Mistral) from one API key instead of managing multiple credentials.

9. **Hit spacebar to rename a node** — click a node → press spacebar → type a new name → press enter. Much faster than right-clicking.

10. **Use Expressions view for dynamic prompts** — switch the system prompt field to "Expression" mode to mix static text with dynamic `{{ }}` values from previous nodes.

11. **XML tags in prompts** — wrap prompt sections in XML tags (`<constraints>`, `<instructions>`, `<examples>`) for two benefits: easier for you to edit later, and LLMs understand nested structure better.

### Airtable Tips

12. **Button field beats Checkbox** — the instructor initially used a checkbox to trigger webhooks but switched to a Button. Buttons are faster (one click), cleaner UI, and open the URL directly. Checkboxes require watching for changes (webhook trigger) which is slightly more complex.

13. **Status columns for every workflow** — always add `Incomplete / Processing / Complete` status for every action. It gives the client visibility and prevents accidental re-runs.

14. **Processing status FIRST** — update status to "Processing" immediately when the button is clicked, BEFORE any AI runs. This is client-facing UX — without it, users think the system is frozen.

15. **Linked records over text fields** — always use Airtable's Linked Record field type to connect tables, not plain text that stores a name. Linked records give you: automatic relational joins, the ability to pull fields from linked tables in n8n, and visual relational views in Airtable.

16. **Group by keyword** — in the Keywords table, add a Group By on the `Seed Keyword` field. This makes it much easier to see which long-tail keywords belong to which seed keyword.

17. **Rich text for blog content** — create a second version of your blog content field with rich text formatting enabled. The plain text field is for API operations; the rich text field is for human review.

18. **Don't click buttons twice** — each keyword button creates new records. Clicking "Get Long Tail Keywords" twice for the same keyword creates duplicates. Future improvement: add deduplication logic. For now, only click once and verify the status changed to "Processing".

19. **Record IDs as arrays** — when linking to another Airtable record via n8n's Airtable node, the record ID MUST be in array format: `["recXXX"]`. A plain string will fail silently or error.

20. **Enable Typecast for dates** — in n8n's Airtable node, enable the "Typecast" option for date fields. Without it, n8n's ISO date format may not match Airtable's expected format and you'll get errors.

### DataForSEO Tips

21. **Header Auth over inline credentials** — NEVER put your Base64 credentials directly in the HTTP Request node headers or body. Always use n8n's Generic Credential → Header Auth. When you export workflow JSON, credentials in Header Auth are encrypted; credentials in node parameters are not.

22. **Base64 format** — your credential must be: `Basic <base64encoded(email:password)>`. The word "Basic" with a capital B, then a space, then the Base64 string. No quotes.

23. **Monitor the cost dashboard** — check `app.dataforseo.com` regularly to see what each endpoint is costing you. This helps you optimise and remove expensive endpoints that aren't adding enough value.

24. **Limit results** — always add a `limit` parameter to DataForSEO requests. Without it, you can get 1,000+ results (expensive and overwhelming). Start with 3 for testing, increase to 10–20 for production.

25. **Autocomplete needs extra call** — the autocomplete endpoint doesn't return historical data (volume, CPC, difficulty). You must make a second call to the "Keywords for Keywords" endpoint passing the autocomplete results as an array to get that data.

### AI Model Selection Tips

26. **Reasoning models for planning** — use Gemini 1.5 Pro or similar reasoning models for the Content Planner stage. You want the model to "think" about article structure before writing.

27. **Creative models for writing** — Claude 3.5 Sonnet is the instructor's #1 choice for blog content writing. It produces more natural, human-sounding prose than GPT or Gemini.

28. **Cheap models for research** — Gemini Flash is sufficient for the Research Agent stage since the model's main job is passing queries to Perplexity and formatting the output, not creative thinking.

29. **Start cheap, upgrade if needed** — always start with cheaper/faster models. Only upgrade to more expensive models (Gemini 1.5 Pro, Claude Opus, GPT-4o) if the cheaper models can't handle the task well.

30. **Perplexity sonar model** — start with `sonar` (cheapest), not `sonar-deep-research`. Only upgrade if research quality is insufficient.

### SEO Content Strategy Tips

31. **One keyword = one article max** — never write two articles targeting the same keyword. They'll compete with each other in Google rankings (keyword cannibalisation).

32. **Target low difficulty + high volume** — keywords with `LOW` difficulty are ones you can realistically rank for. High volume means people are actually searching. Find the sweet spot.

33. **Long-tail first** — start with long-tail keywords (easier to rank, less competition). As you accumulate authority, you'll start ranking for short-tail keywords automatically.

34. **Semantic keywords, not keyword stuffing** — the Content Planner generates a list of semantic keywords (related phrases). Weave these naturally into the article. Never force a keyword into a sentence where it doesn't fit.

35. **3 internal links per article** — link from each article to 3 other articles on the same website. This builds your topic cluster and passes authority between pages.

36. **Scan the sitemap** — before generating articles, check the sitemap URL for the company's blog. Avoid writing about topics that are already covered (add this as a future workflow improvement).

### Prompt Engineering Tips

37. **Use a Prompt Generator project in Claude** — create a dedicated Claude project that specialises in generating 80% prompts from short briefs. This saves enormous time and produces far better first-draft prompts than writing from scratch.

38. **Give examples in prompts** — when using a prompt generator, paste examples of articles you want to emulate (e.g. a good listicle from OutRank, a good informative article). The prompt generator will extract structural patterns from these examples.

39. **Plan → Research → Write (in that order)** — the instructor initially tried Research → Plan → Write, then switched. Planning first creates targeted research questions; that targeted research produces much better source material than broad research upfront.

40. **Avoid em dashes in prompts** — explicitly say "avoid em dashes" in your Content Writer prompt. Em dashes are a telltale sign of AI-generated content. Most AI models default to using them heavily.

---

## 16. Quick Recall Test

Test yourself on these key concepts before your next study session.

**Q1:** What does the Airtable Button formula look like to trigger an n8n webhook?
> Answer: `= "<your_webhook_url>?record_id=" & RECORD_ID()`

**Q2:** Why must you update status to "Processing" BEFORE running the AI?
> Answer: Client UX — without it, the user sees no change for 30+ seconds and thinks it's broken.

**Q3:** What is keyword cannibalisation and why is it bad?
> Answer: Writing two articles targeting the same keyword — they compete with each other in Google rankings, both rank lower than if you just wrote one definitive article.

**Q4:** Name the 4 DataForSEO endpoints used for long-tail keyword research.
> Answer: Related Keywords, Keyword Suggestions, Keyword Ideas, Autocomplete

**Q5:** Why use Header Auth instead of inline credentials in HTTP Request nodes?
> Answer: When you export the workflow as JSON and share it, Header Auth credentials are encrypted. Inline credentials in node parameters are exposed in plain text in the JSON.

**Q6:** What is the Base64 format for DataForSEO credentials?
> Answer: `Basic <base64(youremail@example.com:yourAPIpassword)>`

**Q7:** Why write the blog article section by section in a loop instead of all at once?
> Answer: Writing all at once produces only 600–700 words despite 1,800 being requested. Splitting into sections (loop) gets 2,000+ words total, one section at a time.

**Q8:** How does the Content Writer maintain context about what's been written in previous loop iterations?
> Answer: A `Temporary Article` field in Airtable stores the running article. Each iteration reads it (article so far), writes the new section, then writes the combined article back to the temp field.

**Q9:** Which model is best for the Content Planner and why?
> Answer: Gemini 1.5 Pro — it has strong reasoning capability for planning well-structured content. Reasoning models "think longer" which produces better structure.

**Q10:** Which model is best for the Content Writer and why?
> Answer: Claude 3.5 Sonnet — it produces the most natural, human-sounding creative writing. The instructor explicitly said it's "really, really good at creating content."

**Q11:** What is a topic cluster (hub and spoke model)?
> Answer: A hub article targets a seed keyword (broad, hard to rank). Multiple spoke articles each target one long-tail keyword (easier to rank) and all link back to the hub. Together they signal authority to Google.

**Q12:** Why is OutRank interesting to reverse-engineer?
> Answer: It charges $99/month but outputs 90-100% AI-detected content. You can build the same thing yourself for $1-5 in API calls, making it a profitable client offering.

**Q13:** What does the scale calculation for this system look like?
> Answer: 1 company → ~5 URLs → 50 seed keywords → ~950 long-tail keywords → ~9,500 subtopics. This is why you use buttons to choose WHICH keywords to process, not "process all".

**Q14:** What is the difference between the Competition Index and Keyword Difficulty fields from DataForSEO?
> Answer: Competition Index is a number (0.0–1.0). Keyword Difficulty is text (LOW/MEDIUM/HIGH). They both measure how hard a keyword is to rank for, but in different formats.

**Q15:** What is V2 of this system and what makes it different from V1?
> Answer: V2 replaces Airtable with Supabase (proper database with row-level security), and uses a web framework like Lovable/Retool for the front-end with full user authentication. V1 is a single-user prototype; V2 is a multi-tenant SaaS product.

---

*End of Day 04 — Section 6 Study Guide*
*Total: 30 lectures (6.31–6.60) | Next: Section 7*
