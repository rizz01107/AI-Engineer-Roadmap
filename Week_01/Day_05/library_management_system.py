class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


library = []


while True:

    print("\n" + "=" * 40)
    print("     LIBRARY MANAGEMENT")
    print("=" * 40)

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Choose: ")

    # Add Book
    if choice == "1":

        title = input("Title: ")
        author = input("Author: ")

        library.append(Book(title, author))

        print("Book Added Successfully!")

    # View Books
    elif choice == "2":

        if len(library) == 0:
            print("No Books Available.")

        else:

            for book in library:

                status = "Available" if book.available else "Borrowed"

                print(f"{book.title} | {book.author} | {status}")

    # Search Book
    elif choice == "3":

        search = input("Enter Book Title: ")

        found = False

        for book in library:

            if book.title.lower() == search.lower():

                status = "Available" if book.available else "Borrowed"

                print(book.title, "-", book.author, "-", status)

                found = True

        if not found:
            print("Book Not Found")

    # Borrow Book
    elif choice == "4":

        title = input("Enter Book Title: ")

        for book in library:

            if book.title.lower() == title.lower():

                if book.available:

                    book.available = False
                    print("Book Borrowed Successfully!")

                else:

                    print("Book Already Borrowed")

                break

        else:

            print("Book Not Found")

    # Return Book
    elif choice == "5":

        title = input("Enter Book Title: ")

        for book in library:

            if book.title.lower() == title.lower():

                book.available = True

                print("Book Returned Successfully!")

                break

        else:

            print("Book Not Found")

    # Exit
    elif choice == "6":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")