# Study Log — Cloud + AI Automation Specialist Plan

**Name:** Khandaker Sadain Hasan  
**Location:** Leicester, UK  
**Plan:** 104-week Cloud + AI Automation Specialist programme  
**Start date:** 01 May 2026  
**AWS SAA target:** October 2026  

This log records daily study activity as evidence of consistent 
learning throughout a structured 24-month cloud certification 
and portfolio-building programme.

---

## Week 1 — 01 May to 07 May 2026
**Theme:** AWS Compute Fundamentals + AI Foundations + Environment Setup

---

### Day 1 — Friday 01 May 2026

**Topic studied:** Environment setup — AWS, GitHub, VS Code, AWS CLI

**What I did:**
- Created AWS account and set $10 billing alarm
- Created GitHub account and cloud-ai-portfolio repository
- Installed VS Code with AWS Toolkit and Python extensions
- Installed and configured AWS CLI with IAM credentials
- Created project-01-portfolio-site folder and README on GitHub

**What I built:**
- GitHub repository: cloud-ai-portfolio
- project-01-portfolio-site README (in progress)

**Key things learned:**
- AWS billing alarm setup to protect free tier
- AWS CLI configured with Access Key and Secret Key
- GitHub repo structure for a professional portfolio

**Still unsure about:**
- Nothing major today — setup day went smoothly

**Anki cards added:** 0 (setup day — cards start Day 3)

---

### Day 2 — Saturday 02 May 2026

**Topic studied:** AI foundations — Claude prompt engineering

**What I did:**
- Set up claude.ai account
- Practised 5 prompt techniques: direct, role-based, 
  chain-of-thought, format-specific, iterative refinement
- Explored Claude vs ChatGPT differences
- Added prompting-notes.md to GitHub

**What I built:**
- prompting-notes.md — documented all 5 prompt techniques with examples

**Key things learned:**
- Role-based prompting produces significantly better results 
  when context (banking IT background) is included
- Claude has longer context window than ChatGPT — better for 
  technical explanations
- Format-specific prompts (ask for tables) faster to read and memorise

**Still unsure about:**
- Claude Projects feature — will set up properly on Day 5

**Anki cards added:** 0 (AI day — AWS cards start Day 3)

---

### Day 3 — Sunday 03 May 2026

**Topic studied:** Amazon EC2 fundamentals

**What I did:**
- Watched EC2 section of AWS SAA course (Digital Cloud Training)
- Launched first EC2 instance: t3.micro, Amazon Linux 2023
- Created key pair (my-keypair.pem)
- Connected via EC2 Instance Connect in browser
- Ran basic Linux commands: ls, whoami, pwd
- Stopped instance after learning (important — free tier)
- Read DCT training notes: EC2 pp.11-16

**What I built:**
- project-02-ec2-auto-scaling folder and README on GitHub
- Screenshot of running EC2 instance added to GitHub

**Key things learned:**
- EC2 = virtual server in the cloud. AMI = template to launch it
- Stop vs Terminate: Stop preserves EBS volume, Terminate deletes it
- t2.micro = free tier eligible (750 hrs/month for 12 months)
- 5 instance type categories: General Purpose, Compute Optimised, 
  Memory Optimised, Accelerated Computing, Storage Optimised
- EBS = the network-attached hard drive on EC2 (8GB by default)

**Still unsure about:**
- AMI creation process — will cover Day 6
- Auto Scaling Groups — coming Week 2

**Anki cards added:** 0

---

### Day 4 — Monday 04 May 2026

**Topic studied:** Revision day + Anki setup

**What I did:**
- Set up Anki account at ankiweb.net
- Installed Anki desktop and AnkiDroid on phone
- Created AWS SAA Study deck
- Added Cards 1-13 covering Days 1-3 content
- Answered 5 revision questions without notes
- Synced Anki between desktop and phone
- Checked AWS billing dashboard ($0 spend confirmed)

**What I built:**
- Anki deck: AWS SAA Study (13 cards)

**Key things learned:**
- Spaced repetition: Anki shows cards just before you forget them
- Syncing between desktop and phone keeps revision going 
  during care shifts

**Still unsure about:**
- Difference between Standard and Convertible Reserved Instances
- Will add this to Anki tomorrow

**Anki cards added:** Cards 1-13

---

### Day 5 — Tuesday 05 May 2026

**Topic studied:** AI tools — Claude prompt engineering deep dive + ASG intro

