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

	def displayText(self, text, clear = True, lines = False):
		if clear:
			self.clearConsole()
		print text
		if lines:
			print '-------------------------'

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

	def dumpYaml(self, filepath, option):
		with open(filepath, 'w') as outfile:
			newAttb = outfile.write(yaml.dump(option,default_flow_style=False) )
		return newAttb

	def loadYaml(self, filepath):
		with open(filepath, "r") as file_descriptor:
			personInfo = yaml.load(file_descriptor)
		return personInfo

	def createYaml(self, filepath,option):
		with open(filepath, 'w') as outfile:
			newAcc = outfile.write(yaml.dump(option,default_flow_style=False) )
		return newAcc

class Prompt():
	def __init__(self, **kwargs):
		self.kwargs = kwargs
		for arg in kwargs:
			value = raw_input(kwargs[arg] + ": ")
			kwargs[arg] = value

	def __getitem__(self, key):
		return self.kwargs[key]




