# 🧪 Recon Notebook

- Type: Red Team/Blue Team
- Difficulty: Intermediate
- Status: Completed

## 🎬 Scenario

You're building a lightweight recon-tracking tool for personal use before engagements. Write a Python script that: stores a list of target dictionaries (`ip`, `os`, `notes`), lets you loop through and print a formatted summary of each, and writes that summary to a text file using safe `with open()` file handling. This is a real, reusable pattern — the seed of every note-taking/reporting tool.

## 🎯 Objective

Build a Python script that stores a list of target hosts, prints a formatted summary to the terminal, and saves the same summary to `recon_report.txt`.

## 🧠 Skills Practiced

- Iterating over a list of dictionaries with `enumerate()`
- f-string formatting
- Writing to terminal and file from one function
- `try/except` around file I/O

## 🏗️ Environment

- **OS:** CachyOS Linux
- **Language:** Python 3
- **Tools:** terminal, code editor
- **Dataset/Target:** 3 hard-coded fictional hosts

## 💻 Implementation

```python
hosts = [
    {"ip": "192.168.1.10", "os": "Linux", "notes": "Web server"},
    {"ip": "192.168.1.20", "os": "Windows", "notes": "Domain controller"},
    {"ip": "192.168.1.30", "os": "Mac OS", "notes": "workspace"},
]

try:
    with open("recon_report.txt", "w") as file:
        def log(text):
            print(text)
            print(text, file=file)

        for i, host in enumerate(hosts, start=1):
            log(f"Host {i}")
            log(f"IP: {host['ip']}")
            log(f"OS: {host['os']}")
            log(f"Notes: {host['notes']}")
            log("---")

except PermissionError:
    print("Could not write to recon_report.txt — permission denied.")
```

The `log()` function is defined inside the `with` block and writes to both the terminal and the open file in one call, keeping the two outputs guaranteed identical.

## 📊 Results

```text
Host 1
IP: 192.168.1.10
OS: Linux
Notes: Web server
---
Host 2
IP: 192.168.1.20
OS: Windows
Notes: Domain controller
---
Host 3
IP: 192.168.1.30
OS: Mac OS
Notes: workspace
---
```

Terminal output and `recon_report.txt` matched exactly.

## Evidence
<img width="646" height="332" alt="image" src="https://github.com/user-attachments/assets/b5f8368c-b6dd-4245-b90f-4827ac0692b6" />
<img width="646" height="332" alt="image" src="https://github.com/user-attachments/assets/ffc5699d-3b7a-4103-90b9-68bfbf021c12" />



## 🧠 What I Learned

- Separating presentation from persistence, while driving both from one function, avoids duplicated logic
- `try/except` around file writes prevents silent data loss on a permissions failure

## 🔮 Future Improvements

- Replace hard-coded hosts with real scan results once sockets/port scanning is covered
