# Network Reachability Checker

## Overview
Simple Python-based network automation tool that validates reachability of devices from a CSV inventory.

## What it does
- Reads device list from CSV
- Executes ping checks
- Determines reachability (True/False)
- Outputs results to a CSV file with timestamps

## Why this matters
This demonstrates basic network automation patterns:
- Input → Process → Output
- Infrastructure validation
- Scripted troubleshooting

## Technologies used
- Python
- subprocess (OS command execution)
- CSV parsing

## How to run

1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Run script:
   python3 reachability_check.py

## Example output

google_dns (8.8.8.8) reachable: True  
cloudflare_dns (1.1.1.1) reachable: True  
pixel_tether_gateway (192.168.226.241) reachable: True  

## Future improvements
- Add TCP port checks (HTTP, SSH)
- Add parallel execution
- Add logging instead of print
- Integrate with network APIs

