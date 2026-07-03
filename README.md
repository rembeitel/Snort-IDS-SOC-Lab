# Snort IDS Network Detection SOC Lab

## Overview

This project is a network-based SOC home lab built to practice intrusion detection, alert triage, and incident investigation using **Snort IDS**.

After completing host-based detection work with Wazuh, I wanted to build a lab focused on **network visibility**: seeing attacker behavior as it moves across the wire, writing detection rules, reviewing alerts, and documenting findings like a SOC analyst.

The lab was built in an isolated VirtualBox environment with:

- **Kali Linux** as the attacker machine
- **Ubuntu Server** as the target system
- **Ubuntu + Snort IDS** acting as the network sensor/router between the attacker and target networks

## Lab Goals

The main goals of this lab were to:

- Build a routed virtual network for IDS monitoring
- Configure Snort to inspect traffic between attacker and target systems
- Write custom Snort rules for common attack behaviors
- Simulate reconnaissance, brute force, insecure protocol usage, and DoS-style traffic
- Review Snort alerts and map findings to MITRE ATT&CK
- Document the investigation process with screenshots, alerts, and analyst notes

## Simulated Attacks

The lab includes detection and documentation for:

- ICMP ping/reachability testing
- Nmap SYN scan
- Nmap FIN scan
- Nmap Xmas scan
- FTP brute-force simulation with Hydra
- Telnet/insecure protocol detection
- SSH connection attempts
- HTTP connection attempts
- Limited SYN flood-style traffic with hping3

## Skills Demonstrated

This project demonstrates hands-on experience with:

- Snort IDS setup and configuration
- Custom Snort rule writing
- Linux networking and IP forwarding
- Firewall and iptables troubleshooting
- Network traffic analysis
- Alert validation and triage
- MITRE ATT&CK mapping
- SOC-style investigation documentation
- Python-based alert visualization

## MITRE ATT&CK Mapping

| Activity | MITRE Technique |
|---|---|
| Nmap scanning | T1046 - Network Service Discovery |
| FTP brute force | T1110 - Brute Force |
| SSH/Telnet access attempts | T1021 - Remote Services |
| Telnet traffic | T1021.004 - SSH and Telnet |
| SYN flood-style traffic | T1498 - Network Denial of Service |

## Key Takeaway

This lab helped reinforce that effective SOC analysis is not just about generating alerts. It is about understanding the full context: source IPs, destination ports, timing, protocol behavior, attack patterns, and how each alert fits into a larger investigation.

The project gave me practical experience moving from raw IDS alerts to detection logic, investigation notes, MITRE mapping, and response recommendations.

## Repository Contents

```text
architecture/     Network design and lab layout
attacks/          Individual attack walkthroughs and evidence
detections/       MITRE mapping, triage notes, and detection logic
dashboard/        Python/Streamlit alert visualization
images/           Screenshots from lab execution
response/         Firewall containment and response notes
snort/            Snort rules and sample alert output
final-report.md   Full SOC-style project report
