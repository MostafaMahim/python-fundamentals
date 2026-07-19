class NegativeValueError(Exception):
    pass



def check_age(age):
    if age < 0:
        raise NegativeValueError("Age can not be a negative value !")
    return f"input age: {age}"

result = check_age(-4)

try:
    result = check_age(-10)

except NegativeValueError as e:
    print(f"Error: {e}")


