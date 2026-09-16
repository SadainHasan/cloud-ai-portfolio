# n8n Node Masterclass — Complete Reference Guide
**Date:** 16 Sep 2026 | **Course:** n8n Masterclass | **Hasan's Study Reference**
**Purpose:** Master 30 nodes that cover 95%+ of all real-world automations

> **How to use this document:** Read once end-to-end to build mental models, then use as a lookup reference. Each node has: what it does → visual diagram → key settings → real example → when to use → tips & tricks.

---

## Table of Contents

| # | Node | Category | Page |
|---|------|----------|------|
| 1 | Manual Trigger | Trigger | §1.1 |
| 2 | Schedule Trigger | Trigger | §1.2 |
| 3 | Webhook | Trigger | §1.3 |
| 4 | Error Trigger | Trigger | §1.4 |
| 5 | Form Trigger | Trigger | §1.5 |
| 6 | IF | Flow Control | §2.1 |
| 7 | Switch | Flow Control | §2.2 |
| 8 | Merge | Flow Control | §2.3 |
| 9 | Split Out | Flow Control | §2.4 |
| 10 | Split In Batches | Flow Control | §2.5 |
| 11 | Aggregate | Flow Control | §2.6 |
| 12 | Filter | Flow Control | §2.7 |
| 13 | Wait | Flow Control | §2.8 |
| 14 | No Operation | Flow Control | §2.9 |
| 15 | Edit Fields (Set) | Data | §3.1 |
| 16 | Rename Keys | Data | §3.2 |
| 17 | Code | Data | §3.3 |
| 18 | HTTP Request | Integration | §4.1 |
| 19 | Respond to Webhook | Integration | §4.2 |
| 20 | Airtable | Integration | §4.3 |
| 21 | Google Sheets | Integration | §4.4 |
| 22 | Send Email | Integration | §4.5 |
| 23 | Slack | Integration | §4.6 |
| 24 | AI Agent | AI | §5.1 |
| 25 | Basic LM Chain | AI | §5.2 |
| 26 | Chat Model | AI | §5.3 |
| 27 | Structured Output Parser | AI | §5.4 |
| 28 | Tools (Perplexity/Calculator) | AI | §5.5 |
| 29 | Memory (Buffer) | AI | §5.6 |
| 30 | Sticky Note | Utility | §6.1 |
|   | **Node Combination Patterns** | Patterns | §7 |
|   | **When to Use Which Node — Decision Tree** | Reference | §8 |
|   | **Quick Recall Test** | Test | §9 |

---

## The 80/20 Rule of n8n

The instructor has built **150+ client automations**. Here is what he found:

```
╔══════════════════════════════════════════════════════════╗
║  13 nodes  →  covers 80% of all automations             ║
║  30 nodes  →  covers 95%+ of everything you'll ever     ║
║              need as a consultant                        ║
╚══════════════════════════════════════════════════════════╝
```

Do NOT try to learn every n8n node (there are 400+). Master these 30 deeply and you can build anything a client throws at you.

---

## How n8n Executes (Must Know First)

Before learning individual nodes, understand how n8n runs:

```
RULE 1: Left → Right, Top → Bottom
══════════════════════════════════
[Trigger] ──► [Node A] ──► [Node B] ──► [Node C]

RULE 2: Branching — TOP branch always runs FIRST
══════════════════════════════════════════════════
                    ┌──► [Branch A — runs 1st] ──► ...
[Node] ────────────►│
                    └──► [Branch B — runs 2nd] ──► ...

RULE 3: One node runs once per INPUT ITEM
══════════════════════════════════════════
[3 items in] ──► [HTTP Request] = HTTP Request runs 3 TIMES
                                  (once per item)

RULE 4: Sequential — NOT parallel
══════════════════════════════════
Branch A runs → Branch A FINISHES → Branch B starts
(Never at the same time)
```

**Data format — everything is JSON items:**
```json
[
  { "name": "Alice", "email": "alice@test.com" },
  { "name": "Bob",   "email": "bob@test.com"   }
]
```
Every node receives a list of JSON items and outputs a list of JSON items.

---

# SECTION 1 — TRIGGER NODES

> Triggers are the START of every workflow. Without a trigger, nothing runs. You can only have ONE trigger per workflow.

---

## §1.1 Manual Trigger

```
┌─────────────────┐
│  ▶ Manual       │
│    Trigger      │
└────────┬────────┘
         │
         ▼ (only when you click "Execute" in n8n)
```

**What it does:** Starts the workflow when YOU click the "Execute Workflow" button in the n8n editor. Produces a single empty item `{}` as output.

**When to use:**
- During testing and development
- When you want to manually run a workflow on demand
- As a placeholder before replacing with a real trigger

**Key setting:** None — just drop it and connect it.

**⚠️ Important:** When you activate a workflow, the Manual Trigger is IGNORED. Activating only enables Schedule/Webhook/App triggers. Manual trigger only works in the editor.

**💡 Tip:** Use Manual Trigger + "Pin Data" during development. Once you pin the output of a node, n8n uses that pinned data instead of re-running the node — saves API calls and speeds up testing.

---

## §1.2 Schedule Trigger

```
┌──────────────────────────┐
│  🕐 Schedule Trigger      │
│  "Every day at 9:00 AM"  │
└────────────┬─────────────┘
             │ fires at scheduled time
             ▼
         [next node]
```

**What it does:** Runs your workflow automatically at set times. Uses "cron expressions" under the hood (but n8n gives you a friendly UI for it).

**Key settings:**

| Setting | What it controls |
|---------|-----------------|
| **Trigger Interval** | How often: Minutes, Hours, Days, Weeks, Months, Custom Cron |
| **Hour / Minute** | When within the interval |
| **Day of Week** | Monday–Sunday (for weekly triggers) |
| **Timezone** | Always set this! Default is UTC. Set to Europe/London |

**Examples:**

```
Every day at 9 AM London time:
  Interval = Days  |  Hour = 9  |  Minute = 0  |  Timezone = Europe/London

Every Monday at 8 AM:
  Interval = Weeks  |  Day = Monday  |  Hour = 8  |  Minute = 0

Every 30 minutes:
  Interval = Minutes  |  Every = 30
  
First day of every month:
  Custom Cron: 0 9 1 * *
  (minute=0, hour=9, day=1, month=any, weekday=any)
```

**Cron expression format (if you use Custom):**
```
* * * * *
│ │ │ │ │
│ │ │ │ └── Day of week (0=Sun, 1=Mon ... 6=Sat)
│ │ │ └──── Month (1–12)
│ │ └────── Day of month (1–31)
│ └──────── Hour (0–23)
└────────── Minute (0–59)
```

**When to use:**
- Daily/weekly reports sent to Slack or email
- Reminders that fire at a specific time
- Pulling data from a source on a schedule (e.g. check new orders every 30 mins)
- Midnight database syncs

**⚠️ Common mistake:** Forgetting to set the timezone. n8n defaults to UTC — if you're in London (BST = UTC+1), your "9 AM" trigger fires at 10 AM local time during summer.

**💡 Tip:** After saving a Schedule Trigger, look at the right side of the node — n8n shows you exactly WHEN it will fire next. Always check this before activating.

---

## §1.3 Webhook

```
External System                    n8n
     │                              │
     │  POST /webhook/abc123        │
     │  Body: { "name": "Alice" } ──►──► [Webhook Node] ──► [next node]
     │                              │
     │  ◄── Response (200 OK) ──────│
```

**What it does:** Creates a unique URL. When any external system sends data to that URL (via HTTP POST/GET), your workflow wakes up and runs with that data.

