from functions import *
from replaceStandard import *
from files import *
from variables import *

from caseConvert import convertCasing

import sys

def main():
	# define the output variables
	fileContents = """"""
	outFileName = "out.rs"

	if (len(sys.argv) <= 1):
		print("Please specify an input file...")
		print("$ python3 ./main.py <inFile> (outFile)")
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

		fileContents += f"fn {CfunctionName}() " + "{"

		fileContents += functionContents(CfunctionName, CfileContents)[0] + "}\n\n"

	# extract all the variables out of the source file
	Cvariables = findVariables(fileContents)

	for variable in Cvariables:
		reformattedVariable = reformatVariable(variable)

		fileContents = fileContents.replace(f"{variable[0]} {variable[1]} = {variable[2]}", reformattedVariable)

	fileContents = replaceFunctions(fileContents)
	fileContents = convertCasing(fileContents)

	# create the output file
	writeFile(outFileName, fileContents)

main()