# Python imports
# Flask imports
# Third-Party imports
from flask_testing import TestCase
# Project Imports
from apps import create_app, db
from apps.products.exceptions import ProductDoesNotExist
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

    def test_get_product_by_id(self):
        new_product = ProductFactory()
        new_product = product_dao.insert_product(new_product)
        self.assertIsInstance(new_product.id, int)
        product_returned = product_dao.get_product_by_id(new_product.id)
        self.assertEqual(new_product, product_returned)

    def test_get_product_by_id_unknown_product(self):
        with self.assertRaises(ProductDoesNotExist):
            product_dao.get_product_by_id(9999)

    def test_get_product_by_code(self):
        new_product = ProductFactory()
        new_product = product_dao.insert_product(new_product)
        self.assertIsInstance(new_product.id, int)
        product_returned = product_dao.get_product_by_code(new_product.code)
        self.assertEqual(new_product, product_returned)

    def test_get_product_by_code_unknown_product(self):
        with self.assertRaises(ProductDoesNotExist):
            product_dao.get_product_by_code(9999)

    def test_clean_products(self):
        new_product = ProductFactory()
        new_product = product_dao.insert_product(new_product)
        self.assertIsInstance(new_product.id, int)
        self.assertEqual(
            len(Product.query.all()),
            2
        )
        product_dao.clean_products()
        self.assertEqual(
            len(Product.query.all()),
            0
        )

