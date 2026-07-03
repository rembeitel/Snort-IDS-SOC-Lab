# Streamlit SOC Dashboard

This optional dashboard parses Snort `alert_fast` output and displays a simple SOC-style view of alerts.

## Expected Alert File

This lab used:

```text
/var/log/snort/snort.alert.fast
```

Copy the alert file into the dashboard folder:

```bash
sudo cp /var/log/snort/snort.alert.fast ~/snort-soc-dashboard/snort.alert.fast
sudo chown $USER:$USER ~/snort-soc-dashboard/snort.alert.fast
```

## Setup

```bash
cd ~/snort-soc-dashboard
python3 -m venv .venv
source .venv/bin/activate
pip install streamlit pandas
```

## Run

```bash
streamlit run app.py
```

If `streamlit` is not found:

```bash
python -m streamlit run app.py
```
