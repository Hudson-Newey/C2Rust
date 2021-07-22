# since rust *likes* snake casing
# a conversion table is needed

import re

def extractWords(variableName):
	regex = "[A-Z]?[a-z]+|[A-Z]+(?![a-z])"

	return re.findall(regex, variableName)

def findVariables(contents):
	regex = "([a-z]+(?:[A-Z]+[a-z]+)+)"

	return re.findall(regex, contents)

def convertToSnakeCase(variableName):
	outContents = ""
	variableWords = extractWords(variableName)

	for i in range(len(variableWords)):
		outContents += variableWords[i].lower()

		if (i < len(variableWords) - 1):
			outContents += "_"

	return outContents

def convertCasing(contents):
	outContents = contents

	toChange = findVariables(contents)

	for variable in toChange:
		outContents = outContents.replace(variable, convertToSnakeCase(variable))

	return outContents