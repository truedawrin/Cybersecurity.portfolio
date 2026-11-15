import socket
import errno

PORTS = [22, 80, 443, 3389, 8080]
TIMEOUT = 1

target = ""
while target == "":
    target = input("Enter target IP: ").strip()

print(f"Scanning {target}...\n")

for port in PORTS:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((target, port))
    except socket.error:
        print(f"Port {port}: error")
        continue

    if result == 0:
        print(f"Port {port} is open")
    elif result == errno.ECONNREFUSED:
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is filtered or unreachable")
