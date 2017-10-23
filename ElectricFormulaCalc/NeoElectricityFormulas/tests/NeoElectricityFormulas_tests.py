from nose.tools import *
from NeoElectricityFormulas import NeoElectricityFormulas as Solver

# Valid test cases - meant to run with no errors
def test_input_simple():
	test1 = "I=1A v=2V"
	output = Solver.parseInput(test1)
	print(output)

def test_input_simple_scale():
	print("")
	test1 = "I=1mA E=3MJ"
	output = Solver.parseInput(test1)
	print(output)

def test_input_float():
	print("")
	test1 = "P=4.0W Q=8C"
	test2 = "v=8.0535V R=85mO"
	# Shortening Ohm to O makes things very ambiguous
	# In the future we will want the option of 2/3 characters units (Ohm, sec, min, hr, etc)
	test3 = "R=100O P=4923.234234W"
	
	tests = [test1, test2, test3]
	for test in tests:
		output = Solver.parseInput(test)
		print(output)


# todo: write invalid test cases:
# subtle (missing unit, two periods, bad character, etc)
# outrageous (complete garbled input)
# random (generate some random characters and input them)
# large (use very large numbers)
