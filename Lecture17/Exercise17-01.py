import self as self


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


widget = Inventory("Widget", 1112223334, 10.00)
widget.restock(30)
widget.sell(10)
print(widget.quantity)
print(widget.sales)
widget.changeprice(20.0)
widget.sell(10)
print(widget.quantity)
print(widget.sales)
