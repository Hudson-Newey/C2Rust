def readFile(filePath):
	return open(filePath, "r").read()

def writeFile(filePath, contents):
	filePointer = open(filePath, 'w')

	filePointer.write(contents)
	filePointer.close()