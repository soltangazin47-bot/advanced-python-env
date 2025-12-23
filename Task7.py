a = input().split()
d = {}

for x in a:
    d[x] = d.get(x, 0) + 1

print("Purchase frequency:")
for x in d:
    print(f"{x}: {d[x]}")

m = max(d, key=d.get)
print("Most popular item:", m)

o = [x for x in d if d[x] == 1]
print("Purchased once:", " ".join(o))

print("Sorted by frequency:")
for x, y in sorted(d.items(), key=lambda t: -t[1]):
    print(x, y)
