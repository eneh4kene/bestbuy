import products
import store
import promotions

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, qty=100),
    products.Product("Bose QuietComfort Earbuds", price=250, qty=500),
    products.Product("Google Pixel 7", price=500, qty=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, qty=250, maximum=1)
]

# Create promotion catalog
second_half_price = promotions.SecondItemHalfPrice("Second Half price!")
third_one_free = promotions.BuyTwoGetOneFree("Third One Free!")
thirty_percent = promotions.PercentageDiscount("30% off!", 30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)



best_buy = store.Store(product_list)

def start(store):
    print('''  Store Menu
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
            print("Total items in store:", store.get_total_quantity())
        elif user_choice == "3":
            shopping_list = []
            while True:
                print("When you want to finish order, enter empty text.")
                product_index = input("Which product # do you want? ")
                if not product_index:
                    break
                quantity = input("What amount do you want? ")
                if not quantity:
                    break
                try:
                    product_index = int(product_index)
                    quantity = int(quantity)
                    active_products = store.get_all_products()
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

            if shopping_list:
                total_price = store.order(shopping_list)
                print(f"Total amount of your purchase is: ${total_price:.2f}")
            else:
                print("No items were ordered.")
        elif user_choice == "4":
            print("Thank you for using the store.")
            break

if __name__ == "__main__":
    start(best_buy)
