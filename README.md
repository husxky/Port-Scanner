# Port-Scanner
A lightweight TCP port scanner built from scratch in Python to understand how tools like Nmap work under the hood. Given a target IP/hostname and a port range, it checks which ports are open and attempts to grab service banners for identification.
## Features

- Scans a specified range of TCP ports on a target host
- Resolves hostnames to IP addresses automatically
- Detects open ports using raw socket connections
- Attempts banner grabbing to identify running services
- Clean, readable console output with scan timing

## How It Works

The scanner uses Python's built-in `socket` library to attempt a TCP connection to each port in the given range. A successful connection (`connect_ex` returning `0`) means the port is open. For open ports, it tries to read any data the service sends back (a "banner"), which can reveal what software is running.

## Usage

```bash
python port_scanner.py
```

You'll be prompted for:
- **Target**: an IP address or hostname (e.g. `127.0.0.1` for your own machine)
- **Port range**: start and end port (e.g. `1` to `1024`)

## Example Output
Starting scan on target: 127.0.0.1
Time started: 2026-09-19 14:32:01
Port 22 OPEN -> Banner: SSH-2.0-OpenSSH_8.9
Port 80 OPEN

Scan finished: 2026-09-19 14:32:05
Total open ports found: 2
Open ports: [22, 80]


## ⚠️ Disclaimer

This tool is for **educational purposes only**. Only scan hosts you own or have explicit written permission to test. Unauthorized port scanning of systems you don't control may violate computer misuse laws (e.g., the Computer Fraud and Abuse Act in the US).

## Built With

- Python 3
- `socket` (standard library)

## Possible Future Improvements

- Multithreading for faster scans
- Export results to CSV/JSON
- Service/version fingerprinting
- Command-line arguments instead of interactive prompts
