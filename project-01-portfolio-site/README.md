# Project 01 — Cloud Portfolio Website

**Author:** Hasan
**MSc Cloud Computing** — University of Leicester (2020–2022)

Cloud portfolio of Hasan — building toward AWS SAA, AZ-104, and CSAP.

---

## Project Overview

A professional cloud portfolio website hosted entirely on AWS using 
S3 for static file storage and CloudFront as a global CDN.
No web servers. No maintenance. Costs approximately £1/month.

---

## Architecture

[User] → [Route 53] → [CloudFront] → [S3 Bucket]

---

## AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Static website hosting |
| Amazon CloudFront | Global CDN and HTTPS |
| Amazon Route 53 | DNS management (optional) |
| AWS Certificate Manager | Free SSL/TLS certificate |

---

## Status
🔄 In progress — Week 1 of 104-week Cloud + AI plan

---

## What I Learned
- How to host a static website on S3 with public access
- How CloudFront caches and delivers content globally
- How Origin Access Control (OAC) secures S3 from direct access

---

## Cost
Approximately $0.50–$1.00/month for a low-traffic portfolio site.
Compared to £10–15/month for traditional shared hosting.

---

*Built as part of a 24-month Cloud + AI Automation Specialist plan*
*AWS CCP certified January 2022 | AWS SAA target: October 2026*
