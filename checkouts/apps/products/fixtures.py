# Python imports
import json
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.models import Product
from apps.products import product_dao


def load_product_fixture():
    product_fixture_file = "/checkouts/apps/products/fixtures/products.json"
    with open(product_fixture_file) as file:
        data = json.load(file)
        product_dao.clean_products()
        for product_item in data:
            product = Product(
                code=product_item['code'],
                name=product_item['name'],
                db_price=product_item['db_price']
            )
            product_dao.insert_product(product=product)
