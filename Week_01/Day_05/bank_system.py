class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Deposit Successful")

    def withdraw(self, amount):

        if amount > self.__balance:
            print("Insufficient Balance")

        else:
            self.__balance -= amount
            print("Withdrawal Successful")

    def show_balance(self):
        print("Current Balance =", self.__balance)


account = BankAccount()

while True:

    print("\n" + "=" * 35)
    print("          BANK")
    print("=" * 35)

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("\nChoose: ")

    if choice == "1":

        amount = float(input("Enter Amount: "))
        account.deposit(amount)

    elif choice == "2":

        amount = float(input("Enter Amount: "))
        account.withdraw(amount)

    elif choice == "3":

        account.show_balance()

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")