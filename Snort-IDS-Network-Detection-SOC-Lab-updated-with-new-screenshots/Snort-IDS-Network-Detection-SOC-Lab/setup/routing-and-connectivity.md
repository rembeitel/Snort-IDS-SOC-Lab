# Routing and Connectivity Setup

## Snort VM IP Setup

```bash
sudo ip addr add 10.10.10.1/24 dev enp0s8
sudo ip addr add 10.10.20.1/24 dev enp0s9
sudo ip link set enp0s8 up
sudo ip link set enp0s9 up
sudo sysctl -w net.ipv4.ip_forward=1
```

## Kali IP and Route

```bash
sudo ip addr add 10.10.10.10/24 dev enp0s8
sudo ip link set enp0s8 up
sudo ip route replace 10.10.20.0/24 via 10.10.10.1 dev enp0s8
```

## Target IP and Route

```bash
sudo ip addr add 10.10.20.20/24 dev enp0s8
sudo ip link set enp0s8 up
sudo ip route replace 10.10.10.0/24 via 10.10.20.1 dev enp0s8
```

## Forwarding Troubleshooting

During the lab, the Snort VM had a `FORWARD` chain policy of `DROP`.

Diagnostic command:

```bash
sudo iptables -L FORWARD -n -v
```

Problem observed:

```text
Chain FORWARD (policy DROP ...)
```

Fix:

```bash
sudo ufw disable
sudo iptables -F FORWARD
sudo iptables -P FORWARD ACCEPT
sudo sysctl -w net.ipv4.ip_forward=1
```

Expected result:

```text
Chain FORWARD (policy ACCEPT)
```

## Connectivity Validation

From Kali:

```bash
ping -c 4 10.10.10.1
ping -c 4 10.10.20.1
ping -c 4 10.10.20.20
```

Evidence:

![Kali ping success](../images/attack-01-kali-ping-and-syn-scan.png)
