temps = [

    ("Mon", 20), 
    ("Tue", 25), 
    ("Wed", 18)

    ]

print(temps[0])
hottest_day = temps[0]   # start by assuming the first is the max
for day, temp in temps:
    print(day)
    if temp > hottest_day[1]:
        hottest_day = (day, temp)

print(hottest_day)   # ('Tue', 25)
 