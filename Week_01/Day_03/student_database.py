print("=" * 40)
print("      STUDENT DATABASE")
print("=" * 40)

students = []

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # Add Student
    if choice == "1":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = {
            "Name": name,
            "Age": age,
            "Course": course
        }

        students.append(student)

        print("\n✅ Student Added Successfully!")

    # View Students
    elif choice == "2":

        if len(students) == 0:
            print("\nNo students found.")

        else:
            print("\n----- Student List -----")

            for student in students:
                print(f"Name   : {student['Name']}")
                print(f"Age    : {student['Age']}")
                print(f"Course : {student['Course']}")
                print("-" * 25)

    # Search Student
    elif choice == "3":

        search = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["Name"].lower() == search.lower():

                print("\nStudent Found")
                print(student)

                found = True
                break

        if not found:
            print("Student Not Found.")

    # Delete Student
    elif choice == "4":

        delete = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["Name"].lower() == delete.lower():

                students.remove(student)

                print("Student Deleted Successfully.")

                found = True
                break

        if not found:
            print("Student Not Found.")

    # Exit
    elif choice == "5":

        print("\nThank you for using Student Database.")
        break

    else:
        print("Invalid Choice!")