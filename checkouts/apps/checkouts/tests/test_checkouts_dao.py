# Python imports
# Flask imports
# Third-Party imports
from flask_testing import TestCase
# Project Imports
from apps import create_app, db
from apps.checkouts.exceptions import CheckoutDoesNotExist
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.checkouts import checkouts_dao


class CheckoutDAOTestCase(TestCase):

    def create_app(self):
        app = create_app(env="test")
        return app

    def setUp(self):
        db.session.remove()
        db.drop_all()
        db.create_all()
        db.session.commit()
        self.checkout = CheckoutFactory()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_insert_product(self):
        new_checkout = checkouts_dao.insert_checkout(self.checkout)
        self.assertIsInstance(new_checkout.id, int)

    def test_get_checkout_by_id(self):
        new_checkout = CheckoutFactory()
        new_checkout = checkouts_dao.insert_checkout(new_checkout)
        self.assertIsInstance(new_checkout.id, int)
        checkout_returned = checkouts_dao.get_checkout_by_id(new_checkout.id)
        self.assertEqual(new_checkout, checkout_returned)

    def test_get_checkout_by_id_unknown_checkout(self):
        with self.assertRaises(CheckoutDoesNotExist):
            checkouts_dao.get_checkout_by_id(99999)

    def test_get_checkout_by_checkout_number(self):
        new_checkout = CheckoutFactory()
        new_checkout = checkouts_dao.insert_checkout(new_checkout)
        self.assertIsInstance(new_checkout.id, int)
        checkout_returned = checkouts_dao.get_checkout_by_checkout_number(new_checkout.checkout_number)
        self.assertEqual(new_checkout, checkout_returned)

    def test_get_checkout_by_checkout_number_unknown_checkout(self):
        with self.assertRaises(CheckoutDoesNotExist):
            checkouts_dao.get_checkout_by_checkout_number("99999")
