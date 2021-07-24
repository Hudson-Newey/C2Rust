import re

def escapeChars(string):
	charsToEscape = ["[", "]", "\'", "\"", "(", ")", "-", "+", "*", ".", ":"]

	returnString = string

	for char in charsToEscape:
		returnString = returnString.replace(char, "\\" + char)

	return returnString

def findOperator(string):
	operators = "(==|!=|>=|<=|<|>)"

	return re.findall(operators, string)[0]
