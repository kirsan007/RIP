
import unittest
from unittest.mock import MagicMock
from chain.index import router, Request, db

#db.creatUser = MagicMock(return_value=True)

def auth(login, password):
    res = router.handleRequest(Request(
        'auth',
        {
            "login": login,
            "password": password
        }
    ))
    return res
def createUser(login, password, permission, token):
    res = router.handleRequest(Request(
        'createUser',
        {
            "login": login,
            "password": password,
            "permission": permission
        },
        token
    ))
    return res

fakeLogin = "fakeLogin"
fakePassword = "fakePassword"
fakePermission = 5

class Test(unittest.TestCase):
    def testAdmin(self):
         #with self.subTest(human=human):
         #db.signIn = MagicMock(return_value="123")
         res = auth("admin1", "admin")
         self.assertTrue(res.success)
         self.assertTrue(isinstance(res.data, str))

    def testFakeUser(self):
        res = auth(fakeLogin, fakePassword)
        self.assertFalse(res.success)
        #self.assertTrue(res.data is None)

    def testNewUser(self):
        adminRes = auth("admin", "admin")

        res = createUser(fakeLogin, fakePassword, fakePermission, adminRes.data)
        self.assertTrue(res.success)

        res = auth(fakeLogin, fakePassword)
        self.assertTrue(res.success)
        self.assertTrue(isinstance(res.data, str))

        user = db.usersByLogins[fakeLogin]
        self.assertEqual(user.permission, fakePermission)


if __name__ == '__main__':
    unittest.main()