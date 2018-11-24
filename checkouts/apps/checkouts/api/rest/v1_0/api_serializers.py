# Python imports
# Flask imports
# Third-Party imports
from marshmallow import Schema, fields
# Project Imports
from apps.purchase_items.api.rest.v1_0.api_serializers import PurchaseItemSerializer


class CheckoutCreateSerializer(Schema):
    product = fields.String(load_only=True, allow_none=False)
    quantity = fields.Integer(load_only=True, allow_none=False)


class CheckoutDetailSerializer(Schema):
    id = fields.Integer(dump_only=True)
    checkout_number = fields.String(dump_only=True)
    price = fields.Decimal(dump_only=True, places=2, as_string=True)
    discount = fields.Decimal(dump_only=True, places=2, as_string=True)
    total = fields.Decimal(dump_only=True, places=2, as_string=True)
    purchases = fields.Nested(PurchaseItemSerializer, dump_only=True, many=True)
