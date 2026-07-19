class InSufficientFundsError(Exception):
    pass

class IncorrectPinError(Exception):
    pass


def verify_pin(correct_pin,entered_pin):
    if entered_pin != correct_pin:
        raise IncorrectPinError("Incorrect PIN")
    return True

#Withdraw task
def withdraw(balance, amount):
    if amount > balance:
        raise InSufficientFundsError("Insufficient Funds!")
    return balance - amount


balance = 1000
amount = 1500

# Flow 1: correct PIN, but withdrawal exceeds balance
try:
    correct_pin = 1234
    entered_pin = 1234  #Taking PIN from user
    verify_pin(correct_pin,entered_pin)
    remaining_balance = withdraw(balance,amount)
    print(f"Remaining Balance: {remaining_balance}")

except IncorrectPinError as e:
    print(f"Error: {e}")

except InSufficientFundsError as e:
    print(f"Error: {e}")


# Flow 2: incorrect PIN, withdrawal never attempted
try:
    correct_pin = 1234
    entered_pin = 4535  #Taking PIN from user
    verify_pin(correct_pin,entered_pin)
    remaining_balance = withdraw(balance,amount)
    print(f"Remaining Balance: {remaining_balance}")

except IncorrectPinError as e:
    print(f"Error: {e}")

except InSufficientFundsError as e:
    print(f"Error: {e}")




