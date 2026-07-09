
def add(num1,num2):
    return num1+num2

a= 10
b=10
result = add(a, b)
print(result)






def is_even(number):
    if number % 2 == 0:
        return True
    else: return False


number1 = 7
number2 = 10
print(is_even(number1))
print(is_even(number2))




def greet(name, default = "Hello"):
    return f"{default} {name}"




name = "mostafa"

result1 = greet(name)
print(result1)

result2 = greet(name, "hi")
print(result2)
