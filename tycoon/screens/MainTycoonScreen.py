from tycoon.base.Functions import *

class MainTycoonScreen(Functions):
	def __init__(self, person):
		Functions.__init__(self)
		self.person = person
		self.displayText("Screen!")