# DevOps Linux and Scripting Practice

## Description

This repository contains practice scripts and notes created while learning foundational Linux command-line skills, Bash scripting, Python scripting, and Git version control, specifically focused on building a base for a career in DevOps.

This follows a structured learning plan aiming to cover core DevOps competencies.

## Learning Journey & Contents

This repository documents the initial phases of the learning plan:

### 1. Linux Fundamentals & Core Utilities
*   Basic navigation (`pwd`, `cd`, `ls`)
*   File/Directory manipulation (`mkdir`, `touch`, `cp`, `mv`, `rm`)
*   Permissions (`chmod`, `chown`, `chgrp`)
*   Text processing (`cat`, `less`, `head`, `tail`, `grep`, `wc`, `|`)
*   Text editing (`nano`)
*   Process management (`ps`, `top`, `kill`, `&`, `jobs`, `fg`, `bg`)
*   Basic Networking (`ip`, `ping`, `dig`, `ss`, `curl`, `wget`)
*   Package management (`apt`)
*   SSH & Secure Copy (`ssh`, `ssh-keygen`, `ssh-copy-id`, `scp`, `rsync`)
*   User & Group Management (`useradd`, `usermod`, `groupadd`, `sudo`, `visudo`)
*   Service Management (`systemctl`, `journalctl`) - Includes Nginx practice.
*   Finding Files (`find`, `locate`, `which`)
*   Environment Variables (`env`, `export`, `.bashrc`)
*   Disk Usage (`df`, `du`, `lsblk`)

### 2. Git & Version Control
*   Repository initialization (`git init`, `git clone`)
*   Core workflow (`git add`, `git commit`, `git status`, `git log`)
*   Branching & Merging (`git branch`, `git switch`/`checkout`, `git merge`)
*   Handling conflicts (manual resolution)
*   Remotes (`git remote`, `git push`, `git pull`, `git fetch`) - Integration with GitHub.
*   Ignoring files (`.gitignore`)
*   Inspecting changes (`git diff`)
*   Amending, reverting, resetting, stashing (`git commit --amend`, `git revert`, `git reset`, `git stash`)

### 3. Scripting Basics

*   **Bash Scripting:**
    *   Shebang (`#!/bin/bash`)
    *   Variables, Arguments (`$1`, `$?`, `$#`)
    *   Command Substitution (`$(...)`)
    *   Conditional Logic (`if`, `elif`, `else`, `[ ]`, file/string/numeric tests)
    *   Loops (`for`, `while`, reading files line-by-line)
    *   Example Scripts: `checker.sh`, `user_processor.sh`, `read_file.sh` (if you created them)
*   **Python Scripting (for DevOps):**
    *   Setup (`python3`, `pip`, `venv`) - Understanding PEP 668.
    *   Basic Syntax & Data Types (`str`, `int`, `float`, `bool`, `list`, `dict`, `None`)
    *   Running External Commands (`subprocess.run`, error handling)
    *   Control Flow (`if`/`elif`/`else`, `for`, `while`)
    *   Functions (`def`, parameters, return values, scope)
    *   Example Scripts:  `syntax.py`, `run_commands.py`, `conditions.py`, `loops.py`, `functions.py`, `manage_service.py`

## How to Use

*   Clone the repository: `git clone <repository_url>`
*   Bash scripts (`.sh`) can be run using `bash script_name.sh` or made executable (`chmod +x script_name.sh`) and run via `./script_name.sh`.
*   Python scripts (`.py`) should generally be run within a Python 3 virtual environment:
    1.  `python3 -m venv venv` (create environment)
    2.  `source venv/bin/activate` (activate environment)
    3.  `pip install -r requirements.txt` (if a requirements file exists - good practice to add later!)
    4.  `python3 script_name.py [arguments]`
    5.  `deactivate` (when finished)
*   **Note:** Some scripts (like `manage_service.py`) use `sudo` internally and require appropriate privileges to run successfully.

## Next Steps

Continuing the DevOps learning roadmap, focusing on:
*   Cloud Computing (AWS/Azure/GCP Core Services)
*   Containerization (Docker)
*   CI/CD (Jenkins/GitLab CI/GitHub Actions)
*   Infrastructure as Code (Terraform)
*   Configuration Management (Ansible)
*   Monitoring (Prometheus/Grafana/ELK)

---

*This repository reflects a personal learning journey and is a work in progress.*
