import promotions


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

        self._name = name
        self._price = price
        self._quantity = quantity
        self.active = True
        self.promotions = []

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @property
    def quantity(self) -> float:
        """
        Getter for quantity.
        :return: Quantity (float)
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value
        self.check_balance()

    def set_promotion(self, promotion: promotions.Promotion) -> None:
        """Add a promotion to the product."""
        if promotion not in self.promotions:
            self.promotions.append(promotion)

    def remove_promotion(self, promotion: promotions.Promotion) -> None:
        """Remove a promotion from the product."""
        if promotion in self.promotions:
            self.promotions.remove(promotion)

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
        """Show product details including promotions."""
        promo_info = ""
        if self.promotions:
            promo_info = " (Promotions: " + ", ".join(promo.name for promo in self.promotions) + ")"

        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity} {promo_info}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Updates the product's quantity and returns the total price.
        :param quantity: Quantity to purchase (int)
        :return: Total price (float)
        """

        self._validate_purchase(quantity)

        base_price = self.price * quantity

        total_discount = self.__apply_discounts(base_price, quantity)

        total_price = base_price - total_discount

        self._update_quantity(quantity)

        self.check_balance()

        return total_price

    def _validate_purchase(self, quantity: int) -> None:
        """
        Validates the purchase. Can be overridden by subclasses for custom validation.
        :param quantity: Quantity to purchase (int)
        """
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available.")

    def _update_quantity(self, quantity: int) -> None:
        self.quantity -= quantity

    def __apply_discounts(self, base_price: float, quantity: int) -> float:
        """
            Calculate each Promotion Discount and set to the Base price
        :param base_price: base_price of the product (float)
        :param quantity: quantity of the product (int)
        """
        total_discount = 0
        for promotion in self.promotions:
            promotion_price = promotion.apply_promotion(self, quantity)
            discounted_price = base_price - promotion_price
            total_discount += discounted_price
        return total_discount


class NonStockedProduct(Product):
    """Represents a product with no physical stock, such as a license."""

    def __init__(self, name, price):
        """Initialize the NonStockedProduct with a fixed quantity of 0."""
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """Override set_quantity to prevent changes to quantity."""
        raise ValueError("Quantity cannot be changed for NonStockedProduct.")

    def _validate_purchase(self, quantity: int) -> None:
        """
        Validates the purchase. Can be overridden by subclasses for custom validation.
        :param quantity: Quantity to purchase (int)
        """
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

    def _update_quantity(self, quantity):
        self.quantity = 0


    def show(self) -> str:
        """Show product details with special characteristics."""
        return f"{super().show()} (Non-Stocked Product)"


class LimitedProduct(Product):
    """Represents a product with a purchase limit."""

    def __init__(self, name, price, quantity, maximum):
        """Initialize the LimitedProduct with a max purchase limit."""
        super().__init__(name, price, quantity)
        self.max_per_order = maximum

    def _validate_purchase(self, quantity: int) -> None:
        """Validate the purchase against maximum allowed per order."""
        super()._validate_purchase(quantity)
        if quantity > self.max_per_order:
            raise ValueError(
                f"Cannot purchase more than {self.max_per_order} units of {self.name} in a single order."
            )

    def show(self) -> str:
        """Show product details with special characteristics."""
        return f"{super().show()} (Limited to {self.max_per_order} per order)"
