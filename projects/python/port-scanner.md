# 🛠️ Python Port Scanner

<div align="center">

![Language](https://img.shields.io/badge/Language-Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Category](https://img.shields.io/badge/Category-Network_Tooling-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

</div>

## 📊 Metadata
| Field | Value |
| :--- | :--- |
| **Type** | Project (Reusable Tool) |
| **Language** | Python 3 |
| **Concepts Used** | Sockets, TCP handshake, `connect_ex`, timeouts, error handling, loops |


## 📌 Overview
A lightweight TCP port scanner written in Python. The script prompts the user for a target IP address, iterates over a predefined list of common ports, and attempts a TCP connection to each one using Python's built-in `socket` module. It reports whether each port is **open** (accepting connections) or **closed** (refusing them), with a one-second timeout to keep the scan fast.

This is a **reusable tool** — the first real security utility built from scratch. It demonstrates how a scanner works under the hood, before relying on mature tools like Nmap later in the curriculum.

## 🎯 Objectives
- Understand how a TCP connection is established at the code level.
- Learn how Python's `socket` module maps to real network behavior.
- Build a functional, reusable tool that performs genuine network reconnaissance against authorized targets.
- Practice safe error handling so a single failed connection does not crash the entire scan.

## 🧠 Concepts Applied
- **Sockets:** The programming interface to the operating system's networking stack.
- **TCP Three-Way Handshake:** The scanner uses TCP because it is connection-oriented — an "open" port means the handshake was accepted.
- **`connect_ex` vs `connect`:** `connect_ex` returns an error code instead of raising an exception, making it ideal for scanning many ports in a loop.
- **Timeouts:** Without a timeout, the scanner would hang indefinitely on filtered ports. `settimeout(1)` bounds each attempt to one second.
- **Error Handling:** `try`/`except` ensures a single unresponsive port does not crash the scan.

## 💻 Implementation

### Source Code
```python
import socket

target = ""

while target == "":
    target = input("Enter target IP: ")

ports = [22, 80, 443, 3389, 8080]

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    except socket.error:
        print(f"Error scanning port {port}")
