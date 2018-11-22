# Python imports
import unittest
# Flask imports
# Third-Party imports
from flask_restful import Api
# Project Imports
from apps import create_app, db
from apps.products.api.rest.v1_0.api_urls import ProductAPIUrls
from apps.products.tests.mocks import ProductFactory
from apps.urls import Router


class ProductAPITestCase(unittest.TestCase):

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

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_product_list(self):
        response = self.client.get(
            ProductAPIUrls.product_list,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
