import subprocess # Popen: opening shell commands
import datetime # recording times to figure out how long to wait
import time # sleep command
import sys # stdout buffer write
import csv # Write data

CSV_BUFFER_SIZE = 1 # TODO: Put this somewhere more sensical

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

# TODO: Rewrite interface in Cython around C++ custom code
def interfaceDHT11():
    # Perform the data recording once every 60s on the :00
    DHT11Interface = Sensor(sensorname="DHT11", interfacecommand = "./recordDHT11")
    while(True):
        # Every CSV_BUFFER_SIZE entries, write what we got to CSV
        if(len(DHT11Interface.EntriesBuffer)%CSV_BUFFER_SIZE == 0):
            DHT11Interface.EntriesToCSV()
            
        try:
            waitToMinute()
            # TODO: Start recording success/failure rates
            DHT11Interface.callInterface()
            
        except:
            #print("DHT11 interfacing exception")
            raise

    
# Given the amount of seconds we are into the current minute, subtract that from 60
# Then wait that amount of time: We wait until the start of the next minute
def waitToMinute():
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
        self.GoodRecordings = 0 # For getting a % of how many sensor recordings fail
        self.BadRecordings = 0

    def EntriesToCSV(self):
        import csv
        
        # Write all the entries to a csv
        with open(file=self.SensorName+".csv", mode='a') as outputfile:
            writer = csv.writer(outputfile)
            #for entry in self.EntriesBuffer:
            for i in range(0, len(self.EntriesBuffer)):
                # csv.writer expects a list of the indiviual columns, but our C already gives it comma seperated, so we split by comma into a list just so csv.writer will add them back in
                writer.writerow(self.EntriesBuffer.pop(0).split(","))


    # abstract the subprocess call here, run a certain preset command and pipe stdout to list entries
    def callInterface(self):
        try:
            #process = subprocess.Popen([interfacename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            ShellCallResults = ShellCall(command=self.InterfaceCommand)
            ReturnCode = ShellCallResults['returncode']
            StdOut = ShellCallResults['stdout']
            StdErr = ShellCallResults['stderr']
            self.BadRecordings += len(StdErr.split("\n"))-1

            # TODO: get this logic up out of here
            # If the C program returned cleanly; add the (what should be) one line of comma seperated data
            if(ReturnCode == 0):
                self.Entries.append(StdOut)
                self.EntriesBuffer.append(StdOut)
                self.GoodRecordings += 1 # Would this make more sense somewhere else?

            SuccessRate = (float(self.GoodRecordings)/float(self.BadRecordings+self.GoodRecordings))*100
            print("Success Rate: %.2f\t(Good: %d, Bad: %d)"%(SuccessRate, self.GoodRecordings, self.BadRecordings))
            
        except:
            print(self.SensorName+"interfacing exception")
            raise


main()
