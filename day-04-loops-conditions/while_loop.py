while True:
    answer = input("Enter yes or no: ")
    if answer in ("yes", "no"):
        break
    print("Invalid, try again")


    while True:
        answer = input("Enter yes or no: ")
        if answer in ("yes","no"):
            break
        print("Invalid, try again")










        count = 0
while True:          # infinite loop on purpose
    count += 1
    if count == 3:
        continue     # skip this iteration, go to next
    if count == 6:
        break        # exit the loop entirely
    print(count)