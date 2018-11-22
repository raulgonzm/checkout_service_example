# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.api.rest.v1_0 import api_serializers
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory


class CheckoutAPISerializersTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.checkout = CheckoutFactory()
        self.purchase_item = PurchaseItemFactory(
            product=self.product,
            checkout=self.checkout
        )
        self.product.purchases.append(self.purchase_item)
        self.checkout.purchases.append(self.purchase_item)

    def test_checkout_create_serialization(self):
        serializer = api_serializers.CheckoutCreateSerializer(many=True)
        data, errors = serializer.load([
            {'product': 1, 'quantity': 2},
            {'product': 2, 'quantity': 1},
        ])
        self.assertIsInstance(data, list)
        self.assertEqual(data[0]['product'], 1)
        self.assertEqual(data[0]['quantity'], 2)
        self.assertEqual(data[1]['product'], 2)
        self.assertEqual(data[1]['quantity'], 1)

    def test_checkout_detail_serialization(self):
        serializer_class = api_serializers.CheckoutDetailSerializer()
        result = serializer_class.dump(self.checkout)
        self.assertEqual(result.data['id'], self.checkout.id)
        self.assertEqual(result.data['checkout_number'], self.checkout.checkout_number)
        self.assertEqual(result.data['price'], str(round(self.checkout.price, 2)))
        self.assertEqual(result.data['discount'], str(round(self.checkout.discount, 2)))
        self.assertEqual(result.data['total'], str(round(self.checkout.total, 2)))
        self.assertIn("purchases", result.data)