**The two webhook URLs:**
```
Test URL:       https://your-n8n.com/webhook-test/abc123
Production URL: https://your-n8n.com/webhook/abc123

IMPORTANT:
- Test URL   → only works when you're in the n8n editor with the workflow open
- Production URL → only works when the workflow is ACTIVE (saved + toggled on)
```

**Key settings:**

| Setting | Options | When to use |
|---------|---------|-------------|
| **HTTP Method** | GET, POST, PUT, DELETE | POST for forms/data. GET for URL-based triggers |
| **Path** | Custom URL path | Make it descriptive: `/new-lead`, `/payment-complete` |
| **Authentication** | None, Basic Auth, Header Auth | Always add auth for production webhooks |
| **Respond** | Immediately / When last node finishes | "Immediately" = fast UX. "Last node" = can send dynamic response |
| **Response Code** | 200, 201, 400 etc. | 200 = success |
| **Response Body** | JSON, text, binary | What gets sent back to the caller |

**Real-world example — Typeform → CRM:**
```
[Typeform Form submitted]
        │
        ▼ POST to your webhook URL
[Webhook Node]
  Method: POST
  Path: /new-lead
        │
        ▼ body.name = "Alice", body.email = "alice@test.com"
[Edit Fields] → format the data
        │
        ▼
[Airtable] → create record in CRM table
        │
        ▼
[Send Email] → welcome email to Alice
```

**When to use:**
- Any time an external app needs to trigger your workflow (Typeform, Stripe, Shopify, WhatsApp, your own website)
- Building APIs (your workflow IS the API endpoint)
- Real-time triggers (something happens NOW → workflow runs NOW)

**When NOT to use:**
- When you need time-based scheduling → use Schedule Trigger instead
- When there's a pre-built n8n integration → use that node instead of HTTP webhooks

**💡 Tips:**
1. Always test with the Test URL first, then switch to Production URL
2. Add header auth (`X-API-Key`) so only authorised systems can trigger your workflow
3. Use "Respond to Webhook" node at the end to send back a proper JSON response
4. Save the webhook URL somewhere — you can't change it without breaking existing integrations

---

## §1.4 Error Trigger

```
NORMAL WORKFLOW:
[Trigger] ──► [Node A] ──► [Node B] ──► FAIL! ◄── Error occurs here
                                           │
                                           │ n8n automatically sends
                                           ▼ error data to:

ERROR HANDLING WORKFLOW:
[Error Trigger] ──► [Format Error Message] ──► [Send Slack Alert]
```

**What it does:** A special trigger that ONLY fires when another workflow in your n8n instance fails. Used to build error monitoring systems.

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **Workflow** | Leave empty = catches errors from ALL workflows |

**Data it provides:**
```json
{
  "execution": {
    "id": "12345",
    "url": "https://your-n8n.com/execution/12345",
    "workflowId": "67",
    "workflowName": "SEO Content Generator",
    "error": {
      "message": "HTTP Request failed: 401 Unauthorized",
      "node": "DataForSEO API"
    }
  }
}
```

**Example error monitoring workflow:**
```
[Error Trigger]
      │
      ▼ has: workflowName, error.message, execution.url
[Edit Fields]
  errorMsg = "🚨 " + workflowName + " failed: " + error.message
  link     = execution.url
      │
      ▼
[Slack] → send to #alerts channel
```

**💡 Tips:**
1. Build this workflow on DAY ONE of any client project — errors in the dark are dangerous
2. Include the execution URL in the Slack message so you can click straight to the failed run
3. This workflow must be ACTIVE to catch errors — don't forget to activate it

---

## §1.5 Form Trigger (n8n Forms)

```
                    n8n generates a form page:
                    ┌────────────────────────┐
                    │  Your Business Form    │
                    │  Name: [_____________] │
[Form Trigger] ◄────│  Email: [____________] │
                    │  [Submit]              │
                    └────────────────────────┘
```

**What it does:** n8n creates a hosted web form (no coding needed). When someone fills it in and submits, your workflow fires with their data.

**When to use:**
- Quick internal tools for clients (no front-end developer needed)
- Intake forms, request forms, feedback forms
- V1 client-facing interfaces before building a proper front-end

**Limitation:** The form is hosted on your n8n URL — not your client's domain. For branded forms, use Typeform + Webhook instead.

---

# SECTION 2 — FLOW CONTROL NODES

> These nodes control HOW data moves through your workflow — branching, looping, combining, filtering.

---

## §2.1 IF Node (Conditional Branch)

```
                         TRUE path ──► [Do This]
[Data] ──► [IF Condition?]
                         FALSE path ──► [Do That]
```

**What it does:** Tests a condition on each item. If TRUE, item goes right path. If FALSE, item goes left/bottom path. Like an if/else statement in code.

**Key settings:**

| Setting | Example |
|---------|---------|
| **Value 1** | `{{ $json.status }}` — the field to check |
| **Operation** | equals, not equals, contains, greater than, less than, is empty, regex |
| **Value 2** | `"approved"` — what to compare against |

**Operations reference:**
```
Text:     equals | not equals | contains | starts with | ends with | regex | is empty
Number:   equal | not equal | greater than | less than | greater or equal | less or equal
Boolean:  true | false
Date:     after | before | equals
```

**Multi-condition example:**
```
IF: status = "approved" AND score >= 80
  TRUE  ──► Send contract
  FALSE ──► Add to nurture list
```

**Real example — lead routing:**
```
[Webhook: new lead]
      │
      ▼
[IF: lead.budget > 5000]
      │
      ├── TRUE ──► [Notify Sales Director] + [Create Proposal]
      │
      └── FALSE ──► [Add to Newsletter] + [Send Info Pack]
```

**⚠️ Important:** IF node only has TWO outputs — TRUE and FALSE. If you need 3+ paths, use Switch node instead.

**💡 Tips:**
1. You can add multiple conditions with AND/OR logic
2. Case sensitivity matters — `"Active"` ≠ `"active"`. Use `.toLowerCase()` in a Code node first if unsure
3. Checking if a field EXISTS: use "is not empty" on the field
4. The item still flows through BOTH paths — it doesn't get duplicated, each path just gets a copy

---

## §2.2 Switch Node (Multi-Branch)

```
                         ──► [Path 1: UK]
                         ──► [Path 2: US]
[Data] ──► [Switch: country?]
                         ──► [Path 3: EU]
                         ──► [Default: Other]
```

**What it does:** Routes items to one of MANY different paths based on a value. Like a switch/case statement. Can have unlimited output branches.

**When to use instead of IF:**
- 3 or more possible paths
- Routing based on a category/status field
- Different processing for different item types

**Settings:**

| Setting | What it does |
|---------|-------------|
| **Mode** | Rules (each branch has a condition) OR Expression (one expression returns the output number) |
| **Value** | The field to check |
| **Rules** | One per output: "equals X → output 1", "equals Y → output 2" |
| **Fallback Output** | Where unmatched items go (like default case) |

**Real example — support ticket router:**
```
[Webhook: ticket arrives]
      │
      ▼
[Switch: ticket.department]
      │
      ├── "billing"     → [Billing Team Slack]
      ├── "technical"   → [Tech Team Slack] + [Create Jira]
      ├── "sales"       → [Sales CRM]
      └── default       → [General Inbox Email]
```

**💡 Tip:** Switch is better than chaining multiple IF nodes. One Switch with 5 outputs is cleaner than 4 IFs chained together.

---

## §2.3 Merge Node

```
[Branch A: 3 items] ──────────────────────────┐
                                               ▼
                                          [MERGE] ──► [Combined output]
                                               ▲
[Branch B: 3 items] ──────────────────────────┘
```

**What it does:** Combines the outputs of two branches back into one stream. Like a junction — two roads become one.

