import re

def findVariables(contents):
	variables = []
	dataTypes = "(int|double|float|char)"

	checkList = [f"{dataTypes} (.+?) = (.+?);", f"\({dataTypes} (.+?)()(?:\)|,)", f", {dataTypes} (.+?)(),", f", {dataTypes} (.+?)()\)"]

	for regex in checkList:
		variables += re.findall(regex, contents)

	print(variables)

	return variables

def reAlignDatatype(CdataType):
	conversionTable = {
		"int": "i32",
		"float": "f32",
		"double": "f64",
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
	variableType = variable[0]
	variableValue = variable[2]

	if (variable[0] == "char"):
		regex = "\[[0-9]+\]"
		charStringLength = re.findall(regex, variableName)[0]

		variableName = variableName.replace(charStringLength, "")

	formatedVariable = ""
	if (len(variableValue) > 0):
		formatedVariable = "let "

		if (shouldBeMutable(variableName, contents)):
			formatedVariable += "mut "

		formatedVariable += f"{variableName}: {reAlignDatatype(variableType)} = {variableValue}"

		if ("std::string::String" in formatedVariable):
			formatedVariable += ".to_string()"
	else:
		formatedVariable += f"{variableName}: {reAlignDatatype(variableType)}"

	return formatedVariable