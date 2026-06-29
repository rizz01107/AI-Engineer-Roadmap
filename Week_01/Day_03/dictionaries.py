student = {
    "name":"Rizwan",
    "age":23,
    "city":"Lahore"
}

print(student["name"])

# Methods
print(student.keys())

print(student.values())

print(student.items())

print(student.get("name"))

print(student.update({"city": "Layyah"}))

print(student.pop("age"))

# print(student.clear())

# Loop

for key,value in student.items():

    print(f"{key}: {value}")

# Nested Collections

students = [

    {
        "name":"Rizwan",
        "age":23
    },

    {
        "name":"Sara",
        "age":21
    }

]

for student in students:

    print(student["name"])