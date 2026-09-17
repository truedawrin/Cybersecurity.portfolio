# 📚 Linux Users, sudo, and Processes

## 📌 Definition

Linux separates a normal user account from the unrestricted `root` superuser, using `sudo` to grant temporary elevated privilege for a single command rather than running everything as root.

## 🧠 Core Concept

The principle of least privilege: give an account only the access it needs for the task at hand — running as root permanently removes the safety net that limits both your own mistakes and any malicious code's reach.

## ⚙️ How It Works

```bash
whoami          # current user
sudo <command>  # run one command as root
su root         # switch to root entirely
ps aux          # list all running processes
top             # live process/resource view
kill <PID>      # terminate by Process ID
```

Every running program is a process with a unique PID; `/proc/<PID>/` contains real information about that specific process.

## 🔐 Cybersecurity Relevance

Running as root removes error boundaries (a bad command can damage the whole system), lets any script/malware you run inherit full system access, and reduces the audit trail `sudo` provides. This directly connects to privilege escalation in Level 11 — the goal of many exploits is gaining exactly the elevated access `sudo` deliberately gates.

## 💻 Example

```bash
ps aux | head -10
# PID 1 is systemd, running as root — the very first process Linux starts
```

## 🧪 Practical Example

Confirmed `whoami` returns a normal user account, then reasoned through why nearly every core system process in `ps aux` runs as root while personal applications don't need to.

## ⚠️ Common Mistakes

- Treating `sudo` as a formality rather than a genuine security boundary
- Not recognizing that a compromised script run under a normal user is contained, while the same script run as root is not

## 🔗 Related Concepts

- [[Linux Filesystem and Permissions]]
- [[Linux Services Logs and Cron]]

## 🧠 Key Takeaways

- Least privilege is a recurring theme across nearly every later level, not a Linux-specific idea
- `sudo` logging creates an accountability trail that a permanent root session does not
