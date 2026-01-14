import json

with open("students.json", "r", encoding="utf-8") as f:
    s = json.load(f)

u = []

for i in s:
    a = sum(i["grades"]) / len(i["grades"])
    c = i.copy()
    c["average"] = a
    u.append(c)

with open("students_updated.json", "w", encoding="utf-8") as g:
    json.dump(u, g, indent=4)
