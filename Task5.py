import re

p = r'^[ABCEHKMOPTXY]\d{3}[ABCEHKMOPTXY]{2}$'
n = int(input())

for _ in range(n):
    s = input().strip()
    print("Yes" if re.fullmatch(p, s) else "No")
