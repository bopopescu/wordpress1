import sqlite3
from config import db_info
import mysql.connector

class DbManager:

    # db
    # https://blowup-bbs.com/mysql-connector-python-developer-guide/

    mode = "sqlite"
    mysqlConfig = db_info
    dbPath = "Wordpress.db"
    con = ""

    TABLE_ACCOUNT = "Account"
    COLUMN_ACCOUNT_ID = "id"
    COLUMN_ACCOUNT_NAME = "name"
    COLUMN_ACCOUNT_LOGIN_URL = "login_url"
    COLUMN_ACCOUNT_LOGIN_ID = "login_id"
    COLUMN_ACCOUNT_LOGIN_PW = "login_pw"
    COLUMN_ACCOUNT_CREATEDATE = "createdate"

    def __init__(self):

        if self.mode == "sqlite":
            self.con = sqlite3.connect(self.dbPath)
            # self.con = mysql.connector.connect(**self.mysqlConfig)
            query = "CREATE TABLE IF NOT EXISTS " + self.TABLE_ACCOUNT + "(" \
                    + self.COLUMN_ACCOUNT_ID + " integer primary key autoincrement," \
                    + self.COLUMN_ACCOUNT_NAME + " text," \
                    + self.COLUMN_ACCOUNT_LOGIN_URL + " text," \
                    + self.COLUMN_ACCOUNT_LOGIN_ID + " text," \
                    + self.COLUMN_ACCOUNT_LOGIN_PW + " text," \
                    + self.COLUMN_ACCOUNT_CREATEDATE + " text" \
                                                       ")"
        print(query)
        c = self.con.cursor()

        try:
            c.execute(query)
            self.con.commit()
            c.close()
        except Exception as e:
            print(e)

    def getConnect(self):
        return self.con