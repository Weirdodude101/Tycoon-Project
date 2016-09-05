from tycoon.base import Localizer
from tycoon.base import Globals
from tycoon.account.AccountLogin import *
from tycoon.account.AccountRegister import *
import sys
class TycoonGame(AccountLogin, AccountRegister):

	def __init__(self, dClear = False):
		AccountLogin.__init__(self)
		AccountRegister.__init__(self)
		self.menu()

	def menu(self):
		self.displayText("Welcome to the Tycoon Project")
		self.displayText("Please choose one of the following options!", clear = False)
		self.displayOptions(option1 = ("Login", self.initiateLogin), option2 = ("Register", self.initiateRegister))
		option = raw_input("Enter here: ")
		#self.optionDict[int(option)]()
		try:	
			self.optionDict[int(option)]()
		except:
			self.displayText("Invalid option, please try again!")
			self.menu()
		
game = TycoonGame()
