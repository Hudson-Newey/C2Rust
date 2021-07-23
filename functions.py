import re

from tools import escapeChars

def extractFunctions(text):
	regex = "(.+?) (.+?)\((.*?)\).*?(?:{)"
	foundFunctions = re.findall(regex, text)

	return foundFunctions

def functionContents(functionName, functionParam, Cfile):
	regex = functionName + "\(" + escapeChars(functionParam) + "\).*?{(.+?)}"
	functionContents = re.findall(regex, Cfile, re.DOTALL)

	return functionContents