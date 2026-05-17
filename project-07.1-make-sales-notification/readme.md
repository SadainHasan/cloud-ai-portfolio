# Project 07.1 — Make.com: Google Sheets to Slack Sales Notification

**Status:** Live (Make.com free tier)
**Built:** 16 May 2026
**Tools:** Make.com · Google Sheets · Slack
**GitHub:** https://github.com/SadainHasan/cloud-ai-portfolio
**Portfolio site:** https://d2ven7lubrbrhs.cloudfront.net
**Business site:** https://cloudflowautomations.co.uk
**Builder:** Khandaker Sadain Hasan | Cloud + AI Automation Consultant

---

## What Problem Does This Solve?

Every sales team that logs prospects into a spreadsheet faces a coordination problem.
The spreadsheet is updated — but the people who need to act on it are not notified.
A salesperson adds a new lead from a conference. Their manager does not know. A follow-up
call that should happen within the hour happens three days later, after someone
happens to open the spreadsheet. The lead has already gone cold.

This automation eliminates that gap entirely. The moment a new row appears in the
Prospects spreadsheet — whether added by a salesperson in the field, a data entry
assistant in the office, or a connected form — Slack sends a formatted notification
to the sales-team channel within minutes. Every team member sees it. The prospect
gets called while the conversation is still warm.

For a small sales team of 2–5 people, this automation removes the need for any
manual "have you seen the new lead?" messages. It also creates an automatic log
of when each lead entered the pipeline — useful for reporting and accountability.

---

## What This Is

This project demonstrates a production-ready Make.com scenario that connects Google
Sheets to Slack using a polling trigger. The scenario watches the Prospects spreadsheet
for new rows, extracts the prospect's details (name, email, country, phone, and notes),
and posts a formatted notification message to the designated Slack channel.

The scenario was built following the official Make.com getting-started tutorial,
which is the standard onboarding path for new Make.com users. This project documents
the full process and business context so it can serve as a reference for client
engagements of the same type.
┌─────────────────────────────────────────────────────────────┐
│                    DATA ENTRY POINT                          │
│                                                             │
│  Salesperson adds new prospect row to Google Sheets:         │
│  First Name | Last Name | Country | Email | Phone | Details  │
│                                                             │
└─────────────────────────┬───────────────────────────────────┘
│ New row detected (polling, ~15 min)
▼
┌─────────────────────────────────────────────────────────────┐
│                    MAKE.COM SCENARIO                         │
│                                                             │
│  [Trigger: Google Sheets — Watch New Rows]                  │
│     • Polling trigger: checks every 15 minutes              │
│     • Limit: 20 rows per run                                │
│     • Headers: Row 1 (First Name, Last Name, etc.)          │
│     • Tracks last processed row — no duplicates             │
│                                                             │
│            ↓ bundle flows to next module ↓                  │
│                                                             │
│  [Action: Slack — Send a Message]                           │
│     • Channel: #sales-team (public)                         │
│     • Message: formatted with all 6 prospect fields mapped  │
│     • Connection: OAuth2 Slack user connection              │
└─────────────────────────┬───────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│              SALES TEAM — SLACK #sales-team                 │
│                                                             │
│  "New prospect added! 🎉                                    │
│   Name: Sarah Ahmed                                         │
│   Email: sarah.ahmed@example.com                            │
│   Country: UK                                               │
│   Phone: 07700 900123                                        │
│   Details: Interested in cloud automation for accountancy"  │
└─────────────────────────────────────────────────────────────┘
---

## Steps

### Step 1: Plan the Scenario

Before opening Make.com, defined the automation in plain English:
"When a new row appears in the Prospects spreadsheet, send a Slack notification
to the sales-team channel."

Applications needed: Google Sheets, Slack.
Trigger: new spreadsheet row.
Action: Slack message with prospect data.
Permissions required: Google Sheets read access, Slack workspace write access.

### Step 2: Set Up Slack Channel

1. Opened Slack workspace
2. Clicked three dots next to Channels → Create channel
3. Named channel: sales-team
4. Set visibility: Public
5. Clicked Create

### Step 3: Set Up Google Sheets

1. Opened sheets.google.com
2. Created new blank spreadsheet
3. Renamed to: Prospects
4. Added column headers in Row 1:
   - A1: First Name
   - B1: Last Name
   - C1: Country
   - D1: Email
   - E1: Phone Number
   - F1: Details
