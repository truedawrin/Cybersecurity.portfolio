# 📚 Linux Services, Logs, SSH, and Cron

## 📌 Definition

`systemd` manages background services; `journalctl`/`/var/log` record system activity; SSH provides secure remote access; `cron` schedules recurring tasks.

## 🧠 Core Concept

Every running service is a potential attack surface, every log is a forensic record, and cron is a mechanism for **persistence** — code that survives reboots or being killed once.

## ⚙️ How It Works

```bash
systemctl list-units --type=service --state=running
journalctl -u <service-name>
ssh username@ip
ssh-keygen -t ed25519
crontab -e
echo $PATH
```

`$PATH` is the ordered list of directories the shell searches for commands — PATH manipulation is a real attack vector where malicious code is placed earlier in that search order.

## 🔐 Cybersecurity Relevance

An unfamiliar running service is a classic sign of misconfiguration or compromise. Cron entries are a common malware persistence mechanism — even if killed once, scheduled code re-runs automatically. Key-based SSH auth resists brute-forcing in a way password auth cannot, since the private key never travels over the network.

## 💻 Example

```bash
0 2 * * * /home/true-dawrin/backup.sh
# minute hour day month weekday — runs daily at 2:00 AM
```

## 🧪 Practical Example

Listed real running services, checked `journalctl` for one, confirmed SSH server was inactive (client-only setup) versus SSH client being present, and explained why an attacker prefers a cron job over running malicious code only once.

## ⚠️ Common Mistakes

- Confusing "no entries" in `journalctl` for a service with an error, when it usually just means the service has never run/logged
- Overlooking `$PATH` order as a real, exploitable attack surface

## 🔗 Related Concepts

- [[Linux Users Sudo and Processes]]
- [[Windows Fundamentals]]

## 🧠 Key Takeaways

- Persistence (surviving reboots/kills) is the key concept connecting cron, services, and later Windows Registry Run keys
- Logs are the raw material for incident response — understanding where they live matters before ever doing forensics
