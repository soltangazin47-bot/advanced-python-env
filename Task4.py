n, m = map(int, input().split())
s = input().strip()

u = set()
for i in range(n - m + 1):
    u.add(s[i:i+m])

print(len(u))
