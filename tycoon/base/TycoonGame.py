from tycoon.base import Localizer
from tycoon.base import Globals
from tycoon.account.AccountLogin import *
from tycoon.account.AccountRegister import *

class TycoonGame(AccountLogin, AccountRegister):

	def __init__(self):
		AccountLogin.__init__(self)
		AccountRegister.__init__(self)
		self.menu()

	def menu(self):
		pass

game = TycoonGame()