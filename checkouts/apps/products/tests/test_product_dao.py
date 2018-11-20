# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.models import Product
from apps.products.tests.mocks import ProductFactory
from apps.products import product_dao
from apps import CheckoutApp


class ProductModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.app, self.db = CheckoutApp(env="test")
        self.db.session.remove()
        self.db.drop_all()
        self.db.create_all()
        self.db.session.commit()
        self.product = ProductFactory()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_get_all_products(self):
        products = product_dao.get_all_products()
        self.assertEqual(len(products), 1)
        self.assertIsInstance(products[0], Product)

    def test_insert_product(self):
        new_product = ProductFactory()
        new_product = product_dao.insert_product(new_product)
        self.assertIsInstance(new_product.id, int)
        products = product_dao.get_all_products()
        self.assertEqual(len(products), 2)

