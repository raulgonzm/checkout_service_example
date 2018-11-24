# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.api.rest.v1_0 import api_controllers


class CheckoutAPIUrls:

    checkout_create = '/api/rest/v1_0/checkouts/'
    checkout_detail = '/api/rest/v1_0/checkouts/<string:checkout_number>/'

    @classmethod
    def init_checkout_api_urls(cls, api):
        api.add_resource(api_controllers.CheckoutCreationAPIController, cls.checkout_create)
        api.add_resource(api_controllers.CheckoutDetailAPIController, cls.checkout_detail)
        return api
