from tycoon import yaml
import sys
import os
class Functions(object):

	def __init__(self):
		pass

	def clearConsole(self):
		if sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")

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