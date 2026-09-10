# 📚 Python Fundamentals (Variables, Control Flow, Functions, Lists/Dicts, File & Error Handling)

## 📌 Definition

The core building blocks of the Python language: variables and types, conditional logic, loops, functions, lists, dictionaries, and safe file/error handling — the foundation for every script and tool built in this curriculum.

## 🧠 Core Concept

A program is a sequence of instructions that stores data (variables), makes decisions (control flow), repeats logic (loops), packages reusable behavior (functions), organizes collections of data (lists/dictionaries), and interacts with the outside world safely (files, errors).

## ⚙️ How It Works

- **Variables/types** — Python infers type automatically from the assigned value (`str`, `int`, `bool`, `float`); no declaration needed up front.
- **Control flow** — `if`/`elif`/`else` evaluate conditions top to bottom, running the first true block; indentation defines the block structurally, not stylistically.
- **Loops** — `for` repeats over a known range/collection; `while` repeats as long as a condition holds, useful when the iteration count isn't known in advance.
- **Functions** — `def` packages a reusable block; `return` sends a value back to the caller, unlike `print`, which only displays and discards it.
- **Lists/dictionaries** — lists are ordered and indexed from `0`; dictionaries are accessed by key instead of position, suited to labeled data like a host's `ip`/`os`/`notes`.
- **File/error handling** — `with open(...)` auto-closes a file even on failure; `try`/`except` catches a specific error type and lets the program continue instead of crashing.

## 🔐 Cybersecurity Relevance

Nearly every custom security tool — scanners, log parsers, brute-forcers, recon utilities — is built from exactly these primitives. `try`/`except` specifically matters because a tool scanning many targets shouldn't die on the first failure; graceful error handling is what separates a usable tool from a fragile script.

## 💻 Example

```python
hosts = [
    {"ip": "192.168.1.10", "os": "Linux", "notes": "Web server"},
    {"ip": "192.168.1.20", "os": "Windows", "notes": "Domain controller"},
]

try:
    with open("recon_report.txt", "w") as file:
        for i, host in enumerate(hosts, start=1):
            print(f"Host {i}: {host['ip']} ({host['os']})", file=file)
except PermissionError:
    print("Could not write to file — permission denied.")
```

## 🧪 Practical Example

Home Lab 3.1 [Recon Notebook](/home-labs/personal-labs/python/recon-notebook.md) — a script storing a list of target hosts as dictionaries, formatting and printing each one, and saving the same output to a report file, with `try`/`except` guarding the file write.

## ⚠️ Common Mistakes

- Forgetting the colon (`:`) after `if`/`for`/`def`/`while`
- Confusing `=` (assignment) with `==` (comparison)
- Off-by-one errors with `range()` — `range(5)` gives `0-4`, not `1-5`
- Mixing quote types inside an f-string (e.g., double quotes inside a double-quoted f-string), causing a syntax error
- Letting one bad item in a loop crash an entire batch instead of wrapping it in `try`/`except`

## 🔗 Related Concepts

- [ASCII and Binary Representation]
- [Bash Scripting]
- [Sockets and Port Scanning]

## 🧠 Key Takeaways

- Structuring data as dictionaries makes it easy to extend later without rewriting logic
- Separating presentation (`print`) from persistence (file write) — while driving both from shared logic — is a clean, reusable pattern
- Graceful error handling is a core habit, not an afterthought, for any tool meant to run against multiple targets
