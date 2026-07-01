print("=" * 50)
print("DAY 4 - FUNCTIONS ASSIGNMENT")
print("=" * 50)


# 1
def my_name():
    print("Muhammad Rizwan")


my_name()


# 2
def add(a, b):
    return a + b


print("Addition =", add(20, 30))


# 3
def square(num):
    return num * num


print("Square =", square(5))


# 4
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"


print(even_odd(12))


# 5
def largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    return c


print("Largest =", largest(50, 90, 30))


# 6
def greet(name="Guest"):
    print("Hello", name)


greet()
greet("Rizwan")


# 7
def total(*numbers):

    sum_numbers = 0

    for num in numbers:
        sum_numbers += num

    return sum_numbers


print(total(10, 20, 30, 40))


# 8
def student(**info):

    for key, value in info.items():
        print(key, ":", value)


student(
    Name="Rizwan",
    Age=23,
    Course="AI Engineering"
)


# 9
import math_utils

print(math_utils.add(10, 20))
print(math_utils.subtract(50, 30))
print(math_utils.multiply(5, 6))
print(math_utils.divide(20, 5))


# 10
def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


print("Factorial =", factorial(5))