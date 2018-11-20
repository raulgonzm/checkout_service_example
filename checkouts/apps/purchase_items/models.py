# Python imports
# Flask imports
# Third-Party imports
from sqlalchemy.sql import func
# Project Imports
from apps import CheckoutApp

db = CheckoutApp.db


class PurchaseItem(db.Model):
    __tablename__ = 'purchase_items'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    checkout_id = db.Column(db.Integer, db.ForeignKey('checkouts.id'), nullable=True)

    def __repr__(self):
        return f"<PurchaseItem-{self.id}>"

    @property
    def price(self):
        return self.product.price * self.quantity

