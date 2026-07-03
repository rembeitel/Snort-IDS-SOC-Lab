# Attack 08: Limited SYN Traffic With hping3

## Objective

Generate controlled SYN-based traffic to demonstrate Snort detection of high-volume SYN behavior.

## Command

```bash
sudo hping3 -S -p 80 -c 200 -i u10000 10.10.20.20
```

## Evidence

![Kali hping3 SYN traffic](../images/attack-08-kali-hping3-syn-traffic.png)

## Alert Name

`LAB Possible TCP SYN Scan or SYN Flood`

## Source

`10.10.10.10`

## Destination

`10.10.20.20:80`

## Protocol

TCP

## Observed Behavior

Kali sent repeated SYN packets to TCP/80 on the target. The target responded with SYN-ACK packets, showing that the HTTP service was reachable.

## Likely Cause

Authorized limited SYN traffic simulation from Kali.

## MITRE ATT&CK Mapping

**T1498 - Network Denial of Service**

This maps to Network DoS when SYN traffic is high-volume or intended to degrade availability. In this lab, the traffic was intentionally limited and controlled.

## Severity

Medium in the lab; High if seen at scale or against production services.

## Why It Matters

SYN floods can exhaust service resources and impact availability.

## Recommended Action

- Confirm whether the traffic was authorized.
- Rate-limit or block malicious sources.
- Use SYN cookies and network protections where appropriate.
- Monitor service availability and packet volume.
- Tune IDS thresholds to reduce noise while preserving useful alerting.

## False Positive Considerations

Vulnerability scanners or load-testing tools may generate high SYN rates.
