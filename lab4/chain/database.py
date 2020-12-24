import string
import random

MAX_PERMISSION = 100

class User():
    login: str = None
    password: str = None
    permission: int = None

    def __init__(self, login: str, password: str, permission: int):
        assert permission <= MAX_PERMISSION, "Permition level limit"

        self.login = login
        self.password = password
        self.permission = permission


    def checkPassword(self, password: str):
        return password == self.password

    def checkPermission(self, permission: int):
        return permission <= self.permission


class DB():
    usersByLogins={}
    usersByTokens = {}
    
    def __init__(self, login: str, password: str):
        self.creatUser(login, password, 100)

    def creatUser(self, login, password, permission):
        assert login not in self.usersByLogins, "Login exists"

        self.usersByLogins[login]=User(login, password, permission)

    def makeToken(self, login):
        pool: str = string.ascii_letters
        token = ''.join(random.choices(pool, k=10))
        self.usersByTokens[token] = self.usersByLogins[login]
        return token

    def signIn(self, login, password):
        assert login in self.usersByLogins, "Login not exists"

        user: User = self.usersByLogins[login]
        assert user.checkPassword(password), "Wrong Passworsd"

        return self.makeToken(login)

    def checkToken(self, token):
        if token not in self.usersByTokens:
            return False

        return True


    def checkPermission(self, token, permission):
        assert token in self.usersByTokens, "Wrong Token"

        user: User = self.usersByTokens[token]

        if user.checkPermission(permission):
            return True

        return False

    def deleteUser(self, login):
        assert login in self.usersByLogins, "Wrong Login"

        self.usersByLogins[login] = None
        for token in self.usersByTokens:
            user: User = self.usersByTokens[token]

            if user.login == login:
                self.usersByTokens[token] = None

        return True
