# This file is an experimental online store using OOP
class Product:
    def __init__(self, name, price, qty):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if qty < 0:
            raise ValueError("Quantity cannot be negative")
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
        if quantity > self.quantity:
            raise ValueError("Attempt to purchase more than available stock.")
        self.set_quantity(self.quantity - quantity)
        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, qty=0)  # Set quantity to zero and leave it there.

    def set_quantity(self, quantity):
        super().set_quantity(0)  # Override to always set quantity to zero

    def buy(self, quantity):
        return quantity * self.price  # Allow unlimited purchases

    def show(self):
        return f"{self.name}, Price: {self.price} (Non-Stocked Product)"


class LimitedProduct(Product):
    def __init__(self, name, price, qty, maximum):
        super().__init__(name, price, qty)
        self.maximum = maximum  # Maximum number of times this product can be purchased in an order

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} units of {self.name} in a single order.")
        super().buy(quantity)  # Use the original buy method if within limit

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per Order: {self.maximum}"

    def set_maximum(self, maximum):
        self.maximum = maximum


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