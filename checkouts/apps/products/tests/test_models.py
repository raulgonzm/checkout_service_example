# Python imports
import unittest
from decimal import Decimal
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.tests.mocks import ProductFactory


class ProductModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()

    def test_repr_method(self):
        self.assertEqual(
            self.product.__repr__(),
            f"<Product-{self.product.code}>"
        )

    def test_product_price(self):
        self.assertIsInstance(self.product.price, Decimal)


if __name__ == '__main__':
    unittest.main()
