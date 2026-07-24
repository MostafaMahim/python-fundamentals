#custom Exception
class OutOfStockError(Exception):  
    pass


class Inventory:
    def __init__(self,item_name,quantity):
        self.item_name = item_name
        self.quantity = quantity

    def remove_stock(self,amount):
        if amount > self.quantity:
            raise OutOfStockError(f"Only {self.quantity} units of {self.item_name} available")
        else:
            self.quantity = self.quantity - amount
        return self.quantity

    def add_stock(self,amount):
        self.quantity = self.quantity + amount
        return self.quantity



laptop_stock = Inventory("Laptop",20)

try:
    laptop_stock.remove_stock(100)

except OutOfStockError as e:
    print(f"Error: {e}")


print(laptop_stock.quantity)
