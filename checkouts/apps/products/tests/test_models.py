# Python imports
import unittest
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


if __name__ == '__main__':
    unittest.main()
