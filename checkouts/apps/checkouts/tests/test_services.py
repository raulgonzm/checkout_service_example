# Python imports
import unittest
# Flask imports
# Third-Party imports
import factory
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.models import PurchaseItem
from apps.checkouts import services


class CheckoutServicesTestCase(unittest.TestCase):

    def setUp(self):
        self.checkout = CheckoutFactory()
        self.product = ProductFactory()

    def tearDown(self):
        self.checkout.purchases.clear()

    def test_create_new_purchase_item(self):
        quantity = factory.Faker("pyint")
        new_purchase_item = services._create_new_purchase_item(
            product=self.product,
            quantity=quantity
        )
        self.assertIsInstance(new_purchase_item, PurchaseItem)
        self.assertEqual(new_purchase_item.product, self.product)
        self.assertEqual(new_purchase_item.quantity, quantity)

    def test_scan_new_purchase_item(self):
        quantity = factory.Faker("pyint")
        self.checkout = services.scan_new_purchase_item(
            checkout=self.checkout,
            product=self.product,
            quantity=quantity
        )
        self.assertEqual(len(self.checkout.purchases), 1)
        self.assertEqual(self.checkout.purchases[0].checkout, self.checkout)
        self.assertEqual(self.checkout.purchases[0].product, self.product)
        self.assertEqual(self.checkout.purchases[0].quantity, quantity)

