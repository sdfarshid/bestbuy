import pytest
import products


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


def test_buying_more_than_available_quantity_raises_exception():
    """Test that buying a larger quantity than exists raises an exception."""
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(200)
