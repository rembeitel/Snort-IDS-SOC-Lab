# Final Report: Snort IDS Network Detection SOC Lab

## Executive Summary

This lab built a network-based SOC detection environment using Kali Linux, Ubuntu, Snort 3, and a routed VirtualBox topology. Kali acted as the attacker system, Ubuntu acted as the target, and a Snort VM sat between them as both router and IDS sensor.

The lab successfully generated and detected multiple categories of attacker-like behavior:

- Network reconnaissance
- TCP scan variants
- FTP brute-force-style authentication attempts
- Telnet-port/insecure protocol access
- SSH remote service access
- HTTP service access
- Limited SYN-based traffic

## Environment

| Component | Role | IP |
|---|---|---|
| Kali Linux | Attacker | 10.10.10.10 |
| Snort VM | IDS router/sensor | 10.10.10.1 / 10.10.20.1 |
| Ubuntu Target | Victim host | 10.10.20.20 |

## Detection Results

| Test | Result |
|---|---|
| ICMP connectivity | Successful |
| Nmap SYN scan detection | Successful |
| Nmap FIN scan detection | Successful |
| Nmap Xmas scan detection | Successful |
| FTP brute force detection | Successful |
| Telnet-port detection | Successful |
| SSH detection | Successful |
| HTTP detection | Successful |
| Limited SYN traffic detection | Successful |

## Investigation Findings

### Reconnaissance

Nmap generated TCP scan traffic against the target. Snort detected SYN, FIN, and Xmas scan behavior. These alerts mapped to **T1046 - Network Service Discovery**.

### Credential Access

Hydra generated repeated FTP authentication attempts. Even though no valid password was found, Snort detected the FTP traffic and produced alerts. This mapped to **T1110 - Brute Force**.

### Remote Services

Snort detected Telnet-port and SSH connection attempts. Telnet-port activity was simulated with a netcat listener on TCP/23. These detections mapped to **T1021 - Remote Services** and **T1021.004 - SSH**.

### DoS-Style Traffic

hping3 generated limited SYN traffic against TCP/80. Snort detected this as possible SYN scan or SYN flood behavior. This mapped to **T1498 - Network Denial of Service** when interpreted as availability-impacting traffic.

## Troubleshooting and Lessons Learned

The most important troubleshooting issue was packet forwarding. The Snort VM had a default `FORWARD` policy of `DROP`, preventing Kali-to-target traffic from passing through the IDS router.

Fix:

```bash
sudo ufw disable
sudo iptables -F FORWARD
sudo iptables -P FORWARD ACCEPT
sudo sysctl -w net.ipv4.ip_forward=1
```

This reinforced an important SOC lesson: detection depends on visibility. A sensor must be placed correctly and network traffic must actually flow through it.

## Recommended Defensive Actions

- Disable Telnet and other cleartext protocols.
- Replace FTP with secure file transfer.
- Enforce strong passwords and account lockout controls.
- Restrict SSH access to trusted management networks.
- Monitor for repeated authentication attempts.
- Tune Snort rules based on baseline traffic.
- Correlate IDS alerts with endpoint logs, authentication logs, and firewall logs.

## Portfolio Value

This project demonstrates the ability to:

- Build a routed lab network.
- Configure and validate Snort IDS rules.
- Generate attack traffic safely.
- Triage IDS alerts.
- Map alerts to MITRE ATT&CK.
- Document evidence with screenshots.
- Explain false positives, impact, and response actions.

## Additional Kali Evidence Added

Two additional screenshots were added to the repository to strengthen the attack evidence sections:

- `images/attack-01-02-04-kali-command-sequence.png` shows the Kali-side sequence for successful ICMP connectivity, Nmap SYN scanning, Hydra FTP brute-force simulation, and FIN scanning.
- `images/attack-03-05-06-kali-combined-evidence.png` shows the Kali-side Xmas scan, TCP/23 Telnet-port test behavior, and SSH remote-service access evidence.

These screenshots provide attacker-side context to pair with the Snort alert screenshots and help demonstrate the full SOC workflow from traffic generation to IDS detection.
