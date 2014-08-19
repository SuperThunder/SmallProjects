print "Trig Calc Testing Environment"

import trigcalc
trigfunctionstest = trigcalc.TrigFunctions

def AngASidaTest():	
	trigcalc.TrigFunctions.AngASidA(angleA, sidea)

def SideabcTest():
	sidea = 3; sideb = 4; sidec = 5;
	angleA, angleB, angleC, sidea, sideb, sidec = trigfunctionstest.Sidabc(sidea, sideb, sidec)
	results(angleA, angleB, angleC, sidea, sideb, sidec)

def results(angleA, angleB, angleC, sidea, sideb, sidec):
	results = ("\nAngle A: " + str(math.degrees(angleA)) + "\nAngle B: " + str(math.degrees(angleB)) + "\nAngle C: " + str(math.degrees(angleC)) + "\nSide a: " + str(sidea) + "\nSide b: " + str(sideb) + "\nSide c: " + str(sidec))
	print results

SideabcTest()	
