def parseInput(str_Input):
	# assuming the input comes in as one string like I=2A V=2mV R=802.37kOhm
	tokens = " ".split(str_Input)
	
	for token in tokens:
		# refine - this assumes the input was done exactly right
		parts = "=".split(token)
		
		print("Letter: %s"%parts[0])
		print("Value: %s"%parts[1])
		
		# the value needs to be converted from something like 5V or 2.05GW to a float


# is there a better way to store the variable values?
dict_ElectricVariables = { 
							# Possibly want to initialize to None
							"current": 0.0,
							"voltage": 0.0,
							"time": 0.0,
							"energy": 0.0,
							"resistance": 0.0,
							"power": 0.0
						}

# Stores the relationships between the electric values (current, voltage, etc)
# can this information be stored in a better way?
list_ElectricFormulas = [
						{"gives": voltage, "wants": ["current", "resistance"], formula="current*resistace" }
						]
						
# dict_ElectricVariables is passed to this function
def solveInput(dict_Variables):
	pass

''' some ideas on how to represent the relationships between variables

# Store the unit values absolutely (convert from mV format)
dict_ElecUnit = { "type": "voltage", "value": 5.0 }


# Define a queue of operations that should be perfomed? 
dict_ElecReltn = { "output": "voltage", "ops": ["I", "*", "R"]

# For any relationship we have
- the output variable
- the two input variables
- the operation(s) that must be done to and between both inputs


We know
- Which values we have
- What formulas there are
so if we define
voltage=current*resistance
we can use string operations to get the variables "current" and "resistance" and pull their values from the dict_Variables

Could write a parser that fetches that values of variables as needed and applies operators either between two values (by looking at the 'current' value and the 'next' value) or to a (current) value (like square)
could write the python code that should be executed and use that exec() (?) function

could structure the formulas like
list_dict_ElecReltns = [{ "wants": ["current", "resistance"], "gives":"voltage", "formula"=<formula> }]

We make a list of electrical relations which are:
"wants" mapped to a list of the values needed
"gives" mapped to the output value
"formula" which maps to some kind of format that tells us which variables to use and what to do them
Defining formula exactly is harder, we could
	- put in essentially normal math format and writer a parser for that (like "current*resistance" or "radius^2"
	- put in the raw python code to execute and execute it
	- have a function that just has all the if statements 
		- if the two inputs are not None and the output is None, run the calculation
		- we can this with exec(string) !
	
	def exec_Formula(dict_Variables, wants, formula):
		# Check that all our values are present
		for want in wants:
			if( dict_Variables[want] is None ):
				return None
		
		# We can either define a local dictionary with attributes "current", "voltage", etc
		# and then in the formula the code would be like formula='vars["current"]*vars["voltage]'
		# or we could have formula='current*voltage'. This would require the local vars to be set
		# We could set this by execcing ("%s = %d" %(want, dict_Variables[want]=))
		# The dict is safer but this is a local-only, non networked, hardcoded program so I think it's acceptable
		return exec(formula)

'''

	
'''
Electrical relationships (for a single resistor with DC):

# Voltage: v
v=I*R
v=E/Q

# Current: I
I=V/R

# Power: P


# Charge: Q


# Time: t


# Resistance: R
R=V/I

# Energy: E


'''
