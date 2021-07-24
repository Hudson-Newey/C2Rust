import re

# used to get the name of the variable
from variables import findVariables
from tools import findOperator

def findForLoops(contents):
	forLoopRE = "for \((.+?);(.+?);(.+?)\)"
	forLoops = re.findall(forLoopRE, contents)

	return forLoops

def findEndingCondition(operator, string):
	regex = f"{operator} (.+)"

	return re.findall(regex, string)[0]

def replaceForLoops(contents):
	forLoops = findForLoops(contents)

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

def replaceConditional(contents):
	contents = replaceForLoops(contents)

	return contents