# n8n Day 03 — Workflow Planning, AI Fundamentals & LinkedIn Content System

**Date:** 12 September 2026
**Course Sections:** 3 (3.14–3.18), 4 (4.19–4.29), 5 (5.30)
**Total Lectures Today:** 17 | **Running Total:** 30 / 76

---

## Section 3 — Workflow Planning & AI Fundamentals

### 3.14 — AI Fundamentals: LLMs, Tokens & Models

#### What is an LLM?
A **Large Language Model (LLM)** is an AI trained on massive datasets that predicts the next most likely word in a sequence. Companies like OpenAI, Anthropic, and Google host these models.

Popular models:
- **GPT-4o** — better at logical thinking
- **Claude 3.5 Sonnet** — better at English writing
- **Gemini 1.5 Pro** — strong general model, some free tier

Each model specialises in different areas. The model is what n8n connects to when you use an AI node.

#### What are Tokens?
- Tokens are the unit of cost for LLMs (not exactly characters, but roughly words/word-parts)
- **Input tokens** = the prompt you send
- **Output tokens** = the response you get back
- Both are charged when using the API (not the subscription chat interface)
- Models are cheap right now — thousands of tokens cost very little

> **Practical tip:** More concise, specific prompts = fewer tokens = lower cost + better results. This is prompt engineering.

#### Zero-Shot Prompting
When you type a message into ChatGPT or Claude directly, you are doing **zero-shot prompting**:
- One input → one output
- No tool access, no back-and-forth loops
- This is what the **Basic LLM Chain** node in n8n replicates

---

### 3.14 (continued) — MCP: Model Context Protocol

**MCP (Model Context Protocol)** is a unified standard for AI to interact with external tools. Think of it as **USB-C for AI** — one standard interface for everything.

**Three components:**
1. **MCP Client** — the AI interface (Claude, ChatGPT)
2. **MCP Server** — the middleman that standardises inputs/outputs
3. **MCP Tools** — the external services (Gmail, Slack, Shopify, Notion, Google Calendar)

**Why it matters:** Without MCP, you'd need to read different documentation for every tool (Gmail API, Shopify API, etc.). MCP unifies all of that so AI can interact with any tool through one standard protocol.

---

### 3.14 (continued) — AI Agents vs LLMs

| | LLM (Zero-shot) | AI Agent |
|--|----------------|----------|
| **Interaction** | One input → one output | Iterative, multi-step |
| **Tools** | None | Has access to tools (Gmail, Shopify, Notion, etc.) |
| **Goal** | Answer a question | Complete a task |
| **Decision making** | Follows prompt | Thinks through steps autonomously |

**In n8n:**
- **Basic LLM Chain** = LLM behaviour (prompt → formatted response, no tools)
- **AI Agent node** = Agent behaviour (prompt + tools + iterative reasoning)

**LLM Chain example:** Gmail trigger → Basic LLM Chain → structured output
**AI Agent example:** Broad query → AI Agent with Gmail + Shopify + Notion tools → autonomous task completion

---

### 3.15 — Workflow Planning: Sticky Notes & Mapping

**Golden rule:** Always plan before you build. Lay out the workflow on canvas using sticky notes FIRST, then add nodes.

**Sticky notes in n8n:**
- Shortcut: `Shift + S` or click the sticky note icon
- Written in **Markdown format** — `##` for heading, `**bold**`, `[link text](url)` for links
- Use consistent colour coding (e.g. purple = info, white = workflow stage)

**Planning methodology:**
1. Start with the **end goal** — what problem are you solving?
2. Identify the **trigger** (what starts the workflow?)
3. Identify **inputs** (what data comes in?)
4. Map **data transformations** (what happens to the data?)
5. Identify **outputs** (where does data end up?)
6. Break into the **smallest possible steps** — assume one step per node

---

### 3.16–3.17 — Planning Project: CV Processing Workflow

**Business problem:** A recruitment company receives CVs as both PDFs and image files (photos of CVs). They need all CV data extracted and saved to their HubSpot CRM with consistent formatting.

**Workflow plan (drawn with sticky notes first):**

```
CV Input (PDF or image)
    ↓
Which format? (IF node)
    ↓ TRUE (PDF)          ↓ FALSE (Image)
Extract from File       Mistral OCR
(PDF → text)            (image → text)
    ↓                       ↓
        Basic LLM Chain
   (extract name, email, city)
            ↓
       Edit Fields
   (standardise data format)
            ↓
  HubSpot: Create or Update Contact
```

