# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.api.rest.v1_0.api_serializers import ProductSerializer
from apps.products.tests.mocks import ProductFactory


class ProductSerializersTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()

    def test_product_serialization(self):
        serializer_class = ProductSerializer()
        result = serializer_class.dump(self.product)
        self.assertEqual(result.data['code'], self.product.code)
        self.assertEqual(result.data['name'], self.product.name)
        self.assertEqual(result.data['price'], str(round(self.product.price, 2)))
