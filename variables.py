import re

from tools import escapeChars

# finds all variables in a source file
def findVariables(contents):
	variables = []
	dataTypes = "(int|double|float|char)"

	checkList = [f"{dataTypes} (.+?) = (.+?);", f"{dataTypes} (.+?) = (.+?)", f"\({dataTypes} (.+?)()(?:\)|,)", f", {dataTypes} (.+?)(),", f", {dataTypes} (.+?)()\)"]

	for regex in checkList:
		variables += re.findall(regex, contents)

	return variables

# takes a C datatype and returns the corrosponding rust data type
def reAlignDatatype(CdataType, variableValue):
	conversionTable = {
		"int": "i32",
		"float": "f32",
		"double": "f64",
		"char": "std::string::String"
	}

	rustDataType = conversionTable.get(CdataType)

	if ("&" in variableValue):
		rustDataType = "&" + rustDataType

	return rustDataType

# decides whether a variable is modified in runtime
# defaults to variables being constants
def shouldBeMutable(variableName, contents):
	variableName = escapeChars(variableName)

	REchecks = ["\(" + variableName + "\)", f"{variableName} ="]

	for checkRE in REchecks:
		mutableInstances = re.findall(checkRE, contents)

		if (len(mutableInstances) > 0):
			return True

	return False

# the main calling function to reformat C variables into rust syntax
def reformatVariable(variable, contents):
	variableName = variable[1]
	variableType = variable[0]
	variableValue = variable[2]

	if (variableType == "char"):
		regex = "\[[0-9]+\]"
		charStringLength = re.findall(regex, variableName)

		if (len(charStringLength) > 0):
			variableName = variableName.replace(charStringLength[0], "")

	formatedVariable = ""
	if (len(variableValue) > 0):
		formatedVariable = "let "

		# if the variable gets modified in runtime, make the variable mutable
		if (shouldBeMutable(variableName, contents)):
			formatedVariable += "mut "

		formatedVariable += f"{variableName}: {reAlignDatatype(variableType, variableValue)} = {variableValue}"

		# work around becuase i'm using std::string::String
		if ("std::string::String" in formatedVariable and ("\"" in formatedVariable or "'" in formatedVariable)):
			formatedVariable += ".to_string()"

	else:
		formatedVariable += f"{variableName}: {reAlignDatatype(variableType, variableValue)}"

	return formatedVariable