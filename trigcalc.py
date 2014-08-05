print "crappytrigcalc\n"

import math #used for trigonometric functions,

def main():
	
	print("enter main")
	
	angleA = 0 #need to declare vars here or python throws a UnboundLocalError fit
	angleB = 0
	angleC = 0
	
	if raw_input("is the triangle right-angled (y/n)") == "y": #find whether triangle is right
		isright = True
	
	noofangles = int(raw_input("how many angles do you know?"))
	noofsides = int(raw_input("how many sides do you know?"))
	
	angleinput(noofangles) #get as many angles as the user knows (maxes at 3)
	return angleA, angleB, angleC	
		
	sideinput(noofsides) #get as many sides as the user knows (maxes at 3)
	return sidea, sideb, sidec
	
	angleA = math.radians(angleA) #convert ro radians from degrees as Python's trig funcions use radians
	angleB = math.radians(angleB)
	angleC = math.radians(angleC)
	
	if  isright == True:
		print "now solving a right angled triangled with the values"
		rightanglesolve(angleA, angleB, angleC, sidea, sideb, sidec)
	else:
		print "now solving a non-right angled triangle with the values given"
		nonrightsolve(angleA, angleB, angleC, sidea, sideb, sidec)

#getting angle values, assume user is using degrees
def angleinput(noofangles):

	print("enter angleinput")

	angleA = 0
	angleB = 0
	angleC = 0
	
	if noofangles == 1:
		angleA = int(raw_input("enter angle A's value in degrees"))
	if noofangles == 2:
		angleA = int(raw_input("enter angle A's value in degrees"))
		angleB = int(raw_input("enter angle B"))
	if noofangles >= 3: #assume that if user enters angle value greater than 3 it's a mistype
		angleA = int(raw_input("enter angle A's value in degrees"))
		angleB = int(raw_input("enter angle B"))
		angleC = int(raw_input("enter angle C"))
	
	#if angleA or angleB or angleC >= 91:
	#	print "cannot solve an obtuse triangle!"
	

#getting side lengths
def sideinput(noofsides):

	print("enter sideinput")
	
	sidea = round(0)
	sideb = round(0)
	sidec = round(0)

	if noofsides == 1:
		sidea = int(raw_input("enter side a"))

	if noofsides == 2:
		sidea = int(raw_input("enter side a"))
		sideb = int(raw_input("enter side b"))

	if noofsides >= 3:
		sidea = int(raw_input("enter side a"))
		sideb = int(raw_input("enter side b"))	
		sidec = int(raw_input("enter side c"))

#calculate all the values in a right triangle from an angle, a side, and the implied right angle
def rightanglesolve(angleA, angleB, angleC, sidea, sideb, sidec):
	
	print("enterrightanglesolve")

	sidec = sidea/(math.sin(angleA))
	sideb = sidea/(math.tan(angleA))
	angleB = math.atan(sideb/sidea) #use tan for this so that the given a value is used, reduce round error

def nonrightsolve(angleA, angleB, angleC, sidea, sideb, sidec):
	print "lol how do I solve this"
	
main()
