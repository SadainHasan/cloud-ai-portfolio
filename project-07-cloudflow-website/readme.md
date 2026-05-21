# Project 07 — Cloudflow Automations Company Website

**Live URL:** https://cloudflowautomations.co.uk
**Status:** ✅ LIVE
**Deployed:** May 2026

---

## What Problem Does This Solve?

Most UK small businesses either:
- Pay £10–30/month for slow shared hosting with a control panel they can't manage
- Pay a web agency £500–1,500 upfront + £50/month for a site that sits on a single server
- Have no website at all because it feels too technical or expensive

This project solves that by deploying a production-grade company website with:
- Global CDN — fast loading for anyone in the UK and Europe
- Full HTTPS — required for Google ranking and user trust
- Zero server management — no patches, no server crashes, no downtime from traffic spikes
- Near-zero running cost — under £1/month total

The same architecture that enterprises pay thousands for, running for pocket change.

---

## What This Is

A fully deployed production company website for Cloudflow Automations —
a cloud and AI automation consultancy targeting UK SMEs.

The website is live at cloudflowautomations.co.uk with full HTTPS,
served globally via CloudFront CDN from a completely private S3 bucket.
No server to maintain. No monthly hosting bill beyond $0.50 for DNS.
Scales to millions of visitors with zero infrastructure changes.

---

## Architecture

```
IONOS (Domain Registrar — nameservers delegated to Route 53)
    ↓  NS delegation
Route 53 Hosted Zone (Public DNS authority)
    ↓  Alias A record — free, works at zone apex (root domain)
CloudFront Distribution (CDN, HTTPS, TLS 1.3, OAC)
    ↓  OAC signed request — only this distribution can read S3
S3 Private Bucket (Block All Public Access ON)

ACM Certificate (us-east-1, free, DNS validated) → CloudFront
```

---

## Steps

### Step 1 — Create Private S3 Bucket
- Region: eu-west-2 (London)
- Block All Public Access: ON
- Versioning: Enabled
- Upload: index.html + 4 SVG logo files

### Step 2 — Request ACM Certificate (us-east-1 ONLY)
- Switch region to N. Virginia (us-east-1) before requesting
- Add both root domain and www subdomain to the certificate
- Validation method: DNS validation
- Click "Create records in Route 53" — AWS adds CNAMEs automatically
- Wait for status: Issued (2–5 minutes)

### Step 3 — Create CloudFront Distribution
- Origin: S3 REST endpoint (not website endpoint)
- Origin access: Origin Access Control (OAC) — create new OAC
- Copy OAC bucket policy from yellow banner
- Viewer protocol policy: Redirect HTTP to HTTPS
- Default root object: index.html
- Alternate domain names: cloudflowautomations.co.uk + www
- Custom SSL certificate: attach ACM cert (must show Issued)
- Price class: North America and Europe

### Step 4 — Apply OAC Bucket Policy to S3
- Go to S3 → Permissions → Bucket policy → Edit
- Paste the OAC policy copied from CloudFront
- Policy restricts access to the specific distribution ARN only

### Step 5 — Create Route 53 Alias A Records
- Record 1: root domain (blank name) → Alias → CloudFront distribution
- Record 2: www → Alias → same CloudFront distribution
- Both records: Type A, Alias ON, Region US East (N. Virginia)

### Step 6 — Test
- Wait 10–15 minutes for SSL propagation to 400+ edge locations
- Test raw CloudFront URL first: https://d2fmeq57h9qj6q.cloudfront.net
- Then test custom domain: https://cloudflowautomations.co.uk
- Then test www: https://www.cloudflowautomations.co.uk

---

## Why This Architecture?

**Why S3 instead of a web server (EC2)?**
Static websites have no server-side logic — HTML, CSS, and JavaScript are just files.
S3 stores files. No reason to run a server 24/7 just to serve files when S3 does it
for fractions of a penny per request, with no patching, no crashes, no management.

