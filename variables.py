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

def shouldBeMutable(variableName, contents):
	REchecks = ["\(" + variableName + "\)", f"{variableName} ="]

	for checkRE in REchecks:
		mutableInstances = re.findall(checkRE, contents)

		if (len(mutableInstances) > 0):
			return True

	return False

def reformatVariable(variable, contents):
	variableName = variable[1]

	if (variable[0] == "char"):
		regex = "\[[0-9]+\]"
		charStringLength = re.findall(regex, variableName)[0]

		variableName = variableName.replace(charStringLength, "")

	formatedVariable = "let "
	if (shouldBeMutable(variableName, contents)):
		formatedVariable += "mut "

	formatedVariable += f"{variableName}: {reAlignDatatype(variable[0])} = {variable[2]}"

	if ("std::string::String" in formatedVariable):
		formatedVariable += ".to_string()"

	return formatedVariable