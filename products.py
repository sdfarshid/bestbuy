class Product:
    """
    Represents a product in the store.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Constructor to initialize the product.
        :param name: Name of the product (str)
        :param price: Price of the product (float)
        :param quantity: Quantity of the product (int)
        """
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
        """
        Getter for quantity.
        :return: Quantity (float)
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Setter for quantity. Deactivates the product if quantity is 0.
        :param quantity: New quantity (int)
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        self.check_balance()
        return None

    def is_active(self) -> bool:
        """
        Checks if the product is active.
        :return: True if active, False otherwise (bool)
        """
        return self.active

    def activate(self) -> None:
        """
        Activates the product.
        """
        self.active = True
        return None

    def deactivate(self) -> None:
        """
        Activates the product.
        """
        self.active = False
        return None

    def check_balance(self) -> None:
        """
        Check quantity of product be more than 0  And Change the status
        """
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def show(self) -> str:
        """
        Displays the product details.
        :return: A string representation of the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Updates the product's quantity and returns the total price.
        :param quantity: Quantity to purchase (int)
        :return: Total price (float)
        """
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if quantity > self.quantity:
            raise Exception("Insufficient quantity available.")

        self.quantity -= quantity

        self.check_balance()

        return self.price * quantity