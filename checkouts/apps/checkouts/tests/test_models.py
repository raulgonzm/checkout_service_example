# Python imports
import unittest
from decimal import Decimal
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory


class CheckoutModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.checkout = CheckoutFactory()

    def test_repr_method(self):
        self.assertEqual(
            self.checkout.__repr__(),
            f"<Checkout-{self.checkout.id}>"
        )

    def test_calc_price_empty_purchase(self):
        empty_checkout = CheckoutFactory()
        checkout_price = empty_checkout.calc_price()
        self.assertIsInstance(checkout_price, Decimal)
        self.assertEqual(checkout_price, 0)

    def test_calc_price_only_one_product(self):
        product = ProductFactory()
        checkout = CheckoutFactory()
        purchase_item = PurchaseItemFactory(
            product=product,
            checkout=checkout
        )
        product.purchases.append(purchase_item)
        checkout.purchases.append(purchase_item)
        checkout_price = checkout.calc_price()
        self.assertIsInstance(checkout_price, Decimal)
        self.assertNotEqual(checkout_price, 0)
        self.assertEqual(
            checkout_price,
            product.price * purchase_item.quantity
        )

    def test_calc_price_multiple_products(self):
        product_one = ProductFactory()
        product_two = ProductFactory()
        checkout = CheckoutFactory()
        purchase_item_one = PurchaseItemFactory(
            product=product_one,
            checkout=checkout
        )
        purchase_item_two = PurchaseItemFactory(
            product=product_two,
            checkout=checkout
        )
        product_one.purchases.append(purchase_item_one)
        checkout.purchases.append(purchase_item_one)
        product_two.purchases.append(purchase_item_two)
        checkout.purchases.append(purchase_item_two)
        checkout_price = checkout.calc_price()
        self.assertIsInstance(checkout_price, Decimal)

        self.assertNotEqual(checkout_price, 0)
        self.assertEqual(
            checkout_price,
            (product_one.price * purchase_item_one.quantity) + (product_two.price * purchase_item_two.quantity)
        )

    def test_total_property(self):
        product = ProductFactory()
        checkout = CheckoutFactory()
        purchase_item = PurchaseItemFactory(
            product=product,
            checkout=checkout
        )
        product.purchases.append(purchase_item)
        checkout.purchases.append(purchase_item)
        checkout_total = checkout.total
        self.assertIsInstance(checkout_total, Decimal)
        self.assertNotEqual(checkout_total, 0)
        self.assertEqual(
            checkout_total
            ,
            product.price * purchase_item.quantity
        )


if __name__ == '__main__':
    unittest.main()
