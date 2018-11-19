# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Product-{self.code}>"
