print("=" * 50)
print("        DAY 2 PYTHON ASSIGNMENT")
print("=" * 50)

# -----------------------------------
# 1. Positive / Negative / Zero
# -----------------------------------
print("\n1. Positive / Negative / Zero")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# -----------------------------------
# 2. Even or Odd
# -----------------------------------
print("\n2. Even or Odd")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# -----------------------------------
# 3. Largest of Three Numbers
# -----------------------------------
print("\n3. Largest of Three Numbers")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest Number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest Number:", num2)
else:
    print("Largest Number:", num3)

# -----------------------------------
# 4. Leap Year Checker
# -----------------------------------
print("\n4. Leap Year Checker")

year = int(input("Enter Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

# -----------------------------------
# 5. Multiplication Table
# -----------------------------------
print("\n5. Multiplication Table")

number = int(input("Enter a Number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# -----------------------------------
# 6. Factorial
# -----------------------------------
print("\n6. Factorial")

number = int(input("Enter a Number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)

# -----------------------------------
# 7. Prime Number Checker
# -----------------------------------
print("\n7. Prime Number Checker")

number = int(input("Enter a Number: "))

if number <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

# -----------------------------------
# 8. Sum of First N Numbers
# -----------------------------------
print("\n8. Sum of First N Numbers")

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

# -----------------------------------
# 9. Reverse Number
# -----------------------------------
print("\n9. Reverse Number")

number = input("Enter Number: ")

print("Reverse =", number[::-1])

# -----------------------------------
# 10. Fibonacci Series
# -----------------------------------
print("\n10. Fibonacci Series")

terms = int(input("How many terms? "))

first = 0
second = 1

print("Fibonacci Series:")

for i in range(terms):
    print(first, end=" ")
    next_number = first + second
    first = second
    second = next_number

print("\n")
print("=" * 50)
print("Assignment Completed Successfully!")
print("=" * 50)