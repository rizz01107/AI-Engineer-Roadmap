import math

print("=" * 50)
print("      DAY 5 - OOP ASSIGNMENT")
print("=" * 50)

# -----------------------------------
# 1. Car Class
# -----------------------------------

print("\n1. Car Class")

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)


car = Car("Toyota", "Corolla")
car.display()


# -----------------------------------
# 2. Student Class
# -----------------------------------

print("\n2. Student Class")

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)


student = Student("Muhammad Rizwan", 23, "AI Engineering")
student.display()


# -----------------------------------
# 3. Rectangle Class
# -----------------------------------

print("\n3. Rectangle Class")

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10, 5)

print("Area =", rectangle.area())
print("Perimeter =", rectangle.perimeter())


# -----------------------------------
# 4. Bank Account
# -----------------------------------

print("\n4. Bank Account")

class BankAccount:

    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance =", self.balance)


account = BankAccount()

account.deposit(500)
account.withdraw(300)
account.show_balance()


# -----------------------------------
# 5. Inheritance
# -----------------------------------

print("\n5. Employee & Manager")

class Employee:

    def work(self):
        print("Employee is Working")


class Manager(Employee):

    def manage(self):
        print("Manager is Managing")


manager = Manager()

manager.work()
manager.manage()


# -----------------------------------
# 6. Method Overriding
# -----------------------------------

print("\n6. Method Overriding")

class Person:

    def introduce(self):
        print("I am a Person")


class Teacher(Person):

    def introduce(self):
        print("I am a Teacher")


teacher = Teacher()

teacher.introduce()


# -----------------------------------
# 7. Encapsulation
# -----------------------------------

print("\n7. Laptop")

class Laptop:

    def __init__(self):
        self.__price = 0

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


laptop = Laptop()

laptop.set_price(120000)

print("Price =", laptop.get_price())


# -----------------------------------
# 8. Polymorphism
# -----------------------------------

print("\n8. Dog & Cat")

class Dog:

    def sound(self):
        print("Dog : Bark")


class Cat:

    def sound(self):
        print("Cat : Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# -----------------------------------
# 9. Book Class
# -----------------------------------

print("\n9. Book Class")

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self.price)


book = Book("Python Crash Course", "Eric Matthes", 2500)

book.display()


# -----------------------------------
# 10. Circle Class
# -----------------------------------

print("\n10. Circle")

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


circle = Circle(7)

print(f"Area = {circle.area():.2f}")
print(f"Circumference = {circle.circumference():.2f}")

print("\nAssignment Completed Successfully!")