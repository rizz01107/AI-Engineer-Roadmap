def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total):
    return total / 5


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    return "F"


def check_status(percentage):

    if percentage >= 50:
        return "PASS"

    return "FAIL"


print("=" * 40)
print("     STUDENT RESULT SYSTEM")
print("=" * 40)

name = input("Enter Student Name: ")

subjects = [
    "Math",
    "Physics",
    "English",
    "Computer",
    "AI"
]

marks = []

for subject in subjects:

    score = float(input(f"{subject}: "))
    marks.append(score)

total = calculate_total(marks)

percentage = calculate_percentage(total)

grade = calculate_grade(percentage)

status = check_status(percentage)

print("\n" + "=" * 40)
print("RESULT")
print("=" * 40)

print("Student    :", name)
print("Total      :", total)
print(f"Percentage : {percentage:.2f}%")
print("Grade      :", grade)
print("Status     :", status)