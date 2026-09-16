# n8n Day 04 — Full SEO Content Generation System (Section 6)

**Date:** 16 September 2026
**Section:** 6 (Lectures 6.31 – 6.60) | **30 lectures today** | **Running total: 60 / 76**
**Project built:** SEO Content Generation System (Project 12)
**Tools used:** n8n · Airtable · DataForSEO · Perplexity · OpenAI · Claude

---

## 🎯 What You Will Learn in This Guide

By the end of Section 6 you will be able to:

- Reverse-engineer any SaaS tool into an n8n workflow system
- Build a keyword research pipeline using the DataForSEO API
- Generate high-quality, human-readable, cited blog articles with AI
- Use Airtable as a full back-end database + front-end interface
- Architect a modular, multi-company content system
- Understand topic clusters, long-tail keywords, and SEO content strategy

---

## 📖 Lecture-by-Lecture Breakdown

---

### 6.31 — What We Are Building: Reverse-Engineering OutRank

**The Business Case**

OutRank is a $1 million/year SEO SaaS. But under the hood it is just a set of n8n-style workflows with a nice front-end. The goal of this section is to reverse-engineer OutRank and build our own version — without the monthly fees.

**What OutRank does:**
```
Input: a keyword (e.g. "automation engineer")
         ↓
   Research keyword
         ↓
   Write 2000+ word article
         ↓
   Add images + format
         ↓
Output: SEO-optimised blog article (ready to publish)
```

**What we will build:**
```
6 n8n workflows + Airtable database + Airtable Interface (front-end)
```

**The SEO Reason**
- 93% of users never go past Page 1 of Google
- More content = more keyword coverage = more visibility
- Tools like Surfer SEO, Jasper, Byword, OutRank charge $99/month for 25–30 articles
- We will build the same output ourselves

---

### 6.32–6.33 — System Goals & Architecture

**The 4 goals of our content system:**

| Goal | Details |
|------|---------|
| High-quality articles | Not keyword-stuffed AI trash — actually interesting and useful |
| Beat AI detectors | Sounds human — not flagged by detection tools |
| SEO optimised | Target long-tail keywords, internal linking, topic clusters |
| Fit your workflow | Schedule content, allow edits, notify on completion |

**What makes a good AI blog article:**
- **Human-sounding** — advanced prompting techniques
- **Cited & informational** — referenced sources, statistics
- **Long-form** — 1,000+ words minimum
- **Engaging** — includes diagrams, tables, bullet points, images
- **Internally linked** — links to your other published articles

**The architecture overview:**

```
FRONT END                   BACK END                    AI / DATA
──────────                  ────────                    ─────────
Airtable Interface   ←───   n8n Workflows        ───→  OpenAI / Claude
(V1 — now)          ←───   Airtable Database     ───→  Perplexity
                             DataForSEO API       ───→  DataForSEO
Lovable / Softer            Supabase (V2 later)
(V2 — later)
```

**Two-version build plan:**

| Version | Front-end | Database | Auth |
|---------|-----------|----------|------|
| V1 (now) | Airtable Interface | Airtable | None |
| V2 (later) | Lovable / Webflow / Retool | Supabase | User login + row-level security |

---

### 6.34 — Two-Version Roadmap

**Version 1 focus:**
- Build the back-end n8n workflows first
- Use Airtable as both database AND front-end interface
- Get the content creation working and producing quality output
- Do NOT worry about user authentication yet

**Version 2 plan (later):**
- Replace Airtable front-end with a proper UI (Lovable, Softer, Web, Retool)
- Move database from Airtable → Supabase (handles row-level security + user logins)
- Content creation workflows stay EXACTLY the same

> **Key mindset:** Build the engine first, worry about the dashboard later.

---

### 6.35 — Analysing OutRank: Inputs & Outputs

**OutRank's 6-step onboarding process (inputs we need to replicate):**

