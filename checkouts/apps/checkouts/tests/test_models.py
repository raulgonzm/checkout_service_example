# Python imports
import unittest
# Flask imports
# Third-Party imports
# Project Imports
from apps.checkouts.tests.mocks import CheckoutFactory


class CheckoutModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.checkout = CheckoutFactory()

    def test_repr_method(self):
        self.assertEqual(
            self.checkout.__repr__(),
            f"<Checkout-{self.checkout.id}>"
        )


if __name__ == '__main__':
    unittest.main()