**Merge Modes (CRITICAL to understand):**

```
MODE 1: Append (most common)
──────────────────────────────
Branch A: [item1, item2]
Branch B: [item3, item4]
Output:   [item1, item2, item3, item4]
→ Just stacks all items together. Order = Branch A first, then Branch B.

MODE 2: Merge By Index
──────────────────────────────
Branch A: [{name: "Alice"}, {name: "Bob"}]
Branch B: [{score: 95},     {score: 70} ]
Output:   [{name:"Alice", score:95}, {name:"Bob", score:70}]
→ Zips items by position. Item 1 from A merges with Item 1 from B.
  Useful when you know both lists have the same length and order.

MODE 3: Merge By Key
──────────────────────────────
Branch A: [{id: "1", name: "Alice"}, {id: "2", name: "Bob"}]
Branch B: [{id: "1", score: 95},     {id: "3", score: 80} ]
Output:   [{id:"1", name:"Alice", score:95}]  ← only matched
→ Like a SQL JOIN. Merges items where a key field matches.
  Items without a match are dropped.

MODE 4: Wait
──────────────────────────────
→ Merge node waits until BOTH branches finish, then passes both to output.
  Branch 1 items → output 1, Branch 2 items → output 2.
  Useful when two parallel processes must both complete before continuing.
```

**Real example — parallel research then combine:**
```
[Webhook]
    │
    ├──► [Research Agent A: competitor data] ──────────┐
    │                                                  ▼
    └──► [Research Agent B: keyword data]  ──► [Merge: Append] ──► [Content Writer]
```

**⚠️ Common mistake:** Merge node waits for BOTH branches to complete. If Branch A finishes instantly but Branch B takes 30 seconds, the Merge waits for Branch B. This is correct behaviour — don't confuse it for a bug.

---

## §2.4 Split Out Node

```
BEFORE Split Out:               AFTER Split Out:
──────────────────              ─────────────────
[                               Item 1: { name: "Alice" }
  { name: "Alice" },     ──►   Item 2: { name: "Bob"   }
  { name: "Bob"   },           Item 3: { name: "Carol" }
  { name: "Carol" }
]
One item (with array)           Three separate items
```

**What it does:** Takes an array INSIDE a JSON field and turns each element into a separate n8n item. The opposite of Aggregate.

**Key setting:**

| Setting | Example |
|---------|---------|
| **Field to Split Out** | `keywords` — the array field inside your JSON |
| **Destination Field** | Where to put each value (optional) |
| **Include other fields** | Keep the parent fields alongside each split item |

**Real example — process each keyword:**
```json
Input item:
{
  "company": "Acme Ltd",
  "keywords": ["ai automation", "n8n tutorial", "workflow builder"]
}
```
```
[Split Out: keywords field]
↓
Item 1: { company: "Acme Ltd", keywords: "ai automation" }
Item 2: { company: "Acme Ltd", keywords: "n8n tutorial" }
Item 3: { company: "Acme Ltd", keywords: "workflow builder" }
```
```
[Split Out] ──► [HTTP Request] runs 3 times, once per keyword
```

**💡 Tips:**
1. After Split Out, the NEXT node runs once PER ITEM automatically — no loop needed
2. Use "Include other fields" to keep parent data (like company name) on every item
3. If your array is nested: `keywords.items` — you can use dot notation

---

## §2.5 Split In Batches (Loop)

```
100 items in
     │
     ▼
[Split In Batches: size=10]
     │
     ├─► Batch 1 (items 1–10)  → [process] → ─────────────────┐
     ├─► Batch 2 (items 11–20) → [process] → ─────────────────┤
     │   ...                                                   │
     └─► Batch 10 (items 91–100)→ [process] → ─────────────────┘
                                                               │
                                                               ▼
                                                      (all done, no more batches)
```

**What it does:** Splits items into smaller groups (batches) and processes them one batch at a time. Used for:
1. Rate limiting (only send 10 API calls at a time to avoid hitting limits)
2. Looping (process items one at a time — batch size = 1)
3. Memory management (processing 10,000 rows in groups of 100)

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **Batch Size** | How many items per batch (1 = one at a time = loop) |
| **Options → Reset** | Start over from item 1 (for re-running) |

**The loop pattern (batch size = 1):**
```
[Split In Batches: size=1]
         │ (loops back to itself until all items done)
         ├──► [Edit Fields: add context]
         │
         ▼
    [AI Content Writer]
         │
         ▼
    [Airtable: update record]
         │
         └──► back to [Split In Batches] for next item
```

**⚠️ CRITICAL difference — Split Out vs Split In Batches:**
```
Split Out:
  → Turns array INTO items
  → Next node automatically processes ALL items
  → No loop back

Split In Batches:
  → Takes existing items and processes them in GROUPS
  → Loops back — the workflow physically circles back to the batch node
  → Used when you need context from previous iterations (like the writing context loop)
```

**💡 Tips:**
1. Batch size 1 = the standard loop for sequential processing with context
2. Add a Wait node inside the loop if you need to respect API rate limits
3. The batch node has two outputs: "loop" output (more items) and "done" output (finished)

---

## §2.6 Aggregate Node

```
BEFORE Aggregate:               AFTER Aggregate:
─────────────────               ────────────────
Item 1: { name: "Alice" }       [
Item 2: { name: "Bob"   }  ──►    { name: "Alice" },
Item 3: { name: "Carol" }         { name: "Bob" },
                                  { name: "Carol" }
Three separate items            ]
                                One item (with array)
```

**What it does:** The OPPOSITE of Split Out. Combines many separate items back into one item containing an array. Used before Airtable/Sheets writes where you want to create multiple records at once.

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **Aggregate** | All Item Data (into array) / Individual Fields |
| **Put Output in Field** | Name of the array field in the output |

**When to use:**
- After Split Out + processing, to recombine before writing to database
- When you need ALL results in one place to pass to next step
- After a loop — collect all loop outputs into one array

**Real example — subtopics generator:**
```
[DataForSEO: subtopics endpoint]
         │  (returns 12 items, one per subtopic)
         ▼
[Aggregate: all item data → "subtopics" field]
         │  (now ONE item with array of 12 subtopics)
         ▼
[Airtable: create 12 records at once]
```

**💡 Tip:** Aggregate is your "collect all results" node. Any time you've processed multiple items and need to pass everything to the NEXT step as one chunk, use Aggregate.

---

## §2.7 Filter Node

```
[5 items: Alice(hot), Bob(cold), Carol(warm), Dave(hot), Eve(cold)]
      │
      ▼
[Filter: interestLevel = "hot"]
      │
      ▼
[2 items: Alice(hot), Dave(hot)]   ← cold/warm items DROPPED
```

**What it does:** Removes items that don't match a condition. Items that PASS go through. Items that FAIL are dropped completely (not sent to another path — just gone).

**vs IF node:**
```
IF node:   2 outputs (true path + false path) — BOTH groups continue
Filter:    1 output (matching items only) — non-matching items are REMOVED
```

**When to use Filter vs IF:**
- Use **Filter** when you only care about the matching items and want to discard the rest
- Use **IF** when you need to do DIFFERENT things to the matching vs non-matching items

**Example — only process high-priority tickets:**
```
[Webhook: all support tickets]
      │
      ▼
[Filter: priority = "high"]
      │ (medium + low tickets are gone)
      ▼
[Slack: alert support team]
```

---

## §2.8 Wait Node

```
[Node A] ──► [Wait: 30 minutes] ──► [Node B runs 30 min later]

OR

[Send Email] ──► [Wait: until webhook receives response] ──► [Process response]
```