```
Step 1: Business Input
  → Website URL
  → Auto-complete: business name, description, target audience (AI reads your site)

Step 2: Competitor Input
  → Competitor website URLs
  → What keywords are competitors ranking for?
  → Gaps where you could rank that they are missing

Step 3: Blog Inputs
  → Existing blog/sitemap URL
  → Scans existing content so it does NOT rewrite same keywords
  → Reads your writing style to copy your tone of voice

Step 4: Branding & Style
  → Language preference
  → Tone (professional, casual, etc.)
  → Internal links per article (recommendation: 3)
  → Global article instructions ("always include practical examples")

Step 5: Image Style
  → Brand or realism or watercolor
  → Brand colour hex code
  → Embed YouTube videos, CTAs, infographics, emojis?

Step 6: Keyword Strategy
  → Manual keyword entry OR auto-generate 30 long-tail keywords
  → Based on competitors + your target audience
```

**OutRank's outputs (what we will produce):**
```
Output 1: Content Repository
  → List of all articles created
  → Keyword, difficulty, volume per article
  → Click in to view the full blog content

Output 2: Content Schedule (calendar view)
  → Pre-planned keywords mapped to dates
  → Internal links auto-suggested based on existing articles
```

---

### 6.36–6.37 — Airtable Setup: Company & Branding Tables

**Airtable base structure — Company table:**

```
COMPANY TABLE
─────────────────────────────────────────────
Field                     Type
─────────────────────────────────────────────
Company name              Single line text
Website URL               URL
Company LinkedIn          URL
Product description       Long text (AI-generated)
Who are the ICP?          Long text (AI-generated)
Pain points / Challenges  Long text (AI-generated)
Key Goals / Objectives    Long text (AI-generated)
How do they solve now?    Long text (AI-generated)
Status                    Single select (Incomplete / Complete)
Global article instructions  Long text
Image style               Single select (Brand Realism / Watercolor Realism)
Brand colour              Single line text (hex code, e.g. #3B82F6)
Generate info             Button (triggers webhook in n8n)
─────────────────────────────────────────────
```

> **Tip:** The "Generate info" button in Airtable triggers a webhook in n8n. This is how the front-end activates the back-end without any code.

**Airtable Interfaces:**
- Airtable allows you to build a visual interface on top of your tables
- Users see buttons, forms, and views — not raw spreadsheet data
- Think of it as a no-code portal built on top of your Airtable base

---

### 6.38 — Airtable: Blog Content & Keywords Tables

**Blog Content table:**

```
BLOG CONTENT TABLE
─────────────────────────────────────────────
Field              Type
─────────────────────────────────────────────
Block ID           Auto number (unique ID)
Keyword            Link to Keywords table
Blog content       Long text (AI-generated article)
Status             Single select
─────────────────────────────────────────────
```

**Keywords table:**

```
KEYWORDS TABLE
─────────────────────────────────────────────
Field              Type
─────────────────────────────────────────────
Seed keyword       Single line text
Keyword            Single line text (related long-tail keyword)
Subtopics          Long text (array of sub-keywords)
Subtopics status   Single select (Incomplete / Complete)
Company            Link to Company table
─────────────────────────────────────────────
```

> **Rule:** Always link tables by reference (Link to another record) rather than copy-pasting values. This keeps data consistent and avoids duplication.

---

### 6.39 — n8n: Mapping Inputs & Outputs with Sticky Notes

**Create a new workflow in n8n:** "SEO Content Generation System"

**Planned sticky notes (inputs):**
```
## Inputs
- Branding info (colours, image style)
- Company info / ICP
- Competitor site info
- Keywords
- Blog content (including existing)
```

**Planned sticky notes (outputs):**
```
## Outputs
- Relevant keywords list
- Blog articles (cited)
- Schedule
```

> **Why do this first?** When you revisit this workflow in 6 months, the sticky notes tell you instantly what goes in, what comes out, and why each part exists. Always plan before you build.

---

### 6.40–6.41 — Workflow 1: ICP Generator

**What it does:** Takes a company website URL → uses AI to generate a full Ideal Customer Profile (ICP).

**Flow:**
```
Airtable Button "Generate info" clicked
         ↓
Webhook (n8n receives record_id from Airtable query)
         ↓
GetRecord (Airtable node — reads Company table row by record_id)
         ↓
IfIncomplete (IF node — only runs if Status = "Incomplete")
         ↓
ICP_Research (AI Agent node)
  ├── Tool: Perplexity (searches web for company info)
  └── System prompt: Business Intelligence Analyst
         ↓
UpdateRecord (Airtable node — writes back):
  - Product description
  - Who are the ICP?
  - Pain points / Challenges
  - Key Goals / Objectives
  - How do they currently solve problems?
  - Status → "Complete"
```

