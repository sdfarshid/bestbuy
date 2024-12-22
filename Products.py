class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity: int):

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        self.check_balance()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def check_balance(self) -> None:
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if quantity > self.quantity:
            raise Exception("Insufficient quantity available.")

        self.quantity -= quantity

        self.check_balance()

        return self.price * quantity


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print("--------")
    print(bose.buy(50))
    print("Mac Data")
    print(mac.buy(100))
    print(mac.is_active())

    print("--------")
    print("bose-show")
    print(bose.show())
    print("Mac-show")
    print(mac.show())

    print("--------")
    print("bose-quantity")
    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
