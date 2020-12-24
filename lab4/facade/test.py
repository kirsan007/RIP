

from unittest.mock import MagicMock

import unittest
from facade.program import orderBook, operator
from facade.library import Delivery

class Test(unittest.TestCase):
    def testOrder(self):
        for i in range(2):
            with self.subTest(msg="Testing Ordering"):
                nameBook= "Bill"
                adress = " Leninskii prsp"
                res = orderBook(nameBook, adress)

                if res["success"] == True:
                    delivery:Delivery = res["delivery"]
                    self.assertEqual(delivery.nameBook, nameBook)
                    self.assertEqual(delivery.adress, adress)
                else:
                    self.assertFalse("delivery" in res)

    def test(self):
        for i in range(2):
            operator.isBookAvailable = MagicMock(return_value=True)
            nameBook = "Bill"
            adress = " Leninskii prsp"
            res = orderBook(nameBook, adress)

            self.assertTrue(res["success"])



if __name__ == '__main__':
    unittest.main()
