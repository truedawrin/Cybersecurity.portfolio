def classify(score):
    if score < 0:
        return "INVALID (negative score)"
    if score > 100:
        return "INVALID (exceeds maximum)"
    if score >= 90:
        return "Grade A"
    elif score >= 80:
        return "Grade B"
    elif score >= 70:
        return "Grade C"
    elif score >= 60:
        return "Grade D"
    else:
        return "Grade F"

report_lines = []

try:
    with open("scores.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("scores.txt not found.")
    exit()

for line in lines:
    line = line.strip()
    if not line:
        continue
    try:
        score = int(line)
        result = classify(score)
        report_lines.append(f"{score} -> {result}")
    except ValueError:
        report_lines.append(f"{line} -> INVALID (not a number)")

with open("grade_report.txt", "w") as report:
    for entry in report_lines:
        report.write(entry + "\n")

print("Audit complete. See grade_report.txt")