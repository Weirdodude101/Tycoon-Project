

class AccountObject():

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def getInfo(self):
		accountInfo = {
			"Username": self.username,
			"Password": self.password
		}
		return accountInfo