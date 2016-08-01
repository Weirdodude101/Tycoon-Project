from tycoon import yaml
from tycoon.base.Functions import *
from tycoon.objects.AccountObject import *
from tycoon.base.Globals import *
from tycoon.base.TycoonGame import *

class AccountRegister(Functions):
	def __init__(self):
		Functions.__init__(self)


	def initiateRegister(self, invalid = False):
		if invalid:
			self.displayText("Inalid confirmation, please try again!", clear = True)
		self.displayText("Register your account", clear = False if invalid else True,  lines = True)
		self.info = Prompt(a = "Enter a new username" , b = "Confirm username", c = "Enter a new password", d = "Confirm password")
		if self.info['a'] == self.info['b']:
			if self.info['c'] == self.info['d']:
				self.accObj = AccountObject(self.info['a'], self.info['c'])
				info = self.accObj.getInfo()
				self.createYaml(dbPath + "{0}.yaml".format(self.info['a'].lower()), info)
				TycoonGame()
			else:
				self.initiateRegister(True)
		else:
			self.initiateRegister(True)