**What I did:**
- Practised all 5 Claude prompt techniques in claude.ai
- Set up Claude Project with full background context
- Used Claude to generate Anki cards on Auto Scaling
- Added Cards 14-19 covering ASG and ELB topics
- Decided to delay Claude API to Week 10 
  (API requires payment — not needed for learning stage)
- Added study-log.md to GitHub (this file)

**What I built:**
- Claude Project: AWS SAA Study (persistent context across chats)
- study-log.md on GitHub (this file)
- Anki cards 14-19 on Auto Scaling and Load Balancing

**Key things learned:**
- Claude role-based prompts using banking background produce 
  much more relevant explanations
- Claude Projects remembers your context — no need to 
  re-explain background each session
- ASG: Min/Desired/Max settings, 4 scaling policy types
- ALB (Layer 7, HTTP) vs NLB (Layer 4, TCP, extreme performance)
- EC2 health checks vs ELB health checks in ASG

**Still unsure about:**
- Step Scaling vs Simple Scaling — need to review difference
- Will check Card 16 back content covers all 4 policy types

**Anki cards added:** Cards 14-19 (ASG, ELB, CIDR)

---

### Day 6 — Wednesday 06 May 2026

**Topic studied:** AMI deep dive, EBS Snapshots, ELB introduction

**What I did:**
- Read DCT training notes: AMI pp.13-14, EBS Snapshots pp.31-37, 
  ELB pp.38-43
- Created first custom AMI (my-first-ami) from EC2 instance
- Created first EBS Snapshot from 8GB root volume
- Explored ELB console — reviewed all 4 load balancer types
- Added 5 Anki cards on AMI, snapshots, and ELB

**What I built:**
- Custom AMI: my-first-ami (Amazon Linux 2023, eu-west-2)
- EBS Snapshot: my-first-snapshot
- Updated project-02-ec2-auto-scaling README checklist
- Architecture diagram: project-02-architecture.png 
  (draw.io export — Internet > ALB > Auto Scaling Group)
  
**Key things learned:**
- EBS-backed AMI: must stop instance first. Persistent storage.
- Instance store-backed AMI: cannot stop, data lost on termination
- Snapshots are incremental — only changed blocks saved after first
- Snapshots are region-specific, EBS volumes are AZ-specific
- Use DLM (Data Lifecycle Manager) to automate snapshot backups
- ALB = Layer 7 HTTP/HTTPS content routing
- NLB = Layer 4 TCP/UDP extreme performance static IP
- GLB = Layer 3/4 for security appliances (firewalls, IDS)

**Still unsure about:**
- ELB cross-zone load balancing — need to read more
- When to use GLB vs WAF for security — will ask AWS Maya

**Anki cards added:** Cards 20-25

---

### Day 7 — Thursday 07 May 2026

**Topic studied:** Build day — Project 1 complete

**What I did:**
- Built complete S3 + CloudFront portfolio website
- Created S3 bucket with static website hosting
- Uploaded index.html portfolio page
- Created CloudFront distribution with HTTPS
- Site is now live at https://d2ven7lubrbrhs.cloudfront.net
- Added screenshots to GitHub README

**What I built:**
- Live portfolio website: https://d2ven7lubrbrhs.cloudfront.net
- project-01-portfolio-site fully documented on GitHub
- 3 screenshots added to project README

**Key things learned:**
- S3 static hosting serves HTML but needs bucket policy for public access
- CloudFront adds HTTPS, caching, and global edge delivery
- CloudFront deployment takes 5-15 minutes to propagate globally
- Redirect HTTP to HTTPS is best practice — always enable this
- Price class: North America and Europe sufficient for UK portfolio

**Still unsure about:**
- Origin Access Control (OAC) — want to add this next
- Route 53 custom domain setup — future task

**Anki cards added:** Cards 25-29

---

## Week 2 — 08 May to 14 May 2026
**Theme:** AWS VPC Networking Deep Dive

---

### Day 8 — Thursday 08 May 2026

**Topic studied:** VPC fundamentals — 
custom VPC, subnets, Internet Gateway, route tables

**What I did:**
- Read DCT training notes: VPC pp.117-125
- Created custom VPC (my-custom-vpc, 10.0.0.0/16)
- Created 4 subnets across 2 AZs (2 public, 2 private)
- Created and attached Internet Gateway (my-igw)
- Created public route table with 0.0.0.0/0 → IGW route
- Enabled auto-assign public IP on public subnets
- Created Project 03 on GitHub with full documentation

