# Response and Containment Notes

## Issue Observed

Kali could not consistently reach the target because the Snort VM was acting as a router but had a `FORWARD` chain policy of `DROP`.

Diagnostic command:

```bash
sudo iptables -L FORWARD -n -v
```

Observed:

```text
Chain FORWARD (policy DROP ...)
```

## Fix Applied

```bash
sudo ufw disable
sudo iptables -F FORWARD
sudo iptables -P FORWARD ACCEPT
sudo sysctl -w net.ipv4.ip_forward=1
```

## Why This Matters

In a routed IDS lab, packet forwarding must be enabled and allowed. Snort can only inspect traffic that actually crosses the sensor interface. If Linux forwarding or firewall policy blocks the traffic, the IDS will not see the full attack path.

## SOC Lesson

This was a valuable operational lesson: network detection requires more than writing signatures. Analysts and detection engineers also need to understand routing, interface placement, firewalls, and packet flow.

## Optional Containment Example

After confirming Telnet-port traffic, a containment rule could be added:

```bash
sudo iptables -I FORWARD -s 10.10.10.10 -d 10.10.20.20 -p tcp --dport 23 -j DROP
```

Validation:

```bash
nc -vz -w 3 10.10.20.20 23
```

Expected result after blocking:

```text
timed out
```

Remove rule:

```bash
sudo iptables -D FORWARD -s 10.10.10.10 -d 10.10.20.20 -p tcp --dport 23 -j DROP
```
