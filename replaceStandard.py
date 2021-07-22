def replaceFunctions(contents):
	contents = contents.replace("printf", "println!")
	contents = contents.replace("return 0;", "")

	return contents