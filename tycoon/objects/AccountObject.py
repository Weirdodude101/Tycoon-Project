

class AccountObject():

	def __init__(self, username, password, money = 0):
		self.username = username
		self.password = password
		self.money = money

	def getInfo(self):
		accountInfo = {
			"Username": self.username,
			"Password": self.password,
			"Money": self.money
		}
		return accountInfo
		