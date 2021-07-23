import re

from rustLib import addLibrary

def replaceFunctions(contents):
	contents = contents.replace("printf", "println!")
	inlineVar = ["%c", "%i", "%f", "%d"]
	for varType in inlineVar:
		contents = contents.replace(varType, "{}")

	contents = contents.replace("\nreturn 0;", "")

	# replace the CLI input
	CinputRE = ["(gets\((.+?)\))"]

	isInFunc = False

	for inputFunc in CinputRE:
		foundInFunc = re.findall(inputFunc, contents)

		if (len(foundInFunc) > 0):
			isInFunc = True

		for func in foundInFunc:
			contents = contents.replace(func[0], f"io::stdin().read_line(&mut {func[1]})")

	if (isInFunc):
		contents = addLibrary("std::io", contents)


	return contents
