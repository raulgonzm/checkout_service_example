# Python imports
import unittest
# Flask imports
# Third-Party imports
import factory
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.models import PurchaseItem
from apps.purchase_items.tests.mocks import PurchaseItemFactory
from apps.purchase_items import services


class PurchaseItemServicesTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.checkout = CheckoutFactory()
        self.purchase_item = PurchaseItemFactory(
            product=self.product,
            checkout=self.checkout
        )
        self.product.purchases.append(self.purchase_item)
        self.checkout.purchases.append(self.purchase_item)

    def test_create_new_purchase_item(self):
        quantity = factory.Faker("pyint").generate({})
        new_purchase_item = services.create_new_purchase_item(
            product=self.product,
            quantity=quantity
        )
        self.assertIsInstance(new_purchase_item, PurchaseItem)
        self.assertEqual(new_purchase_item.product, self.product)
        self.assertEqual(new_purchase_item.quantity, quantity)
