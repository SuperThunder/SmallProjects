import subprocess # Popen: opening shell commands
import datetime # recording times to figure out how long to wait
import time # sleep command
import sys # stdout buffer write
import csv # Write data

CSV_BUFFER_SIZE = 5 # TODO: Put this somewhere more sensical

def main():
    try:
        compileInterfaces()
    except:
        print("Compiling exception")
    
    # TODO: thread each interface in its own thread
    interfaceDHT11()
    

# Compile the C programs
# If complexity grows, a makefile may be more suitable
# You do need to make sure the C code will compile properly
def compileInterfaces():
    process = subprocess.Popen(["gcc", "-o", "recordDHT11", "recordDHT11.c", "-lwiringPi", "-lwiringPiDev"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # communicate() returns a tuple (stdoutdata, stderrdata)
    # Stdout and stderr are returned as a UTF8 bytes object we must decode to avoid having control characters everywhere
    stdout, stderr = process.communicate()
    print("STDOUT\n"+("-"*80))
    decodedStdout = stdout.decode('utf-8')
    print("STDERR\n"+("-"*80))
    decodedStderr = stderr.decode('utf-8')
    print(decodedStdout)
    print(decodedStderr)

    ReturnCode = process.returncode
    print("Return: "+str(ReturnCode))


def interfaceDHT11():
    # Perform the data recording once every 60s on the :00
    DHT11Interface = Sensor(sensorname="DHT11", interfacecommand = "./recordDHT11")
    while(True):
        # Every CSV_BUFFER_SIZE entries, write what we got to CSV
        if(len(DHT11Interface.Entries)%CSV_BUFFER_SIZE == 0):
            DHT11Interface.EntriesToCSV()
            
        try:
            waitToMinute()
            DHT11Interface.callInterface()
            
        except:
            #print("DHT11 interfacing exception")
            raise

    
# Given the amount of seconds we are into the current minute, subtract that from 60
# Then wait that amount of time: We wait until the start of the next minute
def waitToMinute():
    # TODO: We seem to get some time drift - do we need to keep track of the exact second we need to wait to?
    currentTime = datetime.datetime.now()
    timeToWait = 60 - currentTime.second
    time.sleep(timeToWait)

# Runs a command in subprocess, waiting for it to complete, then return the result as a dictionary
def ShellCall(command):
    process = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print("STDOUT\n"+("-"*80))
    decodedStdout = stdout.decode('utf-8')
    print(decodedStdout)
    
    print("STDERR\n"+("-"*80))
    decodedStderr = stderr.decode('utf-8')
    print(decodedStderr)
            
    ReturnCode = process.returncode
    print("Return: "+str(ReturnCode))

    return {'stdout':decodedStdout, 'stderr':decodedStderr, 'returncode':ReturnCode}

# Stores the information about and output of a particular sensor
class Sensor:
    def __init__(self, sensorname, interfacecommand):
        self.Entries = [] # List of all entries
        self.EntriesBuffer = [] # List of entries that still need to be written to file
        self.SensorName = str(sensorname)
        self.InterfaceCommand = str(interfacecommand) # such as "./recordDHT11"
        

    def EntriesToCSV(self):
        import csv
        # Write all the entries to a csv
        with open(file=self.SensorName+".csv", mode='a') as outputfile:
            reader = csv.writer(outputfile)
            #for entry in self.EntriesBuffer:
            for i in range(0, len(self.EntriesBuffer)):
                reader.writerow(self.EntriesBuffer.pop([0]))



    # abstract the subprocess call here, run a certain preset command and pipe stdout to list entries
    def callInterface(self):
        try:
            #process = subprocess.Popen([interfacename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            ShellCallResults = ShellCall(command=self.InterfaceCommand)
            ReturnCode = ShellCallResults['returncode']
            StdOut = ShellCallResults['stdout']

            # TODO: get this logic up out of here
            # If the C program returned cleanly; add the (what should be) one line of comma seperated data
            if(ReturnCode == 0):
                self.Entries.append(StdOut)
                self.EntriesBuffer.append(StdOut)
                
        except:
            print(self.SensorName+"interfacing exception")
            raise


main()