5. Added one row of sample prospect data for testing

### Step 4: Create the Make.com Scenario

1. Clicked + Create a new scenario in Make.com dashboard
2. Renamed scenario to: New Prospect Notification
3. Clicked Save icon to save the scenario

### Step 5: Add Google Sheets Trigger Module

1. Clicked the + circle on the blank canvas
2. Searched for Google Sheets
3. Selected Watch New Rows (polling trigger)
4. Created OAuth2 connection to Google account
5. Authorised Make.com to access Google Sheets
6. Connection saved for future reuse

### Step 6: Configure the Trigger

Settings applied:
- Drive: My Drive
- Search Method: Search by path
- Spreadsheet ID: Prospects (selected via file browser)
- Sheet Name: Sheet1
- Table contains headers: Yes
- Row with headers: A1:Z1 (default)
- Limit: 20

Saved module settings. In the Choose where to start dialog:
selected All (processes existing rows first, then new ones).

### Step 7: Test the Trigger Module

1. Right-clicked Google Sheets module
2. Selected Run this module only
3. Output bubble appeared: 1 bundle processed
4. Clicked bubble — confirmed all 6 fields visible in output:
   - First Name, Last Name, Country, Email, Phone Number, Details
5. Data matched the sample row in the spreadsheet exactly

### Step 8: Add Slack Action Module

1. Clicked + to the right of Google Sheets module
2. Searched for Slack, selected Send a Message
3. Created Slack (user) OAuth2 connection
4. Authorised Make.com in the Slack workspace
5. Connection saved

### Step 9: Map Data Between Modules

Configured the Slack message:
- Channel: sales-team (Public channel, selected from list)
- Text field: mapped all 6 fields from the Google Sheets module

Final message template:
New prospect added! 🎉
Name: {{1.First Name}} {{1.Last Name}}
Email: {{1.Email}}
Country: {{1.Country}}
Phone: {{1.Phone Number}}
Details: {{1.Details}}
Mapping process: clicked each field in the mapping panel to insert
{{module_number.field_name}} variables into the message text.
First Name and Last Name placed on the same line with a space between them.

Saved module settings. Saved entire scenario.

### Step 10: Test the Complete Scenario

1. Right-clicked Google Sheets module → Choose where to start → All
2. Clicked Run once
3. Google Sheets module: green bubble showing 1 bundle processed
4. Slack module: green bubble showing 1 bundle processed
5. Opened Slack #sales-team channel
6. Confirmed notification received with all 6 fields correctly populated
7. Verified: data in Slack message matched spreadsheet row exactly

### Step 11: Activate the Scenario

Toggled scenario On. Make.com now monitors the Prospects spreadsheet
automatically and sends a Slack notification for every new row added.

---

## Understanding Make.com Concepts (Learned During Build)

### Bundles

A bundle is one set of data flowing through the scenario. One spreadsheet row =
one bundle. If 3 rows are added before the scenario runs, the Google Sheets trigger
outputs 3 bundles. Each bundle then passes independently through the Slack module,
resulting in 3 separate Slack notifications — one per prospect.

Credit consumption:
- Google Sheets trigger module: 1 credit per run (regardless of how many bundles output)
- Slack action module: 1 credit per bundle processed (3 rows = 3 credits)

### Trigger Types

- Polling triggers (like Watch New Rows): check for new data at scheduled intervals.
  Google Sheets is a polling trigger.
- Instant triggers: fire immediately via webhook when an event occurs.
  For real-time notifications, webhook-based triggers are needed.

### Connections

OAuth2 connections link Make.com to external apps. Once created, a connection is
reusable across all scenarios. One Google connection can be used in multiple
scenarios that read from Google Sheets, Drive, Forms, or Gmail.

---

## Why This Architecture?

### Why Google Sheets as the data source?

Google Sheets is the most common data entry tool for small sales teams. Most
SME clients already use it. It requires no additional software purchase, no
IT setup, and every team member knows how to add a row to a spreadsheet.
More importantly, connecting a spreadsheet to automation is the fastest way
to show a non-technical client what automation can do — they understand
spreadsheets, they see the notification arrive in Slack, and the value
proposition is immediately clear.

### Why Slack for notifications?

