# DevOps Learning and Practice

## Description

This repository contains practice scripts and notes created while learning foundational **Linux command-line skills, Bash scripting, Python scripting, Git version control, Intro to Docker, Docker Compose, Intro to AWS Core Services, AWS Networking & Compute, Kubernetes(K8s), Infrastructure as Code(Terraform), and CI/CD Integration & Monitoring Basics** specifically focused on building a base for a career in DevOps.

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
    
### 4. Intro to AWS & Core Services

Introduced to Cloud Computing concepts (IaaS, PaaS, SaaS) and the AWS Global Infrastructure (Regions, Availability Zones). Learned about the Shared Responsibility Model and the AWS Free Tier.
*   **Account Setup:** Created an AWS account and secured the root user with MFA.
*   **IAM (Identity & Access Management):** Understood Users, Groups, Roles, Policies, and the Principle of Least Privilege. Created an administrative IAM user with MFA for regular tasks.
*   **EC2 (Elastic Compute Cloud):** Launched a basic Ubuntu EC2 instance. Learned about AMIs, Instance Types, SSH Key Pairs for secure login, and Security Groups (basic firewall rules). Connected to the instance using SSH. Terminated the instance.
*   **S3 (Simple Storage Service):** Basic introduction to object storage concepts (Buckets, Objects, Keys). Created a bucket, uploaded/downloaded an object via the console.
*   **VPC (Virtual Private Cloud):** Conceptual overview of AWS networking (CIDR, Subnets, Route Tables, Internet Gateway) and how EC2 instances fit within a VPC. Understood the role of the Default VPC.

### 5. Docker Fundamentals

Learned about containerization concepts and why Docker is used to solve the "it works on my machine" problem. Key concepts covered:
*   Images vs. Containers
*   Dockerfile basics (FROM, WORKDIR, COPY, RUN, EXPOSE, ENV, CMD)
*   Docker Engine (Daemon, API, CLI)
*   Docker Hub / Registries
*   Running containers (`docker run`, `-it`, `-d`, `-p`, `--name`)
*   Managing containers (`docker ps`, `docker logs`, `docker stop`, `docker rm`)
*   Managing images (`docker images`, `docker rmi`)
*   Installed Docker Desktop for WSL integration.
*   Built a custom image for a simple Python Flask application.

## Docker Volumes

Understood the need for persistent data for containers, as container filesystems are ephemeral.
*   Learned about Docker Volumes as the preferred persistence mechanism.
*   Used `-v volume-name:/container/path` to mount volumes.
*   Demonstrated data persistence across container removal.
*   Briefly discussed Bind Mounts (`-v /host/path:/container/path`) for development/config.

### 6. Docker Compose

Learned how Docker Compose simplifies managing multi-container applications.
*   Defined services, networks, and volumes in a `docker-compose.yml` file.
*   Used `docker compose up -d --build` to build and start services.
*   Used `docker compose ps`, `docker compose logs`, and `docker compose down` to manage the application stack.
*   Configured a simple Flask app service using Compose.

### 7. CI/CD Concepts

Introduced the core ideas behind Continuous Integration (CI) and Continuous Delivery/Deployment (CD).
*   **CI:** Frequent code integration, automated builds, automated testing. Goal: Early error detection, rapid feedback.
*   **CD (Delivery):** Automatically deploying validated builds to staging environments. Goal: Always having a releasable version.
*   **CD (Deployment):** Automatically deploying validated builds to production. Goal: Maximum release velocity.
*   Discussed benefits (speed, quality, reduced risk) and common tools (Jenkins, GitLab CI, GitHub Actions).
*   Recognized Docker's role in providing consistent build/test environments and as a deployment artifact.

### 8. AWS Deeper Dive.[VPC(Routing,Security), E2C(AMIs, Storage options, User Data)]
*   **Created a custom AMI from an instance and modified Security Group**
    *   Prepare SSH Key and Security Group.
    *   Launch EC2 Instance with User Data.
    *   Verify Nginx Installation: Connect via SSH and check if Nginx is running without manual installation. Test web access.
    *   Create Custom AMI.
    *   Terminate Original Instance.
    *   Launch New Instance from Custom AMI.
    *   Verify New Instance.
    *   Terminate Second Instance.

## 8. Introduction to Kubernetes (K8s)

Transitioned from Docker/Compose to understanding container orchestration for running applications at scale.

### Core Concepts:
- **Problems Solved:** Addressed challenges beyond Docker Compose like scaling, self-healing, service discovery, and rolling updates.
- **Declarative Model:** Defined desired state using YAML manifests, letting Kubernetes reconcile the current state.
- **Basic Architecture:**
    - **Control Plane:** API Server, etcd, Scheduler, Controller Manager.
    - **Nodes (Workers):** Kubelet, Kube-proxy, Container Runtime.

### Key Kubernetes Objects:
- **Pods:** Smallest deployable unit, encapsulating one or more containers, storage, and network IP. Ephemeral.
- **Deployments:** Manage stateless applications by declaratively defining Pod replicas and handling rolling updates/rollbacks via ReplicaSets. Provides self-healing.
- **Services:** Provide stable network endpoints (IP/DNS) and load balancing to access a set of Pods.
    - Types explored: `ClusterIP` (internal), (briefly mentioned `NodePort`, `LoadBalancer`).
- **Namespaces:** Partition a physical cluster into virtual clusters for organization, access control, and resource quotas. Used `default`, `kube-system`, and created custom `dev`/`staging` namespaces.
- **ConfigMaps:** Store non-confidential configuration data as key-value pairs.
- **Secrets:** Store sensitive data (passwords, API keys). Values are base64 encoded.
    - Consumed ConfigMaps/Secrets in Pods via environment variables and volume mounts.

### Interaction Tool: `kubectl`
- The primary command-line tool for interacting with the Kubernetes API.
- **Setup:** Enabled Kubernetes in Docker Desktop and configured `kubectl`.
- **Basic Commands:**
    - `kubectl config current-context`, `kubectl cluster-info`, `kubectl get nodes`
    - `kubectl get pods/services/deployments/namespaces [-n <namespace>] [-A]`
    - `kubectl describe <type> <name> [-n <namespace>]`
    - `kubectl apply -f <filename.yaml>` (for creating/updating resources)
    - `kubectl delete -f <filename.yaml>` (for deleting resources)
    - `kubectl logs <pod_name> [-f] [-n <namespace>]`
    - `kubectl exec -it <pod_name> -- bash [-n <namespace>]`
    - `kubectl scale deployment <name> --replicas=<count> [-n <namespace>]`
    - `kubectl port-forward service/<service_name> <local_port>:<service_port> [-n <namespace>]`
- **YAML Manifests:** Learned to define Deployments, Services, Namespaces, ConfigMaps, and Secrets using YAML.

### Practical Exercises:
- Deployed Nginx using YAML manifests (Deployment and Service).
- Deployed Nginx into separate `dev` and `staging` namespaces.
- Created and consumed ConfigMaps and Secrets in a Pod.

---
*(Next up in K8s: Persistent Volumes, different Service types in detail, advanced Deployment strategies)*

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
