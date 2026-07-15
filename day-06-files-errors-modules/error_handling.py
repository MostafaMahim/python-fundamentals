
try:
    with open("ghost_file.txt","r") as file:
        content = file.read()

except FileNotFoundError:
    print("File doesn't exist")




def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

result = safe_divide(10, 0)
result2 = safe_divide(10,2)
print(result)
print(result2)


def get_number(value):
    try:
        num = int(value)
        return num
    except ValueError:
        return 'Invalid number'



result = get_number("42")
result2 = get_number("abc")
print(result)
print(result2)



try:
    x = 10 / 2

except ZeroDivisionError:
    print('Error')

else:
    print(x)

finally:
    print('Operation attempted')
