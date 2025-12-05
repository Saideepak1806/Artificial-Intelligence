print("Simple Calculator")
print("Choose an operation: +  -  *  /")

op = input("Enter operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b == 0:
        result = "Error: Division by zero"
    else:
        result = a / b
else:
    result = "Invalid operation"

print("Result:", result)
