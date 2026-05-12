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

**Anki cards added:** Cards 35-40
**Deck total:** 40 cards ✅


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
| Week 1 | 29 | 29 |

---

## GitHub Projects

| Project | Status | Week started |
|---|---|---|
| project-01-portfolio-site | ✅ Live | Week 1 |
| project-02-ec2-auto-scaling | 🔄 In progress | Week 1 |

---

*Updated daily — part of a 104-week Cloud + AI Automation plan*  
*MSc Cloud Computing, University of Leicester*
