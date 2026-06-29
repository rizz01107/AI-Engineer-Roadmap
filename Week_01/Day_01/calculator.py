print("=" * 40)
print("      SIMPLE CALCULATOR")
print("=" * 40)

# User Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operator:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("%  Modulus")
print("** Exponent")
print("// Floor Division")

operator = input("\nEnter operator: ")

print("\n" + "=" * 40)

# Calculator Logic
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif operator == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")

elif operator == "%":
    if num2 != 0:
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Error: Division by zero is not allowed.")

elif operator == "**":
    print(f"{num1} ** {num2} = {num1 ** num2}")

elif operator == "//":
    if num2 != 0:
        print(f"{num1} // {num2} = {num1 // num2}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator!")

print("=" * 40)
print("Thank you for using the calculator!")
print("=" * 40)