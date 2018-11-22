# Python imports
# Flask imports
# Third-Party imports
# Project Imports


class CheckoutDoesNotExist(Exception):

    def __init__(self, checkout_id, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = f"The Checkout object requested does not exist. ID {checkout_id}"
        super(CheckoutDoesNotExist, self).__init__(msg)
        self.checkout_id = checkout_id
        self.messages = msg
