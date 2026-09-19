"""
GitHub Automated Audit Logger
Securely records and commits post publishing executions, status, and metadata
to the task4 GitHub repository without exposing secrets.
"""

import os
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOGS_DIR = PROJECT_ROOT / "logs"
JSONL_LOG_PATH = LOGS_DIR / "audit_trail.jsonl"
MARKDOWN_LOG_PATH = LOGS_DIR / "ACTIVITY_LOG.md"

def get_env_token() -> Optional[str]:
    """Check for GITHUB_TOKEN or GH_TOKEN from env or .env file securely"""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("GITHUB_TOKEN=") or line.startswith("GH_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None

def ensure_logs_dir():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    if not MARKDOWN_LOG_PATH.exists():
        with open(MARKDOWN_LOG_PATH, "w", encoding="utf-8") as f:
            f.write(
                "# 📜 Fastn Publisher — Automatic GitHub Audit Log\n"
                "> **Repository:** [haseeb786-code/task4](https://github.com/haseeb786-code/task4)  \n"
                "> **Workflow:** `wf_6cfc644efb9d` (`track04_fixed`) | **Org:** `personal_29e5272ccca34fc5d046`  \n"
                "> **Automation Engine:** FastAPI + Fastn Fan-Out + GitHub Sync  \n\n"
                "This document is automatically updated and committed by the publishing workflow whenever a post is created or published.\n\n"
                "---\n\n"
                "## 📊 Live Execution Audit Trail\n\n"
                "| Timestamp (UTC) | Post ID | Title | Platforms & Status | Overall Status | Slack ID / Permalink | GitHub Commit |\n"
                "| :--- | :--- | :--- | :--- | :---: | :--- | :---: |\n"
            )

def record_audit_to_github(audit_entry: Dict[str, Any]) -> Dict[str, Any]:
    """
    Records an execution entry into:
    1. logs/audit_trail.jsonl
    2. logs/ACTIVITY_LOG.md
    3. Git commits locally to branch main and attempts push if token/credentials present.
    """
    ensure_logs_dir()
    
    timestamp = audit_entry.get("timestamp") or datetime.now(timezone.utc).isoformat()
    row_id = audit_entry.get("row_id") or f"post_{int(datetime.now().timestamp())}"
    title = audit_entry.get("title", "Untitled")
    overall_status = audit_entry.get("overall_status", "Published")
    destinations = audit_entry.get("destinations", [])
    retry_status = audit_entry.get("retry_status", "None")
    workflow_info = audit_entry.get("workflow_info", {})
    
    # Extract destination summary
    platforms_summary = []
    slack_permalink = ""
    slack_id = ""
    
    for dest in destinations:
        dest_name = dest.get("destination", "unknown").capitalize()
        if dest.get("skipped"):
            platforms_summary.append(f"{dest_name}: SKIPPED")
        elif dest.get("success"):
            platforms_summary.append(f"{dest_name}: ✓ OK")
            if dest.get("destination") == "slack":
                slack_permalink = dest.get("permalink", "")
                slack_id = dest.get("id", "")
        else:
            err = dest.get("error", "Error")
            platforms_summary.append(f"{dest_name}: ✗ ({err[:25]})")
            
    summary_str = " | ".join(platforms_summary) if platforms_summary else "N/A"
    
    # 1. Append to JSONL
    full_log_data = {
        "timestamp": timestamp,
        "post_id": row_id,
        "title": title,
        "overall_status": overall_status,
        "retry_status": retry_status,
        "workflow_info": workflow_info,
        "destinations": destinations,
        "summary": summary_str
    }
    
    with open(JSONL_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(full_log_data) + "\n")
        
    # 2. Append to Markdown Table
    slack_display = f"[`{slack_id}`]({slack_permalink})" if (slack_id and slack_permalink) else (slack_id or "N/A")
    markdown_row = f"| `{timestamp}` | `{row_id}` | {title[:35]} | {summary_str} | **{overall_status}** | {slack_display} | [PENDING] |\n"
    
    with open(MARKDOWN_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(markdown_row)

    # 3. Perform Git Commit
    git_result = {"committed": False, "pushed": False, "commit_hash": None, "note": None}
    try:
        # Check git status
        subprocess.run(["git", "add", "logs/"], cwd=str(PROJECT_ROOT), capture_output=True, check=True)
        
        commit_msg = f"audit: Auto-record post {row_id} publishing execution [{overall_status}]"
        commit_proc = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True
        )
        
        # Get commit hash
        hash_proc = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True
        )
        commit_hash = hash_proc.stdout.strip()
        git_result["committed"] = True
        git_result["commit_hash"] = commit_hash
        
        # Update Markdown with real commit link
        with open(MARKDOWN_LOG_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        commit_link = f"[`{commit_hash}`](https://github.com/haseeb786-code/task4/commit/{commit_hash})"
        content = content.replace("| [PENDING] |\n", f"| {commit_link} |\n")
        with open(MARKDOWN_LOG_PATH, "w", encoding="utf-8") as f:
            f.write(content)
            
        # Stage & amend the commit with the finalized table
        subprocess.run(["git", "add", "logs/ACTIVITY_LOG.md"], cwd=str(PROJECT_ROOT), capture_output=True)
        subprocess.run(["git", "commit", "--amend", "--no-edit"], cwd=str(PROJECT_ROOT), capture_output=True)

        # 4. Optional secure push if token is available
        token = get_env_token()
        if token:
            remote_url = f"https://x-access-token:{token}@github.com/haseeb786-code/task4.git"
            push_proc = subprocess.run(
                ["git", "push", remote_url, "main"],
                cwd=str(PROJECT_ROOT),
                capture_output=True,
                text=True,
                timeout=10
            )
            if push_proc.returncode == 0:
                git_result["pushed"] = True
                git_result["note"] = "Pushed to GitHub main branch."
            else:
                git_result["pushed"] = False
                git_result["note"] = f"Push error: {push_proc.stderr}"
        else:
            git_result["pushed"] = False
            git_result["note"] = f"Committed to local Git repo ({commit_hash}). Push ready."
            
    except Exception as e:
        git_result["note"] = f"Git operation error: {e}"
        
    return {
        "status": "Logged",
        "jsonl_path": str(JSONL_LOG_PATH),
        "markdown_path": str(MARKDOWN_LOG_PATH),
        "git": git_result
    }
