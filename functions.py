import re

def extractFunctions(text):
	regex = "(.+?) (.+?)\(\).*?(?:{)"

	return re.findall(regex, text)

def functionContents(functionName, Cfile):
	regex = functionName + "\(\).*?{(.+?)}"
	functionContents = re.findall(regex, Cfile, re.DOTALL)

	return functionContents