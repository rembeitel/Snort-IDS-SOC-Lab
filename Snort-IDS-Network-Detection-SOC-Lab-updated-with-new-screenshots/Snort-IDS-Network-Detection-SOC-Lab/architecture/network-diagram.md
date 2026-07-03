# Network Architecture

## Logical Topology

```text
                     VirtualBox Isolated Lab

                   attacker-net: 10.10.10.0/24
                   target-net:   10.10.20.0/24

        Kali Attacker
        10.10.10.10
             |
             | attacker-net
             |
        Snort IDS Sensor / Router
        enp0s8: 10.10.10.1
        enp0s9: 10.10.20.1
             |
             | target-net
             |
        Ubuntu Target
        10.10.20.20
```

## Why the Snort VM Was Placed in the Middle

The Snort VM was used as a router between the attacker and target networks. This design ensures that traffic from Kali to the Ubuntu Target must pass through the Snort sensor.

This is better than placing all VMs on one flat network because a flat network may not reliably expose VM-to-VM traffic to the Snort interface, depending on VirtualBox adapter behavior.

## Interface Roles

| VM | Interface | IP | Purpose |
|---|---:|---:|---|
| Kali | Internal adapter | 10.10.10.10/24 | Attacker subnet |
| Snort | enp0s8 | 10.10.10.1/24 | Attacker-side gateway |
| Snort | enp0s9 | 10.10.20.1/24 | Target-side gateway |
| Target | Internal adapter | 10.10.20.20/24 | Target subnet |

## Required Routes

### Kali

```bash
sudo ip route replace 10.10.20.0/24 via 10.10.10.1 dev enp0s8
```

### Target

```bash
sudo ip route replace 10.10.10.0/24 via 10.10.20.1 dev enp0s8
```

### Snort Router

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```
