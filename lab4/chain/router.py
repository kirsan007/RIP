from chain.database import MAX_PERMISSION

class Route():
    auth: bool = None
    permission: int = None
    handler = None

    def __init__(self, handler, auth: bool, permission: int):
        self.handler = handler
        self.auth = auth

        #assert not (not auth and permission > 0), "Permission must be '0' for public routes"

        self.permission = permission

class Response():
    success: bool = None
    data = None

    def __init__(self, success, data=None):
        self.success = success
        self.data = data

class Request():
    route: str = None
    data = None
    token: str = None

    def __init__(self, route: str, data=None, token: str = None):
        self.route = route
        self.data = data
        self.token = token

class Router():
    routes = {}
    middlewares = []

    def addRoute(self, route: str, handler, auth=True, permission=MAX_PERMISSION):
        self.routes[route] = Route(handler, auth, permission)

    def addMiddleware(self, middleware):
        self.middlewares.append(middleware)

    def handleRequest(self, request: Request):
        try:
            assert request.route in self.routes, "Wrong Route"

            route: Route = self.routes[request.route]

            for middleware in self.middlewares:
                middleware(request, route)

            result = route.handler(request, route)

            return Response(True, result)

        # Обработка ошибок созданных через 'assert'
        except AssertionError as e:
            # Проверка на наличие сообщения об ошибке
            if len(e.args) > 0:
                print("Error: ", e.args[0])
                return Response(False, e.args[0])
            
            return Response(False, "Internal error")
        # Обработка всех других ошибок
        except Exception as e:
            print("Internal error: ", e)
            return Response(False, "Internal error")
