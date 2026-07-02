group_a = {"Mostafa", "Sara", "Amir", "Nadia"}
group_b = {"Sara", "Kevin", "Amir", "Priya"}



first_letters = set()

for name in group_a:
    first_letters.add(name[0])
print(first_letters)


print(group_a & group_b)
print(group_a | group_b)
print(group_a - group_b)
