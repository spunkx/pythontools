import csv
import os.path
from datetime import datetime
from time import strftime


def writeCSV(description, startDate, endDate, startTime, endTime, hours, hourlyRate, costEstimation):
    with open('hours.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([description, startDate, endDate, startTime, endTime, hours, hourlyRate, costEstimation])


def converttimeSeconds(hours, minutes, seconds):
    hourSeconds = int(hours) * 3600
    hourMinutes = int(minutes) * 60

    timeSeconds = int(hourSeconds) + int(hourMinutes) + int(seconds)

    return timeSeconds

        
def calcHours(startTime, endTime):
    #add handling later for different days

    starttimeArray = startTime.split(":")
    endtimeArray = endTime.split(":")

    #this do in seprate function
    startSeconds = converttimeSeconds(starttimeArray[0], starttimeArray[1], starttimeArray[2])
    endSeconds = converttimeSeconds(endtimeArray[0], endtimeArray[1], endtimeArray[2])
    secondsDifference = endSeconds - startSeconds

    return secondsDifference


def calcCost(secondsDifference, hourlyRate):
    #careful of rounding errors
    secondsRate = int(hourlyRate) / 3600
    return secondsRate * secondsDifference
    



isFile = os.path.exists("hours.csv")
if(isFile == False):
    with open('hours.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["description","startDate", "endDate", "startTime", "endTime", "workingTime", "hourlyRate", "costEstimation"])
else:
    try:
        myfile = open("hours.csv", "r+")
    except IOError:
        print("Please close the file before you run me!")
        exit()
    

hourlyRate = input("Enter hourly rate as an integer: ")

now = datetime.now()
startdateTime = now.strftime("%d/%m/%Y %H:%M:%S")
startDate = startdateTime.split()[0]
startTime = startdateTime.split()[1]

print("type 'end' to finish recording session")
userInput = input()

if userInput == "end".lower():
    now = datetime.now()
    enddateTime = now.strftime("%d/%m/%Y %H:%M:%S")
    endDate = enddateTime.split()[0]
    endTime = enddateTime.split()[1]

    secondsDifference = calcHours(startTime, endTime)
    costEstimation = calcCost(secondsDifference, hourlyRate)

    #https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds
    m, s = divmod(secondsDifference, 60)
    h, m = divmod(m, 60)
    hours = f'{h:d}:{m:02d}:{s:02d}'
    description = input("enter description for hours: ")
    writeCSV(description, startDate, endDate, startTime, endTime, hours, hourlyRate, costEstimation)
    
