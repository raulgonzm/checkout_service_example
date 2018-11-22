# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps import db
from apps.checkouts.models import Checkout


def insert_checkout(checkout):
    db.session.add(checkout)
    db.session.commit()
    return checkout


def get_checkout_by_id(checkout_id):
    return Checkout.query.get(checkout_id)
