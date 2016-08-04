from tycoon import yaml
from tycoon.base.Functions import *
from tycoon.base.Globals import *
from tycoon.screens.MainTycoonScreen import *

class AccountLogin(Functions):
	def __init__(self):
		Functions.__init__(self)
		

	def initiateLogin(self, invalid = False):
		if invalid:
			self.displayText("Invalid information entered, please try again!", clear = True)
		self.displayText("Enter your information", clear = False if invalid else True, lines = True)
		self.info = Prompt(a = "Username", b = "Password")
		try:
			self.check = self.loadYaml(dbPath.format(self.info['a'].lower()))
			if self.info['b'] == self.check["Password"]:
				MainTycoonScreen(self.check)
		except:
			self.initiateLogin(True)