# n8n Day 02 — The 13 Core Nodes & Execution Essentials
**Date:** 08 September 2026 | **Course:** n8n Masterclass | **Section:** 2 (Lectures 2.7–2.8)
**Category:** 🟣 AI Automation

---

## What You Learned Today

Section 2 introduced the **80/20 rule of n8n** — master just 13 nodes and you can build 80% of all real-world automations. The instructor has built 150+ client automations using only these 13 nodes.

---

## Part 1 — Execution Essentials (Conventions You Must Know)

Before building complex workflows, you need to understand how n8n runs them.

### 1. Flow Direction: Left → Right, Top → Bottom

```
[Trigger] → [Node A] → [Node B] → [Node C]
```

Workflows always run left to right. When two branches split from the same node, **the top branch always runs first** — then the bottom branch.

```
                   ┌→ [Branch A — runs FIRST]
[Trigger] → [Node]─┤
                   └→ [Branch B — runs SECOND]
```

### 2. Sequential Execution (NOT Parallel)

n8n executes nodes one after another — **not at the same time**. If Branch A takes 10 seconds, Branch B waits until it's done.

> This is called **synchronous execution**. Important for debugging — if something fails, everything after it stops.

### 3. Nodes Run Once Per Input

If 5 items (rows) enter a node, the node runs **5 times** — once for each item.

**Example:**
- You have a list of 5 leads in an array
- You use **Split Out** to turn the array into 5 individual items
- The next node (e.g. IF, Send Email) runs **5 times** — once per lead

```
[Array: 5 leads] → [Split Out] → [IF node runs ×5] → [Email node runs ×5]
```

### 4. Branching with IF Nodes

You can split a workflow into two paths based on a condition:

```
[Data] → [IF: interestLevel = "High"] → TRUE path → [Add to CRM]
                                       → FALSE path → [Add to Newsletter]
```

### 5. Active vs Inactive

- **Inactive** = workflow only runs when you manually click "Execute" (for testing)
- **Active** = workflow runs automatically based on its trigger (Schedule, Webhook, App Event)

> You can only activate a workflow that has a non-manual trigger. Always test first, then activate.

---

## Part 2 — The 13 Core Nodes

Grouped into 5 categories:

### Category 1: Triggers (3 nodes)

| Node | What It Does | When to Use |
|------|-------------|-------------|
| **Manual Trigger** | Start workflow by clicking a button | Testing and development |
| **Schedule Trigger** (Cron) | Run at set times — every day at 9am, every Monday, etc. | Daily reports, reminders, recurring tasks |
| **Webhook** | Triggered by an external system sending data to your URL | Form submissions, Stripe payments, Typeform responses |

**Real example — Schedule Trigger:**
```
Every day at 9am → Send me an email with today's date
```

**Real example — Webhook:**
```
Customer fills in contact form → Data POSTs to n8n URL → Create CRM record → Send welcome email
```

---

### Category 2: Data Processing (5 nodes)

| Node | What It Does | Real Use |
|------|-------------|---------|
| **Split Out** | Flattens an array into individual items | Turn a list of 5 leads into 5 separate rows |
| **Aggregate** | Merges individual items back into one array | Collect results from 5 runs → one combined list |
| **Set / Edit Fields** | Create, rename, or modify data fields | Combine firstName + lastName into "full name" |
| **IF** | Branch the workflow based on a condition | If interestLevel = High → go to CRM. If not → go to newsletter |
| **Code** | Write custom JavaScript for complex transformations | Remove commas from names, calculate values, format strings |

**Split Out example:**
```json
Input:  { "leads": [ {"name": "Sarah"}, {"name": "Mike"}, {"name": "Emma"} ] }
         ↓  Split Out (field: "leads")
Output: Item 1: {"name": "Sarah"}
        Item 2: {"name": "Mike"}
        Item 3: {"name": "Emma"}
```

**Set/Edit Fields example:**
```
Input:  { firstName: "Sarah", lastName: "Johnson" }
Set node creates: full name = "{{ $json.firstName }}, {{ $json.lastName }}"
Output: { firstName: "Sarah", lastName: "Johnson", "full name": "Sarah, Johnson" }
```

