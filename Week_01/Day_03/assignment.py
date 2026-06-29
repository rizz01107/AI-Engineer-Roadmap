print("=" * 50)
print("        DAY 3 PYTHON ASSIGNMENT")
print("=" * 50)

# -----------------------------------
# 1. List of 5 Fruits
# -----------------------------------
print("\n1. List of Fruits")

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# -----------------------------------
# 2. Add and Remove Fruits
# -----------------------------------
print("\n2. Add and Remove Fruits")

fruits.append("Pineapple")
fruits.append("Watermelon")

fruits.remove("Banana")

print("Final List:", fruits)

# -----------------------------------
# 3. Tuple of 5 Subjects
# -----------------------------------
print("\n3. Tuple of Subjects")

subjects = ("Math", "Physics", "Chemistry", "English", "Computer Science")

for subject in subjects:
    print(subject)

# -----------------------------------
# 4. Set with Duplicate Numbers
# -----------------------------------
print("\n4. Unique Numbers using Set")

numbers = {1, 2, 3, 4, 5, 2, 3, 4, 1, 5}

print(numbers)

# -----------------------------------
# 5. Union, Intersection, Difference
# -----------------------------------
print("\n5. Set Operations")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))

# -----------------------------------
# 6. Dictionary
# -----------------------------------
print("\n6. Student Dictionary")

student = {
    "Name": "Muhammad Rizwan",
    "Age": 23,
    "City": "Lahore",
    "Course": "AI Engineering"
}

print("\nKeys:")

for key in student.keys():
    print(key)

print("\nValues:")

for value in student.values():
    print(value)

print("\nKey : Value")

for key, value in student.items():
    print(f"{key} : {value}")

# -----------------------------------
# 7. Update Age
# -----------------------------------
print("\n7. Update Age")

student["Age"] = 23

print(student)

# -----------------------------------
# 8. Nested Dictionary
# -----------------------------------
print("\n8. Nested Dictionary")

students = {
    "Student1": {
        "Name": "Ali",
        "Age": 20,
        "Course": "AI"
    },

    "Student2": {
        "Name": "Sara",
        "Age": 21,
        "Course": "ML"
    },

    "Student3": {
        "Name": "Ahmed",
        "Age": 22,
        "Course": "Data Science"
    }
}

for student_id, info in students.items():
    print(f"\n{student_id}")

    for key, value in info.items():
        print(f"{key}: {value}")

# -----------------------------------
# 9. Highest Number without max()
# -----------------------------------
print("\n9. Highest Number")

numbers = [10, 45, 7, 99, 32, 56]

highest = numbers[0]

for number in numbers:

    if number > highest:
        highest = number

print("Highest Number:", highest)

# -----------------------------------
# 10. Character Frequency
# -----------------------------------
print("\n10. Character Frequency")

text = input("Enter a word: ")

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1

    else:
        frequency[char] = 1

print("\nCharacter Frequency")

for key, value in frequency.items():
    print(f"{key} = {value}")

print("\n" + "=" * 50)
print("Assignment Completed Successfully!")
print("=" * 50)