Slack is where sales teams already spend their working day. A notification in
the existing tool they watch constantly is far more effective than an email
that requires switching context. For clients already on Slack, this is the
right delivery channel. For clients not on Slack, the Email action module
(used in Project 07.2) is the equivalent choice.

### Why a polling trigger instead of instant?

Google Sheets does not support instant/webhook triggers in Make.com because
Google does not expose a native webhook for spreadsheet row additions.
Polling is the correct architecture for this data source. The 15-minute
latency is acceptable for most prospect notification use cases. For
true real-time notification, the data entry point should be changed —
for example, using a Google Form with a webhook trigger instead.

---

## Exam Relevance (AWS SAA-C03)

This is not an AWS project, but the concepts map directly to AWS architecture patterns.

| Make.com Concept | AWS Equivalent | SAA-C03 Relevance |
|-----------------|---------------|-------------------|
| Polling trigger | SQS polling / Lambda with scheduled EventBridge | Event-driven architecture |
| Instant trigger (webhook) | SNS → Lambda / API Gateway trigger | Push-based event processing |
| Bundle processing | SQS message processing | Queue-based decoupling |
| Connection (OAuth2) | IAM roles / Secrets Manager | Secure credential management |
| Make.com free tier ops limit | Lambda free tier invocations | Cost-aware architecture |

Understanding event-driven architecture from Make.com makes Lambda trigger
patterns click faster when you study them. The mental model is identical.

---

## Tools Used

### Make.com
- Plan: Free (1,000 operations/month)
- Scenario: New Prospect Notification
- Trigger: Google Sheets — Watch New Rows (polling, every 15 minutes)
- Action: Slack — Send a Message
- Operations per run: 1 (trigger) + N (1 per prospect row)
- Connection type: OAuth2 for both Google and Slack

### Google Sheets
- Spreadsheet: Prospects
- Columns: First Name, Last Name, Country, Email, Phone Number, Details
- Access: Read-only from Make.com
- Cost: Free

### Slack
- Channel: #sales-team (public)
- Access: User OAuth2 connection
- Cost: Free workspace

---

## Cost

| Resource | Monthly Cost | Notes |
|----------|-------------|-------|
| Make.com (free tier) | £0 | 1,000 ops/month |
| Google Sheets | £0 | Free |
| Slack (free workspace) | £0 | Free |
| **Total** | **£0/month** | Scales to ~£9/month (Make Core) at high volume |

---

## Business Value

| Client Type | Pain Removed | Value Delivered |
|-------------|-------------|-----------------|
| Small sales team (2–5) | Manual "did you see the new lead?" messages | Every new prospect auto-notified in Slack within 15 min |
| Recruitment agency | Manual checking of candidate spreadsheets | New candidate row → instant team notification |
| Event/conference team | Leads added to sheet during event go unnoticed | Real-time alerts during the event itself |
| Property management | New tenant enquiry logged in sheet | Letting manager alerted immediately |

**Setup time:** 60–90 minutes
**Suggested setup fee (post-ILR):** £150–£250
**Monthly support:** £0–£30/month
**Payback for client:** Single converted prospect covers setup cost

---

## Screenshots

| File | Description |
|------|-------------|
| day16-project71-slack-channel-created.png | #sales-team channel created in Slack |
| day16-project71-google-sheet-setup.png | Prospects spreadsheet with headers and sample row |
| day16-project71-scenario-builder.png | Make.com scenario builder — blank canvas renamed |
| day16-project71-google-sheets-module.png | Google Sheets Watch New Rows module added |
| day16-project71-connection-created.png | OAuth2 connection to Google created |
| day16-project71-trigger-configured.png | Trigger module configured with all settings |
| day16-project71-module-test-output.png | Module test output showing prospect bundle data |
| day16-project71-slack-module-added.png | Slack Send a Message module added and connected |
| day16-project71-data-mapped.png | Slack message text with all Google Sheets fields mapped |
| day16-project71-test-run-success.png | Full scenario run — green bubbles on both modules |
| day16-project71-slack-notification-received.png | Slack #sales-team showing the formatted notification |
| day16-project71-scenario-live.png | Scenario toggled On and running live |

---

*Built as part of the 104-week Cloud + AI Automation portfolio*
*GitHub: https://github.com/SadainHasan/cloud-ai-portfolio*
*Business: https://cloudflowautomations.co.uk*
---

## Architecture
