# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.api.rest.v1_0.api_controllers import CheckoutCreationAPIController


class CheckoutAPIUrls:

    checkout_create = '/api/rest/v1_0/checkouts/'

    @classmethod
    def init_checkout_api_urls(cls, api):
        api.add_resource(CheckoutCreationAPIController, cls.checkout_create)
        return api
