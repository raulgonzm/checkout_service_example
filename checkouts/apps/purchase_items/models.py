# Python imports
# Flask imports
# Third-Party imports
from sqlalchemy.sql import func
# Project Imports
from apps import db


class PurchaseItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f"<PurchaseItem-{self.id}>"

