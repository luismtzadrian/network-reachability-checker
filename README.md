# Network Reachability Checker

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight Python automation tool for validating network device reachability from a CSV inventory.  
Built as part of a NetOps automation learning path — replacing manual ping sweeps with a repeatable, scriptable workflow.

---

## The Problem This Solves

Network engineers routinely validate device reachability before and after changes — maintenance windows, circuit cutovers, BGP failovers, firewall rule pushes. Doing this manually via ping is slow, error-prone, and leaves no audit trail.

This tool automates that pattern:
CSV Inventory → IP Validation → Ping Check → Timestamped Results CSV

Same logic behind tools like SolarWinds NCM reachability polls and pre-change validation scripts in Ansible playbooks — just built from scratch to understand the fundamentals.

---

## What It Does

- Reads a device inventory from CSV (`hostname`, `ip`)
- Validates IP address format before attempting ping
- Executes cross-platform ping checks (macOS, Linux, Windows)
- Skips invalid IPs gracefully with console warnings
- Outputs structured results to `results.csv` with timestamps
- Accepts custom inventory file via CLI argument

---

## Technologies

| Component | Purpose |
|---|---|
| `subprocess` | Runs OS-level ping commands |
| `ipaddress` | Validates IP format before execution |
| `csv` | Reads inventory, writes results |
| `platform` | Detects OS for correct ping syntax |
| `sys.argv` | Accepts custom input file from CLI |
| `datetime` | Timestamps every result |

> No external dependencies — stdlib only. No pip install required.

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/luismtzadrian/network-reachability-checker.git
cd network-reachability-checker

# Optional: create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Run with default inventory
python3 reachability_check.py

# Run with custom inventory
python3 reachability_check.py mixed_devices.csv
```

---

## Input Format

```csv
hostname,ip
core-router-01,10.0.0.1
cloudflare_dns,1.1.1.1
bad_device,999.999.999.999
```

---

## Example Output

**Terminal:**
google_dns (8.8.8.8) reachable: True
cloudflare_dns (1.1.1.1) reachable: True
Invalid IP address for bad_device: 999.999.999.999
lab_server (10.255.255.1) reachable: False

**results.csv:**
hostname,ip,reachable,checked_at
google_dns,8.8.8.8,True,2026-04-30T18:10:39
cloudflare_dns,1.1.1.1,True,2026-04-30T18:10:41
lab_server,10.255.255.1,False,2026-04-30T18:10:46

---

## Roadmap

- [ ] TCP port checks (SSH/22, HTTP/80, HTTPS/443)
- [ ] Parallel execution with `concurrent.futures`
- [ ] Structured logging (`logging` module) instead of print
- [ ] SNMP reachability check option
- [ ] Netmiko integration for SSH-based validation
- [ ] Output to JSON for API/pipeline consumption

---

## About

Built by [Luis Adrian Martinez Vergara](https://iamadrian.tech) — Network Associate Director | CCNP | NetOps Automation  
Part of a 100-day first-principles engineering challenge.
