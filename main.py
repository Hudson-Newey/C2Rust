from functions import *
from replaceStandard import *
from files import *
from variables import *

from caseConvert import convertCasing

import sys
from os import path

def main():
	# define the output variables
	fileContents = """"""
	outFileName = "out.rs"

	if (len(sys.argv) <= 1):
		print("\x1B[33mPlease specify an input file...\x1b[0m")
		print("$ python3 ./main.py <inFile> (outFile)")
		exit()

	if (not path.exists(sys.argv[1])):
		print("\x1B[33mError 404!\nC File not found...\x1b[0m")
		exit()

	if (len(sys.argv) > 2):
		outFileName = sys.argv[2]

	CfileName = sys.argv[1]
	CfileContents = readFile(CfileName)

	Cfunctions = extractFunctions(CfileContents)

	# write the C functions into rust format
	for function in Cfunctions:
		CfunctionName = function[1]
		CfunctionType = function[0]
		CfunctionParams = function[2]

		fileContents += f"fn {CfunctionName}({CfunctionParams}) " + "{"

		fileContents += functionContents(CfunctionName, CfunctionParams, CfileContents) + "}\n\n"

	# extract all the variables out of the source file
	Cvariables = findVariables(fileContents)

	for variable in Cvariables:
		variableName = variable[1]
		variableType = variable[0]
		variableValue = variable[2]
		
		reformattedVariable = reformatVariable(variable, fileContents)

		# check if the variable has a default value
		if (len(variableValue) > 0):
			fileContents = fileContents.replace(f"{variableType} {variableName} = {variableValue}", reformattedVariable)
		else:
			fileContents = fileContents.replace(f"{variableType} {variableName}", reformattedVariable)

	fileContents = replaceFunctions(fileContents)
	fileContents = convertCasing(fileContents)

	# create the output file
	writeFile(outFileName, fileContents)

main()