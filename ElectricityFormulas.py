'''
Created on Apr 25, 2014
'''

''' ToDo
Change program so that it takes the variables the user has and calculates as many values as possible
Could possibly do this by having program try every formula it has values for;
determining whether or not it has a value by if the value equals to 0;
(which would be set by default)

Setup loop so that user can exit out of it
'''

# Converts between common electricity formulas and variables
print "Common Electricity Formulae Conversion Alpha\nNote this program does not handle significant figures!"

# The variables used in input/calculation
current = float(0) # Variable is I, formula I=q/t, unit Amperes (A)
charge = float(0) # Variable is q, formula q=t(I), unit Coulombs (C)
time = float(0) # Variable is t, formula t=q/I, unit Seconds (S)
voltage = float(0) # Variable is V, formula V=E/q, unit Volts (V)
energy = float(0) # Variable is E, E=V(q), unit Joules (J)
resistance = float(0) # Variable is R, formula R=V/I, unit Ohms (Greek letter omega)
power = float(0) # Variable is P, formula P=E/t, unit Watts (W)
sigfigs = int(0) # Variable used to control significant figures, not currently implemented

# Strings used to quickly print often used phrases
currentstr = "Current(I), measured in Amperes(A)"
chargestr = "Charge(q), measured in Coulombs (C)"
timestr = "Time (t), measured in Seconds (S)"
voltagestr = "Voltage (V), measured in Volts(V)"
energystr = "Energy, (E), measured in Joules(J)"
resistancestr = "Resistance (R), measured in Ohms (Omega)"
powerstr = "Power (P), measured in Watts (W)"
valuefor = "Enter the value for"


looptrue = True
while(looptrue == True):
    # Give user options and ask what they want to do or (NOT IMPLEMENTED: if they want to quit), bad input = ask again
    def main():
        print "\nType in the value you wish to solve for\n\t", currentstr,"\n\t", chargestr, "\n\t", timestr,
        print  "\n\t", voltagestr, "\n\t", energystr, "\n\t", resistancestr, "\n\t", powerstr
        runchoice = str(raw_input(""))
        if(runchoice.lower() == "current"): # Goes to function based on what user typed
            current() 
        elif(runchoice.lower() == "charge"):
            charge()
        elif(runchoice.lower() == "time"):
            time()
        elif(runchoice.lower() == "voltage"):
            voltage()
        elif(runchoice.lower() == "energy"):
            energy()
        else: 
            print "Invalid Input"
            main()  # Restart to main if input was not recognized
        
    # Solving for Current
    def current():
        charge = float(raw_input("Enter the value for Charge (q), as measured in Coulombs (C): "))
        time = float(raw_input("Enter the value for Time (t), as measured in Seconds (S): "))
        current = charge / time
        print "The current of ", charge, "coulombs over ", time, "seconds", "is ", current, "amperes."
        raw_input()
        main() # Go back to main function after user presses Enter
        
    # Solving for Charge
    def charge():
        current = float(raw_input("Enter the value for Current (I), as measured in Amperes (A): "))
        time = float(raw_input("Enter the value for time (t), as measured in Seconds (S): "))
        charge = time*current
        print "The charge of ", current, "amperes for ", time, "seconds is ", charge, "coulombs."
        raw_input()
        main()
        
    # Solving for Time    
    def time():
        current = float(raw_input("Enter the value for Current (I), as measured in Amperes (A): "))
        charge = float(raw_input("Enter the value for Charge (q), as measured in Coulombs (C)"))
        time = charge / current
        print "The time taken by ", charge, "coulombs at ", current, "amperes is ", time, "seconds."
        raw_input()
        main()
        
    # You get the idea, these defs solve things
    def voltage():
        print valuefor, energystr # Code structure changes to efficient input form here
        energy = float(raw_input(""))
        print valuefor, chargestr
        charge = float(raw_input(""))
        voltage = energy / charge
        print "The potential difference of ", energy, "joules with ", charge, "coulombs is ", voltage, "volts."
        raw_input()
        main()
      
    def energy():
        print valuefor, voltagestr
        voltage = raw_input("")
        print valuefor, chargestr
        charge = raw_input("")
        energy = voltage * charge
        print "The energy used with", charge, "coulombs with a potential difference of ", voltage, "volts is ", energy, "joules."
        raw_input()
        main()
        
        
    def resistance():
        print valuefor, voltagestr
        voltage = raw_input("")
        print valuefor, currentstr
        resistance = voltage / current
        raw_input()
        print "The resistance of ", voltage, "volts with ", current, "amperes is ", resistance, "ohms."
        main()
        
    def power():
        print valuefor, energystr
        energy = raw_input("")
        print valuefor, timestr
        time = raw_input("")
        power = energy / time
        print "The power of ", energy, "joules over ", time, "seconds is ", power, "watts."        
        raw_input()
        main()
        
    main() # Starts program
