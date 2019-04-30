import eel
from lib.Wordpress import Wordpress
from lib.Master import Account

def main():
	eel.init("web")
	eel.start("account-add.html")

@eel.expose
def bt_login(id):
	_wordpress = Wordpress()
	account = _wordpress.getAccountById(id)
	_wordpress.login(account)

@eel.expose
def bt_delete(id):
	_wordpress = Wordpress()
	_wordpress.deleteAccount(id)
	bt_search_post_list()

@eel.expose
def bt_search_post_list():

	_list = []
	_wordpress = Wordpress()
	_list = _wordpress.getAccount()

	eel.delete_rows()

	for account in _list:
		idnum = account.getId()
		blog_name = account.getName()
		login_id = account.getLoginId()
		login_pw = account.getLoginPw()
		login_url = account.getLoginUrl()

		eel.add_record(idnum, blog_name, login_id, login_pw, login_url)


@eel.expose
def add_account(blog_name, login_url, login_id, login_pw):
	_wordpress = Wordpress()
	account = Account()
	account.setName(blog_name)
	account.setLoginId(login_id)
	account.setLoginPw(login_pw)
	account.setLoginUrl(login_url)
	_wordpress.addAccount(account)


if __name__ == "__main__":
	main()