'''Contains all tests for the product class'''
import pytest
from products import Product
from promotions import PercentageDiscount, SecondItemHalfPrice, BuyTwoGetOneFree

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

def test_percentage_discount():
    product = Product("Widget", 10.00, 100)
    promotion = PercentageDiscount("20% off", 20)
    product.set_promotion(promotion)
    assert product.buy(5) == 40.00  # 20% off 50

def test_second_item_half_price():
    product = Product("Gadget", 20.00, 100)
    promotion = SecondItemHalfPrice("Second item half price")
    product.set_promotion(promotion)
    assert product.buy(3) == 50.00  # 2 full price, 1 half price

def test_buy_two_get_one_free():
    product = Product("Thingamajig", 15.00, 100)
    promotion = BuyTwoGetOneFree("Buy 2, get 1 free")
    product.set_promotion(promotion)
    assert product.buy(3) == 30.00  # 2 full price, 1 free



pytest.main()

