with open("data.txt","w") as file:
    file.write("Big Marry\ntaters\nFries")



with open("data.txt","r") as file:
    for line in file:
        print(line.strip())

with open("data.txt","a") as file:
    file.write("Mini Sandwitch")

with open("data.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
    print(count)

        


