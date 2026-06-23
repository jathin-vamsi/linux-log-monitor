from collections import defaultdict
from datetime import datetime

LOG_FILE = "auth.log"
REPORT_FILE = "incidents.txt"

def load_logs():
    with open(LOG_FILE, "r") as f:
        return f.readlines()

def detect_events(logs):

    alerts = []
    failed_logins = defaultdict(int)

    for line in logs:

        if "Failed password" in line:
            ip = line.split()[-1]
            failed_logins[ip] += 1

        if "sudo:" in line:
            alerts.append(
                f"SUDO ACTIVITY DETECTED -> {line.strip()}"
            )

        if "useradd:" in line:
            alerts.append(
                f"NEW USER CREATED -> {line.strip()}"
            )

    for ip, count in failed_logins.items():

        if count >= 3:
            alerts.append(
                f"BRUTE FORCE SUSPECTED FROM {ip} ({count} failures)"
            )

    return alerts

def generate_report(alerts):

    with open(REPORT_FILE, "w") as f:

        f.write("=== INCIDENT REPORT ===\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        if not alerts:
            f.write("No suspicious activity detected.\n")
            return

        for alert in alerts:
            f.write(alert + "\n")

def main():

    logs = load_logs()

    alerts = detect_events(logs)

    generate_report(alerts)

    print("\n=== SECURITY ALERTS ===\n")

    if not alerts:
        print("No suspicious activity detected.")

    for alert in alerts:
        print(alert)

if __name__ == "__main__":
    main()
