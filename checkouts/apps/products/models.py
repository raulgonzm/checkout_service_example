# Python imports
from decimal import Decimal
# Flask imports
# Third-Party imports
from sqlalchemy.sql import func
# Project Imports
from apps import db
from apps.purchase_items.models import PurchaseItem


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    code = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    db_price = db.Column(db.Float, nullable=False)
    purchases = db.relationship(PurchaseItem, backref='product', lazy=True)

    def __repr__(self):
        return f"<Product-{self.code}>"

    @property
    def price(self):
        return Decimal(self.db_price)
