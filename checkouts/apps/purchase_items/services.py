# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.purchase_items.models import PurchaseItem


def create_new_purchase_item(product, quantity):
    return PurchaseItem(
        product=product,
        quantity=quantity
    )
