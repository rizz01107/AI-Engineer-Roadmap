def student(name, age, course):
    print("Name :", name)
    print("Age :", age)
    print("Course :", course)

student("Rizwan", 23, "AI")

# Default Parameters

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Rizwan")

# *args

def add(*numbers):

    total = 0

    for number in numbers:
        total += number

    print("Total =", total)

add(10, 20)
add(10, 20, 30, 40)

# **kwargs

def student(**info):

    for key, value in info.items():
        print(key, ":", value)

student(name="Rizwan", age=23, course="AI")