**What it does:** Pauses the workflow execution for a set time, OR waits until a specific event happens (like a webhook response). The workflow is SUSPENDED — it doesn't use resources while waiting.

**Wait modes:**

| Mode | What it does |
|------|-------------|
| **Time Interval** | Wait X minutes/hours/days |
| **Specific Date/Time** | Wait until a specific timestamp |
| **Webhook** | Suspend and wait until a specific webhook URL is called |

**When to use:**
- Sending a follow-up email 24 hours after first contact
- Pausing between API calls to respect rate limits
- Building human-in-the-loop workflows (wait for human approval before continuing)
- Checking if something happened before proceeding

**Real example — follow-up sequence:**
```
[Lead form submitted]
        │
        ▼
[Send welcome email]
        │
        ▼
[Wait: 3 days]
        │
        ▼
[IF: has_replied = false?]
        │
        ├── TRUE ──► [Send follow-up email]
        └── FALSE ──► [No action needed]
```

**💡 Tip:** Wait node is KEY for building automated sequences without coding timers. The workflow literally "sleeps" and wakes up at the right time — your server doesn't need to do anything in between.

---

## §2.9 No Operation (No Op)

```
[IF: condition]
      ├── TRUE ──► [Send Email]
      └── FALSE ──► [No Op] ← does nothing, just ends the branch
```

**What it does:** Does absolutely nothing. Just passes items through unchanged. Like a blank `else {}` in code.

**When to use:**
- As a placeholder for a branch you haven't built yet
- To "close" a branch cleanly without leaving dangling connections
- During testing — connect to No Op to see what items arrive there

**💡 Tip:** When you're building a workflow and know one branch needs work later, connect it to a No Op with a Sticky Note explaining what should go there. Makes your workflow cleaner and easier to revisit.

---

# SECTION 3 — DATA MANIPULATION NODES

> These nodes transform and reshape your data without calling external services.

---

## §3.1 Edit Fields Node (previously "Set" Node)

```
INPUT item:                          OUTPUT item:
{                                    {
  "first_name": "Alice",              "full_name": "Alice Smith",
  "last_name": "Smith",     ──►       "email": "alice@test.com",
  "email": "alice@test.com",          "lead_score": 85
  "phone": "07700900001",             (phone removed)
  "raw_score": "85"                 }
}
```

**What it does:** Add, remove, or transform fields on your items. The most frequently used node in n8n. You'll use this in almost every workflow.

**Three modes:**

```
MODE 1: Manual Mapping (most common)
  → You define each field you want in the output
  → Set field name → set value (can reference input fields with expressions)
  → Only the fields YOU define appear in the output

MODE 2: Add Fields (Keep All)
  → Keeps ALL existing fields AND adds new ones
  → Good when you just want to add a calculated field

MODE 3: Remove Fields
  → Keep all EXCEPT the ones you list
  → Good for cleaning sensitive data before logging
```

**Expressions — the key to dynamic fields:**
```
Static value:   "London"
Expression:     {{ $json.city }}              — reference a field from input
Expression:     {{ $json.first + " " + $json.last }}  — concatenate
Expression:     {{ $json.price * 1.2 }}       — calculate
Expression:     {{ new Date().toISOString() }} — current timestamp
Expression:     {{ $json.name.toLowerCase() }} — transform string
Expression:     {{ $('Webhook').item.json.id }} — reference a DIFFERENT node's output
```

**Real example — formatting lead data:**
```
INPUT (from Typeform):
{ "q1": "Alice Smith", "q2": "alice@test.com", "q3": "I need help with SEO" }

[Edit Fields: Manual]
  name    = {{ $json.q1 }}
  email   = {{ $json.q2 }}
  message = {{ $json.q3 }}
  source  = "typeform"
  created = {{ new Date().toISOString() }}

OUTPUT:
{ name: "Alice Smith", email: "alice@test.com", message: "I need help...", source: "typeform", created: "2026-09-16T09:00:00Z" }
```

**💡 Tips:**
1. Always rename cryptic field names (q1, q2) to human-readable names early in the workflow
2. Use "Add Fields" mode when you just want to add 1-2 fields without losing existing data
3. The expression editor has autocomplete — type `$json.` and it shows available fields
4. `{{ $json.field ?? "default value" }}` — use `??` for null-safe defaults

---

## §3.2 Rename Keys Node

```
INPUT:                    OUTPUT:
{ "Q1_Answer": "Alice" }  { "name": "Alice" }
{ "Q2_Answer": "alice@" } { "email": "alice@" }
```

**What it does:** Renames field names (keys) without changing their values. Simpler than Edit Fields when you ONLY need to rename — no value transformation.

**When to use:**
- API returns ugly field names (`user_first_name_v2`) → rename to `firstName`
- Mapping between two systems with different naming conventions
- Quick cleanup before writing to a database

**💡 Tip:** For simple renames, Rename Keys is faster to set up than Edit Fields. For anything more complex (transforming values, calculations), use Edit Fields.

---

## §3.3 Code Node (JavaScript / Python)

```
[Any data] ──► [Code: custom logic] ──► [Transformed data]
                     ↑
               Write JavaScript or
               Python to manipulate
               items however you want
```

**What it does:** Lets you write custom JavaScript or Python code to process your items. Use when no other node can do what you need.

**Structure:**
```javascript
// The 'items' array contains all input items
// Each item has a 'json' property with your data
// You MUST return an array of items

for (const item of items) {
  // Read input data
  const name = item.json.name;
  
  // Transform it
  item.json.nameUpper = name.toUpperCase();
  item.json.wordCount = name.split(' ').length;
}

return items;  // ALWAYS return items
```

**Practical examples:**

```javascript
// 1. Parse a date and reformat it
for (const item of items) {
  const raw = item.json.created_at;         // "2026-09-16T09:00:00Z"
  const d = new Date(raw);
  item.json.date_formatted = d.toLocaleDateString('en-GB'); // "16/09/2026"
}
return items;

// 2. Filter items (alternative to Filter node)
return items.filter(item => item.json.score > 50);

// 3. Create a new item (discard input)
return [{
  json: {
    summary: items.map(i => i.json.name).join(', '),
    count: items.length
  }
}];

// 4. Split one item into multiple items
const results = [];
for (const tag of items[0].json.tags) {
  results.push({ json: { tag: tag, parent_id: items[0].json.id } });
}
return results;
```

**💡 Tips:**
1. Always `return items` at the end — forget this and get "no output" errors
2. Each item's data is at `item.json.fieldName` — not `item.fieldName`
3. To create brand new items: `return [{ json: { ... } }]`
4. You have access to: `$input` (input items), `$env` (environment vars), `$execution` (execution data)
5. The Code node runs Node.js 18 — you can use modern JS (arrow functions, async/await, etc.)

**When to use Code node:**
- Complex string manipulation
- Date calculations
- Merging arrays in custom ways
- Generating dynamic values (UUIDs, hashes)
- When you'd need 5+ Edit Fields nodes to do the same thing

---

# SECTION 4 — INTEGRATION NODES

> These nodes connect n8n to external services.

---

## §4.1 HTTP Request Node

```
n8n                              External API
 │                                    │
 │  GET https://api.example.com/users │
 │  Headers: { Authorization: "..." } │
 │─────────────────────────────────► │
 │                                    │ processes
 │◄───────────────────────────────── │
 │  Response: { users: [...] }        │
```

