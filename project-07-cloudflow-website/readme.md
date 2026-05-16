# Project 07 — Cloudflow Automations Company Website

**Live URL:** https://cloudflowautomations.co.uk  
**Status:** LIVE ✅  
**Deployed:** May 2026  

---

## What This Is

A fully deployed production company website for Cloudflow Automations — 
a cloud and AI automation consultancy targeting UK SMEs.

The website is live at cloudflowautomations.co.uk with full HTTPS, 
served globally via CloudFront CDN from a private S3 bucket. 
No server to maintain. No monthly hosting bill beyond $0.50 for DNS.

---

## Architecture
ONOS (Domain Registrar — nameservers delegated to Route 53)
↓  NS delegation
Route 53 Hosted Zone (Public DNS authority)
↓  Alias A record — free, works at zone apex
CloudFront Distribution (CDN, HTTPS, TLS 1.3, OAC)
↓  OAC signed request — private, signed by CloudFront service principal
S3 Private Bucket (Block All Public Access ON — only CloudFront can read)ACM Certificate (us-east-1, free, auto-renewing, DNS validated via Route 53)
→ attached to CloudFront distribution
---

## AWS Services Used

**Amazon S3**
- Private bucket: cloudflow-automations-website (eu-west-2)
- Block All Public Access: ON — bucket cannot be accessed directly
- Versioning: enabled — protects against accidental overwrites
- OAC bucket policy applied — only this CloudFront distribution can call s3:GetObject
- Stores: index.html + 4 SVG logo files

**AWS CloudFront**
- Distribution: cloudflow-automations-website
- Origin: S3 REST endpoint (not website endpoint — required for OAC)
- Origin Access Control (OAC): cloudflow-automations-oac — modern replacement for OAI
- Viewer protocol: Redirect HTTP to HTTPS
- Default root object: index.html
- Alternate domain names: cloudflowautomations.co.uk, www.cloudflowautomations.co.uk
- Price class: North America and Europe
- TLS 1.3 with custom ACM certificate

**AWS Certificate Manager (ACM)**
- Region: us-east-1 (N. Virginia) — REQUIRED for CloudFront, regardless of S3 region
- Certificate covers: cloudflowautomations.co.uk + www.cloudflowautomations.co.uk
- Validation: DNS validation via Route 53 (one-click, fully automated)
- Cost: FREE — ACM public certificates have no charge
- Auto-renews before expiry as long as validation CNAME stays in Route 53

**Amazon Route 53**
- Hosted zone: cloudflowautomations.co.uk (Public)
- Root domain record: Alias A → d2fmeq57h9qj6q.cloudfront.net (FREE — no per-query charge)
- www record: Alias A → same CloudFront distribution
- ACM validation CNAMEs: 2 records (auto-created by ACM → Route 53 integration)
- Cost: $0.50/month for the hosted zone + $0.40 per million queries

---

## Website

Built as a single-page HTML site. Dark theme. Mobile responsive.

Sections: Hero, Problem, Services, Projects, Tech Stack, About, Pricing, Contact, Footer

Features:
- Custom SVG logo (C monogram + trailing dots — navy/teal)
- Under Construction amber banner (dismissible)
- Gradient wordmark using Space Grotesk font
- All animations in pure CSS — no JavaScript frameworks

**Logo files:**
- cloudflow-mark-white.svg — favicon + dark background mark
- cloudflow-mark.svg — light background mark
- cloudflow-logo.svg — full horizontal wordmark (light)
- cloudflow-logo-dark.svg — full horizontal wordmark (dark)

---

## Key Learning Points

**Why Alias instead of CNAME at root domain?**  
DNS specification (RFC 1912) forbids CNAME records at the zone apex.  
AWS Alias records are a non-standard extension that behaves like a CNAME  
but resolves as an A record. They are free, work at the root domain,  
and Route 53 automatically updates them if the CloudFront IP changes.

**Why ACM must be in us-east-1?**  
CloudFront is a globally distributed service with a control plane in us-east-1.  
ACM certificates are region-specific. CloudFront can only read certificates  
from the region where its control plane operates — which is us-east-1.  
Creating the certificate in eu-west-2 (or any other region) will cause  
CloudFront to reject it silently.

**Why OAC instead of OAI?**  
OAI (Origin Access Identity) is being deprecated by AWS.  
OAC (Origin Access Control) is the modern replacement. It:
- Supports all S3 regions including newer regions launched after OAI
- Supports SSE-KMS encrypted buckets
- Signs requests using AWS Signature Version 4 (SigV4) — more secure
- Locks the bucket policy to your specific distribution ARN via a condition

**Why not use the S3 website endpoint as CloudFront origin?**  
The S3 website endpoint doesn't support OAC — it requires the bucket to be  
public. Using the S3 REST endpoint keeps the bucket private and allows OAC.

---

## Cost

| Service | Cost |
|---|---|
| S3 storage (5 small files) | ~$0.01/month |
| CloudFront (low traffic) | ~$0.05/month |
| ACM certificate | FREE |
| Route 53 hosted zone | $0.50/month |
| Route 53 queries | ~$0.01/month at low traffic |
| **Total** | **~$0.57/month** |

This architecture scales to millions of visitors with no infrastructure changes.  
The same setup used by enterprise static websites.

---

## Screenshots

**Live website with HTTPS:**
![Live Website](day13-live-website.png)

**CloudFront distribution — Enabled:**
![CloudFront](day13-cloudfront-enabled.png)

**ACM Certificate — Issued:**
![ACM](day13-acm-issued.png)

**Route 53 records:**
![Route 53](day13-route53-records.png)

**Architecture diagram:**
![Architecture](day13-architecture.png)

---

## Business Value

This same architecture pattern can be sold to UK SMEs as a managed service:

- A local restaurant wanting a fast, professional static website: £300–500 setup
- A solicitor firm wanting their brochure site with no server management: £400–600 setup
- A charity wanting reliable low-cost hosting: £200–350 setup

Monthly managed hosting and support: £50–100/month per client.

The architecture is enterprise-grade but costs under £1/month to run.  
That margin is the business model.

**Post-ILR freelance value: £300–600 per client deployment**
