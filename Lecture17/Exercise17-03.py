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


def print(self):
    print(self.item + " barcode: " + str(self.barcode))
    print("Price:", self.price)
    print("Current Inventory:", self.quantity)
    print("Sold so far:", self.sales)
