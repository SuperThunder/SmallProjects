from nose.tools import *
import NeoElectricityFormulas as Solver

def test_input_simple():
	test1 = "I=1A v=2V"
	Solver.parseInput(test1)

def setup():
    print "Setup"
    
def teardown():
    print "Teardown"

def test_basic():
    print "Test ran"

