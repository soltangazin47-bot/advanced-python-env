a = input().strip()
b = input().strip()

n = len(b)
c = b + b
r = set(c[i:i+n] for i in range(n))

x = 0
for i in range(len(a) - n + 1):
    if a[i:i+n] in r:
        x += 1

print(x)
