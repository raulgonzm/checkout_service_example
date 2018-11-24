# Python imports
import uuid
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.models import Checkout
from apps.checkouts import checkouts_dao
from apps.products import product_dao
from apps.purchase_items import services as purchase_item_services


def generate_new_checkout_number():
    return str(uuid.uuid4())


def scan_new_purchase_item(checkout, product, quantity):
    new_purchase_item = purchase_item_services.create_new_purchase_item(
        product=product,
        quantity=quantity
    )
    checkout.scan(purchase_item=new_purchase_item)
    return checkout


def scan_checkout_cart(checkout, cart):
    for item in cart:
        product = product_dao.get_product_by_code(product_code=item['product'])
        scan_new_purchase_item(checkout=checkout, product=product, quantity=item['quantity'])
    return checkout


def create_new_checkout(cart):
    new_checkout = Checkout(checkout_number=generate_new_checkout_number())
    new_checkout = scan_checkout_cart(checkout=new_checkout, cart=cart)
    new_checkout = checkouts_dao.insert_checkout(checkout=new_checkout)
    return new_checkout
