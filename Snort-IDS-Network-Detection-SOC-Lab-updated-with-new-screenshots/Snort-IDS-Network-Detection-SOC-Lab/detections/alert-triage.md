# Alert Triage Notes

## Triage Workflow

For each Snort alert, the analyst should ask:

1. What is the source IP?
2. What is the destination IP and port?
3. Is the source authorized to perform this activity?
4. Is the destination service expected to be exposed?
5. Is this a single event or repeated behavior?
6. Are there related alerts from the same source?
7. Are there host logs confirming success or failure?
8. What response action is appropriate?

## Alert Prioritization

| Alert Type | Priority | Reason |
|---|---:|---|
| FTP brute-force attempts | High | Credential access behavior |
| Telnet connection attempt | High/Medium | Insecure protocol exposure |
| Nmap FIN/Xmas scan | Medium | Reconnaissance behavior |
| SYN scan / SYN flood | Medium/High | Recon or availability concern |
| SSH connection attempt | Low/Medium | Depends on authorization and frequency |
| HTTP connection attempt | Low | Usually benign unless paired with suspicious payloads |

## Example Escalation Statement

A host at `10.10.10.10` generated multiple reconnaissance and remote service connection alerts against `10.10.20.20`, including Nmap scan patterns, FTP connection attempts, Telnet-port access, SSH access, and HTTP traffic. While authorized in the lab, similar activity in production should be investigated as potential reconnaissance and credential access behavior.

## False Positive Strategy

Reduce false positives by:

- Allowlisting approved vulnerability scanners.
- Tuning detection filters for SYN-based rules.
- Correlating service connection alerts with authentication failures.
- Prioritizing unusual protocols like Telnet.
- Investigating repeated events over isolated single packets.
