from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#include the webdriver for chrome in the same directory as a sibling

def main():
    try:
        chrome_options = Options() #instantiate an options class
        chrome_options.add_argument("--headless") #running the web-browser activity in headless mode (i.e. have no visual web browser shown scraping whilst scraping)
        username = input(str("Please input the username whose twitter you'd like to enumerate\n>"))
        driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        driver.get("https://twitter.com/{}/".format(username))
        
        SCROLL_PAUSE_TIME = 1
        bioURLObj = driver.find_element_by_xpath("//p[@class='ProfileHeaderCard-bio u-dir']").text
        twitterNameObj = driver.find_element_by_xpath("//a[@class='ProfileHeaderCard-screennameLink u-linkComplex js-nav']").text
        personalName = driver.find_element_by_xpath("//h1[@class='ProfileHeaderCard-name']/*").text
        location = driver.find_element_by_xpath("//span[@class='ProfileHeaderCard-locationText u-dir']").text
        joinDate = driver.find_element_by_xpath("//span[@class='ProfileHeaderCard-joinDateText js-tooltip u-dir']").text
        mediaCount = driver.find_element_by_xpath("//a[@class='PhotoRail-headingWithCount js-nav']").text
        url = driver.find_element_by_xpath("//span[@class='ProfileHeaderCard-urlText u-dir']/*").text
        verification = driver.find_element_by_xpath("//span[@class='ProfileHeaderCard-badges']/*/*/*").text
        print(verification)
        print(url)
        print(mediaCount)
        print(joinDate)
        print(location)
            # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        scrollLimit = 0
        tweetList = []
        while scrollLimit != 3:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
                time.sleep(80)
            last_height = new_height
            scrollLimit += 1
        tweetOBJ = driver.find_elements_by_xpath("//li[@data-item-type='tweet']")
        for i in tweetOBJ:
          tweetID = i.find_element_by_xpath(".//*[@data-item-id]").text
          tweetText = i.find_element_by_xpath(".//p").text
          tweetStuffConcat = tweetID + tweetText
          tweetList.append(tweetStuffConcat)
        print(tweetList)
    except:
        print("Something went wrong\nDid you include the chromedriver in path or the same directory")
        
if __name__ == "__main__":
    main()
