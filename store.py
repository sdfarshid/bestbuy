from typing import List, Tuple

from Exceptions.InsufficientQuantity import InsufficientQuantity
from products import Product


class Store:
    """
    Represents a store that contains products.
    """

    def __init__(self, products: List[Product]) -> None:
        """
        Constructor for the Store.
        :param products: List of Product instances.
        """
        self.products = products

    def add_product(self, product: Product) -> None:
        """
        Adds a new product to the store.
        :param product: Product instance to be added.
        """
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Removes a product from the store.
        :param product: Product instance to be removed.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.
        :return: Total quantity (int).
        """
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Returns all active products in the store.
        :return: List of active products (List[Product]).
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order for multiple products.
        :param shopping_list: List of tuples (Product, quantity).
        :return: Total price of the order (float).
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"Product '{product.name}' not found in the store.")
            total_price += product.buy(quantity)
        return total_price

    def set_shop_list(self):
        shopping_list = []
        print("\nEnter your order (leave product name empty to finish):")
        while True:
            try:
                product_id = int(input("Please Insert Number of  Product : "))
                all_product = self.get_all_products()
                product = all_product[product_id - 1]
                quantity = int(input("Quantity: "))
                self.check_quantity(product, quantity)
                shopping_list.append((product, quantity))
            except IndexError:
                print(f"Product '{product_id}' not found in the store.")
                break
            except ValueError:
                break
            except InsufficientQuantity as error:
                print(error)

        if len(shopping_list) <=0:
            raise ValueError(f"There is no item in shopping list")

        return shopping_list

    def check_quantity(self, product: Product, quantity: int) -> None:
        try:
            product._validate_purchase(quantity)
        except ValueError as error:
            raise InsufficientQuantity(error)
        except Exception as ExceptionError:
            raise ExceptionError
