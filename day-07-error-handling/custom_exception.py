def check_age(age):
    if age < 0 :
        raise ValueError("Age can not be negative !")
    return f"age is: {age}"

try:
    result1 = check_age(25)
    print(result1)
    result2 = check_age(-5)
    
except ValueError as v:
    print(f"Error: {v}")




class NegativeDepositError(Exception):
    pass



def deposit(amount):
    if amount < 0:
        raise NegativeDepositError("Deposit amount cannot be negative")
    return f"Deposited:{amount}"






try:
    result_1 = deposit(100)
    print(result_1)
    result_2 = deposit(-50)

except NegativeDepositError as e:
    print(f"Error: {e}")