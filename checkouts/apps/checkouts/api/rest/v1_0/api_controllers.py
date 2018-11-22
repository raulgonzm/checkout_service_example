# Python imports
# Flask imports
from flask import request
# Third-Party imports
from flask_restful import Resource
# Project Imports
from apps.checkouts.api.rest.v1_0 import api_serializers
from apps.checkouts import services


class CheckoutCreationAPIController(Resource):
    request_serializer = api_serializers.CheckoutCreateSerializer
    response_serializer = api_serializers.CheckoutDetailSerializer

    def post(self):
        request_serializer_class = self.request_serializer(many=True)
        cart = request_serializer_class.load(request.json).data
        checkout_instance = services.create_new_checkout(cart=cart)
        response_serializer_class = self.response_serializer()
        response_data = response_serializer_class.dump(checkout_instance).data
        return response_data, 201

