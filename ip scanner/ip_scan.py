# ip scan build for learning purpose

import subprocess as ss
import re
import ipaddress
print("Welcome to IP Scan")
print("---------------------------")
ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

user = input("Enter IP: ")

if not re.match(ip_pattern, user):
    print("Invalid IP address format")
    exit()

try:
    ipaddress.ip_address(user)
except ValueError:
    print("Invalid IP address")
    exit()

print("\nScanning... please wait\n")

try:

    ss.run(
        ["nmap", "-A", "-T4", user ,  "-oN", "scan.txt"],
        check=True,
        text=True
    )
    print("\nScan completed successfully")

except Exception as e:
    print("Error occurred:", e)

print("---------------------------")
print("THANK~YOU for using ")