**What I built:**
- Custom VPC with complete subnet architecture
- project-03-vpc-network on GitHub with README and screenshots

**Key things learned:**
- VPC = isolated private cloud network within one region
- Public subnet = has route to IGW. Private = no route to IGW
- AWS reserves 5 IPs per subnet — /24 = 251 usable
- One Internet Gateway per VPC maximum — free resource
- Route table controls traffic routing per subnet
- High availability = subnets in minimum 2 AZs

**Still unsure about:**
- NAT Gateway — how private subnets access internet outbound
- Security Groups vs NACLs — will cover Day 10
- VPC peering — will cover Week 5

**Anki cards added:** Cards 31-35

---

### Day 9 — Saturday 09 May 2026

**Topic studied:** AI automation — n8n installation 
and workflow building

**What I did:**
- Installed n8n on Windows via npm
- Created n8n account at localhost:5678
- Built Workflow 1: Leicester Weather Daily
  - Schedule Trigger → HTTP Request (Open-Meteo API)
  - → Code in JavaScript → Send an Email (SMTP)
  - Gmail SMTP configured with App Password (Port 465)
  - Email received and verified at 9:20pm ✅
  - Workflow set to Active — 8:00am daily
- Built Workflow 2: Study Progress Tracker
  - Execute Workflow → Edit Fields → IF
  - → Edit Fields1 (true) / Edit Fields2 (false)
  - True branch ran correctly (cards=40 >= 30) ✅
  - Both branches tested and verified ✅
- Created Project 06 on GitHub with full README
- All 3 screenshots uploaded to GitHub

**What I built:**
- n8n Workflow 1: Leicester Weather Daily (ACTIVE ✅)
- n8n Workflow 2: Study Progress Tracker (tested ✅)
- project-06-n8n-automation fully documented

**Key things learned:**
- n8n workflow pattern: trigger → process → output
- HTTP Request calls any public API — no code needed
- Code in JavaScript transforms raw JSON into readable text
- Gmail SMTP needs App Password — Port 465 SSL/TLS
- IF node = true/false conditional logic
- Edit Fields (Set) creates data that flows to next nodes
- n8n auto-saves — Publish = activate not save
- Expression {{ $json.field }} links node data together

**Still unsure about:**
- Error handling — what if HTTP Request fails?
- Deploying n8n on AWS EC2 for 24/7 availability

**Anki cards added:** Cards 35-42
**Deck total:** 42 cards ✅

---

### Day 10 — Sunday 10 May 2026

**Topic studied:** NAT Gateway, Security Groups, NACLs
**DCT Book:** pp.121-124

**What I did:**
- Read DCT book: NAT Instances p.121, NAT Gateways pp.122-123,
  Security Groups p.123, Network ACLs p.124
- Created NAT Gateway in public-subnet-1
- Allocated Elastic IP for NAT Gateway
- Updated private route table: 0.0.0.0/0 → NAT Gateway
- Created Security Group: web-server-sg
  Inbound: HTTP 80, HTTPS 443, SSH 22 (My IP only)
  Outbound: All traffic (default)
- Created custom NACL: my-custom-nacl
  Inbound rules: 100 Allow 80, 110 Allow 443, 120 Allow 1024-65535
  Outbound rules: 100 Allow 80, 110 Allow 443, 120 Allow 1024-65535
- Updated VPC architecture diagram to v2 on draw.io
- DELETED NAT Gateway and released Elastic IP same session ✅

**What I built:**
- NAT Gateway — created, learned, DELETED same session ✅
- Security Group: web-server-sg in my-custom-vpc
- Custom NACL: my-custom-nacl with full rules
- VPC architecture diagram v2 uploaded to GitHub

**Key things learned:**
- NAT Gateway = AWS managed, public subnet, IPv4 only,
  cannot associate SG, cannot use as bastion, 45 Gbps max
- NAT Instance = you manage, less reliable, needs SG,
  must disable source/dest check, can be bastion host
- SG = stateful, instance level, allow rules only,
  implicit deny, all rules evaluated, cannot block IPs
- NACL = stateless, subnet level, allow AND deny,
  number order evaluation, separate in/out rules,
  default allows all, custom denies all
- Ephemeral ports 1024-65535 must be in NACL outbound
  because NACLs are stateless — responses need explicit allow
- NACL = first line of defence. SG = second line.
- Memory trick: SG = Stateful Security guard.
  NACL = No memory Checkpoint Lane.

**Still unsure about:**
- VPC peering — will cover in later weeks

**Anki cards added:** Cards 43-47

