# imports a default rust library to the rust code
def addLibrary(libraryName, contents):
	return "use " + libraryName + ";\n\n" + contents

def addLocalModule(modName, contents):
	pass

# to be implemented in future releases
def findEquivilant(libraryName):
	pass