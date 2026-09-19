# Fastn Hackathon 2026 — Final Submission Checklist
**Track 04: Cross-Platform Social Publisher**  
**Submission Deadline:** Saturday, 19 September 2026 at **4:30 PM PKT sharp**

---

## 1. Quick Copy-Paste Form Data

Use this exact text block when filling out the official submission form:

* **Track:** `Track 04 — Cross-platform social publisher`
* **Team Name:** `FourFrontLab`
* **Team Members:** `Taha Nadeem, Haseeb`
* **Fastn Org ID:** `personal_29e5272ccca34fc5d046` (`Hackathon_FourFrontLab`)
* **Workflow Name & ID:** `Track 04 Fixed` (`wf_6cfc644efb9d`)
* **Workflow URL:** `https://app.fastn.dev/integrations?tab=workflows`
* **Google Spreadsheet URL:** `https://docs.google.com/spreadsheets/d/1wquYVUl_EBAUjixTCV-rXPLH4pth7j5OJ0okZRzgD5s/edit`
* **Facebook Page Feed:** `https://www.facebook.com/profile.php?id=61594296098147`
* **Fastn Form Widget ID:** `wgt_c70a813b22ba`
* **Fastn Connect MCP Gateway URL:** `https://mcp.fastn.dev/u-dtpftaoo`

---

## 2. Mandatory Submission Items Status

| Item | Requirement | Status | Action Required |
| :--- | :--- | :---: | :--- |
| **1. Workflow Link** | Working workflow link in Fastn | **READY** | Direct URL: `https://app.fastn.dev/integrations?tab=workflows` (`wf_6cfc644efb9d`) |
| **2. Demo Video** | 2-minute video on Google Drive | **ACTION NEEDED** | Record following [`DEMO_SCRIPT.md`](./DEMO_SCRIPT.md), upload to Drive, verify sharing |
| **3. Video Permissions** | "Anyone with the link can view" | **CRITICAL** | Right-click video in Drive $\rightarrow$ Share $\rightarrow$ General access: **Anyone with the link** |
| **4. Short Document** | Document explaining automation | **READY** | Full documentation in [`README.md`](./README.md) & [`EXECUTIVE_AUDIT_REPORT.md`](./EXECUTIVE_AUDIT_REPORT.md) |
| **5. Screenshots (3+)** | Proof of workflow & destinations | **READY TO CAPTURE** | 1. Workflow Canvas<br>2. Slack #social + Discord embeds + Facebook Page<br>3. Google Sheets Confirmation Matrix |
| **6. Team Details** | Team name, members, track | **READY** | FourFrontLab (Taha & Haseeb), Track 04 |
| **7. Feedback Form** | Mandatory individual form | **ON-SITE** | Both Taha and Haseeb must fill out the form at SEECS, NUST before closing ceremony |

---

## 3. Required Screenshot Capture Guide

Prepare 3 high-resolution screenshots for the submission form:

### Screenshot 1: Fastn Workflow Canvas (`workflow_canvas.png`)
* Go to [Fastn Workflows](https://app.fastn.dev/integrations?tab=workflows).
* Open `Track 04 Fixed` (`wf_6cfc644efb9d`).
* Capture the full canvas showing the input trigger, parallel fan-out branches (Slack, Discord, Facebook), and Google Sheets appendValues log-back node.

### Screenshot 2: Live Multi-Destination Delivery (`destinations_live.png`)
* Side-by-side view (or combined composite) showing:
  * **Slack:** `#social` channel with Block Kit layout, mrkdwn formatting, and button.
  * **Discord:** Server text channel showing the rich embed with tags and color.
  * **Facebook:** `FourFrontLab` page feed showing live post ("Published by Make").

### Screenshot 3: Bi-directional Confirmation Matrix in Google Sheets (`sheets_audit.png`)
* Go to [Google Sheet Matrix](https://docs.google.com/spreadsheets/d/1wquYVUl_EBAUjixTCV-rXPLH4pth7j5OJ0okZRzgD5s/edit).
* Highlight columns showing `Timestamp`, `Title`, `Overall Status` (`Published` / `Partially Published`), `Slack ID`, `Slack Archive Permalink`, and `Fan-out Summary`.
