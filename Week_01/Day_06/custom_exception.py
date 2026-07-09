class AgeError(Exception):
    pass


age = int(input("Enter Age: "))

try:

    if age < 18:
        raise AgeError("Age must be 18 or above.")

    print("Eligible!")

except AgeError as error:

    print(error)