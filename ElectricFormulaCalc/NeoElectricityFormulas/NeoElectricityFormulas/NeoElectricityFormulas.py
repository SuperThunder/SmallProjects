dict_ScientificPrefixes = {
							"u": 0.000001,
							"m": 0.001,
							"k": 1000.0,
							"M": 1000000.0,
							"G": 1000000000.0
							}

# Right now the only unit for time is seconds!
# This describes the variable letters for the different units
dict_ElectricUnits = {
						"t": "time",
						"I": "current",
						"v": "voltage",
						"V": "voltage",
						"Q": "charge",
						"R": "resistance",
						"P": "power",
						"E": "energy"
						}

# This describes the unit letters assigned to each unit
dict_ElectricVariables = {
						"s": "time",
						"A": "current",
						"V": "voltage",
						"C": "charge",
						"O": "resistance",
						"W": "power",
						"J": "energy"
						}

# is there a better way to store the variable values?
dict_ElectricVariableValues = { 
							# Possibly want to initialize to None
							"current": 0.0,
							"voltage": 0.0,
							"time": 0.0,
							"charge": 0.0,
							"energy": 0.0,
							"resistance": 0.0,
							"power": 0.0
						}

# Stores the relationships between the electric values (current, voltage, etc)
# can this information be stored in a better way?
list_ElectricFormulas = [
						{"gives": "voltage", "wants":["current", "resistance"], "formula":"current*resistance" },
						{"gives": "voltage", "wants":["", ""], "formula":"" },
						{"gives": "voltage", "wants":["", ""], "formula":"" },
						{"gives": "current", "wants":["", ""], "formula":"" },
						{"gives": "resistance", "wants": ["", ""], "formula":"" },
						{"gives": "energy", "wants":["", ""], "formula":"" }
						]



def parseInput(str_Input):
	import re
	# assuming the input comes in as one string like I=2A V=2mV R=802.37kOhm
	tokens = str_Input.split(" ")
	#print(tokens)
	
	dict_InputValues = {}
	for token in tokens:
		# refine - this assumes the input was done exactly right
		parts = token.split("=")
		#print("Letter: %s"%parts[0])
		#print("Value: %s"%parts[1])
		
		token_Variable = dict_ElectricUnits[parts[0]]
		#print("Value is for %s"%token_Variable)
		
		# the input has been split into the variable and its value
		# but we still need to split the value into its number component, scale component, and unit (although the unit is never going to be different)
		# Regex to split into number and unit. integer number or decimal number followed by at least one letter
		pattern_Value = re.compile( "^([0-9]+|[0-9]+\.[0-9]+)([a-zA-Z]+)$" )
		pattern_match = pattern_Value.match( parts[1] )
		token_Values = pattern_match.groups()
		
		print(token_Values)
		# Get the number, should always be present
		token_Number = token_Values[0]
		# Get the letters following the number
		if( len(token_Values) == 2 ):
			token_Unit = token_Values[1]			
		else:
			token_Unit = "" # No unit provided - default to no prefix metric
		
		
		# Currently, our system is only one letter for scale and only one letter for unit
		# Units are assumed to be metric and time assumed to be seconds, so for now the second letter can be disregarded
		if( len(token_Unit)==0):
			# no unit given
			pass
		elif( len(token_Unit)==1 ):
			# only one character in unit - could be the unit (V, A, etc) or the scale (m, k, M, etc)
			# Accepting either is a sketchy feature - we may want to enforce unit only!
			if(token_Unit in dict_ScientificPrefixes.keys()):
				token_Prefix = dict_ScientificPrefixes[ token_Unit ]
			elif(token_Unit in dict_ElectricVariables.keys()):
				# We don't use the unit letter for anything, but it is valid
				token_Prefix = 1
			else:
				print("Unknown SI prefix or unit letter!\t'%s'"%token_Unit)
				
		elif( len(token_Unit)==2 ):
			# two chars - both scale and unit should be present
			token_Prefix = dict_ScientificPrefixes[ token_Unit[0] ]
			assert( token_Unit[1] in dict_ElectricVariables )
		else:
			print("Too many characters in unit!")
		
		# the value needs to be converted from something like 5V or 2.05GW to a float
		# Once we have a float we can put the value in the dictionary by name
		token_ScaledValue = float(token_Number) * token_Prefix
		#print("Scaled value of %f (%s)"%(token_ScaledValue, token_Variable))
		
		dict_InputValues[ token_Variable ] = token_ScaledValue
	
	
	return dict_InputValues
	
	
						
# dict_ElectricVariables is passed to this function
def solveInput(dict_Variables):
	def exec_Formula(dict_Variables, wants, formula):
		# Check that all our values are present
		for want in wants:
			if( dict_Variables[want] is None ):
				return None
		
		# set the values that will be needed by the formula
		for want in wants:
			# need to specify the namesace
			exec( "%s = %f"%( want, dict_Variables[want] ), globals(), locals() )
		
		# exec should work here too
		value = eval(formula)
		return value
	
	# cycle through all the formulas and try to get more values with them
	for dict_Formula in list_ElectricFormulas:
		wants = dict_Formula["wants"]
		gives = dict_Formula["gives"]
		formula = dict_Formula["formula"]
		
		# don't run the formula if we already have the value
		if( dict_Variables["gives"]==None ):
			dict_Variables["gives"] = exec_Formula(dict_Variables, wants, formula)
			



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
v=(P*R)**0.5

# Current: I
I=v/R
I=Q/t
I=(P/R)**0.5
I=P/v

# Power: P
P=v*I
P=(v**2)/R
P=R*(I**2)
P=E/t

# Charge: Q
Q=t*I
Q=E/v

# Time: t
t=Q/I
t=E/P

# Resistance: R
R=v/I
R=P/(I**2)
R=(v**2)/power

# Energy: E
E=V*Q
E=P*t

'''
