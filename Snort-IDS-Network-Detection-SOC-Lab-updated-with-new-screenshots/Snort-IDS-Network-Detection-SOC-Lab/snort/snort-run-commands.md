# Snort Run Commands

## Validate Rules

```bash
sudo snort -c /usr/local/etc/snort/snort.lua -R /usr/local/etc/rules/local.rules -T
```

## Run Snort Live

The attacker-side interface in this lab was `enp0s8`.

```bash
sudo mkdir -p /var/log/snort

sudo snort -c /usr/local/etc/snort/snort.lua \
  -R /usr/local/etc/rules/local.rules \
  -i enp0s8 \
  -A alert_fast \
  -l /var/log/snort
```

## Alert File Location

This Snort install wrote fast alerts to:

```text
/var/log/snort/snort.alert.fast
```

View alerts:

```bash
sudo tail -f /var/log/snort/snort.alert.fast
```

View recent alerts:

```bash
sudo tail -30 /var/log/snort/snort.alert.fast
```

## Important Troubleshooting Note

The walkthrough originally expected `alert_fast.txt`, but this install generated:

```text
snort.alert.fast
```

The lab was successful because Snort generated and updated `snort.alert.fast`.
