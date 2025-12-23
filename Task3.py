s = input().strip()
l, r = s.split('=')
v = int(r)

if 'x' in l:
    if l[0] == 'x':
        x = v - int(l[2])
    else:
        x = v - int(l[0])
else:
    if l[1] == '+':
        x = int(l[0]) + int(l[2])
    else:
        x = int(l[0]) - int(l[2])

print(x)
