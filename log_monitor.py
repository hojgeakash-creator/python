#!/usr/bin/env python3

"""
Log Monitoring Script

Features:
1. Monitors a log file in real-time
2. Detects ERROR, WARNING, CRITICAL, FAILED messages
3. Prints alerts to the terminal
4. Keeps monitoring until stopped (Ctrl+C)

Author: Akash
"""

import os
import time
from datetime import datetime

LOG_FILE = "/var/log/syslog"  # Change as needed

KEYWORDS = [
    "ERROR",
    "CRITICAL",
    "FAILED",
    "WARNING"
]


def monitor_log(log_file):
    """Monitor log file continuously."""

    if not os.path.exists(log_file):
        print(f"Log file does not exist: {log_file}")
        return

    print("=" * 60)
    print(f"Monitoring: {log_file}")
    print(f"Started at: {datetime.now()}")
    print("=" * 60)

    with open(log_file, "r") as file:
        # Move to end of file
        file.seek(0, 2)

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            for keyword in KEYWORDS:
                if keyword in line.upper():
                    print(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                        f"ALERT [{keyword}] -> {line.strip()}"
                    )


def main():
    try:
        monitor_log(LOG_FILE)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
