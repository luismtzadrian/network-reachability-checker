import sys
import csv
import ipaddress
import platform
import subprocess
from datetime import datetime

if len(sys.argv) > 1:
    INPUT_FILE = sys.argv[1]
else:
    INPUT_FILE = "devices.csv"

OUTPUT_FILE = "results.csv"

def ping_device(ip_address):
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "2", ip_address]
    else:
        command = ["ping", "-c", "2", ip_address]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def main():
    results = []

    with open(INPUT_FILE, mode="r") as file:
        reader = csv.DictReader(file)

        for device in reader:
            hostname = device["hostname"]
            ip = device["ip"]

            try:
                ipaddress.ip_address(ip)
            except ValueError:
                print(f"Invalid IP address for {hostname}: {ip}")
                continue

            reachable = ping_device(ip)

            results.append({
                "hostname": hostname,
                "ip": ip,
                "reachable": reachable,
                "checked_at": datetime.now().isoformat(timespec="seconds")
            })

            print(f"{hostname} ({ip}) reachable: {reachable}")

    with open(OUTPUT_FILE, mode="w", newline="") as file:
        fieldnames = ["hostname", "ip", "reachable", "checked_at"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    main()