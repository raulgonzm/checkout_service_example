# Python imports
import unittest
import json
# Flask imports
# Third-Party imports
from flask_restful import Api
# Project Imports
from apps import create_app, db
from apps.checkouts.api.rest.v1_0.api_urls import CheckoutAPIUrls
from apps.checkouts.tests.mocks import CheckoutFactory
from apps.products import product_dao
from apps.products.tests.mocks import ProductFactory
from apps.purchase_items.tests.mocks import PurchaseItemFactory
from apps.urls import Router
from apps.checkouts import checkouts_dao


class CheckoutAPITestCase(unittest.TestCase):

    def create_app(self):
        self.app = create_app(env="test")
        return self.app

    def setUp(self):
        self.app = self.create_app()
        Router(Api(self.app))
        db.session.remove()
        db.drop_all()
        db.create_all()
        db.session.commit()
        self.client = self.app.test_client()
        self.product = ProductFactory()
        self.checkout = CheckoutFactory()
        self.purchase_item = PurchaseItemFactory(
            product=self.product,
            checkout=self.checkout
        )
        self.product.purchases.append(self.purchase_item)
        self.checkout.purchases.append(self.purchase_item)
        self.product = product_dao.insert_product(self.product)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_checkout(self):
        data = [
            {
                "product": self.product.id,
                "quantity": 1400
            },
        ]
        response = self.client.post(
            CheckoutAPIUrls.checkout_create,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_create_checkout_unknown_product(self):
        data = [
            {
                "product": 99999,
                "quantity": 1400
            },
        ]
        response = self.client.post(
            CheckoutAPIUrls.checkout_create,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_create_checkout_product_id_none(self):
        data = [
            {
                "product": None,
                "quantity": 1400
            },
        ]
        response = self.client.post(
            CheckoutAPIUrls.checkout_create,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_create_checkout_product_id_zero(self):
        data = [
            {
                "product": 0,
                "quantity": 1400
            },
        ]
        response = self.client.post(
            CheckoutAPIUrls.checkout_create,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_create_checkout_product_id_type_error(self):
        data = [
            {
                "product": "a",
                "quantity": 1400
            },
        ]
        response = self.client.post(
            CheckoutAPIUrls.checkout_create,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_create_checkout_product_quantity_type_error(self):
        data = [
            {
                "product": self.product.id,
                "quantity": "a"
            },
        ]
        response = self.client.post(
            CheckoutAPIUrls.checkout_create,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_create_checkout_empty_request(self):
        data = [{}]
        response = self.client.post(
            CheckoutAPIUrls.checkout_create,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_create_checkout_empty_list_request(self):
        data = []
        response = self.client.post(
            CheckoutAPIUrls.checkout_create,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_detail_checkout(self):
        self.checkout = checkouts_dao.insert_checkout(checkout=self.checkout)
        response = self.client.get(
            f"/api/rest/v1_0/checkouts/{self.checkout.id}/",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_detail_checkout_unknown_checkout(self):
        self.checkout = checkouts_dao.insert_checkout(checkout=self.checkout)
        response = self.client.get(
            f"/api/rest/v1_0/checkouts/99999/",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_detail_checkout_unknown_checkout_type_error(self):
        self.checkout = checkouts_dao.insert_checkout(checkout=self.checkout)
        response = self.client.get(
            f"/api/rest/v1_0/checkouts/a/",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
