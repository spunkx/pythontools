from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#requires chrome webdriver to work
#include the binary file as a sibling in the directory

#this is a proof of concept

def main():
    pasteBinText = []
    chrome_options = Options()
    print("This program curently supports two modes.\n1. Precise string matching, input a series of strings for which you want an exact match\n2. 'relative' string matching, whereby any containment of the string is found. ")
    choice = input(str(">: "))
    Query = input(str("What would you like to enumerate pastebin for?\n>"))
    try:
        chrome_options = Options() #instantiate an options class
        chrome_options.add_argument("--headless") #running the web-browser activity in headless mode (i.e. have no visual web browser shown scraping whilst scraping)
        driver = webdriver.Chrome('D:\\OChewai0\\Downloads\\chromedriver_win32\\chromedriver.exe', options=chrome_options) #must figure a way to include the executable for use, also have a mention for update based on chrome version.
        if choice == "1":
            driver.get('https://google.com/search?q="{}"'.format(Query)) #the link which selenium bot will visit unheadlessly atm
        elif choice == "2":
            driver.get('https://google.com/search?q={}'.format(Query)) #currently looking for nto an exat match 
        head = driver.find_elements_by_xpath("//div[@class='gs-webResult gs-result']")
        URList = []
        for i in head:
            url = i.find_element_by_xpath(".//div[@class='gs-bidi-start-align gs-visibleUrl gs-visibleUrl-long']")
            URList.append(url.text)
        if len(URList) > 0:
            x = len(URList)
            additionalURL = x - 1
            URList.pop(additionalURL)
            print("Congrats, we found something! (your URLs) \n", URList)
        else:
            print("Nothing matches the exact search term you're looking for :( ")   
        if len(URList) > 0:
            loopChoice = input(str("Would you like to loop through the URL(s) you may have just found in the list?\n1 for yes\n2 for no\n> "))
            if loopChoice == "1":
                for link in URList:
                    driver.get("{}".format(link))
                    Rawtext = driver.find_elements_by_xpath("//textarea[@id='paste_code']")
                    for i in Rawtext:
                        purifiedText = i.text
                    fullText = purifiedText+ " is from " + link
                    pasteBinText.append(fullText)
            elif loopChoice == "2":
                print("we hope you enjoyed this service. bye")
        print("The content of google is: \n", google)
    except:
        print("something went wrong\nDid you include the chrome webdriver in path or the same directory?")
    
if __name__ == "__main__":
    main()
