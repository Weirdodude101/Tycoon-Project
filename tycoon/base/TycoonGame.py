from tycoon.base import Localizer
from tycoon.base import Globals
from tycoon.account.AccountLogin import *
from tycoon.account.AccountRegister import *

class TycoonGame(AccountLogin, AccountRegister):

	def __init__(self):
		AccountLogin.__init__(self)
		AccountRegister.__init__(self)
		self.displayText("Welcome to the Tycoon Project")
		self.displayText("Please choose one of the following options!", False)
		self.menu()

	def menu(self):
		self.displayOptions(option1 = ("Login", self.initiateLogin), option2 = ("Register", self.initiateRegister))
		option = raw_input("Enter here: ")
		try:	
			exec(compile('self.optionDict[int(option)]()', '<string>', 'exec'))
		except:
			self.displayText("Invalid option, please try again!")
			self.menu()

game = TycoonGame()