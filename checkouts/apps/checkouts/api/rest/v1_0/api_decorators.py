# Python imports
# Flask imports
# Third-Party imports
from marshmallow import ValidationError
# Project imports
from apps.checkouts.exceptions import CheckoutDoesNotExist
from apps.products.exceptions import ProductDoesNotExist


def error_response_handler(decorated_func):

    def _decorator(view_func):
        def _view(request, *args, **kwargs):
            try:
                return view_func(request, *args, **kwargs)
            except (ValidationError, ProductDoesNotExist) as err:
                return err.messages, 400
            except (TypeError, KeyError):
                return {"error": "Request data is empty or type error"}, 400
            except CheckoutDoesNotExist as err:
                return err.messages, 404
        return _view
    return _decorator(decorated_func)
