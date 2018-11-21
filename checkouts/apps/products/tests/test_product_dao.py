# Python imports
# Flask imports
# Third-Party imports
from flask_testing import TestCase
# Project Imports
from apps import create_app, db
from apps.products.models import Product
from apps.products.tests.mocks import ProductFactory
from apps.products import product_dao


class ProductDAOTestCase(TestCase):

    def create_app(self):
        app = create_app(env="test")
        return app

    def setUp(self):
        db.session.remove()
        db.drop_all()
        db.create_all()
        db.session.commit()
        self.product = ProductFactory()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

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

