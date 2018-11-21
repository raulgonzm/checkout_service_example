# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps import db
from apps.products.models import Product


def insert_product(product):
    db.session.add(product)
    db.session.commit()
    return product


def get_all_products():
    return Product.query.order_by(Product.name).all()
