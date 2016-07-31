from tycoon import yaml
import sys
import os


class Functions(object):

	def __init__(self):
		self.optionDict = {}

	def clearConsole(self):
		if sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")

	def displayText(self, text, clear = True):
		if clear:
			self.clearConsole()
		print text

	def displayOptions(self, **kwargs):
		num = 0
		tempList = []
		for name, item in kwargs.iteritems():
			tempList.append(item)
		reversedList = list(reversed(tempList))
		for item in reversedList:
			num += 1
			print "{0}: {1}".format(num, item[0])
			self.optionDict[num] = item[1]

	def clearOptions(self):
		self.optionList = []

	def dumpYaml(filepath, option):
		with open(filepath, 'w') as outfile:
			newAttb = outfile.write(yaml.dump(option,default_flow_style=False) )
		return newAttb

	def loadYaml(filepath):
		with open(filepath, "r") as file_descriptor:
			personInfo = yaml.load(file_descriptor)
		return personInfo

	def createYaml(filepath,option):
		with open(filepath, 'w') as outfile:
			newAcc = outfile.write(yaml.dump(option,default_flow_style=False) )
		return newAcc