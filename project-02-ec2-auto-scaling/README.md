# Project 02 — EC2 Auto-Scaling Web Server

**Author:** Khandaker Sadain Hasan
**Date started:** 03 May 2026
**Status:** 🔄 In progress

---

## What is EC2?

Amazon EC2 (Elastic Compute Cloud) is AWS's virtual server service 
that lets you launch resizable computing capacity in the cloud — 
eliminating the need to invest in physical hardware upfront.

## What I did today

I launched my first EC2 instance (t2.micro, Amazon Linux 2023) 
on AWS using the free tier, configured a key pair for secure 
access, and successfully connected to the server using EC2 
Instance Connect directly in the browser.

---

## Architecture (planned)

[User] → [Application Load Balancer] → [Auto Scaling Group] → [EC2 Instances]

---

## AWS Services Used

| Service | Purpose |
|---|---|
| Amazon EC2 | Virtual server (t3.micro, Amazon Linux 2023) |
| Amazon EBS | 8GB root volume attached to the instance |
| EC2 Key Pair | Secure SSH access credential |
| Auto Scaling Group | Will be added in next steps |
| Application Load Balancer | Will be added in next steps |

---

## Steps Completed

- [x] Launched EC2 instance (t3.micro, free tier)
- [x] Created key pair (my-keypair.pem)
- [x] Connected via EC2 Instance Connect
- [x] Verified instance running (2/2 status checks passed)
- [ ] Create AMI from instance
- [ ] Set up Auto Scaling Group
- [ ] Attach Application Load Balancer

---

## Screenshot

*(See ec2-running.png below)*

---

## Key Things I Learned

- Stop vs Terminate: Stop preserves the EBS volume, Terminate deletes it
- AMI = Amazon Machine Image — the template used to launch the instance
- t2.micro is free tier eligible for 750 hours/month for 12 months
- EBS = the hard drive attached to my EC2 instance (8GB by default)

---

*Part of a 24-month Cloud + AI Automation Specialist plan*
*AWS CCP certified January 2022 | AWS SAA target: October 2026*
