# 📚 OSI Model & TCP/IP Model

## 📌 Definition
Two layered conceptual frameworks describing how data moves from one machine to another — OSI has 7 layers, TCP/IP condenses this into 4 practical layers.

## 🧠 Core Concept
Each layer only needs to know how to talk to the layer directly above and below it — the same abstraction principle as a function not needing to know how `printf` is implemented internally.

## ⚙️ How It Works

``` text
OSI (7 layers) TCP/IP (4 layers)

7. Application ─┐
6. Presentation ├── 4. Application (HTTP, DNS, SSH)
5. Session     ─┘
4. Transport ────── 3. Transport (TCP, UDP)
3. Network ────── 2. Internet (IP)
2.  Data Link ─┐
1.  Physical   ├── 1. Link (Ethernet, WiFi)
```
Each layer hands data to the layer below it and trusts that layer to do its job, without needing to understand its internals.

## 🔐 Cybersecurity Relevance
Every tool and attack maps to a specific layer: Wireshark displays packets organized by these exact layers; firewalls operate primarily at layers 3-4; web attacks (XSS, SQLi) operate at layer 7; ARP spoofing exploits layer 2. Knowing which layer something operates at tells you immediately what it can and can't do.

## 💻 Example
```text
A Python port scanner using socket.SOCK_STREAM operates at:
- Transport layer (TCP, via SOCK_STREAM)
- Network layer (IP, via the target address)
```

## 🧪 Practical Example
Annotated a [Python port scanner](/projects/python/01.port-scanner.md) line by line, identifying which OSI/TCP-IP layer each part (socket creation, IP address, port, connection attempt) operates at.

## ⚠️ Common Mistakes
- Assuming a tool "sees the whole stack" instead of recognizing it typically operates at one or two specific layers
- Confusing OSI's 7-layer model with TCP/IP's 4-layer model in conversation, without realizing they describe the same reality at different granularity

## 🔗 Related Concepts
- [[TCP UDP and Ports]]
- [[Wireshark]]
- [[ARP and MITM]]

## 🧠 Key Takeaways
- Layering exists so each part of the stack can be understood and built independently
- Real tools (Wireshark, firewalls) are best understood by first asking "which layer does this operate at?"
