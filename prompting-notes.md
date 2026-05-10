# Prompt Engineering Techniques
# A Practical Guide for Cloud + AI Automation Consulting

A reference guide to 5 core prompting techniques for working
with AI models like Claude and GPT-4.
Built during a live AWS study session — every example is real.

Author: Khandaker Sadain Hasan
Role: Cloud + AI Automation Consultant (in progress)
Roadmap: AWS SAA → AZ-104 → AWS CSAP → AI Automation
Goal: Help UK SMEs reduce manual work through cloud and AI systems

---

## Technique 1 — Direct Prompting

### What It Is
Ask clearly and specifically. State exactly what you want,
who it is for, how many items, and what format.

### Rule
The more specific your input, the more useful the output.

### Basic Example
```
List 5 manual processes that small UK accountancy firms
could automate using AI tools like Make.com or n8n.
```

### Real Example From This Session
```
Give me a comparison table of EC2 On-Demand, Reserved,
and Spot purchasing options.
Include: cost, commitment, use case, and whether
it can be interrupted.
```

### Why It Worked
The prompt named the exact topic (EC2 purchasing options),
specified the exact columns (cost, commitment, use case,
interruption), and requested a specific format (table).
The result was a clean, structured, exam-ready table —
with no follow-up needed.

### When To Use
- Requesting structured information
- Asking for lists, tables, or comparisons
- Any time you know exactly what you need

---

## Technique 2 — Role-Based Prompting

### What It Is
Assign the AI a specific role before asking your question.
The AI adjusts its tone, depth, and vocabulary to match.

### Basic Example
```
You are a senior AWS solutions architect.
Explain the difference between EC2 and Lambda
to a non-technical SME business owner in 3 bullet points.
```

### Real Example From This Session
```
You are an AWS instructor teaching a student who spent
13 years as Head of IT at a financial services company
in Bangladesh. Explain EC2 Auto Scaling Groups using
an analogy from banking operations or financial systems.
```

### Why It Worked
By specifying both the role (AWS instructor) and the
student's background (13 years banking IT), the AI
produced a tailored explanation using teller windows,
branch staffing, and month-end surge analogies —
directly relevant to real experience.

### What It Produced
- Teller windows = EC2 instances
- Calling in extra staff = Scaling Out
- Sending staff home = Scaling In
- Staff contract template = Launch Template
- Branch manager = Auto Scaling Policy

### When To Use
- When you want explanations tailored to your background
- When presenting ideas to a specific audience
  (technical team, non-technical client, board level)
- When building client-facing materials in consulting

---

## Technique 3 — Chain-of-Thought Prompting

### What It Is
Tell the AI to think step by step before answering.
Forces deeper reasoning and reduces shallow or wrong answers.

### Trigger Phrases
- "Think step by step"
- "Walk me through your reasoning"
- "Starting from... explain what happens at each stage"

### Basic Example
```
A retail business receives 200 orders per day by email
and enters them manually into a spreadsheet.
Think step by step about how to automate this
using Make.com and Google Sheets.
```

### Real Example From This Session
```
Explain how an EC2 Auto Scaling Group works.
Think step by step, starting from what happens when
a user visits a website that uses Auto Scaling.
```

### Why It Worked
Instead of a vague overview, the AI produced a
complete 9-step walkthrough covering:
- Step 1: User types the URL
- Step 2: Request hits the Load Balancer
- Step 3: EC2 instance handles the request
- Step 4: Traffic grows, CloudWatch monitors
- Step 5: Alarm triggers at 70% CPU
- Step 6: New instances launch from Launch Template
- Step 7: Health check passes, traffic flows
- Step 8: Traffic drops, instances terminated
- Step 9: Instance fails at 2am, replaced automatically

### When To Use
- Learning how a system works end to end
- Designing automation workflows for clients
- Debugging problems (walk through what went wrong)
- Preparing for technical interviews

---

## Technique 4 — Format-Specific Prompting

### What It Is
Tell the AI exactly what format you want the output in.
Different formats suit different purposes.