**Node types used:**
- Webhook → GetRecord → IF → AI Agent → Airtable Update

**The ICP output fields:**
| Field | Description |
|-------|-------------|
| Product description | What the company actually sells |
| Ideal customer profile | Who buys it (size, industry, role, geography) |
| Pain points | What problems those customers face |
| Key goals | What customers are trying to achieve |
| Current solutions | What tools/workarounds they use today |

---

### 6.42 — Keyword Architecture: Topic Clusters

**The keyword hierarchy:**

```
SEED KEYWORD (broad topic)
e.g. "automation engineer"
         │
         ├── Sub keyword 1 (long-tail)
         │   e.g. "automation engineer salary UK 2025"
         │
         ├── Sub keyword 2 (long-tail)
         │   e.g. "how to become an automation engineer"
         │
         ├── Sub keyword 3 (long-tail)
         │   e.g. "automation engineer vs software engineer"
         │
         └── Sub keyword 4 (long-tail)
             e.g. "best automation engineering courses online"
```

**Topic cluster model (hub + spokes):**

```
         [HUB ARTICLE]
         Seed keyword
        /      |      \
[SPOKE]    [SPOKE]   [SPOKE]
 Sub kw1   Sub kw2   Sub kw3
```

- Hub = your main article targeting the broad keyword
- Spokes = individual articles targeting long-tail keywords
- All spokes internally link back to the hub
- This structure BOOSTS your SEO ranking for the seed keyword

**Why long-tail keywords?**
- Short-tail ("cars for sale") = massive competition, nearly impossible to rank
- Long-tail ("red cars for sale under £2000 in Leicester") = low competition, easier to rank
- Build on long-tail → eventually rank for short-tail too

---

### 6.43–6.44 — DataForSEO API: Keyword Research

**What is DataForSEO?**
- A cheap, readily available API for all keyword/SEO data
- Provides: keyword volume, difficulty, related keywords, competitor rankings
- Much cheaper than Semrush or Ahrefs for the same data

**Authentication setup:**
```
DataForSEO uses HTTP Basic Auth (username:password encoded in base64)

Step 1: Go to base64encode.org
Step 2: Type: your_email@example.com:your_api_password
Step 3: Click "Encode"
Step 4: Copy the encoded string

In n8n HTTP Request node:
  → Add Header: Authorization
  → Value: Basic <your_base64_encoded_string>
```

**Better approach — use Credential Header:**
```
HTTP Request node
  → Authentication: Generic Credential Type
  → Credential Type: Header Auth
  → Header Name: Authorization
  → Header Value: Basic <base64_string>
```

> This stores your auth credential once and reuses it across all DataForSEO calls — do not paste the base64 string directly into each node.

**4 methods for getting sub-keywords from DataForSEO:**
1. Related keywords (semantic similarity)
2. Keyword suggestions (autocomplete-style)
3. Keyword ideas (broader expansion)
4. Competitor keywords (what rivals rank for)

---

### 6.45–6.46 — Workflow 2: Keyword Research Pipeline

**What it does:** Takes seed keywords → finds long-tail variations → stores in Airtable.

**Flow:**
```
Seed keywords entered in Airtable (per company)
         ↓
n8n Workflow triggered
         ↓
For each seed keyword:
  Loop Over Items
       ↓
  HTTP Request → DataForSEO API
  (4 different keyword methods run)
       ↓
  Aggregate results (Merge node)
       ↓
  Update Airtable Keywords table:
    - subtopics (array of long-tail keywords)
    - subtopics_status = "Complete"
    - match by keyword ID
```

**Why modular architecture matters:**
- One workflow handles ONE company OR multiple companies
- Add a new company row in Airtable → same workflow runs for that company
- If you service multiple clients → same system, different data
- This is how you turn a tool into a product (SaaS model)

---

### 6.47–6.48 — Storing Keywords in Airtable

**The update operation (not create):**
```
Airtable node → Operation: Update
  → Table: Keywords
  → Match by: ID (the keyword row's unique ID)
  → Fields to update:
       subtopics (array from DataForSEO)
       subtopics_status = "Complete"
```

