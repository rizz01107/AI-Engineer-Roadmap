# -------------------------------
# 1. Print Personal Information
# -------------------------------

print("1. Personal Information")
print("Name: Muhammad Rizwan")
print("Age: 23")
print("City: Gorakhpur")

print("\n-------------------------------")

# -------------------------------
# 2. Basic Calculator
# -------------------------------

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)

print("\n-------------------------------")

# -------------------------------
# 3. Kilometer to Meter
# -------------------------------

km = float(input("Enter Kilometers: "))
meters = km * 1000

print("Meters:", meters)

print("\n-------------------------------")

# -------------------------------
# 4. Minutes to Hours
# -------------------------------

minutes = int(input("Enter Minutes: "))

hours = minutes // 60
remaining = minutes % 60

print(f"{hours} Hours and {remaining} Minutes")

print("\n-------------------------------")

# -------------------------------
# 5. Area of Rectangle
# -------------------------------

length = float(input("Length: "))
width = float(input("Width: "))

area = length * width

print("Area:", area)

print("\n-------------------------------")

# -------------------------------
# 6. Perimeter of Rectangle
# -------------------------------

perimeter = 2 * (length + width)

print("Perimeter:", perimeter)

print("\n-------------------------------")

# -------------------------------
# 7. BMI Calculator
# -------------------------------

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))

print("\n-------------------------------")

# -------------------------------
# 8. Reverse String
# -------------------------------

text = input("Enter Text: ")

print("Reverse:", text[::-1])

print("\n-------------------------------")

# -------------------------------
# 9. Count Vowels
# -------------------------------

text = input("Enter Text: ")

vowels = "aeiouAEIOU"

count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowels:", count)

print("\n-------------------------------")

# -------------------------------
# 10. Multiplication Table
# -------------------------------

number = int(input("Enter Number: "))

print(f"\nMultiplication Table of {number}")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")