---

### Day 11 — Monday 11 May 2026

**Topic:** Revision day — Week 2 review + community research

**What I did:**
- Full Anki review — all 47 cards
- 15 VPC practice questions on ExamTopics
- Answered 20 revision questions without notes
- Researched Leicester community organisations on lcvs.org.uk
- Found [number] potential organisations — noted in Notion
- Added business value paragraphs to Projects 01, 02, 03

**Practice questions:**
- Attempted: 15 VPC questions
- Score: [your score]/15
- Weak areas identified: [topics you got wrong]

**Community research:**
- Found [number] organisations on lcvs.org.uk
- Will contact Day 14 (Wednesday 14 May)

**Anki cards added:** Card 48 (SAA exam format)
**Deck total:** 48 cards

---

### Day 12 — Tuesday 12 May 2026

**Topic studied:** AI/Claude — n8n advanced + OpenAI API
**DCT Book:** Elastic IP p.18 (revision note)

**What I did:**
- Set up OpenAI API account at platform.openai.com
- Added $5 credit — enough for months of learning
- Created API key: n8n-learning
- Enhanced Workflow 1: added OpenAI GPT-4o-mini node
  - Weather data now summarised as friendly AI briefing
  - Tailored for care professional working outdoors ✅
- Built Workflow 3: Email Summariser to Google Sheets
  - Manual Trigger → Set (email input) → OpenAI → Google Sheets
  - AI generates 3-bullet summary of business email
  - Summary saved to Google Sheets automatically ✅
- Updated Project 06 GitHub README and screenshots

**What I built:**
- OpenAI API account with $5 credit
- Workflow 1 enhanced with AI briefing
- Workflow 3: Email Summariser → Google Sheets (complete)
- Project 06 README updated with new sections

**Key things learned:**
- OpenAI API: pay per use, GPT-4o-mini is cheapest model
- $5 = approximately 60,000 summarisation requests
- n8n OpenAI node: Resource=Chat, Operation=Message a Model
- Expression syntax connects OpenAI output to next node:
  {{$('OpenAI').first().json.message.content}}
- Google Sheets node: Append or Update Row operation
- Column mapping uses expressions to reference previous nodes
- This workflow pattern (input → AI → output) is the 
  foundation of every AI automation product

**Still unsure about:**
- How to trigger the Email Summariser from a real incoming
  email automatically — will explore Email Trigger node

**Anki cards added:** Cards 49-51

---

### Day 13 — Wednesday 13 May 2026

**Topic studied:** AWS Cloud — S3 + CloudFront + Route 53 + ACM
**DCT Book:** Route 53, ACM, CloudFront, S3 static hosting — pages 135–149

**What I did:**
- Created private S3 bucket cloudflow-automations-website (eu-west-2)
- Uploaded index.html and 4 SVG logo files to the bucket
- Switched to us-east-1 and requested ACM certificate for cloudflowautomations.co.uk
- Validated certificate with one click via Route 53 — status: Issued ✅
- Created CloudFront distribution with OAC (origin access control)
- Pasted OAC bucket policy into S3 — CloudFront now has signed access ✅
- Added alternate domain names and ACM certificate to CloudFront
- Set index.html as default root object
- Created Route 53 Alias A records for zone apex and www
- Confirmed site live at https://cloudflowautomations.co.uk ✅
- Drew architecture diagram in draw.io
- Built Project 07 README and uploaded screenshots to GitHub

**What I built:**
- Project 07: Cloudflow Automations website — fully live in production
- URL: https://cloudflowautomations.co.uk
- Architecture: IONOS → Route 53 (Alias A) → CloudFront (OAC) → S3 (private)
- Custom SVG logo + Under Construction banner deployed

**Key things learned:**
- ACM certificate for CloudFront MUST be in us-east-1 — not the same
  region as your S3 bucket. This is the most common mistake and a
  favourite SAA exam question
- Alias A record is free and works at the zone apex (root domain).
  CNAME cannot be used at the root domain — DNS specification forbids it.
  This is another frequent SAA exam question
- OAC is the modern replacement for OAI. OAC signs requests with SigV4
  and locks the bucket policy to your specific distribution ARN
- If you forget to set the Default Root Object (index.html) in CloudFront,
  visiting the root URL returns a 403. Very easy to miss
- CloudFront SSL changes take 10–15 minutes to propagate to all edge
  locations. Testing the raw .cloudfront.net URL confirms CloudFront is
  working while you wait for the custom domain SSL to propagate