**Why update not create?**
- The keyword rows already exist (seeded from step 1)
- We are enriching existing rows with subtopic data
- Creating new rows would break the link to the company

**Aggregating subtopics:**
```
n8n Merge node (Combine mode)
  → Combines results from all 4 DataForSEO methods
  → Outputs: one array of subtopics per seed keyword
  → Remove duplicates (Set node or Code node)
```

---

### 6.49–6.50 — Workflow Documentation & Research Agent

**Always document inside n8n with sticky notes:**
```
Sticky Note — Input Sheet:
  → Company info from Airtable
  → Subtopic to write about
  → ICP details

Sticky Note — Research Phase:
  → Perplexity searches 3+ research questions
  → Returns: statistics, examples, expert quotes

Sticky Note — Content Phase:
  → Research results pass to Claude/GPT
  → Writes structured long-form article
```

**Workflow 3: Content Research Agent**

What it does: Takes a subtopic → uses Perplexity to gather citations and statistics.

```
Subtopic selected (from Keywords table)
         ↓
Research Agent (AI Agent node)
  └── Tool: Perplexity (sonar-pro model)
            → Query 1: statistics on this topic
            → Query 2: real-world examples
            → Query 3: expert opinions / data
         ↓
Store research in Airtable or pass to next workflow
```

---

### 6.51–6.53 — Workflow 4: Content Planning Agent

**The problem with writing directly from a subtopic:**
- Writing without a plan = disorganised article
- No flow between sections
- Misses important sub-topics

**Two-step approach (plan then write):**
```
Step 1 — PLANNER MODEL (chain-of-thought, reasoning):
  Input: ICP + subtopic + seed keyword
  Task: Create a structured outline with:
    - H1 title (SEO optimised)
    - 5–8 H2 sections
    - Key points per section
    - Where to embed statistics/examples
    - Internal links to suggest

Step 2 — WRITER MODEL (creative, long-form):
  Input: Structured outline + research citations
  Task: Write 1,800+ words following the plan
```

**Prompt engineering for the planning agent:**
```
You are generating a prompt for a blog article planning agent.

Inputs:
- ICP: {icp_description}
- Subtopic: {long_tail_keyword}
- Seed keyword: {seed_keyword}

Instructions:
- Write semantically similar phrases naturally in the content
- Structure with clear H2 sections
- Each section should have 3+ key points
- Include research question prompts per section
- Target word count: 1,800 words
- Reading level: professional but accessible
```

> **Advanced technique:** Use Claude as your prompt GENERATOR. Feed it meta-instructions → it outputs an optimised prompt → use that prompt in your actual workflow.

---

### 6.54–6.55 — Workflow 5: Research Execution

**Running the research agent:**
```
Article plan (6 sections identified)
         ↓
Loop — for each section (6 iterations):
  Perplexity (sonar-pro) called with:
    → Research question for that section
    → Returns: statistics, examples, citations
         ↓
Aggregate all research
(Merge node → combine 6 research outputs)
```

**Reading the Perplexity logs in n8n:**
- Open execution view → drag up the logs panel
- Or: pop out into new window (easier to read)
- Logs show exactly what Perplexity searched and found
- Each research query runs at very low cost

**Example research output for "AI Automation Skills":**
```
Query 1: Latest industry statistics on growth of AI automation
→ Returns: market size figures, growth % data

Query 2: Real-world examples of AI automation
→ Returns: case studies, company names, outcomes

Query 3: Top in-demand skills for AI automation
→ Returns: skill lists, salary data, course recommendations
```

---

### 6.56–6.57 — Writing Model Selection

**Model comparison for long-form content:**

| Model | Cost | Best for | Context window |
|-------|------|---------|----------------|
| GPT-4o | Medium | Long-form, reliable, good general writing | Large |
| GPT-4o mini | Low | Short-form, simple tasks | Medium |
| Claude 3.5 Sonnet | Higher | Superb reasoning + creative writing | Large |
| Claude 3 Haiku | Low | Fast drafts, simple content | Medium |

**Recommended approach:**
- Use GPT-4o or Claude 3.5 Sonnet for the writing step
- Use cheaper models for research/planning steps
- The writing model is where quality matters most → invest the budget there