**What it does:** Makes any HTTP API call (GET, POST, PUT, PATCH, DELETE). The most powerful node in n8n — if a service has an API, this node can talk to it.

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **Method** | GET (fetch data) / POST (send data) / PUT (replace) / PATCH (update) / DELETE |
| **URL** | The API endpoint URL |
| **Authentication** | How to prove who you are (see below) |
| **Headers** | Key-value pairs sent with the request (Content-Type, API keys) |
| **Body** | JSON/form data sent in POST/PUT requests |
| **Query Parameters** | URL parameters (`?key=value&page=1`) |
| **Response Format** | Auto-detect / JSON / Text / Binary |

**Authentication types:**

```
None               → Public APIs, no auth needed
Generic Credential → Custom headers (e.g. "Authorization: Bearer abc123")
Header Auth        → Single header (e.g. "X-API-Key: mykey")  ← USE THIS for DataForSEO
Basic Auth         → Username + password (Base64 encoded automatically)
OAuth2             → For Google, Slack, etc.
API Key            → Standard API key in header or query param
```

**⚠️ SECURITY RULE:** NEVER put credentials (passwords, API keys) as plain text in the URL or node fields. Always create a **Credential** in n8n and reference it. This way:
- Credentials are encrypted in n8n's database
- When you export/share the workflow JSON, credentials are NOT included
- If someone steals your workflow file, they can't use your API keys

**Import from cURL (time-saving trick):**
```
Most API documentation shows cURL examples:
  curl -X POST "https://api.example.com/data" \
    -H "Authorization: Bearer mykey" \
    -d '{"query": "test"}'

In n8n HTTP Request node:
  1. Click "Import from cURL"
  2. Paste the curl command
  3. n8n auto-fills: URL, method, headers, body

Saves 5 minutes of manual setup per API call!
```

**Response handling:**
```
After HTTP Request, data is at:
  $json               → the parsed JSON response (if API returns JSON)
  $json.data          → nested field
  $json.items[0]      → first item in array
  $json.meta.total    → nested nested field

For DataForSEO specifically:
  $json.tasks[0].result[0].items  → the actual data array
```

**Real example — DataForSEO keyword data:**
```javascript
// HTTP Request settings:
Method: POST
URL: https://api.dataforseo.com/v3/keywords_data/google/search_volume/live
Authentication: Generic Credential → "DataForSEO" (Header Auth)
Body (JSON):
[{
  "keywords": {{ $json.keyword }},
  "location_code": 2826,   // UK
  "language_code": "en"
}]
```

**💡 Tips:**
1. Always check "Include Response Headers" when debugging — headers tell you rate limit status
2. Use "Error on Fail" = OFF during development, then turn it ON in production
3. "Pagination" setting handles APIs that return results across multiple pages automatically
4. Add a Wait node after HTTP Request when looping to avoid rate limit errors (429 Too Many Requests)

---

## §4.2 Respond to Webhook Node

```
External App                      n8n
     │                             │
     │──► POST /webhook/xyz ───────►[Webhook Trigger]
     │                             │
     │                             ▼
     │                        [Process data...]
     │                             │
     │                             ▼
     │◄── { "status": "ok" } ─────[Respond to Webhook]
     │
     │ (External app now knows the workflow succeeded)
```

**What it does:** Sends a custom HTTP response back to whoever triggered your webhook. Without this node, n8n auto-responds with `{}` immediately. With this node, you control:
- What data gets sent back
- When it gets sent (after processing is complete)
- The HTTP status code

**Key settings:**

| Setting | Example |
|---------|---------|
| **Respond With** | JSON / Text / Binary / No Data |
| **Response Body** | `{ "success": true, "id": "{{ $json.record_id }}" }` |
| **Response Code** | 200 (success), 201 (created), 400 (bad request), 500 (error) |
| **Response Headers** | Add Content-Type etc. |

**When to use:**
- When your workflow IS an API (another system calls your webhook and expects a proper response)
- When the calling system needs data back (like a record ID after creating something)
- When you need to return validation errors (400 status)

**⚠️ Setting up the Webhook node for this to work:**
```
In the Webhook node settings:
  "Respond" → set to "When last node finishes"
  (NOT "Immediately" — otherwise the response is sent before Respond to Webhook runs)
```

---

## §4.3 Airtable Node

```
[n8n] ──► [Airtable Node] ──► [Your Airtable Base]
               ↑
       Operations:
       - List records (GET)
       - Get record (by ID)
       - Create record
       - Update record
       - Delete record
       - Search records (filter by formula)
```

**What it does:** Read from and write to Airtable tables. Airtable is used throughout this course as the database + front-end for automation systems.

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **Operation** | List / Get / Create / Update / Delete / Upsert |
| **Base ID** | Which Airtable base (find in Airtable URL) |
| **Table** | Which table within the base |
| **Fields** | Which fields to include (for List/Get) OR field values (for Create/Update) |
| **Filter by Formula** | Airtable formula to filter records (for List) |
| **Max Records** | Limit how many records to fetch |
| **Record ID** | The `rec...` ID needed for Update/Delete operations |

**Common operations with examples:**

```
LIST (fetch records):
  Operation: List
  Filter: {status} = "Pending"
  → Fetches all records where status field = "Pending"

CREATE (new record):
  Operation: Create
  Fields: name → {{ $json.name }}, email → {{ $json.email }}
  → Creates a new record with those values

UPDATE (change existing):
  Operation: Update
  Record ID: {{ $json.record_id }}   ← you need the rec... ID
  Fields: status → "Completed"
  → Updates ONLY the status field on that record

UPSERT (create or update):
  Operation: Upsert
  Lookup Field: email            ← the unique field to match on
  → If record with that email exists: UPDATE it
  → If not: CREATE a new record
```

**Linked record field (array format):**
```
⚠️ IMPORTANT: When setting a linked record field, you MUST pass an ARRAY:

WRONG:  companyId = "recABCDEFGH"
RIGHT:  companyId = ["recABCDEFGH"]

In n8n expression: {{ [$json.company_record_id] }}
                    ↑ wrap in [ ] to make it an array
```

**Typecast setting:**
```
⚠️ For date fields, enable "Options → Typecast" in the Airtable node.
Without it, date format mismatches cause "field cannot accept the provided value" errors.
```

**Filter formula examples:**
```
{status} = "Pending"                           → exact match
{created} > '2026-01-01'                       → date comparison
AND({status} = "Active", {score} > 50)         → multiple conditions
{company} = ""                                 → empty field
NOT({company} = "")                            → not empty
FIND("london", LOWER({city})) > 0             → case-insensitive contains
```

**💡 Tips:**
1. Always store Airtable record IDs (`rec...`) in a field so you can update records later
2. "List" with no filter = ALL records (can be slow on large tables — always add a filter)
3. Airtable has a 5 requests/second rate limit — add a Wait node when processing many records
4. For Button fields: the formula `= "<WEBHOOK_URL>?record_id=" & RECORD_ID()` triggers n8n from Airtable

---

## §4.4 Google Sheets Node

```
[n8n] ──► [Google Sheets] ──► [Your Google Spreadsheet]
                ↑
        Operations:
        - Read rows
        - Append rows
        - Update rows
        - Delete rows
        - Create spreadsheet
```

**What it does:** Read and write Google Sheets. Used for simple tabular data storage — cheaper and more familiar than Airtable for basic use cases.

**When to use Sheets vs Airtable:**
```
Use Google Sheets when:               Use Airtable when:
  → Client already uses Sheets          → You need linked records (relations)
  → Simple flat data (no relations)     → You need Airtable views/interfaces
  → Data is for humans to edit          → You need button triggers
  → Shared with Google Workspace team   → Complex filtering is needed
```

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **Operation** | Read / Append / Update / Clear |
| **Spreadsheet** | Select or enter spreadsheet ID |
| **Sheet** | Which tab/sheet within the spreadsheet |
| **Range** | Cell range (e.g. A1:E100) or leave empty for whole sheet |
| **Key Row** | Row number of headers (usually 1) |
| **Data Mode** | Auto-map (match by header name) or Manual mapping |

