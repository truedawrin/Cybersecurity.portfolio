# 📚 TCP, UDP, and Ports

## 📌 Definition
TCP and UDP are the two core Transport-layer protocols; ports are numeric identifiers that let one IP address host many simultaneous services.

## 🧠 Core Concept
TCP trades speed for guaranteed, ordered, verified delivery via a handshake. UDP trades guarantees for speed by sending data with no handshake or confirmation. A port is like an apartment number on top of an IP's street address.

## ⚙️ How It Works
**TCP three-way handshake:**
```text
Client -- SYN -----------> Server
Client <- SYN-ACK -------- Server
Client -- ACK -----------> Server
```
Sequence numbers let TCP detect missing/out-of-order data and request retransmission.

**UDP:** no handshake — data is just sent, with no confirmation of arrival or order.

**Port ranges:**

0–1023 well-known (often require root to bind)
1024–49151 registered
49152–65535 ephemeral/dynamic


## 🔐 Cybersecurity Relevance
`connect_ex()` returning `0` confirms a full handshake completed — this is exactly what Nmap's connect scan (`-sT`) does. Nmap's SYN scan (`-sS`) deliberately never completes the handshake, making it faster and stealthier, but requires root. UDP scanning is inherently ambiguous ("open or filtered") since there's no handshake to confirm state. Port 445 (SMB) open is a historically high-value finding (EternalBlue/WannaCry).

## 💻 Example
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
result = sock.connect_ex(("127.0.0.1", 80))
# result == 0 means full TCP handshake succeeded
```

## 🧪 Practical Example
Classified port scanner results against `127.0.0.1` as open/closed, referencing what `connect_ex` returning `0` actually confirms about the underlying handshake.

## ⚠️ Common Mistakes
- Treating "no response" the same as "closed" in UDP scanning — it can also mean filtered
- Not realizing a full-connect scan leaves a more complete trace in target logs than a SYN scan

## 🔗 Related Concepts
- [[OSI TCP-IP Model]]
- [[Wireshark]]

## 🧠 Key Takeaways
- TCP = reliability via handshake and sequencing; UDP = speed with no guarantees
- Port state (open/closed/filtered) is determined by whether and how a target responds to a probe
