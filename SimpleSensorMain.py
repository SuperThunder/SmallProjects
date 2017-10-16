import subprocess # Popen: opening shell commands
import datetime # recording times to figure out how long to wait
import time # sleep command
import sys # stdout buffer write
import csv # Write data

# How many entries we should gather before writing them to file. Min 1, set to higher if you want to lower file accesses.
CSV_BUFFER_SIZE = 1 # TODO: Put this somewhere more sensical

# TODO: Attach a timestamp to the current output CSV(s) that shows the start time

def main():
    # TODO: thread each interface in its own thread
    interfaceDHT11()
    

# TODO: Rewrite interface in Cython around C++ custom code
def interfaceDHT11():
    # Perform the data recording once every 60s on the :00
    CompileStr = ["g++", "-std=c++11", "-o", "recordDHT11++", "recordDHT11++.cpp", "-lwiringPi", "-lwiringPiDev"]
    Header = ["Datetime", "Temperature", "Humidity"]
    DHT11Interface = Sensor(sensorname="DHT11", source=CompileStr, command = ["./recordDHT11++"], header=Header)
    DHT11Interface.CompileInterface()
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
def ShellCall(command, verbose = False):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    decodedStdout = stdout.decode('utf-8')
    decodedStderr = stderr.decode('utf-8')
    ReturnCode = process.returncode
    
    if(verbose):
        print("STDOUT\n"+("-"*80))
        print(decodedStdout) 
        print("STDERR\n"+("-"*80))
        print(decodedStderr)
        print("Return: "+str(ReturnCode))

    return {'stdout':decodedStdout, 'stderr':decodedStderr, 'returncode':ReturnCode}


# Stores the information about and output of a particular sensor
class Sensor:
    def __init__(self, sensorname, source, command, header):
        self.Entries = [] # List of all entries
        self.EntriesBuffer = [] # List of entries that still need to be written to file
        self.FileHeader = []
        self.SensorName = str(sensorname)
        self.InterfaceSource = source
        self.InterfaceCommand = command # such as "./recordDHT11"
        self.GoodRecordings = 0 # For getting a % of how many sensor recordings fail
        self.BadRecordings = 0

        # TODO: make the datetime format better
        # What this does is set the output filename as the time the program was run, which seperates things a bit
        self.ResultsFileName = str(datetime.datetime.now().strftime("%Y-%m-%d %T"))+self.SensorName+".csv"
        print("Filename: %s"%self.ResultsFileName)

    def EntriesToCSV(self):
        import csv

        # TODO: Check for existence of file, if not, create it with header
        # Write all the entries to a csv; we need append mode as we write only a few entries at a time
        with open(self.ResultsFileName, mode='a') as outputfile:
            writer = csv.writer(outputfile)
            #for entry in self.EntriesBuffer:
            for i in range(0, len(self.EntriesBuffer)):
                # csv.writer expects a list of the indiviual columns, but our C already gives it comma seperated, so we split by comma into a list just so csv.writer will add them back in
                # TODO: Handle this earleir so CSV code isn't handling string problems
                writer.writerow(self.EntriesBuffer.pop(0).split(","))


    # Compile the C programs
    # If complexity grows, a makefile may be more suitable
    # You do need to make sure the C code will compile properly
    def CompileInterface(self):
        try:
            print(self.InterfaceSource)
            ShellCallResults = ShellCall(command=self.InterfaceSource, verbose=True)
            ReturnCode = ShellCallResults['returncode']
            StdOut = ShellCallResults['stdout']
            StdErr = ShellCallResults['stderr']            
            
        except:
            print(self.InterfaceSource+" Compiling Exception")
            raise


    
    # abstract the subprocess call here, run a certain preset command and pipe stdout to list entries
    def callInterface(self):
        ValidResult = False
        Tries = 0
        Tries_Limit = 30
        CallTime = datetime.datetime.now()
        # If we have 30 failures (which represents a delay of at least 30s), just bail and wait until the next opportunity
        while(ValidResult == False):
            if(Tries > Tries_Limit):
                print("Exceeded %d tries"%Tries_Limit)
                return False
            
            try:
                
                ShellCallResults = ShellCall(command=self.InterfaceCommand)
                ReturnCode = ShellCallResults['returncode']
                StdOut = ShellCallResults['stdout']
                StdErr = ShellCallResults['stderr']
                self.BadRecordings += len(StdErr.split("\n"))-1

                # TODO: get this logic up out of here
                # If the C program returned cleanly; add the (what should be) one line of comma seperated data
                if(ReturnCode == 0):
                    # TODO: Fix datetime format
                    Entry = str(CallTime) + ',' + str(StdOut).replace('\n', "") + ','
                    print(Entry)
                    self.Entries.append(Entry)
                    self.EntriesBuffer.append(Entry)
                    self.GoodRecordings += 1 # Would this make more sense somewhere else?
                    ValidResult = True
                 

            except:
                print(self.SensorName+" interfacing exception")
                raise

            Tries += 1

        # This runtime message needs to be outside of the loop so it gets the whole runtime including retries
        print("Runtime: %s"%str(datetime.datetime.now()-CallTime))
        SuccessRate = (float(self.GoodRecordings)/float(self.BadRecordings+self.GoodRecordings))*100
        print("Success Rate: %.2f\t(Good: %d, Bad: %d)"%(SuccessRate, self.GoodRecordings, self.BadRecordings))



main()
