# Python imports
import unittest
from decimal import Decimal
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory


class PurchaseItemModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.checkout = CheckoutFactory()
        self.purchase_item = PurchaseItemFactory(
            product=self.product,
            checkout=self.checkout
        )
        self.product.purchase.append(self.purchase_item)
        self.checkout.purchase.append(self.purchase_item)

    def test_repr_method(self):
        self.assertEqual(
            self.purchase_item.__repr__(),
            f"<PurchaseItem-{self.purchase_item.id}>"
        )

    def test_price_calc(self):
        purchase_price = self.purchase_item.price
        self.assertIsInstance(purchase_price, Decimal)
        self.assertEqual(
            purchase_price,
            self.purchase_item.quantity * self.product.price
        )