**💡 Tips:**
1. Use "Auto-map" mode — n8n matches fields by the COLUMN HEADER NAME in your sheet
2. First row MUST be headers — this is how n8n knows which column is which
3. For reading, empty rows stop reading — no gaps in your data
4. Sheets has a 60 reads/minute limit per user — add Wait node in loops

---

## §4.5 Send Email (SMTP / Gmail / Outlook)

```
[Trigger] ──► [Build email content] ──► [Send Email] ──► recipient's inbox
```

**What it does:** Sends emails. Can use Gmail, Outlook, SMTP, Mailgun, SendGrid, etc.

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **To** | Recipient email (can be dynamic: `{{ $json.email }}`) |
| **From** | Sender address |
| **Subject** | Email subject line |
| **Email Type** | Text or HTML |
| **Message** | The email body |
| **Attachments** | Binary data to attach |

**HTML email example:**
```html
<h2>Welcome, {{ $json.name }}!</h2>
<p>Thanks for signing up. Here's what happens next:</p>
<ul>
  <li>We'll review your details within 24 hours</li>
  <li>You'll receive your proposal by {{ $json.proposal_date }}</li>
</ul>
<p>Your reference number: <strong>{{ $json.ref_id }}</strong></p>
```

**⚠️ Tips:**
1. For Gmail: use "Gmail OAuth2" credential — NOT your password
2. Test with your own email first before sending to clients
3. HTML emails look better than plain text — use simple HTML
4. Set up email credentials in n8n Credentials ONCE, then reuse across all workflows

---

## §4.6 Slack Node

```
[n8n] ──► [Slack: Send Message] ──► #alerts channel
```

**What it does:** Send messages to Slack channels, DMs, or create/update Slack resources.

**Key settings for "Send Message":**

| Setting | What it does |
|---------|-------------|
| **Channel** | `#general`, `#alerts`, or a User ID for DM |
| **Message** | The text (supports Slack markdown: *bold*, _italic_, `code`) |
| **Attachments / Blocks** | Rich formatted messages with buttons, fields, images |

**Slack message formatting:**
```
Plain text:  Hello team!
Bold:        *Hello team!*
Italic:      _Hello team!_
Code:        `Hello team!`
Link:        <https://google.com|Click here>

Block Kit (rich format):
{
  "blocks": [
    {
      "type": "section",
      "text": { "type": "mrkdwn", "text": "*🚨 Alert:* workflow failed" }
    },
    {
      "type": "section",
      "fields": [
        { "type": "mrkdwn", "text": "*Workflow:*\nSEO Generator" },
        { "type": "mrkdwn", "text": "*Error:*\nAPI timeout" }
      ]
    }
  ]
}
```

**Common use cases:**
```
1. Error alerts:      IF workflow fails → [Slack] #engineering "🚨 Error in [workflow]"
2. Daily reports:     [Schedule] → [Gather data] → [Slack] #sales "📊 Daily numbers"
3. Approvals:         [Form submission] → [Slack] "New request from Alice — approve?"
4. Status updates:    [Long task completes] → [Slack] "✅ 50 articles generated"
```

---

# SECTION 5 — AI NODES

> These nodes connect n8n to AI language models. They work together as a system.

---

## §5.1 AI Agent Node

```
[Input] ──► [AI Agent]
                │
                ├──► THINK: "What do I need to do?"
                │
                ├──► USE TOOL: [Perplexity Search] ──► results back to Agent
                │
                ├──► USE TOOL: [Calculator] ──► result back to Agent
                │
                ├──► THINK: "I have what I need"
                │
                └──► OUTPUT: Final answer
```

**What it does:** An autonomous AI that can reason about a task AND use tools to complete it. The agent decides WHEN to use tools and WHAT to search for — you don't hardcode this.

**Difference from Basic LM Chain:**
```
Basic LM Chain:     Input → LLM → Output (one shot, no tools)
AI Agent:           Input → LLM → [thinks → uses tools → checks results → repeats] → Output
                           (multi-step reasoning, autonomous tool use)
```

**Required sub-nodes (must connect to Agent):**

```
[AI Agent]
    │
    ├── Chat Model   (REQUIRED): which LLM to use
    ├── Memory       (OPTIONAL): remember conversation history
    └── Tools        (OPTIONAL): what the agent can DO
```

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **System Message** | Instructions for the agent — its "personality" and task |
| **User Message** | The actual request/input for this run |
| **Max Iterations** | How many tool-call rounds before it gives up (default 10) |
| **Return Intermediate Steps** | Show the agent's thinking process in output |

**System message structure (best practice):**
```xml
<role>
You are an SEO research specialist. Your job is to find accurate, 
current information about [topic] using web search.
</role>

<instructions>
1. Analyse the research questions provided
2. Search for facts that support each point
3. Always include source URLs
4. Return 5-10 key facts with citations
</instructions>

<constraints>
- Only use information from reputable sources
- Do not include opinions — only verifiable facts
- Include publication date when available
</constraints>
```

**💡 Tips:**
1. XML tags (`<role>`, `<instructions>`) help the LLM parse your prompt better
2. Set Max Iterations to 5 for simple tasks, 15 for complex research
3. "Return Intermediate Steps" is useful for debugging what the agent searched for
4. The agent node outputs ALL its thinking — use an Edit Fields node after to extract just the final answer

---

## §5.2 Basic LM Chain Node

```
[Input text] ──► [Basic LM Chain] ──► [Output text]
                       │
                  (one LLM call,
                   no tools,
                   no loop)
```

**What it does:** A simple, single LLM call. Input → prompt → output. No tools, no reasoning loop. Faster and cheaper than AI Agent.

**Required sub-nodes:**
```
[Basic LM Chain]
    │
    ├── Chat Model  (REQUIRED): which LLM
    └── Output Parser (OPTIONAL): structure the output as JSON
```

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **System Message** | The LLM's role and instructions |
| **User Message** | The actual input/prompt for this call |
| **Fallback Model** | If primary LLM fails, use this one automatically |

**When to use Basic LM Chain vs AI Agent:**
```
Use Basic LM Chain:         Use AI Agent:
→ Text classification        → Research tasks (needs web search)
→ Summarisation              → Multi-step reasoning
→ Format conversion          → Tasks requiring tool use
→ Creative writing           → When you don't know how many steps needed
→ Structured data extraction → Autonomous decision-making
→ Translation
→ Content generation (with pre-gathered research)
```

**Example — content writer:**
```
System: You are an expert blog writer. Write in a conversational, 
        human style at third-grade reading level. Avoid em dashes.
        
User:   Write a 200-word introduction for this article:
        Title: {{ $json.article_title }}
        Keywords: {{ $json.keywords }}
        Research: {{ $json.research_facts }}
```

---

## §5.3 Chat Model Node (OpenAI / Anthropic / Gemini / OpenRouter)

```
[AI Agent or LM Chain]
         │
         └──► [Chat Model: Claude 3.5 Sonnet] ← connects HERE
                      │
                  Sends prompts to
                  the actual LLM API
```

**What it does:** NOT a standalone node — it connects TO an AI Agent or Basic LM Chain and tells it WHICH AI model to use. Think of it as the "engine" that the Agent/Chain uses.

**Available model nodes:**
```
OpenAI Chat Model     → GPT-4o, GPT-4o-mini, GPT-3.5-turbo
Anthropic Chat Model  → Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku
Google Gemini         → Gemini 1.5 Pro, Gemini 1.5 Flash
OpenRouter            → Access to ALL models via one API key ← RECOMMENDED
Ollama                → Local/self-hosted models (free but slower)
```

