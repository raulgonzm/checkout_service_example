# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.fixtures import load_product_fixture


def init_db(db):
    db.create_all()
    db.session.commit()


def load_fixtures(db):
    load_product_fixture()
