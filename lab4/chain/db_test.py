
import unittest
from chain.database import DB, MAX_PERMISSION

db = DB("admin", "admin")

class Test(unittest.TestCase):
    def testAdmin(self):
        self.assertTrue("admin" in db.usersByLogins)

        admin = db.usersByLogins["admin"]

        self.assertEqual(admin.password, "admin")
        self.assertEqual(admin.permission, MAX_PERMISSION)

    def testMakeToken(self):
        token = db.makeToken("admin")

        self.assertTrue(token in db.usersByTokens)

        user = db.usersByTokens[""]


if __name__ == '__main__':
    unittest.main()