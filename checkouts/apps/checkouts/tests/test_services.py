# Python imports
# Flask imports
# Third-Party imports
import factory
from flask_testing import TestCase
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.products.tests.mocks import ProductFactory
from apps.checkouts import services
from apps.products import product_dao
from apps import create_app, db


class CheckoutServicesTestCase(TestCase):

    def create_app(self):
        app = create_app(env="test")
        return app

    def setUp(self):
        db.session.remove()
        db.drop_all()
        db.create_all()
        db.session.commit()
        self.checkout = CheckoutFactory()
        self.product = ProductFactory()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def tearDown(self):
        self.checkout.purchases.clear()

    def test_scan_new_purchase_item(self):
        quantity = factory.Faker("pyint")
        self.checkout = services.scan_new_purchase_item(
            checkout=self.checkout,
            product=self.product,
            quantity=quantity
        )
        self.assertEqual(len(self.checkout.purchases), 1)
        self.assertEqual(self.checkout.purchases[0].checkout, self.checkout)
        self.assertEqual(self.checkout.purchases[0].product, self.product)
        self.assertEqual(self.checkout.purchases[0].quantity, quantity)

    def test_generate_new_checkout_number(self):
        checkout_number_one = services.generate_new_checkout_number()
        checkout_number_two = services.generate_new_checkout_number()
        self.assertIsInstance(checkout_number_one, str)
        self.assertIsInstance(checkout_number_two, str)
        self.assertNotEqual(checkout_number_one, checkout_number_two)

    def test_scan_checkout_cart(self):
        self.assertEqual(len(self.checkout.purchases), 0)
        self.product = product_dao.insert_product(product=self.product)
        cart = [{'quantity': 2, 'product': self.product.id}, ]
        self.checkout = services.scan_checkout_cart(checkout=self.checkout, cart=cart)
        self.assertEqual(len(self.checkout.purchases), 1)
        self.assertEqual(self.checkout.purchases[0].checkout, self.checkout)
        self.assertEqual(self.checkout.purchases[0].product, self.product)
        self.assertEqual(self.checkout.purchases[0].quantity, 2)

    def test_create_new_checkout(self):
        self.product = product_dao.insert_product(product=self.product)
        cart = [{'quantity': 2, 'product': self.product.id}, ]
        new_checkout = services.create_new_checkout(cart=cart)
        self.assertIsInstance(new_checkout.id, int)
        self.assertEqual(len(new_checkout.purchases), 1)
        self.assertEqual(new_checkout.purchases[0].checkout, new_checkout)
        self.assertEqual(new_checkout.purchases[0].product, self.product)
        self.assertEqual(new_checkout.purchases[0].quantity, 2)
