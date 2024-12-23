from typing import List, Tuple
from Products import Products


class Store:
    def __init__(self, products: List[Products]) -> None:
        self.products = products

    def add_product(self, product: Products) -> None:
        self.products.append(product)

    def remove_product(self, product: Products):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Products]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Products, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"Product '{product.name}' not found in the store.")
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [Products("MacBook Air M2", price=1450, quantity=100),
                    Products("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Products("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()