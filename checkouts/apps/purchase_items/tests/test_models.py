# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory


class PurchaseItemModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.purchase_item = PurchaseItemFactory(product_id=self.product.id)

    def test_repr_method(self):
        self.assertEqual(
            self.purchase_item.__repr__(),
            f"<PurchaseItem-{self.purchase_item.id}>"
        )
