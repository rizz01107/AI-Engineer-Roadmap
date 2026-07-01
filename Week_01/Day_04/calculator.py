def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


while True:

    print("\n" + "=" * 35)
    print("         CALCULATOR")
    print("=" * 35)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("\nChoose (1-5): ")

    if choice == "5":
        print("Thank you!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Choice!")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Answer =", add(num1, num2))

    elif choice == "2":
        print("Answer =", subtract(num1, num2))

    elif choice == "3":
        print("Answer =", multiply(num1, num2))

    elif choice == "4":
        print("Answer =", divide(num1, num2))