**First test result (problem discovered):**
```
Expected: 1,800 words
Got:       659 words

Problem: Model underperformed on word count
Reason:  Sections written in isolation — no continuity
```

---

### 6.58 — Solving the Word Count & Quality Problem

**Why sections written in isolation fail:**
```
❌ BAD approach:
  Section 1 → written alone (no context of other sections)
  Section 2 → written alone (might repeat Section 1's research)
  Section 3 → written alone (no flow from previous sections)

Result: Disjointed, repetitive, short
```

```
✅ BETTER approach:
  Plan entire article first (full structure in context window)
          ↓
  Write Section 1 with full article plan visible
          ↓
  Write Section 2 with Section 1 already written (continuity)
          ↓
  Write Section 3 with Sections 1+2 context
          ↓
  Each section flows from the last (like a real writer works)
```

**The writer's mental model:**
- A human writer reads the whole outline before writing anything
- They keep what they've already written in mind as they go
- They avoid repeating themselves
- They build narrative flow paragraph by paragraph

**In n8n terms:**
- Pass the full article plan into context at the START
- Include previously written sections in each subsequent prompt
- Use a Code node or Set node to concatenate all sections at the end

---

### 6.59 — Final Output: Full Blog Article

**What the final article looks like (example: "How to Choose the Right AI Automation Course"):**

```markdown
# How to Choose the Right AI Automation Course for Your Business Needs

## Introduction
[Statistics about AI automation market growth]
[Hook: why businesses are investing in training now]

## What to Look for in an AI Automation Course
- Hands-on project work
- Coverage of real tools (n8n, Make, Zapier)
- Business-focused curriculum

## Top AI Automation Platforms in 2025
| Platform | Best for | Price |
|----------|---------|-------|
| n8n | Complex workflows | Free/self-hosted |
| Make | Visual, beginner-friendly | From $9/month |
| Zapier | Simple automations | From $20/month |

## How to Evaluate Course Quality
[External links to industry sources]
[Checklist format]

## Recommended Learning Path
[Step-by-step from beginner to consultant]

## Conclusion
[Summary + internal links to related articles]
```

**Article quality metrics achieved:**
- ✅ 1,800+ words
- ✅ Multiple H2 and H3 headings
- ✅ External citations (linked to sources)
- ✅ Tables included
- ✅ Bullet-point lists
- ✅ Internal links to related posts
- ✅ Markdown formatted (ready for Webflow/WordPress)

---

### 6.60 — Quality vs OutRank (Conclusion)

**OutRank's own articles show 90–100% AI detection scores.**

This means:
- Even paid $99/month tools produce obviously AI content
- Our own system, with better prompting, can MATCH or BEAT that quality
- The advantage of building your own: you control the prompting, the tone, the style

**Final system overview — 6 workflows:**

```
Workflow 1: ICP Generator
  Input:  Company URL, LinkedIn URL
  Output: Full ICP stored in Airtable

Workflow 2: Keyword Research
  Input:  Seed keywords, company info
  Output: Long-tail keywords + subtopics stored in Airtable

Workflow 3: Subtopic Selection
  Input:  Keyword list from DataForSEO
  Output: Prioritised subtopic for next article

Workflow 4: Content Planning
  Input:  Subtopic, ICP, seed keyword
  Output: Full structured article outline

Workflow 5: Research Execution
  Input:  Article sections from plan
  Output: Cited research per section (via Perplexity)

Workflow 6: Content Writing
  Input:  Outline + research + ICP + brand voice
  Output: 1,800+ word blog article (Markdown format)
```

---

