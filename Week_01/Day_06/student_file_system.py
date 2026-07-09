import os

FILE = "students.txt"

def add_student():

    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")

    with open(FILE, "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("Student Added Successfully!")

def view_students():

    try:

        with open(FILE, "r") as file:

            data = file.readlines()

            if not data:
                print("No Students Found.")

            else:

                print("\nStudent Records")

                for student in data:
                    print(student.strip())

    except FileNotFoundError:

        print("No Student File Found!")

def search_student():

    name = input("Enter Name: ").lower()

    try:

        with open(FILE, "r") as file:

            found = False

            for student in file:

                if student.lower().startswith(name):

                    print(student.strip())

                    found = True

            if not found:
                print("Student Not Found!")

    except FileNotFoundError:

        print("No Student File Found!")

def delete_student():

    name = input("Enter Name to Delete: ").lower()

    try:

        with open(FILE, "r") as file:

            students = file.readlines()

        with open(FILE, "w") as file:

            found = False

            for student in students:

                if not student.lower().startswith(name):

                    file.write(student)

                else:

                    found = True

        if found:
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    except FileNotFoundError:

        print("No Student File Found!")

while True:

    print("\n========================")
    print(" STUDENT FILE SYSTEM")
    print("========================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")