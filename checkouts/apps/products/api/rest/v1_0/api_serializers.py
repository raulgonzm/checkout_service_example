# Python imports
# Flask imports
# Third-Party imports
from marshmallow import Schema, fields
# Project Imports


class ProductSerializer(Schema):
    code = fields.String(dump_only=True)
    name = fields.String(dump_only=True)
    price = fields.Decimal(dump_only=True, places=2, as_string=True)
