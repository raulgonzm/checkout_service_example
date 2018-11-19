# Python imports
# Flask imports
# Third-Party imports
from sqlalchemy.sql import func
# Project Imports
from apps import db
from apps.purchase_items.models import PurchaseItem


class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    checkout_number = db.Column(db.String, nullable=False, unique=True)
    purchases = db.relationship(PurchaseItem, backref='checkout', lazy=True)

    def __repr__(self):
        return f"<Checkout-{self.id}>"
