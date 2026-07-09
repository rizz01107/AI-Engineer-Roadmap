import csv

print("=" * 50)
print("      DAY 6 ASSIGNMENT")
print("=" * 50)

# ------------------------------------
# 1. Create File, Write & Read
# ------------------------------------

print("\n1. Create and Read File")

with open("message.txt", "w") as file:
    file.write("Hello Python")

with open("message.txt", "r") as file:
    print(file.read())

# ------------------------------------
# 2. Append Data
# ------------------------------------

print("\n2. Append Data")

with open("message.txt", "a") as file:
    file.write("\nWelcome to AI Engineering")

with open("message.txt", "r") as file:
    print(file.read())

# ------------------------------------
# 3. Count Characters, Words, Lines
# ------------------------------------

print("\n3. Count Characters, Words, Lines")

with open("message.txt", "r") as file:
    text = file.read()

characters = len(text)
words = len(text.split())
lines = len(text.splitlines())

print("Characters :", characters)
print("Words :", words)
print("Lines :", lines)

# ------------------------------------
# 4. Copy File
# ------------------------------------

print("\n4. Copy File")

with open("message.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("File Copied Successfully!")

# ------------------------------------
# 5. Create CSV
# ------------------------------------

print("\n5. Create CSV")

students = [
    ["Name", "Age", "Course"],
    ["Rizwan", 23, "AI"],
    ["Ali", 21, "ML"],
    ["Sara", 22, "DS"],
    ["Ahmed", 20, "Python"],
    ["Fatima", 24, "NLP"]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(students)

print("CSV Created Successfully!")

# ------------------------------------
# 6. Read CSV
# ------------------------------------

print("\n6. Read CSV")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# ------------------------------------
# 7. Exception Handling
# ------------------------------------

print("\n7. Exception Handling")

try:

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    print("Answer =", num1 / num2)

except ZeroDivisionError:

    print("Cannot Divide By Zero!")

except ValueError:

    print("Invalid Input!")

# ------------------------------------
# 8. File Not Found
# ------------------------------------

print("\n8. File Not Found")

try:

    with open("python.txt", "r") as file:
        print(file.read())

except FileNotFoundError:

    print("File Not Found!")

# ------------------------------------
# 9. Custom Exception
# ------------------------------------

print("\n9. Custom Exception")

class InvalidSalaryError(Exception):
    pass

try:

    salary = int(input("Enter Salary: "))

    if salary < 30000:
        raise InvalidSalaryError("Salary Must Be At Least 30000")

    print("Salary Accepted")

except InvalidSalaryError as error:

    print(error)

# ------------------------------------
# 10. Login System
# ------------------------------------

print("\n10. Login System")

username = "admin"
password = "1234"

attempts = 3

while attempts > 0:

    user = input("Username: ")
    pwd = input("Password: ")

    if user == username and pwd == password:

        print("Login Successful!")
        break

    else:

        attempts -= 1

        print("Invalid Credentials")

        if attempts > 0:
            print("Attempts Left:", attempts)
        else:
            print("Account Locked!")

print("\nAssignment Completed Successfully!")