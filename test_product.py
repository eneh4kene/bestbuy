'''Contains all tests for the product class'''
import pytest
from products import Product

def test_create_normal_product():
    product = Product("Widget", 10.00, 100)
    assert product.name == "Widget"
    assert product.price == 10.00
    assert product.quantity == 100
    assert product.is_active()

def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("Widget", -10.00, 100)  # Invalid price, assuming ValueError is raised on negative

    with pytest.raises(ValueError):
        Product("", 10.00, 100)  # Invalid name, assuming ValueError is raised on empty

    with pytest.raises(ValueError):
        Product("Widget", 10.00, -100)

def test_product_becomes_inactive_at_zero_quantity():
    product = Product("Gadget", 20.00, 1)
    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()

def test_purchase_modifies_quantity():
    product = Product("Gadget", 20.00, 50)
    product.buy(30)
    assert product.quantity == 20

def test_buying_more_than_exists_raises_exception():
    product = Product("Gadget", 20.00, 10)
    with pytest.raises(Exception):  # Assuming an Exception is raised for over-purchasing
        product.buy(20)


pytest.main()

