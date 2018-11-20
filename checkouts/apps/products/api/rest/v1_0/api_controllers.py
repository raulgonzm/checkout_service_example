# Python imports
# Flask imports
# Third-Party imports
from flask_restful import Resource
# Project Imports
from apps.products.api.rest.v1_0.api_serializers import ProductSerializer
from apps.products import product_dao


class ProductAPIController(Resource):
    serializer = ProductSerializer

    def get_objects(self):
        return product_dao.get_all_products()

    def get(self):
        serializer_class = self.serializer(many=True)
        data = serializer_class.dumps(self.get_objects())
        return data, 200

