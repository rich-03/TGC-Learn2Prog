class Inventory:
    item = ""
    barcode = 0
    quantity = 0
    price = 0.00
    sales = 0.00

    def __init__(self, product, bar, pr):
        self.item = product
        self.barcode = bar
        self.price = pr

    def changeprice(self, newprice):
        self.price = newprice

    def sell(self, n):
        self.quantity -= n
        self.sales += self.price * n

    def restock(self, n):
        self.quantity += n


shoes = Inventory("shoe", 1234512345, 30.00)
shoes.restock(100)
shirts = Inventory("shirt", 9876598765, 25.00)
shirts.restock(80)
shoes.sell(10)
shirts.sell(30)
shoes.sell(50)
print(shoes.quantity)
print(shoes.sales)
print(shirts.quantity)
print(shirts.sales)
