grades = {
    "Mostafa": 
    {
        "Math": 85,
        "Science": 78,
        "English": 92
    },
    "Sara": {"Math": 90, "Science": 95, "English": 88},
    "Amir": {"Math": 60, "Science": 55, "English": 70}
}


# ============================================================
# TASK 1: Calculate and print each student's average score
# ============================================================
name_with_average = {}
for name,subjects in grades.items():
    total = 0
    for subject_scores in subjects.values():
        total = total+ subject_scores
    average = round(total/len(subjects),2)
    name_with_average[name] = average

for name,score in name_with_average.items():
    print(f"{name} got average score: {score}")


# ============================================================
# TASK 2: Find each student's strongest and weakest subject
# ============================================================
for name,subjects in grades.items():
    strongest_subject_score = 0
    strongest_subject = ""
    weakest_subject_score = 999
    weakest_subject = ""

    for subject_name,subject_score in subjects.items():
        if subject_score > strongest_subject_score :
            strongest_subject_score = subject_score
            strongest_subject = subject_name
        if subject_score < weakest_subject_score :
            weakest_subject_score = subject_score
            weakest_subject = subject_name

    print("--"*10)
    print(name)
    print("--"*10)
    print(f"Strongest Subject: {strongest_subject} with score of: {strongest_subject_score}")
    print(f"Weakest Subject: {weakest_subject} with score of: {weakest_subject_score}")


# ============================================================
# TASK 3: Find the student with the highest overall average
# ============================================================
best_student = ""
all_averages = {}
for name,subjects in grades.items():
    total = 0
    for subject_score in subjects.values():
        total = total+ subject_score
        average = round(total/len(subjects),2)
    all_averages[name]= average

# {'Mostafa': 85.0, 'Sara': 91.0, 'Amir': 61.67}
highest_score = 0
highest_score_holder = ""
for name,highest_average in all_averages.items():
    if highest_score<highest_average:
        highest_score = highest_average
        highest_score_holder = name
print(f"{highest_score_holder} get highest average mark with average: {highest_score}")

highest_overall_average = 0
best_student = ""

for name,subjects in grades.items():
    total = 0
    for subject_name,subject_score in subjects.items():
        total = subject_score+total
        average = round(total/len(subjects),2)
        if average > highest_overall_average :
            highest_overall_average = average
            best_student = name
print(f"Best Students: {best_student:<10} Highest Mark: {highest_overall_average}")


# ============================================================
# TASK 4: Build pass_students dict (average >= 75) via comprehension
# ============================================================
pass_students = {name: average for name,average in name_with_average.items() if average >=75 }
print(f"Pass students: {pass_students}")