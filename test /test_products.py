import pytest
import products
import promotions


def test_create_product():
    """ Test that creating a normal product works   """
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_invalid_details():
    """Test that creating a product with invalid details raises an exception."""
    with pytest.raises(ValueError):
        products.Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):
        products.Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_when_quantity_is_zero():
    """Test that a product becomes inactive when quantity reaches zero."""
    product = products.Product("MacBook Air M2", price=1450, quantity=1)
    product.set_quantity(0)
    assert product.is_active() is False


def test_product_purchase():
    """Test that purchasing a product modifies the quantity and returns the correct total price."""
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(5)
    assert total_price == 1450 * 5
    assert product.quantity == 95


def test_product_with_promotions():
    """Test that promotions are applied correctly."""
    product = products.Product("MacBook Air M2", price=100, quantity=10)
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    product.set_promotion(second_half_price)

    total_price = product.buy(4)  # 2 at full price, 2 at half price
    assert total_price == pytest.approx((2 * 100) + (2 * 50))  # 300


def test_product_with_promotion_ThirdOneFree():
    """Test that promotions are applied correctly."""
    product = products.Product("MacBook Air M2", price=100, quantity=10)
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    product.set_promotion(third_one_free)

    total_price = product.buy(3)  # 2 paid, 1 free
    assert total_price == pytest.approx(2 * 100)  # 200


def test_product_purchase_with_promotion_thirty_percent():
    """Test that purchasing a product modifies the quantity and returns the correct total price."""
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    product.set_promotion(thirty_percent)
    total_price = product.buy(1)
    assert total_price == pytest.approx(1450 - (1450 * 30) / 100)
    assert product.quantity == 99


def test_product_purchase_with_promotion_thirty_percent_and_SecondHalfPrice():
    """Test that purchasing a product modifies the quantity and returns the correct total price."""
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    second_half_price = promotions.SecondHalfPrice("Second Half price!")

    product.set_promotion(thirty_percent)
    product.set_promotion(second_half_price)
    total_price = product.buy(3)
    assert total_price == pytest.approx((1450 * 3) - (725 + (3 * (1450 * 30) / 100)))
    assert product.quantity == 97


def test_buying_more_than_available_quantity_raises_exception():
    """Test that buying a larger quantity than exists raises an exception."""
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(200)
