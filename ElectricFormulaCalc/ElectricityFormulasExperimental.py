'''
Created on Apr 25, 2-114
'''

''' ToDo
Change program so that it takes the variables the user has and calculates as many values as possible
Could possibly do this by having program try every formula it has values for;
determining whether or not it has a value by if the value equals to -1;
(which would be set by default)

Setup loop so that user can exit out of it
'''

# Converts between common electricity formulas and variables
print "Common Electricity Formulae Conversion Alpha\nNote this program does not handle significant figures!"



looptrue = True
while(looptrue == True):




    # Give user options and ask what they want to do or (NOT IMPLEMENTED: if they want to quit), bad input = ask again
	def main():
        
		# The variables used in input/calculation
		current = float(-1) # Variable is I, formula I=q/t, unit Amperes (A)
		charge = float(-1) # Variable is q, formula q=t(I), unit Coulombs (C)
		time = float(-1) # Variable is t, formula t=q/I, unit Seconds (S)
		voltage = float(-1) # Variable is V, formula V=E/q, unit Volts (V)
		energy = float(-1) # Variable is E, E=V(q), unit Joules (J)
		resistance = float(-1) # Variable is R, formula R=V/I, unit Ohms (Greek letter omega)
		power = float(-1) # Variable is P, formula P=E/t, unit Watts (W)
		sigfigs = int(-1) # Variable used to control significant figures, not currently implemented

		# Strings used to quickly print often used phrases
		currentstr = "Current(I), measured in Amperes(A) "
		chargestr = "Charge(q), measured in Coulombs (C) "
		timestr = "Time (t), measured in Seconds (S) "
		voltagestr = "Voltage (V), measured in Volts(V) "
		energystr = "Energy, (E), measured in Joules(J) "
		resistancestr = "Resistance (R), measured in Ohms (Omega) "
		powerstr = "Power (P), measured in Watts (W) "
		valuefor = "Enter the value for "

		print "\nEnter the values you know from the following list\n\t", currentstr,"\n\t", chargestr, "\n\t", timestr,
        	print  "\n\t", voltagestr, "\n\t", energystr, "\n\t", resistancestr, "\n\t", powerstr
        	runchoice = str(raw_input(""))
        	
		if "current" in runchoice.lower(): #forgot about my commonly used strings when writing this part
		    current = float(raw_input("Enter the value for current, measured in Amperes (A)"))
		if "charge" in runchoice.lower():
		    charge = float(raw_input("Enter the value for charge, measured in Coulombs (C)"))
		if "time" in runchoice.lower():
		    time = float(raw_input("Enter the value for time, measured in Seconds (S)"))
		if "voltage" in runchoice.lower():
		    voltage = float(raw_input("Enter the value for voltage, measured in Volts (V)"))
		if "energy" in runchoice.lower():
		    energy = float(raw_input("Enter the value for energy, measured in Joules (J)"))
		if "resistance" in runchoice.lower():
		    resistance = float(raw_input("Enter the value for resistance, measured in Ohms (Omega)"))
		if "power" in runchoice.lower():
		    power = float(raw_input("Enter the value for power, measured in Watts (W)"))
	
		for i in range(5): #go through all the solving equations 5 times to make really sure we have everything we can get
#could probably simplify this a bit by having a couple of tiers for the ifs, like especially for a variable like power...	
			if charge != -1 and time != -1:
				current = charge/time
			if time != -1 and current != -1:
				charge = time*current
			if charge != -1 and current != -1:
				time = charge/current
			if energy != -1 and charge != -1:
				voltage = energy/charge
			if voltage != -1 and charge != -1:
				energy = voltage*charge
			if energy != -1 and voltage != -1:
				charge = energy/voltage
			if voltage != -1 and current != -1:
				resistance = voltage/current
				power = voltage*current
			if resistance != -1 and current != -1:
				voltage = resistance*current
				power = resistance*current**2
			if voltage != -1 and resistance != -1:			
				current = voltage/resistance
				power = voltage**2/resistance
			if energy != -1 and time != -1:			
				power = energy/time
			if power != -1 and time != -1:
				energy = power*time
			if energy != -1 and power != -1:		
				time = energy/power
			if power != -1 and voltage != -1:
				current = power/voltage
				resistance = voltage**2/power
			if power != -1 and resistance != -1:
				current = (power/resistance)**0.5
				voltage = (power*resistance)**0.5			        
			if power != -1 and current != -1:
				resistance = power/current**2	

			results = "\n" + currentstr + str(current) + "\n" + chargestr + str(charge) + "\n" + timestr + str(time) + "\n" + voltagestr + str(voltage) + "\n" + energystr + str(energy) + "\n" + resistancestr + str(resistance) + "\n" + powerstr + str(power) + "\n"
			print "Results of the calculation, a value of -1 means there was insufficient data to calculate:", results, "\n"

	main() # Starts program