- The full architecture cost: approximately $0.57/month. Enterprise-grade
  setup for less than a cup of coffee

**Still unsure about:**
- How CloudFront handles cache invalidations at scale — will explore
  invalidation strategies and TTL management in a later session

**Anki cards added:** Cards 52–59
**Deck total: 59 cards** ✅

---
### Day 14
**Anki cards added:** Cards 60–62
**Deck total: 62 cards** ✅
---
## Day 15 — Friday 15 May 2026
**Topic:** AWS S3 — Storage Classes, Lifecycle Rules, Versioning
**Category:** AWS / CLOUD (Blue day)
**Time spent:** 90 min

**What I did:**
- Watched S3 section of DCT SAA course
- Created S3 bucket `hasan-s3-lifecycle-demo-2026` in eu-west-2
- Uploaded 10 test files
- Configured lifecycle rule: Standard → IA (30d) → Glacier (90d) → Delete (365d)
- Enabled versioning and tested with a re-upload and a delete operation
- Observed DELETE marker behaviour — soft delete with versioning enabled
- Started Project 5 on GitHub

**Key things I learned:**
- 6 S3 storage classes and when to use each
- Lifecycle rules are XML applied at bucket level — configured via console
- Objects must be in Standard for 30 days before transitioning to IA
- Objects smaller than 128KB do not benefit from IA transition
- Versioning cannot be disabled once enabled — only suspended
- DELETE with versioning = DELETE marker, not permanent deletion

**What I am still unsure about:**
- 

**Anki cards added:** 3 (Running total: ~66)
**GitHub commits:** 2

---

## Day 16 — Saturday 16 May 2026

**Topic:** Make.com — Visual Automation Workflows
**Category:** PURPLE — AI / Claude
**Time spent:** 90 minutes
**Week:** 3, Day 2

### What I built today
- Project 07.1: Google Sheets → Slack sales notification (Make.com official tutorial)
- Project 07.2: Google Forms → Gmail enquiry automation

### Key things I learned
- Make.com core vocabulary: Scenario, Module, Operation, Bundle, Trigger, Action
- Polling triggers vs instant/webhook triggers and when to use each
- Data mapping syntax: {{module_number.field_name}}
- How credits are consumed: trigger = 1 credit/run; action = 1 credit/bundle
- Practical difference between n8n (power/privacy) and Make.com (simplicity/client-friendly)

### What confused me
- Credit consumption difference between trigger and action modules
- How to choose between polling and webhook triggers for a given client

---
## Day 17 — Sunday 17 May 2026

**Topic:** Python + boto3 — Automate AWS with Code
**Category:** GREEN — Build Project
**Time spent:** 90 minutes
**Week:** 3, Day 3

### What I built
- list_ec2.py — lists all EC2 instances with state
- list_s3.py — lists all S3 buckets
- create_bucket.py — creates a bucket programmatically
- cost_audit.py — Project 08, flags stopped EC2 instances > 7 days

### Key things I learned
- boto3 uses the same credentials as the AWS CLI (~/.aws/credentials)
- describe_instances() returns Reservations → Instances (nested structure)
- IAM least privilege: boto3-scripts user has only the permissions it needs
- Never use root credentials in scripts — always use a dedicated IAM user
- S3 bucket creation requires LocationConstraint for any region outside us-east-1

### What confused me
- Why does S3 need LocationConstraint but EC2 just needs region_name?
- How to paginate describe_instances for accounts with many instances

---
## Day 18 — Monday 18 May 2026
### Topic: TEAL — Week 3 Full Revision (S3 + Python)

**What I revised:**
- S3 storage classes and minimum storage durations
- Versioning behaviour with delete markers
- MFA Delete — root-only, cannot be enabled by IAM users
- SRR vs CRR — both are valid since 2019
- S3 Object Lock — WORM, Governance vs Compliance mode
- boto3: list_buckets, list_objects_v2, upload_file, download_file

**ExamTopics practice: 15 questions**
- Score: [fill in] / 15
- Weak areas: [fill in]

**Python from memory:**
- list_buckets: [ ✅ / ❌ ]
- list_objects: [ ✅ / ❌ ]
- upload_file:  [ ✅ / ❌ ]
- download_file: [ ✅ / ❌ ]

**Portfolio work:**
- Added list_objects.py to Project 05 (S3 File Manager)
- Script uses pagination — handles buckets with 1000+ objects
- Added error handling for AccessDenied and NoSuchBucket

