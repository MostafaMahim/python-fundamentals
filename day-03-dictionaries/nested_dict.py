employees = {
    "e1": {
        "name": "Mostafa",
        "department": "Engineering",
        "salary": 75000
        },
    "e2": {"name": "Sara", "department": "Marketing", "salary": 65000},
    "e3": {"name": "Amir", "department": "Engineering", "salary": 10000}
}


print(employees["e3"]["salary"])

for key,value in employees.items():
    # name =  value["name"]
    # department =  value["department"]
    # salary =  value["salary"]
     name, department , salary = value.values()
     print(f"{name} works in {department} earning ${salary}")




highest_paid_employee = ""
highest_salary = 0
for key,value in employees.items():
     if highest_salary < value["salary"]:
          highest_salary = value["salary"]
          highest_paid_employee = value["name"]
    
print(f"Highest paid emplyee is : {highest_paid_employee}")

    
total_salary = 0
for values in employees.values():
     if values["department"] == "Engineering":
       total_salary = total_salary+ values["salary"]
    
print("Total salary of Engineering department is : ", total_salary)