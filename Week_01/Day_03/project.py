print("=" * 40)
print("         CONTACT BOOK")
print("=" * 40)

contacts = {}

while True:

    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # Add Contact
    if choice == "1":

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone

        print("✅ Contact Added Successfully!")

    # Search Contact
    elif choice == "2":

        name = input("Enter Name to Search: ")

        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact Not Found.")

    # Delete Contact
    elif choice == "3":

        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully.")
        else:
            print("Contact Not Found.")

    # View Contacts
    elif choice == "4":

        if len(contacts) == 0:
            print("No Contacts Available.")

        else:

            print("\n----- Contact List -----")

            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    # Exit
    elif choice == "5":

        print("\nThank you for using Contact Book.")
        break

    else:
        print("Invalid Choice! Please Try Again.")