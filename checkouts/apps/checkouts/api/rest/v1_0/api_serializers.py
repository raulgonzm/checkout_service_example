# Python imports
# Flask imports
# Third-Party imports
from marshmallow import Schema, fields
# Project Imports


class CheckoutCreateSerializer(Schema):
    product = fields.Integer(load_only=True, allow_none=False)
    quantity = fields.Integer(load_only=True, allow_none=False)


class CheckoutDetailSerializer(Schema):
    id = fields.Integer(dump_only=True)
    checkout_number = fields.String(dump_only=True)
    price = fields.Decimal(dump_only=True, places=2, as_string=True)
    discount = fields.Decimal(dump_only=True, places=2, as_string=True)
    total = fields.Decimal(dump_only=True, places=2, as_string=True)
