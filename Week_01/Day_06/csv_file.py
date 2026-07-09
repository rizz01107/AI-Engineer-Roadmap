import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Rizwan", 23, "AI Engineering"])
    writer.writerow(["Ali", 21, "Machine Learning"])

print("CSV File Created Successfully!")