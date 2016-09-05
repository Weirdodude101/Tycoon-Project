from tycoon.base.Functions import *
from tycoon.base import Localizer

class MainTycoonScreen(Functions):
	def __init__(self, player):
		Functions.__init__(self)
		self.player = player
		self.money = player["Money"]
		self.displayText(Localizer.gameScreenWelcome.format(player["Username"]), lines = True)
		
		self.displayText(Localizer.moneyDisp.format(self.money), clear = False)