**Why OpenRouter is recommended:**
```
Without OpenRouter:               With OpenRouter:
  OpenAI API key                    One OpenRouter API key
  Anthropic API key          ──►    Access to ALL models
  Google AI API key                 Easy to switch models
  Mistral API key                   Compare models easily
  (4 accounts, 4 keys)              (1 account, 1 key)
```

**Model selection guide:**
```
┌─────────────────────┬──────────────────────┬──────────┬─────────────┐
│ Task                │ Best Model           │ Cost     │ Speed       │
├─────────────────────┼──────────────────────┼──────────┼─────────────┤
│ Planning/reasoning  │ Gemini 1.5 Pro       │ Medium   │ Medium      │
│ Research            │ Gemini 1.5 Flash     │ Low      │ Fast        │
│ Creative writing    │ Claude 3.5 Sonnet    │ Medium   │ Medium      │
│ Simple tasks        │ GPT-4o-mini          │ Very Low │ Very Fast   │
│ Complex reasoning   │ Claude 3 Opus        │ High     │ Slow        │
│ Latest news         │ Perplexity Sonar     │ Medium   │ Medium      │
└─────────────────────┴──────────────────────┴──────────┴─────────────┘
```

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **Model** | Which specific model within the provider |
| **Temperature** | 0 = factual/deterministic, 1 = creative/random |
| **Max Tokens** | Maximum response length |
| **Fallback Model** | Backup if primary fails |

**Temperature guide:**
```
0.0 → Perfect for: data extraction, classification, structured output
0.3 → Perfect for: factual writing, summaries, translations
0.7 → Perfect for: blog writing, marketing copy, creative content
1.0 → Perfect for: brainstorming, fiction, very creative tasks
```

---

## §5.4 Structured Output Parser

```
[AI output: "The score is 85 and the status is active"]
                         │
                         ▼
              [Structured Output Parser]
              Schema: { score: number, status: string }
                         │
                         ▼
              [Clean JSON: { "score": 85, "status": "active" }]
```

**What it does:** Forces the LLM to return valid JSON matching a schema you define. Without this, LLMs return plain text — messy and hard to use in the next node.

**Why it's important:**
```
Without Output Parser:
  LLM returns: "Based on my analysis, the lead score is 85 and the status is active."
  Next node can't do: $json.score  ← undefined!
  
With Output Parser:
  LLM returns: { "score": 85, "status": "active" }
  Next node can do: $json.score → 85  ✓
```

**How to define your schema (two ways):**

```
WAY 1: Auto from description
  → Describe what you want in plain English
  → n8n generates the JSON schema automatically
  → Quickest method

WAY 2: Manual JSON Schema
  → Write the exact schema yourself
  → More control, more reliable
  
Example schema:
{
  "type": "object",
  "properties": {
    "article_title": { "type": "string" },
    "target_keyword": { "type": "string" },
    "sections": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "header": { "type": "string" },
          "word_count": { "type": "number" }
        }
      }
    }
  }
}
```

**💡 Tips:**
1. ALWAYS use Output Parser when you need structured data from AI (for the next node to use)
2. Keep schemas simple — the more complex, the more likely the LLM makes mistakes
3. If you get parse errors: simplify the schema, or add "Output repair chain" (n8n has this built-in)
4. For blog content (a single string): schema is just `{ "content": { "type": "string" } }`

---

## §5.5 Tools (Perplexity, Calculator, HTTP, etc.)

```
[AI Agent]
    │
    └── Tools (the Agent can USE these):
         ├── [Perplexity Search Tool] ← web search with citations
         ├── [Calculator Tool]         ← maths
         ├── [HTTP Request Tool]       ← call any API
         ├── [Code Tool]               ← run code
         └── [Airtable Tool]           ← read/write database
```

**What tools do:** They're like superpowers you give to an AI Agent. The agent decides WHEN to use them based on what the task needs.

**Perplexity Search Tool:**
```
When connected to an AI Agent:
  Agent receives: "Research the top 5 AI automation trends in 2026"
  Agent thinks: "I need to search the web for this"
  Agent calls: Perplexity("AI automation trends 2026")
  Perplexity returns: facts + source URLs
  Agent uses: those facts to write its response

Why Perplexity over Google?:
  → Perplexity already filters/summarises results
  → Returns the actual answer + citation (not just links)
  → Better for AI agents than raw Google results
```

**HTTP Request Tool:**
```
Gives the AI Agent the ability to call ANY API.
The agent can construct the request itself based on the task.
More flexible than pre-configured HTTP Request nodes.
Use when: the agent needs to decide WHAT to search for dynamically.
```

---

## §5.6 Memory Node (Window Buffer Memory)

```
Conversation 1: "My name is Alice"
Conversation 2: "What is my name?"

Without memory:    AI says "I don't know your name"
With memory:       AI says "Your name is Alice" ✓
```

**What it does:** Gives an AI Agent short-term memory of the conversation. Without memory, each message to the agent is independent — it forgets everything said before.

**Key settings:**

| Setting | What it does |
|---------|-------------|
| **Context Window Length** | How many previous messages to remember (default 5) |
| **Session ID** | Unique ID per conversation/user — keeps different users' memories separate |

**When to use:**
- Building chatbots that need conversation context
- Multi-turn AI interactions
- Any workflow where the AI needs to reference earlier messages

**Session ID pattern:**
```javascript
// Use user's email or session ID to separate memories:
Session ID: {{ $json.user_email }}

// This means:
// Alice's chat history stays with Alice
// Bob's chat history stays with Bob
// (Even if they use the same workflow)
```

---

# SECTION 6 — UTILITY NODES

---

## §6.1 Sticky Note

```
                    ┌─────────────────────────────┐
                    │ 📝 TODO: Add error handling  │
                    │ This node calls DataForSEO.  │
[HTTP Request] ─────│ Rate limit: 10 req/sec       │
                    │ Auth: see 'DataForSEO' cred  │
                    └─────────────────────────────┘
```

**What it does:** A yellow post-it note on your workflow canvas. Does NOTHING technically — just holds documentation for humans reading the workflow.

**Why use it (very important):**
```
Month 1 Hasan: "Of course I know what this node does!"
Month 4 Hasan: "What the... why is there a random HTTP Request here?
                What does it call? Why is it looping? Why 10 retries?"

Sticky Notes prevent this. Future you (and clients) will thank you.
```

**Best practices:**
1. Add a Sticky Note at the START of every workflow explaining what it does
2. Add notes next to complex logic explaining WHY (not just what)
3. Use for TODOs and known limitations
4. Note credential names so others know which credentials are needed
5. Colour-code your notes (n8n supports different colours)

---

# SECTION 7 — NODE COMBINATION PATTERNS

> The real skill isn't knowing individual nodes — it's knowing how to COMBINE them. Here are the patterns you'll use over and over.

---

## Pattern 1: Trigger → Enrich → Store

```
[Webhook: new form submission]
        │
        ▼
[Edit Fields: rename ugly field names]
        │
        ▼
[HTTP Request: enrich with company data from Clearbit]
        │
        ▼
[Edit Fields: combine original + enriched data]
        │
        ▼
[Airtable: create record in CRM]
        │
        ▼
[Send Email: notify sales team]
```

**Used for:** CRM enrichment, lead capture, form processing

---

## Pattern 2: Schedule → Fetch → Process → Report

```
[Schedule: every Monday 8 AM]
        │
        ▼
[Airtable: list all "Active" leads]
        │
        ▼ (one item per lead)
[HTTP Request: check each lead's website status]
        │
        ▼
[IF: website is down?]
        ├── YES ──► [Slack: alert #sales "Lead's website is down: ..."]
        └── NO  ──► [No Op]
        │
        ▼
[Aggregate: all results into summary]
        │
        ▼
[Send Email: weekly summary report]
```

