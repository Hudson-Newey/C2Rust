def escapeChars(string):
	charsToEscape = ["[", "]", "\'", "\"", "(", ")", "-", "+", "*", ".", ":"]

	returnString = string

	for char in charsToEscape:
		returnString = returnString.replace(char, "\\" + char)

	return returnString