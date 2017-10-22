from nose.tools import *
from NeoElectricityFormulas import NeoElectricityFormulas as Solver

def test_input_simple():
	test1 = "I=1A v=2V"
	Solver.parseInput(test1)