**Anki cards added:** 2 (Cards 74–75)
**Running deck total:** 75 cards

---

## Day 19 — Tuesday 19 May 2026

**Topic:** Claude API — Building AI-Powered Tools
**Category:** PURPLE — AI / Claude
**Time spent:** ~90 minutes (plus extra debugging time)
**Week:** 3, Day 5

### What I built
- basic_claude_call.py — minimal Claude API call, one question in, one answer out
- claude_study_assistant.py — interactive command-line tutor with "AWS Maya" persona,
  error handling, and session log saving
- Added both scripts to project-06-n8n-business-automation/claude-api/ on GitHub

### Key things I learned
- anthropic Python SDK — pip install anthropic
- client.messages.create() — the core API call pattern
- system= parameter is the system prompt — defines persona, tone, and output format
- max_tokens controls response length and cost
- claude-haiku-4-5-20251001 is the cheapest model — ~£0.01 per study session
- The system prompt IS the product. The Python code is just plumbing.
- PowerShell uses $env:VAR syntax — NOT cmd.exe %VAR% syntax
- git config --global must be set before first commit on any new machine
- Red text in PowerShell does not always mean failure — git writes to stderr

### Problems faced and resolved
1. PowerShell vs cmd.exe syntax for environment variables — fixed with $env: prefix
2. GitHub repo not cloned to this machine — fixed with git clone
3. git clone showed red NativeCommandError — not an error; clone succeeded
4. Wrong folder name in plan (n8n-automation) vs GitHub (n8n-business-automation) — used GitHub name
5. git commit failed: Author identity unknown — fixed with git config --global

### Energy / Confidence
- Energy: 5/5 — Excellent
- Confidence: 4/5 — Could explain this to someone else

**Anki cards added:** 5 (Cards 76–80)
**Running deck total:** 80 cards

---

## Certification Progress

| Certification | Target | Status |
|---|---|---|
| AWS CCP | Jan 2022 | ✅ Certified (expired) |
| AWS SAA-C03 | Oct 2026 | 🔄 Week 1 of 27 |
| AZ-104 | Jan 2027 | 📅 Planned |
| AWS CSAP | Apr 2027 | 📅 Planned |
| Terraform Associate | May 2027 | 📅 Planned |

---

## Anki Progress

| Week | Cards added | Total deck |
|---|---|---|
| Week 1 | 1 | 29 |
| Week 2 | 30 | 62 |
| Week 3 (Days 15–18) | 13 | 75 |
| Week 3 (Day 19) | 5 | 80 |
---

## GitHub Projects

| Project | Status | Week started | Notes |
|---|---|---|---|
| project-01-portfolio-site | ✅ Live | Week 1 | S3 + CloudFront — live at d2ven7lubrbrhs.cloudfront.net |
| project-02-ec2-auto-scaling | 🔄 In progress | Week 1 | AMI created, diagram added |
| project-03-vpc-network | ✅ Built | Week 2 | VPC + 4 subnets + IGW + NAT Gateway + SG + NACL complete |
| project-05-s3-file-manager | ✅ Built | Week 3 | S3 lifecycle rules, versioning, SSE-S3 encryption, boto3 audit script |
| project-06-n8n-business-automation | ✅ Built | Week 2 | 3 workflows live — weather briefing, study tracker, email summariser + OpenAI |
| project-06-n8n-business-automation/claude-api | ✅ Built | Week 3 | Claude API study assistant — AWS Maya persona, system prompt, error handling |
| project-07-cloudflow-website | ✅ Live | Week 2 | S3 + CloudFront + Route 53 + ACM — live at cloudflowautomations.co.uk |
| project-08-aws-cost-audit | ✅ Built | Week 3 | boto3 cost audit script — flags idle EC2, stopped instances, orphaned resources |

---

*Updated daily — part of a 104-week Cloud + AI Automation plan*  
*MSc Cloud Computing, University of Leicester*

---

## Day 25 — Saturday 25 July 2026
**Topic:** Community Volunteer Project Prep
**Category:** AMBER — Community Volunteer
**Time spent:** ~90 minutes
**Week:** 4, Day 4 of the week

### What I built
- volunteer-outreach-tracker.csv — 5 Leicester organisations identified with contact details
- volunteer-service-offer.md — pro-bono cloud and automation offer description
- volunteer-outreach-template.md — personalised email template for each organisation
- volunteer-project-scope-draft.md — 5-bullet scope for top candidate organisation
- project-10-community-volunteer/ folder created on GitHub with stub README

