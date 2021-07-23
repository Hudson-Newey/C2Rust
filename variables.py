import re

def findVariables(contents):
	regex = "(int|double|float|char) (.+?) = (.+?);"

	return re.findall(regex, contents)

def reAlignDatatype(CdataType):
	conversionTable = {
		"int": "i8",
		"float": "i16",
		"double": "i32",
		"char": "std::string::String"
	}

	return conversionTable.get(CdataType)

def reformatVariable(variable):
	variableName = variable[1]

	if (variable[0] == "char"):
		regex = "\[[0-9]+\]"
		charStringLength = re.findall(regex, variableName)[0]

		variableName = variableName.replace(charStringLength, "")

	# future releases should not make every variable mutable
	# although, this is easier for the prototyping process
	formatedVariable = "let mut "

	formatedVariable += f"{variableName}: {reAlignDatatype(variable[0])} = {variable[2]}"

	if ("std::string::String" in formatedVariable):
		formatedVariable += ".to_string()"

	return formatedVariable