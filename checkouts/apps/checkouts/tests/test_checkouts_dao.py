# Python imports
# Flask imports
# Third-Party imports
from flask_testing import TestCase
# Project Imports
from apps import create_app, db
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
