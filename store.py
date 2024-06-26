# The Store class will contain one variable - a list of products that exist in the store
import products

class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    # method to add a new product object
    def add_product(self, product):
        self.list_of_products.append(product)

    # removes a product from the store
    def remove_product(self, product):
        self.list_of_products.remove(product)

    # prints the total qty of items in the store
    def get_total_quantity(self):
        total_qty = 0
        for product in self.list_of_products:
            if isinstance(product, products.NonStockedProduct):
                continue  # Skip non-stocked products in quantity total
            total_qty += int(product.get_quantity())
        return total_qty

    # gets the list of active products in the store
    def get_all_products(self):
        list_of_all_active_products = []
        for product in self.list_of_products:
            if product.is_active():
                list_of_all_active_products.append(product)
        return list_of_all_active_products

    # Gets a list of tuples, where each tuple has 2 item. Product (Product class) and quantity (int).
    # Buys the products and returns the total price of the order.
    def order(self, shopping_list):
        total_order_price = 0
        for item in shopping_list:
            product, quantity = item
            try:
                if product in self.list_of_products:
                    total_order_price += product.buy(quantity)
                else:
                    print(f"Product '{product.name}' not found in the store.")
            except ValueError as e:
                print(e)  # This will print error messages like the one for exceeding maximum purchase amounts
        return total_order_price
