try:

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

    print("Answer =", result)

except ZeroDivisionError:

    print("Cannot Divide by Zero!")

except ValueError:

    print("Please Enter Numbers Only!")

finally:

    print("Program Finished.")