# Python imports
import unittest
from decimal import Decimal
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.pricing_rules.services import get_current_discounts
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory


class CheckoutModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.checkout = CheckoutFactory()

    def set_up_test_data_env(self, num_products):
        products = []
        purchases = []
        checkout = CheckoutFactory()
        for item in range(0, num_products):
            product = ProductFactory()
            purchase_item = PurchaseItemFactory(
                product=product,
                checkout=checkout
            )
            product.purchases.append(purchase_item)
            checkout.purchases.append(purchase_item)
            products.append(product)
            purchases.append(purchase_item)
        return products, checkout, purchases

    def calc_checkout_price(self, checkout):
        current_discounts = get_current_discounts()
        total_price = Decimal(0.0)
        for item in checkout.purchases:
            discounted = [item.price]
            for discount in current_discounts:
                discounted.append(discount.apply_to_price_purchase(purchase=item))
            total_price += min(discounted)
        return total_price

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
        products, checkout, puchases = self.set_up_test_data_env(num_products=1)
        checkout_price = checkout.calc_price()
        self.assertIsInstance(checkout_price, Decimal)
        self.assertNotEqual(checkout_price, 0)
        self.assertEqual(
            checkout_price,
            self.calc_checkout_price(checkout=checkout)
        )

    def test_calc_price_multiple_products(self):
        products, checkout, puchases = self.set_up_test_data_env(num_products=10)
        checkout_price = checkout.calc_price()
        self.assertIsInstance(checkout_price, Decimal)
        self.assertNotEqual(checkout_price, 0)
        self.assertEqual(
            checkout_price,
            self.calc_checkout_price(checkout=checkout)
        )

    def test_total_property(self):
        products, checkout, puchases = self.set_up_test_data_env(num_products=5)
        checkout_total = checkout.total
        self.assertIsInstance(checkout_total, Decimal)
        self.assertNotEqual(checkout_total, 0)
        self.assertEqual(
            checkout_total,
            self.calc_checkout_price(checkout=checkout)
        )

    def test_scan(self):
        self.assertEqual(len(self.checkout.purchases), 0)
        product_one = ProductFactory()
        purchase_item_one = PurchaseItemFactory(
            product=product_one,
            checkout=self.checkout
        )
        self.checkout.scan(purchase_item=purchase_item_one)
        self.assertEqual(len(self.checkout.purchases), 1)
        product_two = ProductFactory()
        purchase_item_two = PurchaseItemFactory(
            product=product_two,
            checkout=self.checkout
        )
        self.checkout.scan(purchase_item=purchase_item_two)
        self.assertEqual(len(self.checkout.purchases), 2)


if __name__ == '__main__':
    unittest.main()
