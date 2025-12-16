A = float(input())

int_part = int(A)
frac_part = A - int_part

result = frac_part * 100 + int_part / 100
print(result)