**Why CloudFront instead of serving directly from S3?**
S3 is a single region (eu-west-2). A user in Scotland hitting eu-west-2 is fine.
A user in London or Manchester is also fine. But without a CDN, the response comes
from one fixed location. CloudFront caches the files at 400+ edge locations globally,
so every user gets the response from the nearest location — faster loading, lower latency.
CloudFront also handles HTTPS termination and forces HTTP → HTTPS redirect at the edge.

**Why OAC instead of making S3 public?**
A public S3 bucket can be accessed directly by anyone with the URL — bypassing
CloudFront entirely. This means: no HTTPS enforcement, no CDN caching, potential
cost from direct S3 access, and no security control. OAC keeps the bucket completely
private. Only the specific CloudFront distribution (locked by ARN in the bucket policy)
can call s3:GetObject. Everything else is denied.

**Why Route 53 Alias A instead of CNAME?**
DNS RFC 1912 (written in the 1980s) forbids CNAME records at the zone apex — the root
of a domain. You cannot have cloudflowautomations.co.uk as a CNAME. Only subdomains
can be CNAMEs (www.cloudflowautomations.co.uk can). AWS Alias records solve this —
they resolve as A records at the DNS level, auto-update if CloudFront IPs change,
and are completely free (no per-query charge unlike CNAME).

**Why ACM in us-east-1 even though S3 is in eu-west-2?**
CloudFront is a global service but its management control plane runs from us-east-1.
ACM certificates are region-specific. CloudFront can only read ACM from the region
its control plane operates in — us-east-1. A certificate created in eu-west-2 is
invisible to CloudFront. This is the single most common mistake with this setup.

---

## Exam Relevance (AWS SAA-C03)

