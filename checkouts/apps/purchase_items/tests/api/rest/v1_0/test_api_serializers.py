# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.purchase_items.api.rest.v1_0 import api_serializers
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory


class PurchaseItemAPISerializersTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.checkout = CheckoutFactory()
        self.purchase_item = PurchaseItemFactory(
            product=self.product,
            checkout=self.checkout
        )
        self.product.purchases.append(self.purchase_item)
        self.checkout.purchases.append(self.purchase_item)

    def test_checkout_detail_serialization(self):
        serializer_class = api_serializers.PurchaseItemSerializer()
        result = serializer_class.dump(self.purchase_item)
        self.assertEqual(result.data['quantity'], self.purchase_item.quantity)
        self.assertEqual(result.data['price'], str(round(self.purchase_item.price, 2)))
        self.assertIn("product", result.data)
