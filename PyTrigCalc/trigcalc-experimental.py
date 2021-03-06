print "crappytrigcalc\n Please arrange your triangle so that:\n\t If you know 1 angle and 2+ sides the known angle is angle A, or\n\t if you know 1 side and 2+ angles the known side is side a"

import math #used for trigonometric functions

def main():
	if __name__ == '__main__':	
		while True:
	
			trisolve = TrigFunctions()
	
			if raw_input("is the triangle right-angled (y/n)") == "y": #find whether triangle is right
				isright = True
				"\n Label and input your triangle so that A is a known angle and C is the 90 degree angle"
			else:
				isright = False
	
			angleA, angleB, angleC, noofangles, AnglesKnown = angleinput()	
			sidea, sideb, sidec, SidesKnown = sideinput() 
	
			angleA = math.radians(angleA) #convert to radians from degrees as Python's trig functions use radians
			angleB = math.radians(angleB)
			angleC = math.radians(angleC)
	
			if  isright == True:
				angleC = 90
				print "now solving a right angled triangle with the values provided"
				if 'a' in SidesKnown and not 'b' in SidesKnown and not 'c' in SidesKnown:
					angleA, angleB, sidea, sideb, sidec = trisolve.AngASida(angleA, sidea)
				elif 'b' in SidesKnown and not 'a' in SidesKnown and not 'c' in SidesKnown:
					angleA, angleB, sidea, sideb, sidec = trisolve.AngASidb(angleA, sideb)
				elif 'c' in SidesKnown and not 'b' in SidesKnown and not 'a' in SidesKnown:
					angleA, angleB, sidea, sideb, sidec = trisolve.AngASidc(angleA, sidec)
				elif 'a' and 'b' and 'c' in SidesKnown: 
					angleA, angleB, angleC, sidea, sideb, sidec = trisolve.Sidabc(sidea, sideb, sidec)
					print angleA, angleB, angleC #debugging prints since output was completely wrong
				results = ("\nAngle A: " + str(math.degrees(angleA)) + "\nAngle B: " + str(math.degrees(angleB)) + "\nAngle C: 90 (cuz it's a right triangle duh)" + "\nSide a: " + str(sidea) + "\nSide b: " + str(sideb) + "\nSide c: " + str(sidec))
			else:
				print "now solving a non-right angled triangle with the values given", SidesKnown, AnglesKnown
				if noofangles == 1:
					if 'a' in SidesKnown and 'b' in SidesKnown:
						angleA, angleB, angleC, sidea, sideb, sidec = trisolve.AngASidab(angleA, sidea, sideb)
					if 'a' in SidesKnown and 'c' in SidesKnown:
						angleA, angleB, angleC, sidea, sideb, sidec = trisolve.AngASidac(angleA, sidea, sidec)
					if 'b' in SidesKnown and 'c' in SidesKnown:
						angleA, angleB, angleC, sidea, sideb, sidec = trisolve.AngASidbc(angleA, sideb, sidec)
					else:
						print "insufficient sides"
						break

				elif noofangles >= 2:
					if 'a' in AnglesKnown.lower() and 'b' in AnglesKnown.lower():
						angleA, angleB, angleC, sidea, sideb, sidec = trisolve.SidaAngAB(sidea, angleA, angleB)
					elif 'a' in AnglesKnown.lower() and 'c' in AnglesKnown.lower():
						angleA, angleB, angleC, sidea, sideb, sidec = trisolve.SidaAngAC(sidea, angleA, angleC)
					elif 'b' in AnglesKnown.lower() and 'c' in AnglesKnown.lower():
						angleA, angleB, angleC, sidea, sideb, sidec = trisolve.SidaAngBC(sidea, angleB, angleC)
					else:
						print "insufficient angles"
						break
				elif noofangles == 0:
					angleA, angleB, angleC, sidea, sideb, sidec = trisolve.Sidabc(sidea, sideb, sidec)
									

							
				results = ("\nAngle A: " + str(math.degrees(angleA)) + "\nAngle B: " + str(math.degrees(angleB)) + "\nAngle C: " + str(math.degrees(angleC)) + "\nSide a: " + str(sidea) + "\nSide b: " + str(sideb) + "\nSide c: " + str(sidec))
			print results	
		
