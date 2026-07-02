students = ["Mostafa", "Sara", "Amir"]

students.append("Nadia")
students.append("Kevin")
print(students)
students.remove("Amir")
print(students)


sorted_students= sorted(students)
print(sorted_students)


for number,name in enumerate(sorted_students,1):
    print(f"{number}.{name}")

print(f"Total number of students: {len(students)}")