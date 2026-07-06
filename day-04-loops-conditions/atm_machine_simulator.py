balance = 500
pin = "1234"
choice = "exit"

withdrawal_balance = 200


entered_pin = "1234"

if not entered_pin == pin:
    print("Incorrect PIN")

else:
    while True:
        if choice == 'balance':
            print(f"Current Balance: {balance}")
            break
        elif  choice == 'withdraw':
            if balance >= 200:
                remaining_balance = balance - withdrawal_balance
                balance = remaining_balance
                print(f"Withdrawal successful. New balance: {balance}")
                break
            else:
                print("Insufficient funds")
        
        elif choice == "exit":
            print(f'Thank you for banking with us')
            break






attempts = ["0000", "1111", "1234"]
count = 0

while count < len(attempts):
    if pin == attempts[count]:
        print(f"{count:<10} : {attempts[count]} ")
        break
    else:
        print('Try Again')
        count +=1
        
        
    
    