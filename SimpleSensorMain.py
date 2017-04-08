from subprocess import call
import datetime

def main():
    compileInterfaces()

    # TODO: thread each interface in its own thread
    interfaceDHT11()
    
    
    

# Compile the C programs
# If complexity grows, a makefile may be more suitable
def compileInterfaces():
    call(["gcc", "-o", "recordDHT11", "recordDHT11.c", "-lwiringPi", "-lwiringPiDev"])
    


def interfaceDHT11():
    # Perform the action once every 60s
    # Subtract the current time from the next minute, then sleep that much tim
    call(["./recordDHT11"])
    


main()
