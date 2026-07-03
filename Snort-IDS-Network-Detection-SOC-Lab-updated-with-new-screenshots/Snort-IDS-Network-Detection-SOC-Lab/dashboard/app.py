import re
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Snort IDS SOC Dashboard", layout="wide")

LOG_FILE = Path("snort.alert.fast")

ALERT_PATTERN = re.compile(
    r'(?P<timestamp>\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+)\s+'
    r'\[\*\*\]\s+\[(?P<gid>\d+):(?P<sid>\d+):(?P<rev>\d+)\]\s+'
    r'"(?P<msg>.*?)"\s+\[\*\*\]\s+'
    r'\[Classification:\s+(?P<classification>.*?)\]\s+'
    r'\[Priority:\s+(?P<priority>\d+)\]\s+'
    r'\{(?P<proto>\w+)\}\s+'
    r'(?P<src_ip>\d+\.\d+\.\d+\.\d+):?(?P<src_port>\d+)?\s+->\s+'
    r'(?P<dst_ip>\d+\.\d+\.\d+\.\d+):?(?P<dst_port>\d+)?'
)


def map_mitre(message: str) -> str:
    msg = str(message).lower()
    if "xmas" in msg or "fin scan" in msg or "syn scan" in msg or "nmap" in msg:
        return "T1046 - Network Service Discovery"
    if "ftp password" in msg or "brute force" in msg or "ftp" in msg:
        return "T1110 - Brute Force"
    if "telnet" in msg:
        return "T1021 - Remote Services"
    if "ssh" in msg:
        return "T1021.004 - Remote Services: SSH"
    if "flood" in msg or "dos" in msg:
        return "T1498 - Network Denial of Service"
    if "http" in msg:
        return "Context-dependent HTTP telemetry"
    if "icmp" in msg or "ping" in msg:
        return "Reconnaissance / Connectivity Check"
    return "Unmapped"


def severity(message: str) -> str:
    msg = str(message).lower()
    if "ftp" in msg or "brute force" in msg or "telnet" in msg:
        return "High"
    if "xmas" in msg or "fin scan" in msg or "syn scan" in msg or "flood" in msg:
        return "Medium"
    return "Low"


def load_alerts(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()

    records = []
    for line in path.read_text(errors="ignore").splitlines():
        match = ALERT_PATTERN.search(line)
        if match:
            records.append(match.groupdict())

    df = pd.DataFrame(records)
    if not df.empty:
        df["priority"] = pd.to_numeric(df["priority"], errors="coerce")
        df["dst_port"] = pd.to_numeric(df["dst_port"], errors="coerce")
        df["mitre"] = df["msg"].apply(map_mitre)
        df["severity"] = df["msg"].apply(severity)
    return df


st.title("Snort IDS SOC Dashboard")
st.caption("Network Detection Lab: Reconnaissance, Brute Force, Insecure Protocols, SSH, HTTP, and SYN Traffic")

df = load_alerts(LOG_FILE)

if df.empty:
    st.warning("No alerts loaded. Copy /var/log/snort/snort.alert.fast to this folder as snort.alert.fast.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Alerts", len(df))
col2.metric("Unique Source IPs", df["src_ip"].nunique())
col3.metric("Unique Destination IPs", df["dst_ip"].nunique())
col4.metric("Mapped Techniques", df["mitre"].nunique())

st.subheader("Recent Alert Feed")
st.dataframe(
    df[["timestamp", "proto", "src_ip", "src_port", "dst_ip", "dst_port", "msg", "classification", "priority", "severity", "mitre"]],
    use_container_width=True
)

st.subheader("Top Alert Types")
st.bar_chart(df["msg"].value_counts())

st.subheader("Top Destination Ports")
st.bar_chart(df["dst_port"].value_counts())

st.subheader("MITRE ATT&CK Mapping")
st.dataframe(df[["msg", "mitre", "severity"]].drop_duplicates(), use_container_width=True)

st.subheader("Analyst Notes")
st.markdown("""
### Investigation Summary

This dashboard displays Snort alerts generated in a controlled VirtualBox SOC lab.

Observed activity includes:

- ICMP connectivity testing
- Nmap SYN / FIN / Xmas scan behavior
- FTP brute-force simulation
- Telnet-port/insecure protocol access
- SSH connection attempts
- HTTP connection attempts
- Limited SYN-based traffic with hping3

### Recommended Response

1. Confirm whether the source IP is authorized.
2. Review destination services and exposed ports.
3. Correlate IDS alerts with target authentication and service logs.
4. Disable insecure services such as Telnet.
5. Harden remote access and file transfer services.
6. Tune Snort rules to reduce false positives.
""")
