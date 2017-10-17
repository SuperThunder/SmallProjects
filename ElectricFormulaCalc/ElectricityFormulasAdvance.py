def main():
    v = {'charge':0.0, 'current':0.0, 'voltage':0.0, 'time':0.0, 'energy':0.0, 'power':0.0, 'resistance':0.0}
    v['charge'] = 10
    print v['charge']
    
    currentstr = "Current(I), measured in Amperes (A) "
    chargestr = "Charge(q), measured in Coulombs (C) "
    timestr = "Time (t), measured in Seconds (S) "
    voltagestr = "Voltage (V), measured in Volts (V) "
    energystr = "Energy, (E), measured in Joules (J) "
    resistancestr = "Resistance (R), measured in Ohms (Omega) "
    powerstr = "Power (P), measured in Watts (W) "    
    
    print "\nEnter the values you know from the following list\n\t", currentstr,"\n\t", chargestr, "\n\t", timestr,
    print  "\n\t", voltagestr, "\n\t", energystr, "\n\t", resistancestr, "\n\t", powerstr
    runchoice = str(raw_input(""))
    
    #whoo much smarter system than before
    for key in v.keys():
        if key in runchoice.lower():
            print "Enter the value for", key
            v[key] = float(raw_input(""))
       

#trying to set up some way to intelligently be able to cover all similar but slightly different relationships between the variables
def solve(val, var1, var2, rel):
    if(var1 <= 0 or var2 <= 0): #don't try to solve anything if we don't have the input for it
        return 0
        
    if(rel == '*'):
        return var1 * var2
    elif(rel == '/'):
        return var1 / var2
    elif(rel == '^*'): #'^' represents square, position represents which var is squared
        return var1**2 * var2
    elif(rel == '^/'):
        return var1**2 / var2
    elif(rel == '*^'):
        return var1 * var2**2
    elif(rel == '/^'):
        return var1 / var2**2
    else:
        print("This should never appear.")
        
main()