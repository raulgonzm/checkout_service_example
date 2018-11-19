# Python imports
import unittest
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
            product_id=self.product.id,
            checkout_id=self.checkout.id
        )

    def test_repr_method(self):
        self.assertEqual(
            self.purchase_item.__repr__(),
            f"<PurchaseItem-{self.purchase_item.id}>"
        )
