# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps import db
from apps.checkouts.models import Checkout
from apps.checkouts.exceptions import CheckoutDoesNotExist


def insert_checkout(checkout):
    db.session.add(checkout)
    db.session.commit()
    return checkout


def get_checkout_by_id(checkout_id):
    checkout = Checkout.query.get(checkout_id)
    if checkout:
        return checkout
    raise CheckoutDoesNotExist(checkout_id=checkout_id)


def get_checkout_by_checkout_number(checkout_number):
    checkout = Checkout.query.filter_by(checkout_number=checkout_number).first()
    if checkout:
        return checkout
    raise CheckoutDoesNotExist(checkout_id=checkout_number)
