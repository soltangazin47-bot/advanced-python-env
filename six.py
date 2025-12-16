a = float(input("First number: "))
op = input("Operation: ")
b = float(input("Second number: "))

if op == "/" and b == 0:
    print("Error: division by zero")
elif op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    print(f"{a} / {b} = {a / b}")
else:
    print("Unknown operation")
