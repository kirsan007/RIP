from chain.database import DB, MAX_PERMISSION
from chain.router import Router, Route, Request


db = DB("admin", "admin")

#region Middlewares
def checkAuth(request: Request, route: Route):
    if route.auth:
        assert db.checkToken(request.token), "Wrong Token"
    
def checkPermission(request: Request, route: Route):
    if route.auth and route.permission > 0:
        assert  db.checkPermission(request.token, route.permission), "Not Permited"
#endregion

#region Handlers
def test(request: Request, route: Route):
    # assert False, "Это проблема"
    print(request.data)
    return request.data

def createUser(request: Request, route: Route):
    return db.creatUser(
        request.data["login"],
        request.data["password"],
        request.data["permission"]
    )

def auth(request: Request, route: Route):
    return db.signIn(
        request.data["login"],
        request.data["password"]
    )
#endregion

router = Router()

router.addMiddleware(checkAuth)
router.addMiddleware(checkPermission)

router.addRoute("test", test, False)
router.addRoute("auth", auth, False)
router.addRoute("createUser", createUser, True, MAX_PERMISSION)

if __name__ == '__main__':

    res = router.handleRequest(Request('test', '123'))

    # Этот запрос будет ошибочным
    res = router.handleRequest(Request(
        'auth',
        {
            "login": "admin",
            "password": "admin"
        }
    ))
    res = router.handleRequest(Request(
        'createUser',
        {
            "login": "Login",
            "password": "123",
            "permission": 5
        },
        res.data
    ))
    res = router.handleRequest(Request(
        'auth',
        {
            "login": "Login",
            "password": "123"
        }
    ))

    pass
