# Linux Log Monitoring & Intrusion Detection Tool

## Overview

A Python-based security monitoring tool that analyzes Linux authentication logs and detects suspicious activities. The project demonstrates basic Security Operations Center (SOC) concepts such as log analysis, event monitoring, brute-force detection, and incident reporting.

## Features

* Failed login detection
* Brute-force attack detection
* Successful login monitoring
* Sudo activity monitoring
* New user creation detection
* Automated incident report generation
* GitHub Actions automation support

## Technologies Used

* Python
* Linux Authentication Logs
* Log Analysis
* Security Monitoring
* GitHub Actions

## Project Structure

```text
linux-log-monitor/
│
├── monitor.py
├── auth.log
├── README.md
└── .github/
    └── workflows/
        └── run.yml
```

## How It Works

1. Reads authentication logs from `auth.log`
2. Parses each log entry
3. Detects suspicious activities:

   * Multiple failed login attempts
   * Potential brute-force attacks
   * Sudo command execution
   * New user account creation
4. Generates security alerts
5. Creates an incident report

## Sample Log Entries

```text
Jun 22 Failed password for root from 192.168.1.50
Jun 22 Failed password for root from 192.168.1.50
Jun 22 Failed password for root from 192.168.1.50
Jun 22 Failed password for root from 192.168.1.50

Jun 22 Accepted password for user from 192.168.1.10

Jun 22 sudo: user executed apt update

Jun 22 useradd: new user hacker created
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/linux-log-monitor.git
cd linux-log-monitor
```

Run the tool:

```bash
python monitor.py
```

## Sample Output

```text
=== SECURITY ALERTS ===

SUDO ACTIVITY DETECTED -> Jun 22 sudo: user executed apt update

NEW USER CREATED -> Jun 22 useradd: new user hacker created

BRUTE FORCE SUSPECTED FROM 192.168.1.50 (4 failures)
```

## Learning Outcomes

This project helped develop understanding of:

* Linux log analysis
* Authentication monitoring
* Security event detection
* Incident reporting
* Python automation
* Basic SOC workflows
* Cybersecurity monitoring concepts

## Future Improvements

* Real-time log monitoring
* Email alerting
* Dashboard for visualization
* IP reputation checking
* SIEM integration
* Threat intelligence feeds