### Available Formats To Request
| Format | Best Used For |
|---|---|
| Table | Comparisons, feature lists |
| Bullet points | Quick summaries |
| Step-by-step | Tutorials, SOPs, workflows |
| JSON | Automation pipelines, APIs |
| Email draft | Client communication |
| 3 sentences | Quick definitions |
| Analogy | Explaining complex concepts simply |

### Basic Example
```
List the top 5 AWS services used in fintech, formatted
as a table with columns:
Service | Use Case | Why Fintech Uses It
```

### Real Example From This Session
```
Explain what an EC2 Auto Scaling Group is in 3 sentences.
```

### What It Produced
A clean 3-sentence definition — no padding, no waffle.
Exactly the right length for a quick revision card
or a client-facing explanation.

### Advanced Example — JSON Output
```
Generate a JSON structure for a client onboarding form
for a small accounting firm. Include: name, email,
business type, monthly turnover, current tools used.
```

### When To Use
- When you need output in a specific structure
- When building automation workflows that need JSON
- When preparing client-ready documents or emails
- When you want exam-style revision answers

---

## Technique 5 — Iterative Refinement

### What It Is
Start with a good prompt, then improve the output
step by step. Your first prompt is never your best.
Refine like a developer refines code.

### Basic Example
```
Round 1: Write an email offering automation consulting
services to a small UK business owner.

Round 2: Make it shorter and add a specific example
of time saved per week.

Round 3: Rewrite it as if the consultant has already
helped 3 UK-based SMEs reduce admin by 40%.
```

### Real Example From This Session

Round 1 — Direct prompt:
```
Give me a comparison table of EC2 On-Demand, Reserved,
and Spot purchasing options. Include: cost, commitment,
use case, and whether it can be interrupted.
```

Round 2 — Iterative refinement:
```
Now add one real-world example from a bank or
financial institution for each row.
```

### Why It Worked
Round 1 produced a clean, structured comparison table.
Round 2 added HSBC, Barclays, and Standard Chartered
real-world examples that made the table exam-ready
and client-presentation ready — without rebuilding
the whole prompt from scratch.

### What Round 2 Added
- HSBC fraud investigation → On-Demand
- Barclays core banking platform → Reserved Instance
- Standard Chartered month-end risk reports → Spot

### The Consulting Mindset
Every client deliverable goes through iterations.
First draft → get the structure right.
Second draft → add specificity and examples.
Third draft → polish for the audience.
AI-assisted iteration makes this 10x faster.

### When To Use
- Building any client-facing document
- Improving exam answers or study notes
- Refining automation workflow designs
- Turning a rough idea into a polished output

---

## How All 5 Techniques Work Together

The most powerful prompts combine multiple techniques:

```
[Role]     You are a UK-based cloud automation consultant.

[Direct]   A solicitor's firm wants to automate
           client intake and document processing.

[CoT]      Think step by step about the best workflow
           using n8n, AWS S3, and Claude API.

[Format]   Present your answer as a numbered
           step-by-step implementation plan with
           estimated time savings per week.

[Iterate]  → Refine: Make it suitable for presenting
           to a non-technical office manager.
```

---

## Prompting Lessons From This AWS Study Session

1. Role-based prompting produces personalised explanations
   that connect new concepts to existing experience

2. Chain-of-thought prompting turns vague topics into
   complete step-by-step technical walkthroughs

3. Format-specific prompting controls output length and
   structure — 3 sentences vs full table vs JSON

4. Iterative refinement builds better outputs layer by layer
   without rewriting prompts from scratch

5. Combining techniques produces consultant-grade outputs
   that are ready for clients or exam revision

---

## Session Notes — AWS Concepts Explained Via Prompting

| Concept | Technique Used | Output Quality |
|---|---|---|
| EC2 explained simply | Direct + Role-based | Banking analogy |
| Auto Scaling Groups | Role-based | Teller window analogy |
| ASG step-by-step | Chain-of-thought | 9-step walkthrough |
| Purchasing options | Format-specific | Clean comparison table |
| Banking examples added | Iterative refinement | HSBC, Barclays, StanChart |

---

*Updated: May 2026*
*Part of a 104-week Cloud + AI Automation roadmap*
*Repository: github.com/SadainHasan/cloud-ai-portfolio*
