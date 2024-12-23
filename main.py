from Products import Products
from Store import Store


def init() -> Store:
    try:
        product_list = [Products("MacBook Air M2", price=1450, quantity=100),
                        Products("Bose QuietComfort Earbuds", price=250, quantity=500),
                        Products("Google Pixel 7", price=400, quantity=250)
                        ]
        return Store(product_list)
    except (Exception, ValueError) as e:
        print("\nAn unexpected error occurred:")
        print(f"Error: {e}")


def start(store_obj: Store):
    while True:
        display_menu()
        choice = input("Please choose a number (1-4): ")

        if choice == "1":
            print("\nProducts in Store:")
            print("\n--------------")
            for index, product in enumerate(store_obj.get_all_products(), start=1):
                print(f"{index}. {product.show()}")
        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")
        elif choice == "3":
            set_order(store_obj)
        elif choice == "4":
            print("\nThank you for visiting Best Buy! Goodbye! 👋")
            break
        else:
            print("\nInvalid choice. Please try again.")
        input("Press Enter to continue ")


def set_order(store_obj):
    shopping_list = []
    print("\nEnter your order (leave product name empty to finish):")
    while True:
        product_name = input("Product Name: ")
        if not product_name:
            break
        quantity = int(input("Quantity: "))

        for product in store_obj.get_all_products():
            if product.name == product_name:
                shopping_list.append((product, quantity))
                break
        else:
            print(f"Product '{product_name}' not found in the store.")
    try:
        total_price = store_obj.order(shopping_list)
        print(f"\nOrder successful! Total price: ${total_price:.2f}")
    except Exception as e:
        print(f"Error: {e}")


def display_menu():
    """Displays the menu options for the user."""
    print("\nWelcome to the Best Buy Store! 🎉")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def main():
    best_buy = init()

    try:
        start(best_buy)
    except Exception as e:
        print("\nAn unexpected error occurred:")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
