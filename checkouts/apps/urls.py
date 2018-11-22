# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.api.rest.v1_0.api_urls import ProductAPIUrls
from apps.checkouts.api.rest.v1_0.api_urls import CheckoutAPIUrls


class Router:

    def __init__(self, api):
        ProductAPIUrls.init_produt_api_urls(api=api)
        CheckoutAPIUrls.init_checkout_api_urls(api=api)
