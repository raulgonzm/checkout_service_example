# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps import db
from apps.products.models import Product
from apps.products.exceptions import ProductDoesNotExist


def insert_product(product):
    db.session.add(product)
    db.session.commit()
    return product


def get_all_products():
    return Product.query.order_by(Product.name).all()


def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if product:
        return product
    raise ProductDoesNotExist(product_id=product_id)


def get_product_by_code(product_code):
    product = Product.query.filter_by(code=product_code).first()
    if product:
        return product
    raise ProductDoesNotExist(product_id=product_code)


def clean_products():
    Product.query.delete()
