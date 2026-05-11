# Project 03 — Custom VPC Network

**Author:** Hasan  
**Date started:** 08 May 2026  
**Status:** 🔄 In progress  
**Week:** 2 of 104

---

## What Problem Does This Solve?

The default AWS VPC is convenient but not suitable for 
production use — all subnets are public and there is no
network isolation between resources.

This project builds a production-ready VPC architecture with:
- Public subnets for internet-facing resources (ALB, NAT Gateway)
- Private subnets for protected resources (RDS, Lambda, EC2)
- High availability across 2 Availability Zones
- Proper routing so private resources can reach internet
  outbound but cannot be reached from internet inbound

---

## Architecture
AWS Cloud (eu-west-2)
┌───────────────────────────────────────────────┐
│              my-custom-vpc                    │
│              10.0.0.0/16                      │
│                                               │
│  ┌─────────────────┐  ┌─────────────────┐     │
│  │  AZ: eu-west-2a │  │  AZ: eu-west-2b │     │
│  │                 │  │                 │     │
│  │ Public Subnet 1 │  │ Public Subnet 2 │     │
│  │  10.0.1.0/24    │  │  10.0.2.0/24    │     │
│  │                 │  │                 │     │
│  │ Private Subnet 1│  │ Private Subnet 2│     │
│  │  10.0.3.0/24    │  │  10.0.4.0/24    │     │
│  └─────────────────┘  └─────────────────┘     │
│                                               │
│  [Internet Gateway — my-igw]                  │
└───────────────────────────────────────────────┘
                      │
                 [Internet]
---

## AWS Services Used

| Service | Purpose |
|---|---|
| Amazon VPC | Isolated private network — CIDR 10.0.0.0/16 |
| Subnets (x4) | Network segments in 2 AZs — 2 public, 2 private |
| Internet Gateway | Connects VPC to the internet |
| Route Tables | Controls traffic routing per subnet |
| Security Groups | Instance-level firewall (coming next) |
| NACLs | Subnet-level firewall (coming next) |

---

## Network Design

| Subnet | CIDR | AZ | Type | Route |
|---|---|---|---|---|
| public-subnet-1 | 10.0.1.0/24 | eu-west-2a | Public | → IGW |
| public-subnet-2 | 10.0.2.0/24 | eu-west-2b | Public | → IGW |
| private-subnet-1 | 10.0.3.0/24 | eu-west-2a | Private | Local only |
| private-subnet-2 | 10.0.4.0/24 | eu-west-2b | Private | Local only |

---

## Steps Completed

- [x] Created VPC — 10.0.0.0/16 (my-custom-vpc)
- [x] Created 4 subnets across 2 AZs (2 public, 2 private)
- [x] Created and attached Internet Gateway (my-igw)
- [x] Created public route table with 0.0.0.0/0 → IGW
- [x] Associated public subnets with public route table
- [x] Enabled auto-assign public IP on public subnets
- [ ] Create Security Groups (Day 10)
- [ ] Create NACLs (Day 10)
- [ ] Create NAT Gateway for private subnets (Day 10)
- [ ] Launch EC2 in public subnet to test connectivity
- [ ] Launch EC2 in private subnet to test isolation

---

## Key Things Learned

- VPC = isolated private network within AWS region
- Subnets are AZ-specific — tie to one AZ only
- Public subnet = has route to Internet Gateway
- Private subnet = no route to Internet Gateway
- AWS reserves 5 IPs per subnet — /24 = 251 usable IPs
- One Internet Gateway per VPC maximum
- Route table controls where traffic goes per subnet

---

## Exam Relevance — AWS SAA-C03

| Topic | What I practiced |
|---|---|
| VPC creation and CIDR blocks | Created 10.0.0.0/16 VPC |
| Subnet design | Public/private across multiple AZs |
| Internet Gateway | Created, attached, added to route table |
| Route tables | Public route with IGW, private route local only |
| High availability | Subnets in 2 AZs for fault tolerance |

---

*Part of a 24-month Cloud + AI Automation Specialist plan*
*MSc Cloud Computing, University of Leicester*
*AWS SAA target: October 2026*