## 🖼️ Visual Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    SEO CONTENT GENERATION SYSTEM                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  USER (Airtable Interface)                                       │
│  ┌──────────────────┐                                           │
│  │ Company Profile   │  → Enter: URL, LinkedIn, competitors     │
│  │ [Generate] button │  → Click button → triggers webhook       │
│  └────────┬─────────┘                                           │
│           │                                                      │
│           ▼                                                      │
│  n8n BACKEND WORKFLOWS                                           │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                                                           │   │
│  │  WF1: ICP Generator                                       │   │
│  │  Website URL → AI Agent + Perplexity → ICP Profile       │   │
│  │                                                           │   │
│  │  WF2: Keyword Research                                    │   │
│  │  Seed keywords → DataForSEO API (4 methods) → Subtopics  │   │
│  │                                                           │   │
│  │  WF3: Subtopic Selection                                  │   │
│  │  All subtopics → Select next unwritten keyword            │   │
│  │                                                           │   │
│  │  WF4: Content Planner                                     │   │
│  │  Subtopic + ICP → GPT/Claude → Structured outline        │   │
│  │                                                           │   │
│  │  WF5: Research Agent                                      │   │
│  │  Outline sections → Perplexity → Citations + stats       │   │
│  │                                                           │   │
│  │  WF6: Content Writer                                      │   │
│  │  Outline + Research → Claude 3.5 Sonnet → Blog article   │   │
│  │                                                           │   │
│  └──────────────────────────────────────────────────────────┘   │
│           │                                                      │
│           ▼                                                      │
│  AIRTABLE DATABASE                                               │
│  ┌────────────┐  ┌──────────────┐  ┌────────────────────┐      │
│  │  Company   │  │   Keywords   │  │   Blog Content     │      │
│  │  (ICP info)│  │ (keyword DB) │  │ (articles + status)│      │
│  └────────────┘  └──────────────┘  └────────────────────┘      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔑 Key Concepts to Remember

| Concept | Explanation |
|---------|-------------|
| Reverse engineering a SaaS | Identify inputs, outputs, and processing steps — then build those as workflows |
| Long-tail keyword | A specific, low-competition search phrase (e.g. "best n8n automation for small business UK") |
| Short-tail keyword | A broad, high-competition term (e.g. "automation software") |
| Topic cluster | Hub article (broad keyword) + spoke articles (long-tail keywords) all internally linked |
| DataForSEO | Cheap API for keyword volume, difficulty, related keywords, competitor analysis |
| Base64 auth | Username:password encoded in base64 for HTTP Basic Authentication |
| ICP | Ideal Customer Profile — who your target customer is, their pain points, goals, and current tools |
| Perplexity sonar-pro | AI search tool with citations — ideal for research agent tasks |
| Chain-of-thought planning | Using a reasoning model to plan BEFORE using a writing model to create |
| Airtable Interface | Visual front-end built on top of Airtable data — no code required |
| V1 → V2 migration | Airtable database → Supabase (for user auth + row-level security) |

---

## 🛠️ Tools & APIs Used

| Tool | Purpose | Cost |
|------|---------|------|
| Airtable | Database + front-end interface (V1) | Free tier available |
| DataForSEO | Keyword research API | Pay per request (very cheap) |
| Perplexity (sonar-pro) | Web research with citations | Per query |
| OpenAI GPT-4o | Content writing | Per 1K tokens |
| Claude 3.5 Sonnet | Premium content writing | Per 1K tokens |
| n8n | Workflow orchestration | Free (self-hosted) |

---

## 📋 Projects Completed in Section 6

| # | Project | Status | Description |
|---|---------|--------|-------------|
| 12 | SEO Content Generation System | ✅ Built | Full 6-workflow system: ICP → Keywords → Research → Planning → Writing → Storage |

---

## 🧠 Recall Test (answer without looking)

1. What percentage of Google searchers never go past Page 1?
2. What does DataForSEO provide and how do you authenticate with it?
3. Explain a topic cluster — what is a hub article vs a spoke article?
4. Why should you use a PLANNING model before a WRITING model?
5. What is the difference between a seed keyword and a long-tail keyword?
6. What does ICP stand for and what 5 fields does the ICP Generator produce?
7. Why is it better to UPDATE a Keywords table row rather than CREATE a new one?
8. What was the first test result for word count and why did it underperform?
9. How do you trigger an n8n workflow from an Airtable button click?
10. What is the V1 → V2 migration plan for this SEO system?

---

## 📌 Key Takeaways

- **SaaS tools are just workflows** — any SaaS product can be reverse-engineered into automation workflows
- **Plan before you build** — sticky notes in n8n save hours of confusion later
- **Long-tail keywords are easier to rank for** — start narrow, build up to broad keywords
- **Use the right model for the right job** — reasoning model for planning, creative model for writing
- **Quality > quantity** — one well-structured article with citations beats 10 keyword-stuffed articles
- **Build modular** — one system that works for multiple companies is more valuable than a one-off tool
