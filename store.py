from typing import List, Tuple
from products import Product


class Store:
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

    def remove_product(self, product: Product):
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
        return sum(product.get_quantity() for product in self.products)

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


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()