### Key things I learned
- AI Founders Section 2: the 5-Step Employee Onboarding System (Personal Preferences, Virtual Workspace, Business Tools, Reusable Playbooks, Performance Stack)
- A client who goes from zero to full Cowork onboarding with 3 connected tools is a £1,000–£2,500 billable service
- Life in the UK Chapter 5: House of Commons (650 elected MPs, more powerful) vs House of Lords (appointed, can delay but not block legislation)
- The PM is not directly elected — the public votes for MPs and the Commons majority leader becomes PM automatically
- A well-scoped volunteer project is identical portfolio evidence to a paid project

### What confused me / still unsure about
- Need to confirm which organisations actually respond to outreach
- Not yet sure which specific automation problem to target — depends on confirmed partner

### Problems faced and resolved (if any)
- None — research and planning day, no technical blockers

### Energy / Confidence
- Energy: /5
- Confidence: /5

**AWS SAA cards added:** 0 (AMBER day)
**LITUK cards added:** 2 (LITUK Cards 3–4)
**AWS SAA deck total:** 94 cards
**Life in the UK deck total:** 4 cards

---

## Day 26 — Sunday 26 July 2026
**Topic:** Full Week 4 Revision — Anki + Practice Questions + Weekly Summary
**Category:** TEAL — Revision Day
**Time spent:** ~90 minutes
**Week:** 4, Day 5 of the week

### What I built
- week-04-summary.md — weekly reflection (topics, projects, gaps, Week 5 focus)
- atlas.md — started personal AI company source-of-truth file (AI Founders skill)

### Key things I learned
- AI Founders Section 3: The 20-Skill AI Agency Stack — 5 layers: Bedrock, Force Multipliers, Brain Trust, Production Floor, Ground Crew
- Build Genesis first — then use it to build all other skills
- DAX = DynamoDB Accelerator — microsecond read latency, eventual consistency only, caches reads NOT writes
- RDS = OLTP (row storage, transactions). Redshift = OLAP (columnar, analytics, petabyte-scale)
- Redshift Spectrum = run SQL directly on S3 without loading into Redshift
- Hot partition problem in DynamoDB = poor partition key choice (low cardinality)

### What confused me / still unsure about
- [Fill in after completing practice questions]

### Problems faced and resolved (if any)
- None — revision day

### Energy / Confidence
- Energy: /5
- Confidence: /5

**Practice question score:** __ / 15 (fill in)
**AWS SAA cards added:** 2 (Cards 95–96: DAX, RDS vs Redshift)
**LITUK cards added:** 0 (Sunday = mock test, not chapter study)
**AWS SAA deck total:** 96 cards
**Life in the UK deck total:** 4 cards
**🎯 Combined total: 100 cards — milestone reached**

---

## Day 27 — Monday 27 July 2026
**Topic:** DynamoDB + ElastiCache
**Category:** 🔵 BLUE — AWS Cloud
**Time spent:** ~90 minutes
**Week:** Week 4, Day 6 of 7

### What I built
- DynamoDB table: `hasan-session-store-2026` (partition key: sessionId, sort key: createdAt)
- Created 2 items and ran a Query by partition key — confirmed single-digit millisecond response
- Screenshots: day27-dynamodb-table.png, day27-dynamodb-query.png
- Claude Routine brief: Overdue Invoice Nudger (5-part template) — saved in Notion as routine-invoice-nudger.md

### Key things I learned
- DynamoDB is NoSQL, serverless, schema-less — data replicated across 3 AZs automatically; max item size 400KB
- DAX = DynamoDB Accelerator — improves READ performance only (milliseconds → microseconds), write-through caching, no app code changes needed
- DynamoDB Global Tables = multi-region, multi-master, 99.999% SLA; strongly consistent reads NOT supported cross-region
- DynamoDB TTL: auto-deletes items after expiry date, no cost, no RCU/WCU consumed, deletion within 48 hours
- ElastiCache exam trigger: read-heavy application + database overloaded with repeated queries → ElastiCache
- Choose Redis: encryption, HIPAA, HA/Multi-AZ, complex data types (sorted sets/lists), persistence, pub/sub
- Choose Memcached: simplicity, multi-threading, elastically scalable object caching, no persistence/encryption needed
- ElastiCache is fully managed — cannot run it on EC2; does not support Spot Instances
- Claude Routines = event-triggered automations (doorbell model) running on Anthropic's cloud — laptop can be closed
- AI Founders Section 4: 13 routines = ready-to-sell products for UK SMEs; 3-routine bundle worth £500–£1,200 setup

