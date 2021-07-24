import re

from tools import escapeChars

def extractFunctions(text):
	# more function return types need to be supported
	functionReturnTypes = "(int|void|char)"

	regex = functionReturnTypes + " (.+?)\((.*?)\).*?(?:{)"
	foundFunctions = re.findall(regex, text)

	return foundFunctions

def functionContents(functionName, functionParam, Cfile):
	# find the end of the function declaration
	# this is done by finding the name + the paramiters + 2 characters to get past
	# the first semicolon
	functionLocIndex = Cfile.index(f"{functionName}({functionParam})")
	functionLocIndex += len(f"{functionName}({escapeChars(functionParam)})") + 2

	# this variable starts at 1 since the function opening bracket
	# is classed as a "functional loop" in the eyes of the converter
	passedLoops = 1
	endFuncLocIndex = functionLocIndex

	while (passedLoops > 0):
		endFuncLocIndex += 1

		if (Cfile[endFuncLocIndex] == "{"):
			passedLoops += 1

		if (Cfile[endFuncLocIndex] == "}"):
			passedLoops -= 1

	functionContents = Cfile[functionLocIndex:endFuncLocIndex]

	return functionContents