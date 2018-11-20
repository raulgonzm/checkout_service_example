# Python imports
# Flask imports
# Third-Party imports
# Project Imports
from apps.purchase_items.models import PurchaseItem


def _create_new_purchase_item(product, quantity):
    return PurchaseItem(
        product=product,
        quantity=quantity
    )


def scan_new_purchase_item(checkout, product, quantity):
    new_purchase_item = _create_new_purchase_item(
        product=product,
        quantity=quantity
    )
    checkout.scan(purchase_item=new_purchase_item)
    return checkout