**Key nodes used:**
- **Form Trigger** OR **Google Drive Trigger** — dual inputs supported
- **Google Drive (Download file)** — download the file from Drive
- **IF node** — route based on file type (PDF vs image)
- **Extract from File** — converts PDF binary to text
- **Mistral AI node (OCR)** — optical character recognition for images ($1 per 1,000 pages)
- **Basic LLM Chain** — extracts structured data (name, email, city) from raw text
- **Edit Fields (Set node)** — standardises output format
- **HubSpot** — creates/updates contact record

**Why OCR?** You can't process a raw image directly. OCR converts image → text so the LLM Chain can then extract the data fields.

---

### 3.18 — AI Fundamentals Summary

The 80% you need to know:
- LLMs predict the next word in a sequence — input tokens + output tokens = cost
- Zero-shot = basic prompt/response. AI Agent = tools + iteration + goal
- MCP = USB-C for AI tools — standardised protocol for connecting AI to external services
- LLM Chain in n8n = formatted AI output with no tool access
- AI Agent in n8n = access to tools, iterative reasoning, broader goals

---

## Section 4 — AI Automation for Social Media: LinkedIn Content System

**Project 10: Build a production-ready LinkedIn content system that:**
- Generates a week of posts in minutes (in your brand voice)
- Gives you full editorial control (review before posting)
- Automatically schedules and posts approved content
- Turns ~5 hours/week into 15 minutes of review

### Architecture: Two Workflows

**Workflow 1 — Content Generator (runs at 8am daily)**
```
Google Sheets Trigger (new row with topic)
    ↓
Filter: Topic not blank AND status = "Not Started"
    ↓
Loop Over Items (process one at a time)
    ↓
Get Brand Guidelines (from Google Sheets "Brand" tab)
    ↓
Basic LLM Chain (write LinkedIn post using topic + brand voice)
+ Structured Output Parser (output as { content: "..." })
    ↓
OpenAI DALL-E 3 (generate matching image)
    ↓
HTTP Request → imgBB (host image, get URL)
    ↓
Google Sheets: Append/Update Row
(write content, image URL, date_created, status = "Draft")
```

**Workflow 2 — Publisher (runs at 9am daily)**
```
Schedule Trigger (daily 9am)
    ↓
Google Sheets: Get All Posts
    ↓
IF node: status = "Approved" AND date_scheduled = today?
    ↓ TRUE                          ↓ FALSE
UploadPost node                  No further action
(post to LinkedIn)
    ↓
Google Sheets: Update Row
(status = "Posted")
```

---

### 4.19 — Google Sheets Setup

**Content Calendar tab columns:**
| Column | Purpose |
|--------|---------|
| id | Unique row identifier (1, 2, 3...) |
| topic | The LinkedIn topic to write about |
| date_created | Auto-filled when post is generated |
| date_scheduled | Manually set when you want to post |
| content | AI-generated post (auto-filled) |
| edited_post | Your edited version (manual) |
| approved | Checkbox — tick when ready to publish |
| status | Not Started → Draft → Approved → Posted |

**Brand tab:** Contains your writing style guidelines — how you write, your tone, what to avoid, examples. This gets pulled into every AI prompt so posts sound like you.

---

### 4.20 — Connecting Google Sheets in n8n

- Use **Google Sheets Trigger** — set to check for new rows
- Connect using OAuth2 Google credential
- Reference the sheet by URL (paste the Google Sheets URL directly)
- Name credentials with the email address for easy identification later

---

### 4.21 — Planning Both Workflows

Key planning insight: **sketch both workflows on the n8n canvas with sticky notes before touching a single node**. Know your inputs, transformations, and outputs before you build.

Workflow 1 inputs: topic (from Sheets), brand guidelines (from Sheets)
Workflow 1 outputs: generated post + image URL (back to Sheets)

Workflow 2 inputs: all posts from Sheets
Workflow 2 outputs: posted to LinkedIn + status updated to "Posted"

---

### 4.22 — Pulling Brand Guidelines

- Add a **Google Sheets (Get Row)** node — not a trigger this time
- Connect to the "Brand" tab URL
- This runs alongside the topic trigger — both execute to give the AI all context it needs
- Best practice: name nodes clearly (e.g. "GetTopic", "GetBrandGuide")

---

