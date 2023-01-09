import re

from rustLib import addLibrary
from variables import findVariables
from tools import chomp

def replaceFunctions(contents):
	rustLibToAdd = []

	contents = contents.replace("printf", "println!")
	inlineVar = ["%c", "%i", "%f", "%d"]
	for varType in inlineVar:
		contents = contents.replace(varType, "{}")

	contents = contents.replace("return 0;", "")

	# replace the CLI input
	CinputRE = ["(gets\((.+?)\))"]

	isInFunc = False

	for inputFunc in CinputRE:
		foundInFunc = re.findall(inputFunc, contents)

		if (len(foundInFunc) > 0):
			rustLibToAdd.append("std::io")

		for func in foundInFunc:
			contents = contents.replace(func[0], f"io::stdin().read_line(&mut {func[1]})")

	# replace C int variable increment with Rust syntax
	# eg. i++ -> i += 1
	regex = "(.+?(?:\+\+|\-\-))(?:;|\))"

	variableIncrements = re.findall(regex, contents)

	for var in variableIncrements:
		var = chomp(var)
		varName = var.replace("++", "")
		varName = varName.replace("--", "")
		contents = contents.replace(var, f"{varName} += 1")


	# add all the required rust libraries
	# should always be the last thing done
	for rustLib in rustLibToAdd:
		contents = addLibrary(rustLib, contents)

	return contents
