product = {
    "name": "Laptop",
    "price": 1200,
    "stock": 15
}

print(product.get("name", "unknown"))

product["brand"] = "Dell"
print(product)

product["price"] = 1100

print(product.get("warranty","Not specified"))

for key,value in product.items():
    print(f"{key}: {value}")