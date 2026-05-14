# Project 03 — Custom VPC Network

**Author:** Khandaker Sadain Hasan
**Location:** Leicester, UK
**Date started:** 08 May 2026
**Status:** 🔄 In progress

---

## What Problem Does This Solve?

The default AWS VPC has all subnets public — unsuitable
for production workloads. Placing all resources in a flat
public network fails every security audit. A financial
institution running trading systems on AWS without network
segmentation would expose databases and application servers
directly to the internet.

This custom VPC creates a properly segmented network with
public and private tiers across two Availability Zones.
Public subnets host internet-facing resources only. Private
subnets host databases and servers that should never be
directly reachable from the internet. Security Groups and
NACLs provide defence-in-depth at both instance and subnet
level — directly reflecting real-world banking IT regulatory
compliance requirements.

---

## Architecture

### Version 1 — VPC with subnets and Internet Gateway
![VPC Architecture Diagram](project-03-vpc-architecture.png)

### Version 2 — Updated with NAT Gateway traffic flow
![VPC Architecture v2](project-03-vpc-architecture-v2.png)

---

## Traffic Flows

**Public subnet — inbound and outbound:**
Internet → Internet Gateway → Public Subnet → EC2
EC2 → Internet Gateway → Internet

**Private subnet — outbound only via NAT:**
Private EC2 → NAT Gateway (public subnet) → Internet Gateway → Internet
Internet → BLOCKED — cannot reach private subnet directly

**Security layers:**

| Layer | Service | Level | State | What it does |
|---|---|---|---|---|
| First | NACL | Subnet | Stateless | Checks all packets both ways |
| Second | Security Group | Instance | Stateful | Remembers connections |

---

## Components Built

| Component | Name | Details |
|---|---|---|
| VPC | my-custom-vpc | CIDR: 10.0.0.0/16, Region: eu-west-2 |
| Public Subnet 1 | public-subnet-1 | 10.0.1.0/24 — eu-west-2a |
| Public Subnet 2 | public-subnet-2 | 10.0.2.0/24 — eu-west-2b |
| Private Subnet 1 | private-subnet-1 | 10.0.3.0/24 — eu-west-2a |
| Private Subnet 2 | private-subnet-2 | 10.0.4.0/24 — eu-west-2b |
| Internet Gateway | my-igw | Attached to my-custom-vpc |
| Public Route Table | public-route-table | 0.0.0.0/0 → my-igw |
| Private Route Table | private-route-table | 0.0.0.0/0 → NAT Gateway |
| NAT Gateway | my-nat-gateway | Regional mode — deleted after learning |
| Security Group | web-server-sg | HTTP 80, HTTPS 443, SSH 22 (My IP) |
| Network ACL | my-custom-nacl | Allow 80, 443, 1024-65535 in/out |

---

## Screenshots

### Private route table — showing NAT Gateway route
![Private route table](private-route-table.png)

### NAT Gateway — Status: Available
![NAT Gateway](nat-gateway.png)

### Security Group — inbound rules
![Security Group](security-group.png)

### Custom NACL — inbound rules including ephemeral ports
![NACL Rules](nacl-rules.png)

---

## Steps Completed

- [x] Created custom VPC (10.0.0.0/16)
- [x] Created 2 public subnets across 2 AZs
- [x] Created 2 private subnets across 2 AZs
- [x] Created and attached Internet Gateway
- [x] Created public route table with internet route
- [x] Associated public subnets with public route table
- [x] Created Regional NAT Gateway in public-subnet-1
- [x] Updated private route table: 0.0.0.0/0 → NAT Gateway
- [x] Created Security Group: web-server-sg (HTTP/HTTPS/SSH)
- [x] Created custom NACL with inbound and outbound rules
- [x] Added ephemeral ports (1024-65535) to NACL outbound rules
- [x] Architecture diagram updated to v2 with NAT Gateway
- [x] NAT Gateway DELETED after learning session ✅
- [ ] Launch EC2 to test connectivity end to end
- [ ] Add VPC Flow Logs

---

## Key Things Learned

- VPC = isolated private network — like a bank's internal network
- What makes a subnet public is NOT its name — it is whether
  the route table has a route to the Internet Gateway
- AWS reserves 5 IPs per subnet — /24 = 251 usable addresses
- One Internet Gateway per VPC maximum
- NAT Gateway must be in a PUBLIC subnet — allows private
  subnet instances OUTBOUND internet access only
- Regional NAT Gateway covers all AZs automatically —
  better than the traditional Zonal approach (one per AZ)
- Security Groups = stateful, instance level, ALLOW only,
  cannot block specific IPs — use NACLs for that
- NACLs = stateless, subnet level, ALLOW and DENY,
  evaluated in number order, first match wins
- Ephemeral ports (1024-65535) must be allowed in NACL
  outbound rules or response traffic is blocked
- NACL = first line of defence. Security Group = second line.
- Memory trick: SG = Stateful Security guard.
  NACL = No memory Checkpoint Lane.

---

## Exam Relevance — AWS SAA-C03

| Topic | Covered |
|---|---|
| VPC CIDR blocks | ✅ 10.0.0.0/16 — 65,536 addresses |
| Public vs private subnets | ✅ Both created across 2 AZs |
| Internet Gateway | ✅ Created, attached, and route configured |
| Route tables | ✅ Public (→ IGW) and private (→ NAT) |
| Multi-AZ design | ✅ eu-west-2a and eu-west-2b |
| NAT Gateway | ✅ Regional mode — private subnet outbound |
| Security Groups | ✅ Stateful, allow only, instance level |
| Network ACLs | ✅ Stateless, allow and deny, subnet level |
| Defence in depth | ✅ NACL first, Security Group second |
| Ephemeral ports | ✅ 1024-65535 in NACL outbound |

---

## Cost

| Component | Cost |
|---|---|
| VPC | FREE |
| Subnets (4) | FREE |
| Internet Gateway | FREE |
| Route Tables | FREE |
| Security Group | FREE |
| Network ACL | FREE |
| NAT Gateway | Created and DELETED same session |
| **Total ongoing** | **$0** |

⚠️ NAT Gateway costs $0.045/hour when running.
Always delete immediately after learning sessions.

---

*Part of a 24-month Cloud + AI Automation Specialist plan*
*MSc Cloud Computing, University of Leicester*
*AWS CCP certified January 2022 — AWS SAA target: October 2026*
