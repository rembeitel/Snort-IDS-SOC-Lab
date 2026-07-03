# GitHub Upload Guide

## Option 1: Upload Through GitHub Web

1. Create a new GitHub repository.
2. Name it:

```text
Snort-IDS-Network-Detection-SOC-Lab
```

3. Upload the contents of this folder.
4. Commit with a message like:

```text
Initial commit: Snort IDS SOC detection lab
```

## Option 2: Upload With Git

From inside the project folder:

```bash
git init
git add .
git commit -m "Initial commit: Snort IDS SOC detection lab"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Snort-IDS-Network-Detection-SOC-Lab.git
git push -u origin main
```

## Suggested LinkedIn Description

I built a network-based SOC home lab using Kali Linux, Ubuntu, Snort IDS, and a routed VirtualBox network.

The lab simulated Nmap reconnaissance, FTP brute-force attempts, Telnet-port/insecure protocol traffic, SSH access, HTTP traffic, and controlled SYN-based traffic. I wrote custom Snort rules, validated alerts, mapped detections to MITRE ATT&CK, and documented the investigation process with screenshots and analyst notes.

This project helped me better understand how network IDS visibility, routing, firewall forwarding, alert triage, and detection logic all come together in a SOC workflow.
