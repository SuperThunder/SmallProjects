import subprocess
import datetime
import time

def main():
    compileInterfaces()

    # TODO: thread each interface in its own thread
    interfaceDHT11()
    
    
    

# Compile the C programs
# If complexity grows, a makefile may be more suitable
# You do need to make sure the C code will compile properly
def compileInterfaces():
        
    process = subprocess.Popen(["gcc", "-o", "recordDHT11", "recordDHT11.c", "-lwiringPi", "-lwiringPiDev"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # communicate() returns a tuple (stdoutdata, stderrdata).
    # out, err = process.communicate()
    
    #print(process.returncode)
    print("STDOUT\n"+("-"*80))
    print(process.stdout.read())
    print("STDERR\n"+("-"*80)+"\n")
    print(process.stderr.read())
    #print("\n")
    out, err = process.communicate()
    print("Return: "+str(process.returncode))


def interfaceDHT11():
    # Perform the data recording once every 60s on the :00
    while(True):
        waitToMinute()
        
        process = subprocess.Popen(["./recordDHT11"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        #print(process.returncode)
        print("STDOUT\n"+("-"*80))
        print(process.stdout.read())
        print("STDERR\n"+("-"*80)+"\n")
        print(process.stderr.read())
        #print("\n")    
        #out, err = process.communicate()
        print("Return: "+str(process.returncode))

    
# Given the amount of seconds we are into the current minute, subtract that from 60
# Then wait that amount of time: We wait until the start of the next minute
def waitToMinute():
    currentTime = datetime.datetime.now()
    timeToWait = 60 - currentTime.second
    time.sleep(timeToWait)
    

# Stores all the entries for a particular interface
class DataRecord:
    def __init__(self, name):
        self.Entries = []
        self.SensorName = name

    def EntriesToCSV():
        import csv
        # Write all the entries to a csv
        with open(file=name+".csv", mode='a') as outputfile:
            reader = csv.reader(outputfile)
            for entry in Entries:
                reader.writerow(entry)


main()
