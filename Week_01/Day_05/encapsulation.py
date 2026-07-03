class Bank:

    def __init__(self):

        self.__balance = 500

    def deposit(self, amount):

        self.__balance += amount

    def show_balance(self):

        print("Balance =", self.__balance)

account = Bank()

account.deposit(200)

account.show_balance()