students = {}

#-----------------------------------1-----------------------
def add_student(name, grade):
    students[name] = grade
    


add_student("Mostafa",90)
add_student("Martufa",80)
add_student("Mahim",99)
add_student("Akash",66)
add_student("hafiz",100)

print(students)

#-----------------------------------2-----------------------
print("-"*10)
def get_grade(name,if_not = "Student not found"):
    return students.get(name,if_not)


student_grade = get_grade("hafiz")
print(student_grade)


#-----------------------------------3-----------------------
print("-"*10)



def update_grade(name, new_grade):
    for get_name,score in students.items():
        if get_name == name:
            students[get_name] = new_grade
            return students
    return "Not found"
    
   
    
updated_student_list= update_grade("Mostafa",100)
print(updated_student_list)



#-----------------------------------4-----------------------
print("-"*10)

def remove_student(name):
    for get_name in students.keys():
        if get_name == name:
            students.pop(name)
            return students 
    return "Student not found"

updated_student_list_2 = remove_student("Mahim")
print(updated_student_list_2)


#-----------------------------------5-----------------------
print("-"*10)

def class_average(*scores):
    total = 0
    for score in scores:
        total = total+score
    return round(total/len(scores),2)


result = class_average(*students.values())
print(result)


#-----------------------------------6-----------------------
print("-"*10)

# {'Mostafa': 99, 'Martufa': 80, 'Akash': 66}


def top_student(*student_data):
    top_student = ""
    top_score = 0
    for student_name,score in student_data:
        if top_score < score:
            top_score = score
            top_student = student_name
    return top_student
        
result  = top_student(*students.items())
print(f"Top student: {result}")
