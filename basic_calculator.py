operator = input("Enter an operator (+, -, *, or  /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print("---------------------------------")
    print(f"{num1} {operator} {num2} = {result}")
    print()
elif operator == "-":
    result = num1 - num2
    print("---------------------------------")
    print(f"{num1} {operator} {num2} = {result}")
    print()
elif operator == "*":
    result = num1 * num2
    print("---------------------------------")
    print(f"{num1} {operator} {num2} = {result}")
    print()
elif operator == "/":
    result = num1 / num2
    print("---------------------------------")
    print(f"{num1} {operator} {num2} = {result}")
    print()
else:
    print("The operator is invalid! Please enter the correct operator.")
