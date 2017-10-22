# Generate a CSV of the week's scheduled thermostat temperatures
import csv
from datetime import datetime, date, time, timedelta

OutputFilename = "HeatingSchedule.csv"

def main():
    # Temperatures and times for the HEAT mode
    HeatWeekdayTemps = [22, 19.5, 20, 16]
    HeatWeekdayTimes = [time(6, 45, 0), time(9, 30, 0), time(17, 0, 0), time(22, 0, 0)]
    HeatWeekendTemps = [18, 19.5, 20, 16]
    HeatWeekendTimes = [time(8, 0, 0), time(9, 30, 0), time(17, 0, 0), time(22, 0, 0)]

    # Splat (*) the lists to expand them to the function arguments
    weekday = ThermostatSchedule("Weekday", *HeatWeekdayTemps, *HeatWeekdayTimes)
    weekend = ThermostatSchedule("Weekend", *HeatWeekendTemps, *HeatWeekendTimes)

    # Create a list of the rows that will go into the schedule CSV
    weekday.CreateSchedule()
    weekend.CreateSchedule()

    # Write the generated results to CSV
    weekday.EntriesToCSV()
    weekend.EntriesToCSV()
    
# Handle either weekday or weekend temperatures and times
# http://stackoverflow.com/questions/656297/python-time-timedelta-equivalent
# http://stackoverflow.com/questions/14783858/i-am-trying-to-loop-between-two-times-from-800-to-1700-for-every-15-mins
class ThermostatSchedule():
    def __init__(self, name, tempWake, tempLeave, tempReturn, tempSleep, timeWake, timeLeave, timeReturn, timeSleep):
        # Name of the schedule. Probably Weekday or Weekend.
        self.ScheduleName = str(name)
        # Temperatures
        self.WakeTemp = tempWake
        self.LeaveTemp = tempLeave
        self.ReturnTemp = tempReturn
        self.SleepTemp = tempSleep
        # Times that the temps happen at
        self.WakeTime = timeWake
        self.LeaveTime = timeLeave
        self.ReturnTime = timeReturn
        self.SleepTime = timeSleep

    # Given the times and temps, makes a CSV-ready list of [time:temp] entries
    def CreateSchedule(self):
        self.Entries = []

        print("\n%s"%self.ScheduleName)
        
        # To use timedeltas we unfortunately need to make a datetime object
        start = datetime.combine(date.today(), time())
        end = start+timedelta(hours=24)
        tWake = TimeToDatetime(self.WakeTime)
        tLeave = TimeToDatetime(self.LeaveTime)
        tReturn = TimeToDatetime(self.ReturnTime)
        tSleep = TimeToDatetime(self.SleepTime)
        
        print(start.strftime("%D %T"))
        print(end.strftime("%D %T"))

        now = start
        CurrentTemp = -255
        # At midnight the temperature will be the sleep temp, this does make assumptions about schedule but I'm not writing a library so w/e
        #temp = self.SleepTemp
        
        while now < end:
            # Start is 00:00, so ASSUME our temperature is the sleep temperature.
            if(start <= now < tWake):
                CurrentTemp = self.SleepTemp
                
            elif(tWake <= now < tLeave):
                CurrentTemp = self.WakeTemp
                
            elif(tLeave <= now < tReturn):
                CurrentTemp = self.LeaveTemp
                
            elif(tReturn <= now < tSleep):
                CurrentTemp = self.ReturnTemp

            elif(tSleep <= now < end):
                CurrentTemp = self.SleepTemp
                
            else:
                print(str(now))
                print("WHO KNOWS?")

            self.Entries.append([now.strftime("%T"), CurrentTemp])
            now += timedelta(seconds=60)


    def EntriesToCSV(self):
        with open(file=self.ScheduleName+OutputFilename, mode='w') as OutputFile:
            writer = csv.writer(OutputFile)
            header = "Time, Temperature"
            for entry in self.Entries:
                writer.writerow(entry)
                    
                
# Converts a datetime.time() time to a datetime.datetime() time with today as the data
def TimeToDatetime(TimeTime):
    return datetime.combine(date.today(), TimeTime)

main()
'''
HEAT:
weekday:
6:45AM 22C
9:30AM 19.5
5PM 20
10PM 16

weekend:
8AM 18.0C
9:30AM 19.5
5PM 20
10PM 16


COOL:
weekday:

weekend:

'''
