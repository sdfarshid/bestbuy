from typing import Union

import products
import promotions
from Exceptions.InsufficientQuantity import InsufficientQuantity
from store import Store


def init() -> Store:
    """
    Initializes the store with default products.
    :return: An instance of Store.
      product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        Product("Google Pixel 7", price=400, quantity=250)
                        ]
    """
    try:
        product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        products.Product("Google Pixel 7", price=500, quantity=250),
                        products.NonStockedProduct("Windows License", price=125),
                        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                        ]

        # Create promotion catalog
        second_half_price = promotions.SecondHalfPrice("Second Half price!")
        third_one_free = promotions.ThirdOneFree("Third One Free!")
        thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

        # Add promotions to products
        product_list[0].set_promotion(second_half_price)
        product_list[0].set_promotion(thirty_percent)
        product_list[2].set_promotion(thirty_percent)
        product_list[1].set_promotion(third_one_free)
        product_list[3].set_promotion(thirty_percent)

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
            show_products(store_obj)
        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")
        elif choice == "3":
            show_products(store_obj)
            set_order(store_obj)
        elif choice == "4":
            print("\nThank you for visiting Best Buy! Goodbye! 👋")
            break
        else:
            print("\nInvalid choice. Please try again.")
        input("Press Enter to continue ")


def show_products(store_obj):
    print("\nProducts in Store:")
    print("\n--------------")
    for index, product in enumerate(store_obj.get_all_products(), start=1):
        print(f"{index}. {product.show()}")


def set_order(store_obj: Store) -> Union[Exception, None]:
    """
    Prompts the user to set an order and processes it.
    :param store_obj: The store object containing all products.
    :return: Exception , None
    """
    try:
        shopping_list = store_obj.set_shop_list()
        total_price = store_obj.order(shopping_list)
        print(f"\nOrder successful! Total price: ${total_price:.2f}")
        return None

    except ValueError as error:
        print("Invalid input:", error)
    except RuntimeError as error:
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
    try:
        start(init())
    except ValueError as error:
        print("Invalid input:", error)
    except RuntimeError as error:
        print(f"An unexpected error : {error}")


if __name__ == "__main__":
    main()
