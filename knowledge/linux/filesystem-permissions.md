# 📚 Linux Filesystem and Permissions

## 📌 Definition

Linux organizes everything under a single root (`/`), with no separate drive letters, and controls access via a three-tier owner/group/other permission model.

## 🧠 Core Concept

"Everything is a file" in Linux — even hardware and running processes are represented as files you can read (`/dev`, `/proc`), and every file carries explicit read/write/execute permissions for three distinct audiences.

## ⚙️ How It Works

```
/          — root of everything
/home      — user directories
/etc       — system configuration
/bin       — essential command binaries
/var       — variable data, logs
/tmp       — temporary files, cleared on reboot
/dev       — device files (hardware as files)
/proc      — running process/kernel info, exposed as files
```

```bash
ls -l
-rwxr-xr-- 1 true-dawrin users 220 Aug 26 10:00 script.sh
```

First character: file/directory type. Next 3: owner permissions. Next 3: group. Next 3: everyone else. Numeric form: `r=4, w=2, x=1`, summed per group (`chmod 755`).

## 🔐 Cybersecurity Relevance

Privilege escalation is, at its core, exploiting misconfigured permissions — a file writable when it shouldn't be, or a program running with more privilege than it needs. Malware often manipulates `/proc` entries to hide processes; forensics investigators read `/proc` to catch exactly that.

## 💻 Example

```bash
chmod 755 script.sh
# owner: read+write+execute, group/others: read+execute
```

## 🧪 Practical Example

Ran `ls -l` on real files/directories, correctly identified owner/group/other permissions, and explained why a directory needs execute permission (to `cd` into it) separately from read permission (to list its contents).

## ⚠️ Common Mistakes

- Confusing read permission on a directory (can list contents) with execute permission (can enter/traverse it)
- Assuming a file's permissions alone determine access, ignoring the parent directory's permissions

## 🔗 Related Concepts

- [[Linux Users Sudo and Processes]]
- [[Linux Services Logs and Cron]]

## 🧠 Key Takeaways

- The permission triad (owner/group/other) plus rwx bits fully describes access for any file
- "Everything is a file" is a genuinely practical design principle, not just trivia — it's why `/proc` and `/dev` matter for security work
