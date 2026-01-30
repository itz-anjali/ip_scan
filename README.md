# IP Scanner (Python + Nmap)

This project is a simple Python-based IP scanning tool that uses **Nmap**
to perform an aggressive network scan on a given IP address.

The script includes proper IP address validation to prevent invalid input
and generates a scan report automatically.

---

## 🚀 Features

- IP address validation using Python's `ipaddress` module
- Aggressive Nmap scan (`-A`)
- Fast scan timing (`-T4`)
- Scan results saved to a text file
- Simple and beginner-friendly code
- Lightweight and easy to modify

---

## 🛠 Requirements

- Linux OS
- Python 3
- Nmap
- Root privileges (recommended)

Install Nmap:
```bash
sudo apt install nmap
