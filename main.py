from products import Product
from store import Store


def init() -> Store:
    """
    Initializes the store with default products.
    :return: An instance of Store.
    """
    try:
        product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        Product("Google Pixel 7", price=400, quantity=250)
                        ]
        return Store(product_list)
    except ValueError as error:
        print("Invalid input:", error)
    except Exception as error:
        print("\nAn unexpected error occurred:")
        print(f"Error: {error}")


def start(store_obj: Store) -> None:
    """
    Starts the user interface for interacting with the store.
    :param store_obj: An instance of the Store class.
    """

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


def set_order(store_obj) -> None:
    """
    Prompts the user to select products and quantities to create an order.
    Valid products are added to the shopping list, and the total price is displayed.

    Args:
        store_obj (Store): An instance of the Store class to retrieve products and process the order.

    Raises:
        ValueError: For invalid input or missing products.
        Exception: For other errors during the order process.

    Returns:
        None
    """

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
    except ValueError as error:
        print("Invalid input:", error)
    except Exception as error:
        print(f"Error: {error}")


def display_menu() -> None:
    """Displays the menu options for the user."""
    print("\nWelcome to the Best Buy Store! 🎉")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def main():
    """
    Main function to run the store application.
    """
    best_buy = init()

    try:
        start(best_buy)
    except ValueError as error:
        print("Invalid input:", error)
    except Exception as error:
        print("\nAn unexpected error occurred:")
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