### 4.23 — Setting Up the Output (Append/Update Row)

- Copy the Get Row node → change operation to **Append or Update Row**
- Match rows by the **id column** (unique identifier)
- Map these fields back to the sheet:
  - `id` → `={{ $('GetTopic').item.json.id }}`
  - `Date Created` → `={{ $now.format('yyyy-MM-dd') }}`
  - `Status` → `"Draft"`
  - `Content` → (mapped after AI node is built)
  - `Image` → (mapped after image node is built)

---

### 4.24 — Building the AI Stage (Basic LLM Chain)

**Node setup:**
- Add **Basic LLM Chain** node
- Set prompt as expression — pulls topic and brand guidelines dynamically:
  ```
  Write a LinkedIn post, max 150 characters, on the following topic:
  {{ $('GetTopic').item.json.Topic }}
  
  Using the following brand guidelines:
  {{ $('GetBrandGuide').item.json.guidelines }}
  ```
- Enable **Structured Output Parser** — specify JSON format: `{ "content": "linkedin post here" }`
- This guarantees predictable output field naming every time
- Connect to a model via **OpenRouter** (unified API for GPT-4, Claude, Gemini, etc.)
  - Free option: Gemini 2.0 Flash Experimental (free tier)
  - Paid fallback: GPT-4o-mini (very cheap)

**OpenRouter:** Sign up, create API key, add credits. One API key for all LLMs. Compare token prices on their model page.

---

### 4.25 — Filter + Loop for Processing

**Filter node** (placed BEFORE the loop):
- Only process rows where topic is NOT empty
- Only process rows where status = "Not Started" (prevents overwriting draft posts)

**Loop Over Items node:**
- Processes one row at a time
- Prevents rate limit errors on free model tiers
- Loop back connects to end of flow so every topic gets processed

**Flow order:**
```
Trigger → Filter (not blank, not started) → Loop → Get Brand Guide → LLM Chain → Output → [loop back]
```

---

### 4.26 — Image Generation with DALL-E 3

- Add **OpenAI node** → operation: **Generate Image**
- Model: **DALL-E 3** (requires OpenAI API key with credits — ~$0.04/image)
- Free first 100 credits available
- Prompt: dynamically reference the generated post content
- Add tip: specify "no text in image" to avoid AI-generated text watermarks

**Upload to imgBB (free image hosting):**
- Use **HTTP Request node**
- Method: POST to `https://api.imgbb.com/1/upload`
- Send as form-data with field name `image`, value = binary file
- Response includes `data.url` — the hosted image URL to store in Google Sheets

---

### 4.27 — Uploading Image & Completing Workflow 1

- After imgBB returns the URL, map `data.url` into the Google Sheets output node
- Map `{{ $('Basic LLM Chain').item.json.output.content }}` into the Content column
- Run full flow end-to-end to verify both topics process correctly
- Result: Google Sheets now shows generated content + hosted image URL for each topic

---

### 4.28 — Building Workflow 2: The Publisher

**Schedule Trigger:** Set to daily at 9am (gives 1 hour between generation at 8am and publishing at 9am for manual review)

**Get Posts node:** Google Sheets (Get All Rows) — pulls entire content calendar

