# Python imports
# Flask imports
# Third-Party imports
# Project Imports


class ProductDoesNotExist(Exception):

    def __init__(self, product_id, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = f"The Product object requested does not exist. ID {product_id}"
        super(ProductDoesNotExist, self).__init__(msg)
        self.product_id = product_id
        self.messages = msg