### What confused me / still unsure about
- GSI vs LSI distinction — need to revise with a concrete example (add to Anki queue)
- When to use ElastiCache IN FRONT of DynamoDB vs DAX: ElastiCache for infrequently-changed data; DAX for any DynamoDB read performance

### Problems faced and resolved (if any)
- N/A — theory + hands-on console day, no issues

### Energy / Confidence
- Energy: /5
- Confidence: /5

**AWS SAA cards added:** 5 (Cards 97–101)
**LITUK cards added:** 1 (LITUK Card 5)
**AWS SAA deck total:** 101 cards
**Life in the UK deck total:** 5 cards

---

## 08 September 2026
**Topic:** n8n Introduction, Setup & Core Fundamentals
**Category:** 🟣 PURPLE — AI Automation
**Course:** n8n Masterclass (Udemy)
**Sections completed:** Section 1 (all 6 lessons ✅) + Section 2 lessons 2.7–2.8 ✅

### What I built
- n8n Cloud account set up (14-day free trial)
- **Email Sender workflow**: Manual Trigger + Schedule Trigger (9am daily) + Gmail node with OAuth2 credentials
- Dynamic date expression: `{{ $now.format('dd-LLL-yyyy') }}` — email automatically shows today's date
- Explored the 80/20 workflow canvas showing all 13 core node categories

### Key things I learned
- n8n is a visual drag-and-drop automation tool — connects apps, APIs, and AI without complex code
- Every workflow must start with a trigger (Manual, Schedule, Webhook, or App Event)
- Nodes flow left to right; top branch always executes before bottom branch
- Sequential execution: nodes run one after another, not in parallel
- Nodes run once per input — 5 items entering a node = node runs 5 times
- The 13 core nodes cover 80% of automation use cases across 5 categories: Triggers, Data Processing, Connectivity, Storage, AI
- OAuth2 = "Sign in with Google" style auth — n8n stores token, not your password
- Active toggle must be ON for schedule/webhook triggers to fire automatically
- IF node = branching logic (true/false paths); Use AI nodes only when judgement is needed, not for deterministic if/else logic

### What confused me / still unsure about
- Webhook vs App Event trigger — when to use each in a real client workflow
- HTTP Request authentication types (Bearer token vs API key vs OAuth2)

### Problems faced and resolved
- N/A — smooth setup day, n8n Cloud connected cleanly

### Energy / Confidence
- Energy: /5
- Confidence: /5

**n8n Automation cards added:** 20 (Cards 1–20 — new deck)
**AWS SAA deck total:** 101 cards (unchanged)
**Life in the UK deck total:** 5 cards (unchanged)
**n8n Automation deck total:** 20 cards (NEW deck started)
**🎯 Combined total: 126 cards**

---

## Day 29 — 08 September 2026

**Topic:** n8n Section 2 — The 13 Core Nodes & Execution Essentials
**Category:** 🟣 PURPLE — AI Automation
**Course:** n8n Masterclass (Udemy) | Sections 2.7–2.8

### What I Covered
- The 80/20 rule: 13 nodes cover 80% of all real-world automations
- Execution essentials: left→right flow, top branch first, sequential (not parallel), nodes run once per input
- Active vs Inactive workflows
- The 5 node categories and all 13 nodes in detail
- Split Out — flatten arrays into individual items
- Aggregate — merge items back into one structure
- Set/Edit Fields — create new fields using expressions
- IF node — branch workflows based on conditions
- Code node — custom JavaScript transformations
- HTTP Request — connect to any external API
- Webhook + Webhook Response — receive and reply to external triggers
- Google Sheets + Database nodes — lightweight storage
- Basic LLM Chain — AI judgement for fuzzy rules
- AI Agent — multi-step autonomous AI with memory and tools
- When to use IF vs LLM Chain vs AI Agent

### What I Built
- Studied and imported the 80/20 workflow JSON demonstrating all 13 nodes with live lead data

### What Clicked
- Sequential execution explains why top branch always runs first — it's not parallel
- The distinction between IF (deterministic) and LLM Chain (fuzzy judgement) is key for real projects
- HTTP Request is the universal connector — any app with an API can be connected

### Anki Cards
- **n8n Automation deck:** 20 new cards added (Cards 21–40)
- **AWS SAA deck total:** 101 cards (unchanged)
- **Life in the UK deck total:** 5 cards (unchanged)
- **Combined total: 146 cards**

