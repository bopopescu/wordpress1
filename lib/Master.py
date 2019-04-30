
# Account
class Account:
    id=""
    name=""
    login_url = ""
    login_id = ""
    login_pw = ""
    target=""

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setLoginUrl(self, url):
        self.login_url = url

    def getLoginUrl(self):
        return self.login_url

    def setLoginId(self, login_id):
        self.login_id = login_id

    def getLoginId(self):
        return self.login_id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLoginPw(self, login_pw):
        self.login_pw = login_pw

    def getLoginPw(self):
        return self.login_pw

