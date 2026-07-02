people = [
    ("Mostafa", 25, "Oshawa"),
    ("Sara", 30, "Toronto"),
    ("Amir", 22, "Vancouver")
]

for name,age,city in people:
   print(f"{name} is {age} years old and lives in {city}")
   print("="*10)
 


oldest_person = people[0]


for name,age,city in people:
   if age > oldest_person[1]:
      oldest_person = (name,age,city)

print(f"Oldest person age: {oldest_person[0]}")
   
   


coordinates = (43.6532, -79.3832)
latitude, longitude = coordinates
print(latitude)
print(longitude)




