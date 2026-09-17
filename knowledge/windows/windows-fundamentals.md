# 📚 Windows Fundamentals (vs. Linux)

## 📌 Definition

Windows' architecture, process/service management, Registry, PowerShell, and Event Logs — understood through direct comparison to their Linux equivalents.

## 🧠 Core Concept

Where Linux scatters configuration across text files in `/etc`, Windows centralizes nearly all configuration into a single hierarchical database: the Registry — making it a prime target for both persistence (attackers) and forensic evidence (defenders).

## ⚙️ How It Works

| Linux        | Windows               |
| ------------ | --------------------- |
| `ps aux`     | `Get-Process`         |
| `/etc`       | Registry              |
| `.so`        | `.dll`                |
| `journalctl` | Event Viewer          |
| `systemctl`  | `services.msc` / `sc` |

```powershell
Get-Process | Where-Object {$_.CPU -gt 50} | Sort-Object CPU -Descending
```

PowerShell passes structured **objects** through its pipeline (`|`), not plain text like Bash — enabling direct property filtering without text-parsing.

**Persistence location:** `HKLM/HKCU\...\Run` keys auto-launch programs at startup — a very common real malware persistence mechanism.

## 🔐 Cybersecurity Relevance

PowerShell's power (object pipelines, in-memory execution with no file written to disk) makes it a favorite tool for **fileless malware**, since traditional antivirus scanning files on disk often can't catch code that never touches disk. DLL hijacking exploits the same trust-based loading concept as Linux's `$PATH` manipulation.

## 💻 Example

```powershell
Get-NetIPAddress    # Windows equivalent of `ip addr show`
```

## 🧪 Practical Example

Compared Task Manager to `ps aux`, viewed (without modifying) `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` on a real Windows machine, and ran basic `Get-Process`/`Get-Service` cmdlets in PowerShell.

## ⚠️ Common Mistakes

- Assuming Windows and Linux security concepts don't transfer — most map directly (persistence, least privilege, logging)
- Underestimating PowerShell as "just a shell" rather than a fully capable, security-relevant scripting environment

## 🔗 Related Concepts

- [[Linux Services Logs and Cron]]
- [[Linux Users Sudo and Processes]]

## 🧠 Key Takeaways

- The Registry's Run keys and cron jobs solve the same problem (persistence) on different OSes
- NTFS ACLs are more granular than Linux's rwx model, but also more complex to audit correctly