def angleinput(): 

	angleA = 0 # don't ask why this is here. it makes python happy.
	angleB = 0
	angleC = 0
	noofangles = 0
	
	AnglesKnown = raw_input("Enter the angles you know the value to (so enter A, B, and/or C)")
	
	def AngleInputA():
		angleA = float(raw_input("Enter the value of Angle A: "))
		return angleA

	def AngleInputB():
		angleB = float(raw_input("Enter the value of Angle B: "))
		return angleB
	
	def AngleInputC():
		angleC = float(raw_input("Enter the value of Angle C: "))	
		return angleC
		
	if 'a' in AnglesKnown.lower():
		angleA = AngleInputA()
		noofangles += 1
	if 'b' in AnglesKnown.lower():
		angleB = AngleInputB()
		noofangles += 1
	if 'c' in AnglesKnown.lower():
		angleC = AngleInputC()
		noofangles += 1
	print noofangles
	return(angleA, angleB, angleC, noofangles, AnglesKnown)
	
def sideinput():

	sidea = 0
	sideb = 0
	sidec = 0
		
	SidesKnown = raw_input("Enter the sides you know the value to (so enter a, b, and/or c): ") 
	
	def SideInputA(): 
		sidea = float(raw_input("Enter the value of Side A: "))
		return sidea
		
	def SideInputB():
		sideb = float(raw_input("Enter the value of Side B: "))
		return sideb
	
	def SideInputC():
		sidec = float(raw_input("Enter the value of Side C: "))
		return sidec
		
	if 'a' in SidesKnown:
		sidea = SideInputA()
	if 'b' in SidesKnown:
		sideb = SideInputB()
	if 'c' in SidesKnown:
		sidec = SideInputC()
	
	return(sidea, sideb, sidec, SidesKnown)
	
class TrigFunctions(object): #the idea with this class was to have all the base solving functions for certain sides be easily accessible, but it's ended up more like having all the cases for solving consolidated
	
	def AngASida(self, angleA, sidea): #WARNING: only call 2 term functions for right angled triangle solving!
		sidec = sidea/(math.sin(angleA))
		sideb = sidea/(math.tan(angleA))
		angleB = math.atan(sideb/sidea) #using trig for this isn't really necesarry, you could do math.pi - the known angles
		return(angleA, angleB, sidea, sideb, sidec) # angleC is not returned here because it's the known 90 degree angle
	def AngASidb(self, angleA, sideb):
		sidea = (math.tan(angleA))*sideb
		sidec = sidea/(math.sin(angleA)) #equations here and for angleB are copied from AngASida, in future should rewrite to use given values
		angleB = math.atan(sideb/sidea)
		return(angleA, angleB, sidea, sideb, sidec)
	def AngASidc(self, angleA, sidec):
		sidea = (math.sin(angleA))*sidec
		sideb = sidea/(math.tan(angleA)) #equations here and for angleB are copied from AngASida, in future should rewrite to use given values
		angleB = math.atan(sideb/sidea)
		return(angleA, angleB, sidea, sideb, sidec)
	def Sidabc(self, sidea, sideb, sidec): #cos law under here previously had a - where a + should have been, other parts may still be broken
		angleA = math.acos((sideb**2+sidec**2-sidea**2)/(2*sideb*sidec))
		angleB = math.acos((sidea**2+sidec**2-sideb**2)/(2*sidea*sidec))
		angleC = math.acos((sidea**2+sideb**2-sidec**2)/(2*sidea*sideb))
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidab(self, angleA, sidea, sideb):
		angleB = math.asin((math.sin(angleA)/sidea)*sideb)
		angleC = math.pi - angleA - angleB
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidac(self, angleA, sidea, sidec):
		angleC = math.asin((math.sin(angleA)/sidea)*sidec)
		angleB = math.pi - angleA - angleC
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def AngASidbc(self, angleA, sideb, sidec):
		sidea = math.sqrt((sideb**2+sidec**2)-2*sideb*sidec*math.cos(angleA))
		angleB = math.acos((sidea**2-sideb**2-sidec**2)/(-2*sidea*sidec))
		angleC = math.pi - angleA - angleB
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def SidaAngAB(self, sidea, angleA, angleB):
		angleC = math.pi - angleA - angleB
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def SidaAngAC(self, sidea, angleA, angleC):
		angleB = math.pi - angleA - angleC
		print angleB, angleA, angleC
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	def SidaAngBC(self, sidea, angleB, angleC):
		angleA = math.pi - angleB - angleC
		sideb = (sidea/math.sin(angleA))*math.sin(angleB)
		sidec = (sidea/math.sin(angleA))*math.sin(angleC)
		return(angleA, angleB, angleC, sidea, sideb, sidec)
	

	
main()
