import re

# used to get the name of the variable
from variables import findVariables
from tools import findOperator

def findForLoops(contents):
	forLoopRE = "for \((.+?);(.+?);(.+?)\)"
	forLoops = re.findall(forLoopRE, contents)

	return forLoops

# find the condition to end
# eg. when i > 10 exit loop
# this would return 10
def findEndingCondition(operator, string):
	regex = f"{operator} (.+)"

	return re.findall(regex, string)[0]

# replaces for loops with the rust syntax
def replaceForLoops(contents):
	forLoops = findForLoops(contents)

	# itterates through the C for loops
	# each loop contains a tuple with a format similar to
	# ("int i =0", "i < 10", "i = i + 1")
	for loop in forLoops:
		initialVal = loop[0]
		condition = loop[1]
		increment = loop[2]

		variableName = findVariables(initialVal)[0][1]
		variableInit = findVariables(initialVal)[0][2]
		operator = findOperator(condition)
		
		# find the equivilant operator
		operatorMap = {
			">": "..",
			"<": "..",
			">=": "..1+",
			"<=": "..1+"
		}

		rustOperator = operatorMap[operator]
		Cfor = f"for ({initialVal};{condition};{increment})"
		rustFor = f"for {variableName} in {variableInit}{rustOperator}{findEndingCondition(operator, condition)}"

		contents = contents.replace(Cfor, rustFor)

	return contents

# replaces conditional loops
# this only supports for loops at the current moment
def replaceConditional(contents):
	contents = replaceForLoops(contents)

	return contents