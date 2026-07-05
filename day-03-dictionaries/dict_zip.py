names = ["Mostafa", "Sara", "Amir", "Nadia","Akash"]
scores = [30, 92, 76, 95,60]

combined = dict(zip(names,scores))
print(combined)


# {'Mostafa': 30, 'Sara': 92, 'Amir': 76, 'Nadia': 95}


# passed_students = {}
# for name, score in combined.items():
#     if score >= 80:
#         passed_students[name] = score

# print(passed_students)


passed_students = {name: score for name,score in combined.items() if score >=80}
print(passed_students)





#{'Mostafa': 30, 'Sara': 92, 'Amir': 76, 'Nadia': 95, 'Akash': 60}

# for name,score in combined.items(): 
#     if score >= 80:
#         print(f"pass {score} : {name}")
#     else:
#         print(f"Fail {score} : {name}")


pass_fail = {name: ("pass" if score >=80 else "fail") for name,score in combined.items()}
print(pass_fail)



for name,score in zip(names,scores):
    print(f"{name}: {score}")