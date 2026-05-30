#!/usr/bin/env python3

"""
Linux Health Check Script
Author: Akash

Checks:
1. Hostname
2. OS Information
3. Uptime
4. CPU Usage
5. Memory Usage
6. Disk Usage
7. Top 5 Memory Consuming Processes
"""

import platform
import shutil
import socket
import subprocess
import os


def get_hostname():
    return socket.gethostname()


def get_os_info():
    return platform.platform()


def get_uptime():
    try:
        with open("/proc/uptime", "r") as file:
            uptime_seconds = float(file.readline().split()[0])

        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)

        return f"{days} Days {hours} Hours {minutes} Minutes"

    except Exception as error:
        return f"Unable to fetch uptime: {error}"


def get_cpu_load():
    try:
        load1, load5, load15 = os.getloadavg()
        return f"""
1 Minute Load : {load1}
5 Minute Load : {load5}
15 Minute Load: {load15}
"""
    except Exception as error:
        return f"Unable to fetch CPU load: {error}"


def get_memory_usage():
    try:
        output = subprocess.check_output(
            ["free", "-h"],
            text=True
        )
        return output

    except Exception as error:
        return f"Unable to fetch memory details: {error}"


def get_disk_usage():
    try:
        total, used, free = shutil.disk_usage("/")

        return f"""
Total Disk : {total // (1024 ** 3)} GB
Used Disk  : {used // (1024 ** 3)} GB
Free Disk  : {free // (1024 ** 3)} GB
"""

    except Exception as error:
        return f"Unable to fetch disk usage: {error}"


def get_top_processes():
    try:
        output = subprocess.check_output(
            ["ps", "-eo", "pid,comm,%mem", "--sort=-%mem"],
            text=True
        )

        return "\n".join(output.splitlines()[:6])

    except Exception as error:
        return f"Unable to fetch process details: {error}"


def main():
    print("=" * 60)
    print("LINUX HEALTH CHECK REPORT")
    print("=" * 60)

    print(f"\nHostname : {get_hostname()}")
    print(f"OS       : {get_os_info()}")

    print("\n" + "=" * 60)
    print("UPTIME")
    print("=" * 60)
    print(get_uptime())

    print("\n" + "=" * 60)
    print("CPU LOAD")
    print("=" * 60)
    print(get_cpu_load())

    print("\n" + "=" * 60)
    print("MEMORY USAGE")
    print("=" * 60)
    print(get_memory_usage())

    print("\n" + "=" * 60)
    print("DISK USAGE")
    print("=" * 60)
    print(get_disk_usage())

    print("\n" + "=" * 60)
    print("TOP 5 MEMORY CONSUMING PROCESSES")
    print("=" * 60)
    print(get_top_processes())


if __name__ == "__main__":
    main()
