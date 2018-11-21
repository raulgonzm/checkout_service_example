# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.products.api.rest.v1_0.api_controllers import ProductAPIController


class ProductAPIUrls:

    product_list = '/api/rest/v1_0/products/'

    @classmethod
    def init_produt_api_urls(cls, api):
        api.add_resource(ProductAPIController, cls.product_list)
        return api
