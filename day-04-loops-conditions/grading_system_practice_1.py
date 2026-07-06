score = 80


if score >= 90:
    print(f"Grade is: A")
elif score >= 80 and score < 90:
    print(f"Grade is: B")
elif score >= 70 and score < 80:
    print(f"Grade is: C")
elif score >= 60 and score < 70:
    print(f"Grade is: D")
else: 
    print(f"Grade is: F")







age = 10
has_permission = False


if age >= 18 or (has_permission and age < 18):
    print("Allowed")
else:
    print("Not allowed")









cart =[]

if not cart:
    print("Cart is empty ")
else:
    print("Cart has items")