# 2-Minute Demo Video Script — Fastn Social Publisher
**Fastn Hackathon 2026 — Track 04: Cross-Platform Social Publisher**  
**Team:** FourFrontLab (Taha & Haseeb)  
**Target Duration:** Exactly 1 minute 50 seconds to 2 minutes  
**Format:** Screen recording with voiceover (split-screen or sequenced tabs)

---

## Pre-Recording Checklist & Tabs Setup

Have the following browser tabs open and ready:
1. **Tab 1: Fastn Workflow Canvas** (`wf_6cfc644efb9d` in `app.fastn.dev`).
2. **Tab 2: Google Sheets** ([Live Matrix](https://docs.google.com/spreadsheets/d/1wquYVUl_EBAUjixTCV-rXPLH4pth7j5OJ0okZRzgD5s/edit)).
3. **Tab 3: Slack Channel** (`#social` in `fourfrontlab.slack.com`).
4. **Tab 4: Discord Channel** (Server text announcements).
5. **Tab 5: Facebook Page** ([FourFrontLab Facebook Feed](https://www.facebook.com/profile.php?id=61594296098147)).
6. **Tab 6: Fastn Embeddable Form Widget** (`wgt_c70a813b22ba`).

---

## Step-by-Step Script & Timing

### 0:00 – 0:20 (20s): Problem Statement & Architecture
* **Visual:** Show the Fastn Workflow Canvas (`wf_6cfc644efb9d`) showing the nodes and parallel branches.
* **Voiceover:**
  > *"Hi, we are team FourFrontLab, presenting Track 04: Cross-Platform Social Publisher on Fastn. Marketing and engineering teams struggle to publish announcements across Slack, Discord, Facebook, and Google Sheets without broken formats, missing character limits, or brittle automations where one failing channel crashes the entire pipeline. We solved this natively on Fastn with Audience-Aware Content Polymorphism and a Decentralized Async Fault Isolation Mesh."*

---

### 0:20 – 0:45 (25s): The Input & Trigger (Dual-Head Control)
* **Visual:** Switch to Tab 6 (Fastn Web Form Widget) or Tab 2 (Google Sheets row).
* **Action:** Enter a live test announcement:
  * **Title:** `"Fastn AI Publisher 2.0 Live"`
  * **Content:** `"Delivering real-time announcements with zero-dropout fault isolation!"`
  * **Link:** `"https://fastn.ai"`
  * **Image URL:** Unsplash tech banner URL.
  * **Tags:** `"fastn, ai, automation"`
* **Voiceover:**
  > *"Content can be triggered via scheduled Google Sheets polling, raw webhooks, or this embeddable Fastn form widget. We submit the announcement once with full metadata: title, content, image, link, and tags."*

---

### 0:45 – 1:15 (30s): Parallel Fan-Out & Multi-Platform Verification
* **Visual:** Quickly switch through the live destination tabs in real time:
  1. **Slack (`#social`):** Show the freshly delivered message. Highlight the Block Kit header, formatted mrkdwn body, clickable link button, and image block.
  2. **Discord:** Show the live message with the blurple Rich Embed, timestamp footer, and inline tag fields.
  3. **Facebook Page (`FourFrontLab`):** Refresh the feed to show the post with caption and preview link published live via our webhook relay.
* **Voiceover:**
  > *"Fastn's workflow engine immediately fans out in parallel. Here in Slack #social, our compiler formatted a native Block Kit layout with interactive links and images. In Discord, it rendered a brand-colored Rich Embed with metadata fields. And on our Facebook Page, it posted the complete conversational copy with preview links—all dispatched simultaneously."*

---

### 1:15 – 1:35 (20s): Bi-directional Audit Log-Back in Google Sheets
* **Visual:** Switch to Tab 2 (Google Sheets).
* **Action:** Scroll to the newest confirmation row appended at the bottom. Highlight columns F, G, and H.
* **Voiceover:**
  > *"Crucially, Fastn closes the loop. The workflow captures the Slack message timestamp, builds a permanent archive permalink, records the Facebook post ID, and writes an immutable confirmation row back to Google Sheets. If an operator clicks this permalink, it opens the exact Slack archive message directly."*

---

### 1:35 – 1:55 (20s): Fault Isolation & MCP Gateway Integration
* **Visual:** Show the execution result in Fastn / terminal showing `Partially Published` and show the Antigravity MCP Gateway panel with 205 tools.
* **Voiceover:**
  > *"If Twitter or an unconfigured channel returns an error, our fault isolation mesh catches it without failing the run, returning 'Partially Published' with detailed diagnostic traces. Finally, our entire workflow, widget, and connector bindings were developed and audited using the Fastn Connect MCP Gateway with over 200 live tools. Thank you!"*

---

## Video Submission Checklist:
- [ ] Recording time $\le$ 2 minutes (120 seconds).
- [ ] Export as MP4 / WebM (1080p recommended).
- [ ] Upload to Google Drive.
- [ ] **CRITICAL:** Set link sharing to **"Anyone with the link can view"**.
- [ ] Paste link into the official submission form.
