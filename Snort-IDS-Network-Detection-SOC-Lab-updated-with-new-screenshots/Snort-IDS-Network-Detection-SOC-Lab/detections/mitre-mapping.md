# MITRE ATT&CK Mapping

## Summary Table

| Lab Activity | Alert | MITRE Technique | Why It Fits |
|---|---|---|---|
| Nmap SYN scan | `LAB Possible TCP SYN Scan or SYN Flood` | T1046 - Network Service Discovery | The activity attempts to identify exposed services on a remote host. |
| Nmap FIN scan | `LAB Possible Nmap FIN Scan` | T1046 - Network Service Discovery | FIN scan behavior is reconnaissance-focused. |
| Nmap Xmas scan | `LAB Possible Nmap Xmas Scan` | T1046 - Network Service Discovery | Unusual TCP flags are used to probe service state. |
| FTP brute force | `LAB FTP Password Submitted - Possible Brute Force` | T1110 - Brute Force | Repeated credential attempts are made against a remote service. |
| Telnet-port access | `LAB Telnet Connection Attempt - Insecure Protocol` | T1021 - Remote Services | Telnet is a remote access service and is risky due to cleartext transmission. |
| SSH access | `LAB SSH Connection Attempt` | T1021.004 - Remote Services: SSH | SSH is a remote service commonly used for administration and sometimes abused by adversaries. |
| Limited SYN traffic | `LAB Possible TCP SYN Scan or SYN Flood` | T1498 - Network Denial of Service | High-volume SYN traffic can degrade service availability. |
| HTTP access | `LAB HTTP Connection Attempt` | Context-dependent | HTTP traffic is benign by itself but useful in context with scans or web attacks. |

## Technique Notes

### T1046 - Network Service Discovery

Network service discovery involves identifying services running on remote hosts. In this lab, Nmap SYN, FIN, and Xmas scans were used to generate reconnaissance behavior.

### T1110 - Brute Force

Brute force activity involves repeated attempts to guess credentials. In this lab, Hydra attempted multiple FTP logins against the target.

### T1021 - Remote Services

Remote services include protocols like Telnet and SSH. In this lab, Snort detected connection attempts to TCP/23 and TCP/22.

### T1498 - Network Denial of Service

Network denial of service involves attempts to degrade or block service availability. In this lab, hping3 generated controlled SYN traffic to simulate DoS-style packet behavior.

## Important Analyst Note

MITRE mapping should be used carefully. A single alert does not prove malicious intent. Mapping becomes stronger when the alert is combined with context such as:

- Source host identity
- Authorization status
- Frequency of attempts
- Destination criticality
- Authentication logs
- Follow-up exploitation attempts
- Baseline behavior
