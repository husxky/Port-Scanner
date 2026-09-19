#!/usr/bin/env python3
"""
Simple TCP Port Scanner
------------------------
A beginner-friendly cybersecurity project that scans a target host
for open TCP ports and tries to grab service banners.

⚠️ Only scan hosts you own or have explicit permission to test.
Scanning devices you don't own/control without permission may be illegal.

Usage:
    python port_scanner.py
    (then enter target and port range when prompted)
"""

import socket
from datetime import datetime


def scan_port(target: str, port: int, timeout: float = 0.5):
    """
    Try to connect to a single port on the target.
    Returns True if the port is open, False otherwise.
    """
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # connect_ex returns 0 if the connection succeeds (port is open)
        result = sock.connect_ex((target, port))

        banner = ""
        if result == 0:
            # Try to grab a banner (some services announce themselves)
            try:
                banner = sock.recv(1024).decode(errors="ignore").strip()
            except Exception:
                banner = ""

        sock.close()
        return result == 0, banner

    except socket.error:
        return False, ""


def scan_range(target: str, start_port: int, end_port: int):
    """
    Scan a range of ports on the target and print results as it goes.
    """
    print(f"\nStarting scan on target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = []

    try:
        # Resolve hostname to IP (also validates the target early)
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Could not resolve hostname. Check the target and try again.")
        return

    for port in range(start_port, end_port + 1):
        is_open, banner = scan_port(target_ip, port)
        if is_open:
            line = f"Port {port:<6} OPEN"
            if banner:
                line += f"  -> Banner: {banner[:60]}"
            print(line)
            open_ports.append(port)

    print("-" * 50)
    print(f"Scan finished: {datetime.now()}")
    print(f"Total open ports found: {len(open_ports)}")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found in this range.")


def main():
    print("=" * 50)
    print(" Simple Python Port Scanner")
    print(" (For educational use on systems you own or have permission to test)")
    print("=" * 50)

    target = input("Enter target IP or hostname (e.g. 127.0.0.1): ").strip()

    try:
        start_port = int(input("Start port (e.g. 1): ").strip())
        end_port = int(input("End port (e.g. 1024): ").strip())
    except ValueError:
        print("Ports must be numbers. Exiting.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Ports must be between 1-65535, start <= end.")
        return

    scan_range(target, start_port, end_port)


if __name__ == "__main__":
    main()