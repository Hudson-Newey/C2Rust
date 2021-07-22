import re

def findVariables(contents):
	regex = "(int|double|float|char) (.+?) = (.+?);"

	return re.findall(regex, contents)

def reAlignDatatype(CdataType):
	conversionTable = {
		"int": "i8",
		"float": "i16",
		"double": "i32",
		"char": "&str"
	}

	return conversionTable.get(CdataType)

def reformatVariable(variable):
	variableName = variable[1]

	if (variable[0] == "char"):
		regex = "\[[0-9]+\]"
		charStringLength = re.findall(regex, variableName)[0]

		variableName = variableName.replace(charStringLength, "")

	formatedVariable = "let "

	formatedVariable += f"{variableName}: {reAlignDatatype(variable[0])} = {variable[2]}"

	return formatedVariable