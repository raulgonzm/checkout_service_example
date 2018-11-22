# Python imports
# Flask imports
# Third-Party imports
from marshmallow import Schema, fields
# Project Imports
from apps.products.api.rest.v1_0.api_serializers import ProductSerializer


class PurchaseItemSerializer(Schema):
    quantity = fields.Integer(dump_only=True)
    price = fields.Decimal(dump_only=True, places=2, as_string=True)
    product = fields.Nested(ProductSerializer, dump_only=True, many=False)
