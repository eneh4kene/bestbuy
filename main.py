# the user interface
import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, qty=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, qty=500),
                 products.Product("Google Pixel 7", price=500, qty=250)
               ]
best_buy = store.Store(product_list)

def start(store):
    print(f'''  Store Menu
              ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit''')

    while True:
        user_choice = input("Please choose a number: ")
        if user_choice == "1":
            all_products = store.get_all_products()
            for i, product in enumerate(all_products, 1):
                print(f"{i}. {product.show()}")
        elif user_choice == "2":
            print(store.get_total_quantity())
        elif user_choice == "3":
            while True:
                print("When you want to finish order, enter empty text.")
                shopping_list = []
                active_products = store.get_all_products()
                product_index = input("Which product # do you want? ")
                if not product_index:
                    break
                quantity = input("What amount do you want? ")
                if not quantity:
                    break
                try:
                    product_index = int(product_index)
                    quantity = int(quantity)
                    if product_index <= 0 or product_index > len(active_products):
                        raise ValueError("Invalid product index")
                    selected_product = active_products[product_index - 1]
                    if quantity > selected_product.get_quantity():
                        raise ValueError("Ordered quantity exceeds available stock")
                    item = (selected_product, quantity)
                    shopping_list.append(item)
                except ValueError as e:
                    print("Error:", e)
                    continue
                else:
                    store.order(shopping_list)
                    break
        elif user_choice == "4":
            break


start(best_buy)
