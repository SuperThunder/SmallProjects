print "crappytrigcalc\n"

import math #used for trigonometric functions,

def main():

	if raw_input("is the triangle right-angled (y/n)") == "y": #find whether triangle is right
		isright = True
	else:
		isright = False
	
	noofangles = int(raw_input("how many angles do you know?"))
	noofsides = int(raw_input("how many sides do you know?"))
	
	angleA, angleB, angleC = angleinput(noofangles)	
	sidea, sideb, sidec = sideinput(noofsides) 
	
	angleA = math.radians(angleA) #convert ro radians from degrees as Python's trig functions use radians
	angleB = math.radians(angleB)
	angleC = math.radians(angleC)
	
	if  isright == True:
		print "now solving a right angled triangled with the values provided", "\n Label and input your triangle so that A is a known angle and C is the 90 degree angle"
		rightanglesolve(angleA, angleB, angleC, sidea, sideb, sidec)
	else:
		print "now solving a non-right angled triangle with the values given"
		nonrightsolve(angleA, angleB, angleC, sidea, sideb, sidec)
	

def angleinput(noofangles):

	angleA = 0 # don't ask why this is here. it makes python happy.
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
	
def sideinput(noofsides):

	sidea = 0
	sideb = 0
	sidec = 0
		
	SidesToSolve = raw_input("Which sides do you know the values to? (enter a, b, and/or c, so all three would abc)") 
	
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
	
class TrigFunctions(object): #the idea with this class was to have all the base solving functions for certain sides be easily accessible, but it's ended up more like having all the cases for solving consolidated
	
	def AngASida(angleA, sidea): #WARNING: only call 2 term functions for right angled triangle solving!
		sidec = sidea/(math.sin(angleA))
		sideb = sidea/(math.tan(angleA))
		angleB = math.atan(sideb/sidea) #using trig for this isn't really necesarry, you could do 180 - the known angles
		return(angleA, angleB, sidea, sideb, sidec) # angleC is not returned here because it's the known 90 degree angle
	def AngASidb(angleA, sideb):
		sidea = (math.tan(angleA))*sideb
		sidec = sidea/(math.sin(angleA)) #equations here and for angleB are copied from AngASida, in future should rewrite to use given values
		angleB = math.atan(sideb/sidea)
		return(angleA, angleB, sidea, sideb, sidec)
	def AngASidc(angleA, sidec):
		sidea = (math.sin(angleA))*sidec
		sideb = sidea/(math.tan(angleA)) #equations here and for angleB are copied from AngASida, in future should rewrite to use given values
		angleB = math.atan(sideb/sidea)
		return(angleA, angleB, sidea, sideb, sidec)
	def Sidabc(sidea, sideb, sidec):
		angleA = math.acos((sidea^2-sideb^2-sidec^2)/(-2*sideb*sidec))
		angleB = math.acos((sidea^2-sideb^2-sidec^2)/(-2*sidea*sidec))
		angleC = math.acos((sidea^2-sideb^2-sidec^2)/(-2*sidea*sideb))
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidab(angleA, sidea, sideb):
		angleB = math.asin((math.sin(angleA)/sidea)*sideb)
		angleC = 180 - angleA - angleB
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidac(angleA, sidea, sidec):	
		angleC = math.asin((math.sin(AngleA)/sidea)*sidec)
		angleB = 180 - angleA - angleC
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidbc(angleA, sideb, sidec):
		sidea = math.sqrt((sideb^2+sidec^2)-2*sideb*sidec*math.cos(angleA))
		angleB = math.acos((sidea^2-sideb^2-sidec^2)/(-2*sidea*sidec))
		angleC = 180 - angleA - angleC
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def SidaAngAB(sidea, angleA, angleB):
		angleC = 180 - angleA - angleB
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def SidaAngAC(sidea, angleA, angleC):
		angleB = 180 - angleA - angleC
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def SidaAngBC(sidea, angleB, angleC):
		angleA = 180 - angleB - angleC
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	

	
main()
