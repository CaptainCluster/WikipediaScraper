from bs4 import BeautifulSoup
import requests
import WikipediaScraper_FileWriter

#Asking the user whether he wants to scrape an article or not.
def requestNewProcess():
    try:
        userWantsToStop = False
        userResponse = input("Do you want to scrape something? 0 = No, 1 = Yes ")

        if int(userResponse) == 0:
            userWantsToStop = True
            print("Ending program")
        elif int(userResponse) == 1:
            userWantsToStop = False
            print("Continuing")
        else:
            print("Insert either 0 (No) or 1 (Yes)!") 
    except Exception:
        print("Type in something that is a number (type: integer)")
        userWantsToStop = requestNewProcess()
    return userWantsToStop
            
#Asking the user for the wikipedia article name and the file name for saving the data
def userInputRequest():
    urlBeginning = "https://en.wikipedia.org/wiki/" 
    article = input("What article would you like to scrape from Wikipedia? (use _ for spaces): ")
    url = urlBeginning + article
    fileName = input("What file shall we write the contents into (format: .txt - added automatically): ") + ".txt"
    return [url, fileName]

#Scraping all the p-tags and appending the data into a list
def scrapeProcess(userInputList):
    url = userInputList[0]
    pTagTextList = []    

    #Getting the data from the website
    getRequestData = requests.get(url)
    soup = BeautifulSoup(getRequestData.content, "html.parser")
    pTags = soup.find_all('p')

    #Appending the data into a list that we will return
    for pTag in pTags:
        pTagTextList.append(pTag.text)

    return pTagTextList

#Gathers all the functions necessary for the scraping process
def process():
    userInputList = userInputRequest()                                    #1. Asking the user for the inputs
    tagTextList = scrapeProcess(userInputList)                            #2. Using the given inputs to get the p-tags
    WikipediaScraper_FileWriter.fileWriter(tagTextList, userInputList[1]) #3. Sending the p-tag list and the url to write the data
    print("The results have been written to the desired .txt file")

def main():
    userWantsToStop = False
    while not userWantsToStop: 
        process()
        userWantsToStop = requestNewProcess()
    print("Thank you for using the Wikipedia scraper!")

main()