**IF node conditions (both must be TRUE):**
1. `status` equals `"Approved"`
2. `date_scheduled` equals `{{ $now.format('dd/MM/yyyy') }}` (today's date as string)

**True branch:** Post to LinkedIn
**False branch:** No Operation (do nothing placeholder)

---

### 4.28–4.29 — Posting to LinkedIn via UploadPost

**Why not the native LinkedIn node?** LinkedIn's API requires a developer account approval process that takes time. UploadPost is a certified community node that's pre-approved and simpler.

**UploadPost setup:**
1. Go to uploadpost.com → sign up → connect LinkedIn
2. Generate API key → paste into n8n credential
3. Get your user identifier from UploadPost "Manage Users"

**UploadPost node settings:**
- Operation: Upload Photos (to include image) or Upload Text (text only)
- User identifier: your UploadPost profile name
- Main content: `{{ $json['edited_post'] || $json['content'] }}`
- Photo URL: `{{ $json['image'] }}` (the imgBB URL)
- LinkedIn visibility: choose connections or public

**After posting — update the sheet:**
- Add Google Sheets (Append/Update Row) node after UploadPost
- Match by id, update Status to `"Posted"`
- This prevents the same post from being published multiple times

**Final result:** Active workflow runs every morning, auto-posts approved content and marks it as posted.

---

### 4.29 — Advanced Prompt Engineering & 0% AI Detection

**Two-step prompt to get your brand voice into the LLM Chain:**

**Step 1 — Generate your tone of voice brief (use in Claude/ChatGPT):**
> "Use this guide to walk me through a series of questions and output a detailed brief on my tone of voice for different platforms. Make sure the output has lots of examples as I'm going to create a prompt on this later in order to always write copy in my tone of voice."

**Step 2 — Convert to two documents:**
> "Turn this into two documents for me. Use markdown formatting, return each in a code block: 1) a complete tone of voice brief containing examples — reference different social platforms 2) tone of voice examples."

**Claude Project / Custom GPT system prompt (paste into n8n LLM Chain prompt):**
```
Write copy, as requested and:
- Don't explain why you've written a certain way, just write the output options
- Always output 3 options
- Always refer to my Tone of Voice Brief and Tone of Voice Examples
- Write in a collaborative, practical tone that breaks down complex topics into simple solutions
- Use everyday language instead of technical jargon, focus on business value over features
- Include 'we' language, brief relevant examples, and step-by-step clarity
- Target no-nonsense professionals who value efficiency
- Sound like someone explaining a practical solution to a colleague over coffee
```

---

## Section 5 — Learn Style & Refinement: Getting AI to Write Like You

### 5.30 — Creating Your Personal Tone of Voice Brief

This is the most important exercise in the entire course. Creating a tone of voice brief transforms AI output from "obviously AI-written" to "sounds like me."

**What you end up with:**
1. **Tone of Voice Brief** — comprehensive guidelines on how you write (language patterns, structures, dos/don'ts per platform)
2. **Tone of Voice Examples** — sample posts, emails, and other content in your voice that AI can reference

**How to build it:**

1. Download the **Personal Tone of Voice Playbook** (from course resources)
2. Upload it to Claude or ChatGPT
3. Use prompt from Section 4.29 Step 1 — AI will ask you personalised questions:
   - "What annoys you most about how business is typically done?"
   - "When you picture your dream client, what's their biggest pain point?"
   - "Do you use 'we/us' or 'you/I'? Questions or statements? Technical terms or everyday language?"
4. Answer honestly. Include 2–3 creator examples whose style you admire
5. Use Step 2 prompt to generate the two documents
6. Save both as files in a **Claude Project** (or custom GPT knowledge base)

**Using it daily:**
- Open your copywriting Claude Project
- Ask: "Write me a LinkedIn post on [topic]"
- AI always references your tone brief + examples → consistent brand voice
- Every output is ~80% there — just review and tweak

**Key insight:** Your authentic voice is your competitive advantage. No one else can replicate who you actually are. AI can't write like you without this brief.

---

## Projects Built / Planned Today

| # | Project | Status | Description |
|---|---------|--------|-------------|
| 9 | CV Processing Workflow | Planned | PDF + image CV extraction → HubSpot CRM |
| 10 | LinkedIn Content System | Built | Full 2-workflow system: generate → review → auto-post |
| 11 | Personal Tone of Voice Brief | Built | AI copywriting identity document for brand-consistent posts |

---

## Key Takeaways

- **Plan before you build** — sticky notes on canvas save hours of rebuilding
- **LLM Chain vs AI Agent** — know which tool for which job
- **Structured output parser** — always specify output format for predictable data
- **OpenRouter** — single API key for all LLMs (GPT, Claude, Gemini)
- **Filter + Loop** — essential combo for processing spreadsheet rows reliably
- **UploadPost** — easier LinkedIn API than native LinkedIn node
- **Two workflows** — generate (8am) + publish (9am) with manual review window
- **Tone of voice brief** — most impactful thing you can build for AI-assisted writing

---

## Recall Test

1. What are input vs output tokens, and when do you pay for them?
2. What is the difference between an LLM and an AI Agent in n8n?
3. What is MCP, and what analogy is used to describe it?
4. What is zero-shot prompting?
5. Why do you filter for "not blank" AND "status = Not Started" before the loop?
6. What does the Structured Output Parser do, and why use it?
7. What is OCR, and which service was used for it?
8. What is the role of OpenRouter?
9. Why are there two separate workflows for the LinkedIn system?
10. What are the two documents you produce from the Tone of Voice Playbook exercise?

*(Answers: all covered above — review if any blanks)*