| Topic | Exam Point |
|---|---|
| S3 + CloudFront | Classic SAA pattern — private S3 bucket served via CloudFront with OAC |
| OAC vs OAI | OAI is deprecated. OAC is the correct modern answer. If both appear, choose OAC. |
| ACM region | ACM for CloudFront = us-east-1 ALWAYS — regardless of S3 region or user location |
| Alias vs CNAME | CNAME cannot be used at zone apex. Alias A = free, works at root domain. Always use Alias for AWS resources. |
| Route 53 routing | Simple routing used here — one CloudFront origin. No health checks needed. |
| CloudFront Invalidation | To serve updated content immediately after S3 change: create Invalidation with path /* |
| Default Root Object | Forgetting index.html = 403 on root URL. Classic SAA trick question scenario. |
| SSL propagation | CloudFront distributes cert to 400+ edge locations — takes 10–15 mins. Not an error. |

**Likely SAA exam scenarios this project covers:**
- "A company wants to host a static website with custom domain and HTTPS. Which services?" → S3 + CloudFront + ACM + Route 53
- "Users get 403 when visiting root domain but /about.html works fine." → Missing Default Root Object
- "How do you prevent direct access to S3 while serving via CloudFront?" → OAC bucket policy
- "Certificate created in eu-west-2 is not showing in CloudFront." → Must be in us-east-1

---

## AWS Services Used

### Amazon S3
- Private bucket: cloudflow-automations-website (eu-west-2)
- Block All Public Access: ON
- Versioning: enabled
- OAC bucket policy — only distribution ARN E3KYEAH6NTZC09 can call s3:GetObject
- Cost: ~$0.01/month

### AWS CloudFront
- Distribution ARN: E3KYEAH6NTZC09
- OAC, HTTPS redirect, TLS 1.3, Default root object: index.html
- Alternate domains: cloudflowautomations.co.uk + www
- Price class: North America and Europe
- Cost: ~$0.05/month

### AWS Certificate Manager (ACM)
- Region: us-east-1 — REQUIRED for CloudFront
- DNS validated via Route 53 — one-click
- Cost: FREE

### Amazon Route 53
- Public hosted zone: cloudflowautomations.co.uk
- 2x Alias A records → CloudFront
- Cost: $0.50/month hosted zone + ~$0.01 queries

---

## Cost

| Service | Cost |
|---|---|
| S3 storage | ~$0.01/month |
| CloudFront | ~$0.05/month |
| ACM certificate | FREE |
| Route 53 | ~$0.51/month |
| **Total** | **~$0.57/month** |

---

## Business Value

This architecture is directly sellable to UK SMEs post-ILR (October 2027):

| Client | Setup Fee | Monthly Support |
|---|---|---|
| Local restaurant / cafe | £300–500 | £50/month |
| Solicitor / accountant firm | £400–600 | £75/month |
| Charity or community group | £200–350 | £40/month |
| Estate agent / letting agent | £500–700 | £100/month |

**Running cost: ~$0.57/month. Client value: £300–700 setup + retainer. That margin is the model.**

---

## SEO Fix — Getting Google to Index the Site

**Problem:** The site is live and loads correctly when you type the URL, but it does not appear in Google search results. This is because Google has not crawled or indexed it yet — the site is essentially invisible to search engines.

**Root cause:** A new website with no backlinks, no sitemap submission, and no Google Search Console verification will not be crawled automatically for weeks or months.

---

### What Was Added to the Codebase

Three files were created/updated to fix this:

**1. `robots.txt` (new file)**
Tells all search engine crawlers they are explicitly allowed to crawl the site. Also points to the sitemap. Without this file, some crawlers behave conservatively.

**2. `sitemap.xml` (new file)**
An XML map of every page on the site. When submitted to Google Search Console it tells Google exactly what pages exist and when they were last updated. This is the single biggest trigger for fast indexing.

**3. `index.html` (updated `<head>` section)**
Added five blocks of SEO metadata:
- `<link rel="canonical">` — tells Google the definitive URL of this page (avoids duplicate indexing of www vs non-www)
- `<meta name="robots">` — explicitly instructs crawlers to index and follow all links
- Open Graph tags — enables rich previews when shared on LinkedIn, WhatsApp, Facebook
- Twitter Card tags — enables rich previews on Twitter/X
- JSON-LD schema (ProfessionalService) — tells Google what your business *is* in machine-readable format, which can trigger rich results in search

---

### Step-by-Step: Get Google to Index the Site

#### Step 1 — Upload the New Files to S3

Go to your S3 bucket: `cloudflow-automations-website` (eu-west-2)

Upload these three files from your local project folder:
- `index.html` (replacing the existing one)
- `robots.txt` (new file — upload to root, same level as index.html)
- `sitemap.xml` (new file — upload to root)

For each file, set the Content-Type correctly:
- `index.html` → `text/html`
- `robots.txt` → `text/plain`
- `sitemap.xml` → `application/xml`

#### Step 2 — Invalidate CloudFront Cache

After uploading, CloudFront still has the old files cached at its 400+ edge locations. You must force it to fetch the new versions.

1. Go to **CloudFront** → your distribution (E3KYEAH6NTZC09)
2. Click the **Invalidations** tab
3. Click **Create Invalidation**
4. In the path field, enter: `/*`
5. Click **Create Invalidation**

Wait 1–2 minutes for the invalidation to complete. Status will show **Completed**.

#### Step 3 — Verify the Files Are Live

Open a browser in Incognito mode and test these URLs:

- `https://cloudflowautomations.co.uk/robots.txt` — should show the robots.txt content
- `https://cloudflowautomations.co.uk/sitemap.xml` — should show the XML sitemap
- `https://cloudflowautomations.co.uk/` — should load the website as normal

If all three work, you are ready for Step 4.

#### Step 4 — Set Up Google Search Console

Google Search Console is Google's free tool for website owners. It is how you tell Google your site exists and track whether Google is indexing it.

1. Go to: **https://search.google.com/search-console**
2. Sign in with a Google account (use your Gmail)
3. Click **Add Property**
4. Choose **URL Prefix** (not Domain)
5. Enter: `https://cloudflowautomations.co.uk/`
6. Click **Continue**

#### Step 5 — Verify Ownership

Google needs to confirm you own the site before it gives you data. The easiest method with S3/CloudFront:

**HTML File Method (recommended for S3):**
1. Google will offer you an HTML file to download (e.g. `google1234abcd.html`)
2. Download it
3. Upload it to your S3 bucket root (same location as index.html)
4. Set its Content-Type to `text/html`
5. Invalidate CloudFront again with path `/*`
6. Test the URL: `https://cloudflowautomations.co.uk/google1234abcd.html` — it should load
7. Go back to Search Console and click **Verify**

Alternative: Google will also offer a **meta tag** method. If you choose this, copy the `<meta name="google-site-verification">` tag and add it to the `<head>` of index.html, then re-upload and invalidate.

#### Step 6 — Submit Your Sitemap to Google

Once verified:

1. In Google Search Console, click **Sitemaps** in the left menu
2. In the "Add a new sitemap" field, enter: `sitemap.xml`
3. Click **Submit**

Google will immediately begin crawling your sitemap. Status should change to **Success** within a few minutes.

#### Step 7 — Request Indexing for the Homepage

1. In Google Search Console, use the top search bar and enter: `https://cloudflowautomations.co.uk/`
2. Click **Request Indexing**
3. Google will queue your URL for crawling — usually within 24–72 hours

#### Step 8 — Also Submit to Bing

Bing (Microsoft) is worth 5–10% of UK searches. Submit via **Bing Webmaster Tools**:

1. Go to: **https://www.bing.com/webmasters**
2. Sign in with a Microsoft account
3. Add your site: `https://cloudflowautomations.co.uk/`
4. Import from Google Search Console (one-click if you already verified there)
5. Submit your sitemap: `https://cloudflowautomations.co.uk/sitemap.xml`

---

### How to Check If Google Has Indexed Your Site

Once you have submitted the sitemap and requested indexing, check progress:

**Method 1 — site: search operator**
Go to Google and search: `site:cloudflowautomations.co.uk`
If any results appear, Google has indexed those pages.
If zero results appear, Google has not indexed yet (keep waiting).

**Method 2 — Google Search Console → Coverage**
Click **Pages** in the left menu → look for pages with status **Indexed, not submitted in sitemap** or **Submitted and indexed**.

**Method 3 — URL Inspection Tool**
In Search Console, paste your URL in the top bar → click **Test Live URL** → Google tells you if it can access and index the page.

---

### Timeline Expectations

| Action | Expected Result |
|---|---|
| Upload files + submit sitemap | Google crawls within 24–72 hours |
| First appearance in search results | 1–4 weeks (new sites take time to earn trust) |
| Ranking for brand name (Cloudflow Automations) | 1–2 weeks after indexing |
| Ranking for service keywords (UK AI automation) | 3–6 months (requires content + backlinks) |

---

### What Will NOT Fix Overnight

SEO for competitive keywords like "AI automation UK" or "business automation consultant" takes months and requires:
- Regular content (blog posts, case studies)
- Backlinks from other websites
- Google Business Profile (for local search)
- Page speed optimisation (already excellent with CloudFront)

The steps above fix the **indexing problem** (Google not knowing the site exists). Ranking competitively is a longer-term content and authority-building effort.

---

## Screenshots

**Live website with HTTPS padlock:**
![Live Website](day13-live-website.png)

**CloudFront — Enabled:**
![CloudFront](day13-cloudfront-enabled.png)

**ACM Certificate — Issued:**
![ACM](day13-acm-issued.png)

**Route 53 records:**
![Route 53](day13-route53-records.png)

**Architecture diagram:**
![Architecture](day13-architecture.svg)
