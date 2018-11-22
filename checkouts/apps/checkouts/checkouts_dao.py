# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps import db


def insert_checkout(checkout):
    db.session.add(checkout)
    db.session.commit()
    return checkout