**Used for:** Weekly reports, monitoring, scheduled checks

---

## Pattern 3: Array → Split → Loop → Collect → Write

```
[Airtable: get keyword list]    ← 50 keywords
        │
        ▼
[Split Out: keywords array]    ← 50 separate items
        │
        ▼
[HTTP Request: get volume per keyword]   ← runs 50 times
        │
        ▼
[Edit Fields: format results]
        │
        ▼
[Aggregate: combine all 50 results]    ← back to 1 item
        │
        ▼
[Google Sheets: write all 50 rows]
```

**Used for:** Bulk API processing, batch enrichment, data transformation

---

## Pattern 4: AI Pipeline (Plan → Research → Write)

```
[Webhook: blog request]
        │
        ▼
[Basic LM Chain + Gemini: PLAN the article structure]
  (Output Parser → JSON article plan)
        │
        ▼
[Split Out: article sections]    ← one item per section
        │
        ▼
[AI Agent + Perplexity: RESEARCH each section]
  (searches web, returns facts + citations)
        │
        ▼
[Aggregate: all research together]
        │
        ▼
[Split In Batches: size=1]    ← process sections one by one
        │
        ▼
[Airtable: GET temp_article field]    ← read what's been written so far
        │
        ▼
[Basic LM Chain + Claude: WRITE this section]
  (gets: section plan + research + previous content)
        │
        ▼
[Airtable: UPDATE temp_article field]    ← save running article
        │
        └──► loops back for next section
```

**Used for:** Content generation, multi-step AI pipelines

---

## Pattern 5: Webhook API (Build your own API endpoint)

```
External App                         Your n8n Workflow
     │                                     │
     │  POST /webhook/process-order        │
     │  { orderId: "123", ... }  ──────────►[Webhook]
     │                                     │
     │                                     ▼
     │                               [Process order...]
     │                                     │
     │                                     ▼
     │◄── { "status": "ok",          [Respond to Webhook]
     │      "trackingId": "TRK456" }
```

**Used for:** Building APIs, Zapier/Make replacement webhooks, app integrations

---

## Pattern 6: Error Handling

```
[Main Workflow]                    [Error Workflow]
      │                                  │
      │ fails ────────────────►[Error Trigger]
                                         │
                                         ▼
                              [Edit Fields: format alert]
                                         │
                                         ▼
                              [Slack: #errors] + [Email: support@]
                                         │
                                         ▼
                              [Airtable: log error for audit]
```

**Used for:** Every production workflow — set this up FIRST

---

# SECTION 8 — WHEN TO USE WHICH NODE (DECISION TREE)

```
Q: Do I need to START a workflow?
   ├── Yes, manually while testing     → Manual Trigger
   ├── Yes, on a schedule              → Schedule Trigger
   ├── Yes, when external app sends data → Webhook
   └── Yes, when another workflow fails  → Error Trigger

Q: Do I need to BRANCH the workflow?
   ├── 2 paths (true/false)            → IF Node
   ├── 3+ paths                        → Switch Node
   └── Remove items that don't match   → Filter Node

Q: Do I need to COMBINE data?
   ├── Join two branches back together  → Merge (Append mode)
   ├── Zip two lists by position        → Merge (By Index mode)
   └── SQL-style join by matching field → Merge (By Key mode)

Q: Do I need to LOOP?
   ├── Array inside a field → split into items → Split Out
   ├── Process items one-by-one with context   → Split In Batches (size=1)
   └── Process in groups of 10, 50, 100        → Split In Batches (size=N)

Q: Do I need to COMBINE many items back?
   └── Yes                             → Aggregate

Q: Do I need to TRANSFORM data?
   ├── Rename/add/remove fields         → Edit Fields (Set)
   ├── Only rename field names          → Rename Keys
   ├── Complex logic / calculation      → Code Node
   └── Pause for a period of time       → Wait Node

Q: Do I need to CALL an external service?
   ├── Has n8n built-in node?           → Use that node (Airtable, Sheets, Slack, Email...)
   └── No built-in node?               → HTTP Request Node

Q: Do I need AI?
   ├── Single LLM call (no tools)       → Basic LM Chain + Chat Model
   ├── AI that can search/use tools     → AI Agent + Chat Model + Tools
   ├── Structured JSON from AI          → + Structured Output Parser
   └── AI remembers previous messages   → + Memory Node
```

---

# SECTION 9 — QUICK RECALL TEST

Test yourself — cover the answers and try to answer from memory.

**Q1.** What is the 80/20 rule in n8n?
> **A:** Master 13 nodes and you can build 80% of all automations. 30 nodes covers 95%+.

**Q2.** What's the difference between the Test URL and Production URL in a Webhook node?
> **A:** Test URL only works when you're in the n8n editor. Production URL only works when the workflow is Active.

**Q3.** You have 5 leads, each as a separate item. You use HTTP Request to enrich them. How many times does HTTP Request run?
> **A:** 5 times — n8n runs the node once per input item automatically.

**Q4.** You need to route support tickets to 4 different Slack channels based on department. Which node?
> **A:** Switch node (IF only has 2 outputs; Switch has unlimited).

**Q5.** What's the difference between IF node and Filter node?
> **A:** IF has 2 outputs (true path + false path — both groups continue). Filter has 1 output — items that don't match are DROPPED.

**Q6.** You have an array field called "keywords" inside one item. You want to make API calls for each keyword. What node do you use first?
> **A:** Split Out — it turns the array into separate items. Then HTTP Request runs once per item automatically.

**Q7.** What Merge mode would you use if you have two lists of the same length and want to combine item 1 from list A with item 1 from list B?
> **A:** Merge By Index.

**Q8.** Why is it important to NEVER put API credentials directly in the HTTP Request node's URL or body fields?
> **A:** When you export/share the workflow JSON, hardcoded credentials are visible to anyone. Using n8n Credentials encrypts them and excludes them from exported workflow files.

**Q9.** What's the formula for an Airtable Button field that triggers an n8n webhook?
> **A:** `= "<YOUR_WEBHOOK_URL>?record_id=" & RECORD_ID()`

**Q10.** When writing to an Airtable linked record field from n8n, what format must the value be in?
> **A:** An array: `["recXXXXXXXX"]` — not a plain string.

**Q11.** What temperature setting would you use for creative blog writing? For structured data extraction?
> **A:** Creative writing = 0.7. Structured extraction = 0.0.

**Q12.** An AI Agent can use tools. A Basic LM Chain cannot. When would you choose Basic LM Chain?
> **A:** When you've already gathered all the information the AI needs (research is done) and you just want it to write/transform/classify. No tools needed → LM Chain is faster and cheaper.

**Q13.** You want to generate 6 article sections but each section's writer must see what was written before it (for flow/context). What solution did the n8n masterclass use?
> **A:** Split In Batches (size=1) + a Temporary Article field in Airtable. Each iteration: READ the temp field (previous content) → WRITE new section → UPDATE temp field with new content. Loops until all sections done.

**Q14.** What node would you use to pause a workflow for 24 hours before sending a follow-up email?
> **A:** Wait node (Time Interval mode).

**Q15.** You build a complex workflow and want your clients to understand it 6 months later. What should you add throughout the workflow canvas?
> **A:** Sticky Notes — explaining what each section does, why certain decisions were made, which credentials to use, and any known limitations.

---

*End of n8n Node Masterclass — Complete Reference Guide*
*Total nodes covered: 30 | Patterns covered: 6 | Study time: ~2 hours*

