from bs4 import BeautifulSoup
import urllib.request
import json
import re

#def convert to dictionary

#def convertToDictionary():
def fixElements(unfixed):
    #this function does a join on two elements in the unfixed list
    #then shifts the values back...
    #i.e. 'Account', 'http://www', 'google.com' -> 'Account', 'http://wwwgoogle.com'
    #notice the decrease in the number of elements
    endLoop = len(unfixed)
    i = 0
    joinStrings = ['@','http://', '#']
    for j in joinStrings:
        i = 0
        while True:
            #if i has reached the current value of endLoop 
            #(decrements with every join)
            if i == endLoop:
                break
            #if i is a match to elements in joinStrings
            if unfixed[i] == j:
                #grab the next element to join with the current
                temp = unfixed[i+1]
                #concatinate the current element with the next
                unfixed[i] = unfixed[i] + temp
                #from the current element, loop until the end and shift all
                #the next value back one position
                for k in range(i, endLoop-2):
                    unfixed[k+1] = unfixed[k+2]
                    #due to the shifting keeping the list the same size
                    #we must cut the list off at where the 
                    #elements have been shifted from and to
                    if k == endLoop-3:
					#this will require another counter
                        unfixed.remove(unfixed[k+1])
                        
                endLoop-=1
            i+=1
    return unfixed

with open ("ter.html", encoding="utf-8") as twitterHTML:
    requestDict = {'requestURL' : '', 'requestType' : '', 'target' : '', 'profile' : {'name' : '', 'url' : '', 'DoB' : ''}, 'tweets' : ''}
    #Store the data derived in the above dictionary
    data = twitterHTML.read()
    soup = BeautifulSoup(data, 'html.parser')
    timeline = soup.select('#timeline li.stream-item')
    print("PRINTING TWEETS !!!")
    for tweet in timeline:
        tweetID = tweet['data-item-id'] #attribute selection 
        tweetText = tweet.select('p.tweet-text')[0].get_text()
        print(tweetID, " ", tweetText)

    twitterProfileDetails = soup.find("div","ProfileHeaderCard")
    print("\nPRINTING PERSONAL DETAIL")
    twitterProInfo = []
    for string in twitterProfileDetails.stripped_strings:
        twitterProInfo.append(string)
    
    fixedElements = fixElements(twitterProInfo)
    print(fixedElements)

