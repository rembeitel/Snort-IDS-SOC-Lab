# Attack 02: Nmap FIN Scan

## Objective

Simulate a stealthier reconnaissance technique using an Nmap FIN scan.

## Command

```bash
sudo nmap -sF 10.10.20.20
```

## Evidence

![Kali FIN scan](../images/attack-02-kali-fin-scan.png)

![Kali command sequence including FIN scan results](../images/attack-01-02-04-kali-command-sequence.png)

![Snort FIN alerts](../images/attack-02-snort-fin-alerts.png)

## Alert Name

`LAB Possible Nmap FIN Scan`

## Source

`10.10.10.10`

## Destination

`10.10.20.20`

## Protocol

TCP

## Observed Behavior

Snort detected packets with the FIN flag set against multiple destination ports.

## Likely Cause

Authorized Nmap FIN scan from Kali.

## MITRE ATT&CK Mapping

**T1046 - Network Service Discovery**

FIN scans are commonly used to probe service behavior and gather information about exposed ports.

## Severity

Medium

## Why It Matters

FIN scans may be used to evade simplistic detection or firewall logic. Seeing this in an enterprise network from an unexpected source would be suspicious.

## Recommended Action

- Confirm whether the scan source is approved.
- Review destination services.
- Compare against vulnerability scan schedules.
- Investigate follow-up connection attempts.

## False Positive Considerations

Some network tools or malformed traffic may create FIN-only packets, but repeated FIN probes across many ports are suspicious.
