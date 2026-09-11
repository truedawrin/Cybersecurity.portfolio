# 📚 IP Addressing & Subnetting

## 📌 Definition
IPv4 addressing assigns each device a 32-bit address; subnetting divides a network into smaller pieces using a subnet mask/CIDR notation to separate the network portion from the host portion.

## 🧠 Core Concept
A subnet mask's binary form is a count of 1-bits (network) followed by 0-bits (host) — CIDR notation (`/24`) is just that bit count written directly.

## ⚙️ How It Works

Usable hosts = 2^(host bits) - 2 (subtracting network + broadcast addresses)

Common table:
```text
/24 = 255.255.255.0 → 254 usable hosts
/25 = 255.255.255.128 → 126 usable hosts
/30 = 255.255.255.252 → 2 usable hosts (point-to-point links)
```
Shortcut for converting dotted-decimal to CIDR: `128=1 bit, 192=2, 224=3, 240=4, 248=5, 252=6, 254=7, 255=8`.

## 🔐 Cybersecurity Relevance
Reading a scope document (e.g., `192.168.1.0/24`) instantly tells you the usable host range and broadcast address — essential for defining and respecting engagement boundaries, and for understanding network diagrams during recon.

## 💻 Example
```text
192.168.1.0/24 → usable hosts 192.168.1.1–192.168.1.254, broadcast 192.168.1.255
```

## 🧪 Practical Example
Calculated the network address, broadcast address, and usable host range for `10.20.30.0/26` by hand, then verified using the binary bit-count method.

## ⚠️ Common Mistakes
- Forgetting to subtract 2 for network + broadcast addresses when counting usable hosts
- Confusing the network address (`.0`) or broadcast address (`.255`) with an assignable host address

## 🔗 Related Concepts
- [[OSI TCP-IP Model]]
- [[Routing DNS DHCP]]

## 🧠 Key Takeaways
- CIDR notation is literally a count of binary 1-bits in the subnet mask
- Smaller subnets (e.g., /30) exist deliberately for cases needing only 2 hosts, like router-to-router links
📄
