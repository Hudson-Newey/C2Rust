import re

# escapes characters that need escaping in regex strings
def escapeChars(string):
	charsToEscape = ["[", "]", "\'", "\"", "(", ")", "-", "+", "*", ".", ":"]

	returnString = string

	for char in charsToEscape:
		returnString = returnString.replace(char, "\\" + char)

	return returnString

# extracts the C operator from a string
# this was done to prevent future code duplication
def findOperator(string):
	operators = "(==|!=|>=|<=|<|>)"

	return re.findall(operators, string)[0]