**Code node example (JavaScript):**
```javascript
// Fix formatting — remove comma from "Sarah, Johnson" → "Sarah Johnson"
for (const item of $input.all()) {
  item.json["full name NEW"] = item.json["full name"].replace(/,\s*/g, " ").trim();
}
return $input.all();
```

---

### Category 3: Connectivity & APIs (2 nodes)

| Node | What It Does | Real Use |
|------|-------------|---------|
| **HTTP Request** | Connect to ANY external API — GET, POST, with authentication | Pull product data, send data to any service with an API |
| **Webhook Response** | Send a response back after processing | When a form submits, send back "Thank you" confirmation |

**HTTP Request example:**
```
GET https://dummyjson.com/products
→ Returns list of products as JSON
→ You can then process, filter, store those products
```

> The HTTP Request node is your **Swiss Army knife** — if an app doesn't have a native n8n node, you can connect to it via its API using HTTP Request.

---

### Category 4: Storage (2 nodes)

| Node | What It Does | Real Use |
|------|-------------|---------|
| **Google Sheets** | Read from or write to a Google Sheet | Store leads, log results, update a tracker |
| **Database nodes** | Connect to Airtable, Notion, MySQL, etc. | More structured data storage |

**Google Sheets example:**
```
[Webhook — new enquiry] → [Set Fields] → [Google Sheets — Append Row]
→ Every enquiry automatically adds a row to your client spreadsheet
```

---

### Category 5: AI Integration (2 nodes)

| Node | What It Does | When to Use |
|------|-------------|-------------|
| **Basic LLM Chain** | Send a prompt to an AI model and get a response | When you need AI judgement (not pure IF/ELSE logic) |
| **AI Agent** | An LLM with memory, tools, and the ability to plan | Complex multi-step tasks: research + write + save + email |

**The key distinction:**

> **IF node** = deterministic logic. Use when the rule is clear: "if invoice > £1,000, send to approval"
>
> **Basic LLM Chain** = AI judgement. Use when the rule is fuzzy: "if customer email suggests they might cancel, flag for retention"
>
> **AI Agent** = AI with tools. Use when you need the AI to take multiple actions autonomously: "research this company, summarise it, and add it to my CRM"

**Basic LLM Chain example:**
```
Input: "Your product is too expensive and support is terrible"
Prompt: "Determine if this message is positive or negative. Return sentiment + reasoning."
Output: "Negative — customer mentions price concern and support dissatisfaction"
```

---

## Summary Diagram — The 13 Nodes

```
TRIGGERS          DATA PROCESSING        CONNECTIVITY      STORAGE         AI
──────────        ───────────────        ────────────      ───────         ──
Manual            Split Out              HTTP Request      Google Sheets   Basic LLM Chain
Schedule (Cron)   Aggregate              Webhook Response  Database nodes  AI Agent
Webhook           Set / Edit Fields
                  IF
                  Code
```

---

## Key Expressions from Today

```
{{ $json.firstName }}              → Get a field value from current item
{{ $json["full name"] }}           → Get field with space in name
{{ $input.all() }}                 → All items in the current node (used in Code node)
item.json["new field"] = "value"   → Create a new field in Code node
```

---

## Business Value — What You Can Build With These 13 Nodes

| Business Problem | Nodes Used |
|-----------------|-----------|
| Daily sales report emailed at 9am | Schedule Trigger → Google Sheets → Code → Gmail |
| New enquiry → auto-add to CRM | Webhook → Set Fields → HTTP Request (CRM API) |
| Filter leads by interest level | Split Out → IF → Google Sheets (High) / Email (Low) |
| AI sentiment check on support emails | Webhook → Basic LLM Chain → IF → Alert or Archive |
| Pull products from store → format → save | HTTP Request → Split Out → Set Fields → Google Sheets |

---

## Workflow JSON — 80/20 Node Reference

The course provided a workflow JSON (`80+_+20.json`) demonstrating all 13 nodes with real lead data. Import it into n8n to study each node in context.

**To import:** In n8n → top right menu → Import from file → select `80+_+20.json`

