marks = int(input("Enter your marks: "))

if marks >= 50:

    if marks >= 90:
        print("Grade A+")

    elif marks >= 80:
        print("Grade A")

    elif marks >= 70:
        print("Grade B")

    else:
        print("Grade C")

else:
    print("Fail")