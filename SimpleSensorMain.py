import subprocess # Popen: opening shell commands
import datetime # recording times to figure out how long to wait
import time # sleep command
import sys # stdout buffer write
import csv # Write data

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
    while(True):
        try:
            waitToMinute()
            # TODO: Make a wrapper around subprocess?
            process = subprocess.Popen(["./recordDHT11"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            stdout, stderr = process.communicate()
            print("STDOUT\n"+("-"*80))
            decodedStdout = stdout.decode('utf-8')
            print("STDERR\n"+("-"*80))
            decodedStderr = stderr.decode('utf-8')
            print(decodedStdout)
            print(decodedStderr)
            
            ReturnCode = process.returncode
            print("Return: "+str(ReturnCode))
        except:
            print("DHT11 interfacing exception")

    
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
        self.SensorName = str(name)

    def EntriesToCSV():
        import csv
        # Write all the entries to a csv
        with open(file=name+".csv", mode='a') as outputfile:
            reader = csv.reader(outputfile)
            for entry in Entries:
                reader.writerow(entry)

    # abstract the subprocess call here, run a certain preset command and pipe stdout to list entries
    def callInterface():
        try:
            waitToMinute()
            # TODO: Make a wrapper around subprocess?
            process = subprocess.Popen(["./recordDHT11"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            stdout, stderr = process.communicate()
            print("STDOUT\n"+("-"*80))
            decodedStdout = stdout.decode('utf-8')
            print("STDERR\n"+("-"*80))
            decodedStderr = stderr.decode('utf-8')
            print(decodedStdout)
            print(decodedStderr)
            
            ReturnCode = process.returncode
            print("Return: "+str(ReturnCode))

            # If the C program returned cleanly; add the (what should be) one line of comma seperated data
            if(ReturnCode == 0):
                Entries.append(decodedStdout)
            
        except:
            print(SensorName+"interfacing exception")    


main()
