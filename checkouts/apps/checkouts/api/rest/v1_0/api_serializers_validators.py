# Python imports
# Flask imports
# Third-Party imports
# Project Imports


def validate_cart(cart):
    if len(cart) == 0:
        raise TypeError()
