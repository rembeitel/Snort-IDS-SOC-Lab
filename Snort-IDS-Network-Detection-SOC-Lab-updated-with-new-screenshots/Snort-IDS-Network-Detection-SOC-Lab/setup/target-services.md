# Target Services

The Ubuntu Target VM exposed controlled lab services for IDS testing.

## Services Used

| Port | Service | Purpose |
|---:|---|---|
| 21 | FTP / vsftpd | Brute-force simulation |
| 22 | SSH | Remote service connection detection |
| 23 | Netcat listener simulating Telnet exposure | Insecure protocol detection |
| 80 | Apache HTTP | HTTP connection detection |

## FTP / SSH / HTTP Setup

```bash
sudo apt update
sudo apt install -y openssh-server vsftpd apache2
sudo systemctl enable --now ssh
sudo systemctl enable --now vsftpd
sudo systemctl enable --now apache2
```

## Lab User

```bash
sudo useradd -m -s /bin/bash socuser
echo "socuser:Password123!" | sudo chpasswd
```

## Telnet-Port Simulation

A full Telnet server was not required. A controlled netcat listener was used on TCP/23:

```bash
sudo apt install -y netcat-openbsd
sudo nc -lk -p 23
```

Validation:

```bash
sudo ss -tulpn | grep :23
```

Expected:

```text
tcp LISTEN 0 1 0.0.0.0:23 0.0.0.0:* users:(("nc",pid=...,fd=3))
```

This provided network traffic to TCP/23 so Snort could detect insecure remote access port usage.
