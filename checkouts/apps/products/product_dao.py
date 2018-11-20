# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.models import Product
from apps import CheckoutApp


def insert_product(product):
    CheckoutApp.db.session.add(product)
    CheckoutApp.db.session.commit()
    return product


def get_all_products():
    return Product.query.order_by(Product.name).all()
