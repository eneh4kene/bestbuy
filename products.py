# This file is an experimental online store using OOP
class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = float(price)
        self.quantity = float(qty)
        self.active = True

    # Getter function for quantity.
    def get_quantity(self):
        return self.quantity

    # Setter function for quantity. If quantity reaches 0, deactivates the product.
    def set_quantity(self, quantity):
        self.quantity = float(quantity)
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    # returns a string with the product info
    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    # Buys a given quantity of the product. Returns the total price (float) of the purchase.
    # Updates the quantity of the product.
    def buy(self, quantity):
        total_price_purchased = float(quantity) * self.price
        self.quantity -= quantity
        return total_price_purchased

def main():
    bose = Product("Bose QuietComfort Earbuds", 250, 500)
    mac = Product("MacBook Air M2", 1450, 100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()