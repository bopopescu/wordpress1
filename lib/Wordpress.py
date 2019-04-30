from lib.DbManager import DbManager
from lib.Master import Account
from selenium import webdriver
import time

class Wordpress(DbManager):

    path = r'C:\Users\user\Desktop\chromedriver\chromedriver.exe'
    driver = ""

    def __init__(self):
        super().__init__()

    def login(self, account):
        print("login")

        if self.driver == "":
            self.driver = webdriver.Chrome(self.path)

        self.driver.get(account.getLoginUrl())
        time.sleep(2)
        formId = self.driver.find_element_by_id("user_login")
        formId.send_keys(account.getLoginId())
        formPw = self.driver.find_element_by_id("user_pass")
        formPw.send_keys(account.getLoginPw())
        formBt = self.driver.find_element_by_id("wp-submit")
        formBt.click()


    def addAccount(self, account):

        con = self.getConnect()
        query = "INSERT INTO " \
                + self.TABLE_ACCOUNT + "(" \
                + self.COLUMN_ACCOUNT_NAME + "," \
                + self.COLUMN_ACCOUNT_LOGIN_URL + "," \
                + self.COLUMN_ACCOUNT_LOGIN_ID + "," \
                + self.COLUMN_ACCOUNT_LOGIN_PW + "," \
                + self.COLUMN_ACCOUNT_CREATEDATE + ""\
                ")VALUES(?,?,?,?,datetime(CURRENT_TIMESTAMP))"
        c = con.cursor()
        args = [account.getName(), account.getLoginUrl(),  account.getLoginId(), account.getLoginPw()]
        c.execute(query, args)
        con.commit()

    def getAccountById(self, id):

        con = self.getConnect()
        query = "select * from " + self.TABLE_ACCOUNT + " WHERE " + self.COLUMN_ACCOUNT_ID + " = ?"
        args = [id, ]
        c = con.cursor()
        c.execute(query, args)

        account = Account()
        for row in c:
            account.setId(row[0])
            account.setName(row[1])
            account.setLoginUrl(row[2])
            account.setLoginId(row[3])
            account.setLoginPw(row[4])

        return account

    def deleteAccount(self, id):
        con = self.getConnect()
        query = "DELETE FROM " + self.TABLE_ACCOUNT + " WHERE " + self.COLUMN_ACCOUNT_ID + " = ? "
        args = [id, ]
        c = con.cursor()
        c.execute(query, args)
        con.commit()

    def getAccount(self):

        con = self.getConnect()
        query = "select * from " + self.TABLE_ACCOUNT + " ORDER BY " + self.COLUMN_ACCOUNT_ID + " DESC"
        c = con.cursor()
        c.execute(query)

        list = []
        for row in c:
            account = Account()
            account.setId(row[0])
            account.setName(row[1])
            account.setLoginUrl(row[2])
            account.setLoginId(row[3])
            account.setLoginPw(row[4])
            list.append(account)
        return list
