def total(*numbers):
    total = 0
    for num in numbers:
        total = total+num
    return total

result1 = total(1,2,4,5,6,7)
result2 = total(1,2,4,5)
print(result1)
print(result2)



def describe_person(**info):
    for key,value in info.items():
        print(f"{key}: {value}")




name = "Mostafa"
age = 30
city = "Oshawa"
describe_person(name = "mostafa",age = 30,city = "oshawa")




def average(*scores):
    return sum(scores)/len(scores)







result = average(10,20,30,40)
print(result)