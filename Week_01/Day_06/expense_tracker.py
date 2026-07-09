import csv
import os

FILE = "expenses.csv"

def add_expense():

    category = input("Category: ")
    amount = input("Amount: ")

    with open(FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([category, amount])

    print("Expense Added!")

def view_expenses():

    try:

        with open(FILE, "r") as file:

            reader = csv.reader(file)

            print("\nExpenses")

            for row in reader:
                print(row[0], "-", row[1])

    except FileNotFoundError:

        print("No Expense File Found!")

def total_expense():

    total = 0

    try:

        with open(FILE, "r") as file:

            reader = csv.reader(file)

            for row in reader:
                total += float(row[1])

        print("Total Expense =", total)

    except FileNotFoundError:

        print("No Expense File Found!")

while True:

    print("\n==========================")
    print(" SIMPLE EXPENSE TRACKER")
    print("==========================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")