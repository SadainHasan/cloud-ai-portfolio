# Claude API Study Assistant

**Status:** ✅ Live — Command-line tool
**Built:** Tuesday 19 May 2026
**Author:** Hasan (Khandaker Sadain Hasan) — Cloud + AI Automation Consultant
**GitHub:** https://github.com/SadainHasan/cloud-ai-portfolio
**Portfolio site:** https://d2ven7lubrbrhs.cloudfront.net
**Business:** https://cloudflowautomations.co.uk

---

## What Problem Does This Solve?

Every small business owner or team leader who wants to use AI in their workflows 
faces the same problem: they can use Claude.ai in a browser, but they cannot 
integrate it into their own systems, scripts, or automations. The Claude API 
bridges that gap — it turns Claude from a chatbot into a programmable tool.

For an SME owner, this unlocks scenarios like:

- A letting agent who wants to auto-draft tenancy agreement summaries when a 
  new contract PDF arrives
- A clinic manager who wants patient intake forms processed and categorised 
  automatically
- A warehouse team who wants inbound delivery emails parsed and logged to 
  a spreadsheet without manual data entry

This study assistant is a simple but real demonstration of that capability. 
It shows that Claude can be given a specific persona, domain expertise, and 
output format — and then called programmatically from any Python script, 
n8n workflow, or automation pipeline.

The business value is not the study assistant itself. The business value is 
that this code pattern — system prompt + user input + structured response — 
is the foundation of every AI-powered tool in the portfolio.

---

## What This Is

A command-line Python application that wraps the Anthropic Claude API in a 
specialist persona for AWS SAA-C03 exam coaching. The user types a cloud 
computing question, the script sends it to Claude with a carefully crafted 
system prompt, and Claude responds as "AWS Maya" — an exam-focused tutor 
who connects concepts to banking and financial services analogies.

The project demonstrates two skills clients pay for:

1. **API integration** — calling a third-party AI service from Python with 
   proper authentication, error handling, and model selection
2. **Prompt engineering** — crafting a system prompt that shapes Claude's 
   persona, output format, and domain expertise to produce consistent, 
   useful responses

Both scripts in this folder are production-quality: they read API keys from 
environment variables (never hardcoded), handle API errors gracefully, and 
include clear comments explaining every design decision.

---

## Architecture

```
User (terminal)
      │
      ▼
claude_study_assistant.py
      │
      │  1. Reads ANTHROPIC_API_KEY from environment
      │  2. Sends system prompt + user question via HTTPS
      ▼
Anthropic API
(api.anthropic.com)
      │
      │  3. Returns Claude response (JSON)
      ▼
claude_study_assistant.py
      │
      │  4. Extracts text from response
      │  5. Prints to terminal
      │  6. Optionally saves to session log file
      ▼
User sees answer
```

**No AWS resources required.** This project runs entirely on your local 
machine using the Anthropic API. The only external dependency is the 
`anthropic` Python library and an active API key.

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `basic_claude_call.py` | Minimal proof-of-concept — one question, one answer |
| `claude_study_assistant.py` | Full interactive study assistant with system prompt, error handling, and session logging |

---

## Steps

### Prerequisites

- Python 3.10 or higher installed
- pip package manager available
- Anthropic account at console.anthropic.com
- API key stored as environment variable `ANTHROPIC_API_KEY`

### Step 1 — Get an API Key

1. Go to `https://console.anthropic.com`
2. Sign in or create a free account
3. Navigate to **API Keys** in the left sidebar
4. Click **Create Key**
5. Name it (e.g., `study-assistant-2026`)
6. Copy the key — it starts with `sk-ant-api03-`
7. You will only see it once. Copy it now.

**Security rule:** Never paste this key directly into Python code. 
Never commit it to GitHub. Always use environment variables.

### Step 2 — Store Key as Environment Variable

