# Python imports
# Flask imports
from flask import request
# Third-Party imports
from flask_restful import Resource
# Project Imports
from apps.checkouts.api.rest.v1_0 import api_serializers
from apps.checkouts import services
from apps.checkouts import checkouts_dao
from apps.checkouts.api.rest.v1_0 import api_decorators


class CheckoutCreationAPIController(Resource):
    request_serializer = api_serializers.CheckoutCreateSerializer
    response_serializer = api_serializers.CheckoutDetailSerializer

    @api_decorators.error_response_handler
    def post(self):
        request_serializer_class = self.request_serializer(many=True, strict=True)
        cart = request_serializer_class.load(request.json).data
        if len(cart) == 0:
            raise TypeError()
        checkout_instance = services.create_new_checkout(cart=cart)
        response_serializer_class = self.response_serializer()
        response_data = response_serializer_class.dump(checkout_instance).data
        return response_data, 201


class CheckoutDetailAPIController(Resource):
    serializer = api_serializers.CheckoutDetailSerializer

    def get_objects(self, checkout_id):
        return checkouts_dao.get_checkout_by_id(checkout_id=checkout_id)

    @api_decorators.error_response_handler
    def get(self, checkout_id):
        serializer_class = self.serializer()
        object = self.get_objects(checkout_id=checkout_id)
        data = serializer_class.dump(object).data
        return data, 200

