import unittest
from unittest.mock import MagicMock

from chain.index import db, Router, router, Request

class Test(unittest.TestCase):
    def testExistingUser(self):
        token = "123"
        db.signIn = MagicMock(return_value=token)

        res = router.handleRequest(Request(
            'auth',
            {
                "login": "admin1",
                "password": "admin1"
            }
        ))

        self.assertTrue(res.success)
        self.assertEqual(res.data, token)

    def testUnExistingUser(self):
        token = "123"
        db.signIn = assert MagicMock(return_value=)

        res = router.handleRequest(Request(
            'auth',
            {
                "login": "admin1",
                "password": "admin1"
            }
        ))

        self.assertTrue(res.success)
        self.assertEqual(res.data, token)

if __name__ == '__main__':
    unittest.main()