**Windows (temporary, current session only):**
```cmd
set ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

**Windows (permanent, all future sessions):**
1. Search "Environment Variables" in Windows Start menu
2. Click "Edit the system environment variables"
3. Click "Environment Variables..."
4. Under "User variables", click "New"
5. Variable name: `ANTHROPIC_API_KEY`
6. Variable value: paste your key
7. Click OK three times

### Step 3 — Install the SDK

```cmd
pip install anthropic
```

Verify:
```cmd
pip show anthropic
```

### Step 4 — Run the Basic Script

```cmd
python basic_claude_call.py
```

Expected output: Claude's explanation of S3 lifecycle rules in 3 bullet points, 
printed to your terminal within 3-5 seconds.

### Step 5 — Run the Study Assistant

```cmd
python claude_study_assistant.py
```

You will see a welcome banner. Type any cloud computing question and press Enter.

**Example questions to try:**
- `What is the difference between S3 Standard-IA and S3 One Zone-IA?`
- `When should I use Aurora instead of RDS MySQL?`
- `Explain the difference between Security Groups and NACLs`
- `What is S3 Transfer Acceleration and when would I use it?`

Type `help` to see more examples. Type `quit` to exit.

At the end of the session, you can save a log file of all your questions and answers.

---

## Why This Architecture?

### Why claude-haiku-4-5-20251001 and not a larger model?

Claude Haiku is the most cost-efficient model in the Anthropic lineup. For a 
study assistant that asks factual, domain-specific questions with short expected 
answers, Haiku produces responses that are indistinguishable in quality from 
Sonnet or Opus for this use case. The cost difference is significant:

- Haiku: ~$0.00025 per 1,000 input tokens
- Sonnet: ~$0.003 per 1,000 input tokens
- Opus: ~$0.015 per 1,000 input tokens

A typical study question plus system prompt is approximately 300-400 tokens. 
At 50 questions per session, Haiku costs less than £0.01. Opus would cost 
roughly 60 times more for identical output quality on this task. Cost-aware 
model selection is a skill clients pay for.

### Why a system prompt?

Without a system prompt, Claude gives generic answers. With the "AWS Maya" 
system prompt, Claude:

- Flags exam traps explicitly
- Connects every answer to Hasan's banking background
- Ends every response with a formatted exam tip
- Stays under 250 words (preventing token waste)

This is prompt engineering — shaping the AI's behaviour through instructions 
rather than code. It is one of the highest-value skills in AI consulting because 
it requires no additional infrastructure, just careful thinking about what the 
model should and should not do.

### Why environment variables for the API key?

API keys are credentials. If you hardcode `api_key="sk-ant-..."` in your Python 
file and commit that file to GitHub, your key is permanently exposed in git 
history — even if you delete the line later. Any automated scanner can find it 
in seconds. Anthropic automatically revokes keys found on GitHub, but the 
damage (unexpected charges, compromised applications) may already be done.

Environment variables keep credentials out of code entirely. They are also the 
standard approach used in production AWS environments — Lambda functions, EC2 
instances, and ECS containers all receive credentials through environment 
variables or IAM roles, never hardcoded.

### Why handle API errors explicitly?

The three most common API errors are:
1. `APIConnectionError` — no internet, or API is down
2. `AuthenticationError` — wrong or expired API key
3. `RateLimitError` — too many requests in a short time

Without explicit handling, any of these crashes the script with a Python 
traceback that confuses non-technical users. With explicit handling, the user 
gets a clear, actionable error message. When you build tools for SME clients, 
robust error handling is the difference between a professional product and an 
amateur prototype.

---

## Exam Relevance (AWS SAA-C03)

This project is not directly tested in the AWS SAA-C03 exam, but it builds 
skills that underpin several exam topic areas:

| Exam Topic | Connection | Likely Scenario |
|------------|-----------|----------------|
| AWS Lambda | Claude API calls follow the same serverless pattern: event in → process → response out | "A company wants to process incoming data without managing servers..." |
| API Gateway | The Anthropic API uses REST endpoints — same pattern as AWS API Gateway | "Design a serverless API that calls a third-party service..." |
| IAM / Secrets Manager | API key management mirrors IAM key rotation and Secrets Manager | "How should an application store database credentials securely?" |
| Cost Optimisation | Model selection (Haiku vs Opus) mirrors EC2 instance family selection | "Which approach minimises cost while meeting performance requirements?" |

---

## AWS Services Used

**None** — this project runs entirely on your local machine. No AWS resources 
are required or created. The only cost is Anthropic API usage.

This is intentional: it demonstrates that AI capabilities can be added to any 
workflow without AWS infrastructure, which is often the right answer for small 
SME clients who do not have AWS accounts.

---

## Cost

| Resource | Cost per session (50 questions) | Notes |
|----------|--------------------------------|-------|
| Claude Haiku API | ~£0.005–0.01 | ~350 tokens per question × 50 = 17,500 tokens |
| Anthropic account | £0 (free tier available) | Free tier includes $5 credit for new accounts |
| Python / local machine | £0 | Runs on any laptop |
| **Total** | **~£0.01 per session** | Cheaper than a cup of tea |

**Cost control:** `max_tokens=600` on the study assistant prevents runaway 
costs if Claude attempts to write an unexpectedly long answer.

---

## Business Value

This project directly maps to a service you can offer to SME clients 
**after ILR is granted in October 2027:**

| Client Type | What They Get | One-Off Setup Fee | Monthly Support |
|-------------|--------------|-------------------|----------------|
| Estate agents | AI assistant trained on tenancy law FAQs | £400-600 | £50-80/month |
| GP practices | Patient FAQ bot trained on clinic protocols | £500-800 | £80-100/month |
| Law firms | Legal research assistant for common queries | £600-1,000 | £100-150/month |
| Letting agencies | Tenant communication drafting tool | £300-500 | £40-60/month |

The underlying pattern is identical to this study assistant: system prompt 
defines the domain, API call fetches the answer, output is formatted for the 
client's context. The code complexity is low; the value is in understanding 
the client's domain well enough to write the right system prompt.

---

## Screenshots

| File | Description |
|------|-------------|
| ![API key created](screenshots/day19-api-key-created.png) | Anthropic console showing the new API key in Active status |
| ![Environment variable set](screenshots/day19-env-variable-set.png) | Windows command prompt showing ANTHROPIC_API_KEY confirmed |
| ![Library installed](screenshots/day19-anthropic-installed.png) | pip show anthropic confirming successful installation |
| ![Basic call output](screenshots/day19-basic-call-output.png) | Terminal output of basic_claude_call.py answering S3 lifecycle question |
| ![Study assistant running](screenshots/day19-study-assistant-running.png) | Study assistant banner and first question/answer in terminal |
| ![Session in progress](screenshots/day19-study-assistant-session.png) | Multiple questions answered in a single session |
| ![GitHub push](screenshots/day19-github-push.png) | Git commit and push confirmation |

---

## Lessons Learned

Working with the Claude API for the first time, the most important realisation 
is that **the system prompt is the product**. The Python code is 50 lines and 
largely boilerplate. The system prompt is where all the design thinking goes — 
who is Claude speaking to, what tone, what format, what constraints, what 
domain knowledge to emphasise.

This mirrors something I observed in banking IT: the configuration of a system 
is often more valuable than the system itself. A generic trade settlement engine 
configured for a specific regulatory regime is worth far more than the same 
engine with no configuration. Claude without a system prompt is a general engine. 
Claude with a well-designed system prompt is a specialist tool.

---

*Day 19 of 730 — Week 3, Day 5 — Cloud + AI Automation Specialist*
*github.com/SadainHasan/cloud-ai-portfolio | cloudflowautomations.co.uk*
