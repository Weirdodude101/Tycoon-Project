from tycoon import yaml
from tycoon.base.Functions import *
from tycoon.objects.AccountObject import *

class AccountRegister(Functions):
	def __init__(self):
		Functions.__init__(self)

	def initiateRegister(self):
		print "Register"