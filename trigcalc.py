print "crappytrigcalc\n"

import math #used for trigonometric functions,

def main():

	if raw_input("is the triangle right-angled (y/n)") == "y": #find whether triangle is right
		isright = True
	else:
		isright = False
	
	noofangles = int(raw_input("how many angles do you know?"))
	noofsides = int(raw_input("how many sides do you know?"))
	
	angleA, angleB, angleC = angleinput(noofangles) #get as many angles as the user knows (maxes at 3)	
	sidea, sideb, sidec = sideinput(noofsides) #get as many sides as the user knows (maxes at 3)
	
	angleA = math.radians(angleA) #convert ro radians from degrees as Python's trig funcions use radians
	angleB = math.radians(angleB)
	angleC = math.radians(angleC)
	
	if  isright == True:
		print "now solving a right angled triangled with the values provided", "\n Label and input your triangle so that A is a known angle and C is the 90 degree angle"
		rightanglesolve(angleA, angleB, angleC, sidea, sideb, sidec)
	else:
		print "now solving a non-right angled triangle with the values given"
		nonrightsolve(angleA, angleB, angleC, sidea, sideb, sidec)
	
#getting angle values, assume user is using degrees
def angleinput(noofangles):

	angleA = 0 # don't ask why this is here. it makes python happy.#
	angleB = 0
	angleC = 0
	
	if noofangles == 1:
		angleA = int(raw_input("enter angle A's value in degrees "))
	elif noofangles == 2:
		angleA = int(raw_input("enter angle A's value in degrees "))
		angleB = int(raw_input("enter angle B "))
	elif noofangles >= 3: #assume that if user enters angle value greater than 3 it's a mistype
		angleA = int(raw_input("enter angle A's value in degrees "))
		angleB = int(raw_input("enter angle B "))
		angleC = int(raw_input("enter angle C "))
	
	return(angleA, angleB, angleC)
	#if angleA or angleB or angleC >= 91:
	#	print "cannot solve an obtuse triangle!"
	

#getting side lengths
def sideinput(noofsides):

	sidea = 0
	sideb = 0
	sidec = 0
	
	#def invidiualinput(actualsideinput) #can't remember what I was trying to do here
		
	SidesToSolve = raw_input("Which sides do you know the values to? (enter a, b, and/or c, so all three would abc)") 
	
	#there's gotta be a better way to do this but this works so whatever
	
	def SideInputA(): 
		sidea = int(raw_input("Enter the value of Side A"))
		return sidea
		
	def SideInputB():
		sideb = int(raw_input("Enter the value of Side B"))
		return sideb
	
	def SideInputC():
		sidec = int(raw_input("Enter the value of Side C"))
		return sidec
		
	if 'a' in SidesToSolve:
		sidea = SideInputA()
	elif 'b' in SidesToSolve:
		sideb = SideInputB()
	elif 'c' in SidesToSolve:
		sidec = SideInputC()
	
	return(sidea, sideb, sidec)
	
class TrigFunctions(object) #the idea with this class was to have all the base solving functions for certain sides be easily accessible, but it's ended up more like having all the cases for solving consolidated
	
	def AngASida(angleA, sidea) #WARNING: only call 2 term functions for right angled triangle solving!
		sidec = sidea/(math.sin(angleA))
		sideb = sidea/(math.tan(angleA))
		angleB = math.atan(sideb/sidea) #using trig for this isn't really necesarry, you could do 
		return(angleA, angleB, sidea, sideb, sidec) # angleC is not returned here because it's the known 90 degree angle
	def AngASidb(angleA, sideb)
		sidea = (math.tan(angleA))*sideb
		sidec = sidea/(math.sin(angleA)) #equations here and for angleB are copied from AngASida, in future should rewrite to use given values
		angleB = math.atan(sideb/sidea)
		return(angleA, angleB, sidea, sideb, sidec)
	def AngASidc(angleA, sidec)
		sidea = (math.sin(angleA))*sidec
		sideb = sidea/(math.tan(angleA)) #equations here and for angleB are copied from AngASida, in future should rewrite to use given values
		angleB = math.atan(sideb/sidea)
		return(angleA, angleB, sidea, sideb, sidec)
	def Sidabc
		angleA = math.acos((sidea^2-sideb^2-sidec^2)/(-2*sideb*sidec))
		angleB = math.acos((sidea^2-sideb^2-sidec^2)/(-2*sidea*sidec))
		angleC = math.acos((sidea^2-sideb^2-sidec^2)/(-2*sidea*sideb))
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidab
		angleB = math.asin((math.sin(angleA)/sidea)*sideb)
		angleC = 180 - angleA - angleB
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidac	
		angleC = math.asin((math.sin(AngleA)/sidea)*sidec)
		angleB = 180 - angleA - angleC
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidbc
		sidea = math.sqrt((sideb^2+sidec^2)-2*sideb*sidec*math.cos(angleA))
		angleB = math.acos((sidea^2-sideb^2-sidec^2)/(-2*sidea*sidec))
		angleC = 180 - angleA - angleC
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	
	
	
	#__OLD CODE__
	#calculate all the values in a right triangle from an angle, a side, and the implied right angle 
#def rightanglesolve(angleA, angleB, angleC, sidea, sideb, sidec):
#	
#	sidec = sidea/(math.sin(angleA))
#	sideb = sidea/(math.tan(angleA))
#	angleB = math.atan(sideb/sidea) #use tan for this so that the given a value is used, reduce round error
#	
#	print "\nAngle A is ", math.degrees(angleA), "\nAngle B is ", math.degrees(angleB), "\nAngle C is 90, or should be because it's the implied right angle you said existed", "\nSide A is ", sidea, "\nSide B is ", sideb, "\nSide C is ", sidec
	
#def nonrightsolve(angleA, angleB, angleC, sidea, sideb, sidec):
#	print "lol how do I solve this"
	
main()
