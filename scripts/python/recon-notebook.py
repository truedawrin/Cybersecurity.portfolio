#You're building a lightweight recon-tracking tool for personal use before engagements. 
# Write a Python script that: stores a list of target dictionaries (`ip`, `os`, `notes`), 
# lets you loop through and print a formatted summary of each,
#  and writes that summary to a text file using safe `with open()` file handling. 
# This is a real, reusable pattern — the seed of every note-taking/reporting tool

hosts = [
    {"ip": "192.168.1.10", "os": "Linux", "notes": "Web server"},
    {"ip": "192.168.1.20", "os": "Windows", "notes": "Domain controller"},
    {"ip": "192.168.1.30", "os": "Mac OS", "notes": "workspace"}
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
    print("Could not write to recon_report.txt")