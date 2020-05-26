'''
Author: Taylor Spinks
Date: 14/10/2019
A CSV parser for a CSV file that was extracted from AD

Certain variables names or information have been ommitted
Please note, this was made with very little context or information. I also had no access to the AD, I was given a CSV file and asked to generate some metrics
'''

import csv
import os
import sys
import time

#write a file
def writeFile(fileName, data):
    f = open(fileName, "w")
    if type(data) is list:
        for item in data:
            f.write(item)
    else:
        f.write(data)
    
    f.close()
#write a dictionary into a csv format
def writeCsv(fileName, data):
    with open(fileName, mode='w') as csv_file:
        fieldnames = data.keys()
        wr = csv.DictWriter(csv_file, fieldnames=fieldnames)
        wr.writeheader()
        wr.writerow(data)


def getCsv():
    #initialise all values
    sizeOfRecord = 0.0
    namedAccounts = 0
    account1 = 0
    tempAccounts = 0
    account2 = 0
    lockedoutAccounts = 0
    disabledAccounts = 0
    disabPassNotReq = 0
    domainAdminCounter = 0
    #all account codes for users
    userAccountCodes = {'512' : 0, '546' : 0, '66048' : 0, '66050' : 0, '66080' : 0, '66082' : 0, '262656' : 0, '262658' : 0, \
    '262688' : 0, '262690' : 0, '328192' : 0, '328194' : 0, '328224' : 0, '328226' : 0}
    
    with open('19-05-31 All-AD-Users-All-attributes.csv', newline='') as csvfile:
        recordsReader = csv.DictReader(csvfile, delimiter=',')
        lineCount = 0
        currCodeCounter = 0
        for row in recordsReader:
            if lineCount == 0:
                csvColumns = ("\n".join(row))
                writeFile("csvColumns.txt", "CSV Columns: \n" + str(csvColumns))
                lineCount += 1
            else:
                if(row['DisplayName'] != ''):
                    namedAccounts += 1

                distinguisedName = row['DistinguishedName']
                splitDistName = distinguisedName.split(",")
                email = row['EmailAddress']

                #get the number of staff and students via domain information
                for elem in splitDistName:
                    if elem == "OU=Temporary Accounts" and "OU=Temp Users":
                        tempAccounts += 1
                    elif (((email != '') and ((email.split("@")[1]) == "emailaddress")) and elem == "OU=Account"):
                        account1 += 1
                    elif (((email != '') and ((email.split("@")[1]) == "emailaddress")) and elem == "OU=AnotherAcount"):
                        account2 += 1
                    elif ((elem[0:5].lower() == "CN=ADM".lower()) or (elem[0:7].lower() == "CN=admin".lower()) or ((email != '') and ((email.split("@")[1]) == "ads.domain.domain.domain"))):
                        domainAdminCounter += 1

                lineCount += 1

                if row['LockedOut'] == "TRUE":
                    lockedoutAccounts += 1
                if row['Enabled'] == "FALSE":
                    disabledAccounts += 1
                    if row['PasswordNotRequired'] == "TRUE":
                        disabPassNotReq += 1

                codeNumbers = 0
                codeArray = userAccountCodes.keys()
                for code in codeArray:
                    #print("this is the code", code)
                    #print("this is the row accoutn control", row['userAccountControl'])
                    if code == row['userAccountControl']:
                        currCodeCounter = codeNumbers + 1
                        previousCount = userAccountCodes.get(code)
                        #print("previous count", previousCount)
                        test = currCodeCounter + previousCount
                        #print("new count", test)
                        userAccountCodes.update({code : currCodeCounter + previousCount})
                        #print(userAccountCodes)


        print(userAccountCodes)
        valueList = list(userAccountCodes.values())
        codeArray = userAccountCodes.keys()
        test = list(codeArray)
        unamedAccounts = lineCount - namedAccounts
        csvStats = {'All Accounts': lineCount, 'Named Accounts' : namedAccounts, 'Unnamed Accounts' : unamedAccounts, \
        'Number of Accounts' : account1, 'Number of Accounts' : account2, \
        'Number of temp accounts' : tempAccounts, 'Number of Domain admins' : domainAdminCounter, \
        'Number of locked accounts' : lockedoutAccounts, 'Number of disabled accounts' : disabledAccounts, \
        'Number of disabled accounts with no password' : disabPassNotReq}
        
        k = 0
        l = 0
        while k < len(codeArray):
            code = test[k]
            value =  valueList[l]
            csvStats.update({code : value})
            k += 1
            l += 1

        writeCsv("Account_Metrics.csv", csvStats)
        print(f'done did {lineCount} lines')




if __name__ == '__main__':
    getCsv()

    
    
