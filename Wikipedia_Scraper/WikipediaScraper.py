from bs4 import BeautifulSoup
import requests
import WikipediaScraper_FileWriter

def mainWhileLoop():
    try:
        userWantsToStop = False
        retryRequest = input("Do you want to scrape something? 0 = No, 1 = Yes ")
        if int(retryRequest) == 0:
            userWantsToStop = True
            print("Ending program")
        elif int(retryRequest) == 1:
            userWantsToStop = False
            print("Continuing")
        else:
            print("Insert either 0 (No) or 1 (Yes)!") 
    except Exception:
        print("Type in something that is a number (type: integer)")
        userWantsToStop = mainWhileLoop()
    return userWantsToStop
            

def userInputRequest():
    urlBeginning = "https://en.wikipedia.org/wiki/" #English Wikipedia site
    article = input("What article would you like to scrape from Wikipedia? (use _ for spaces): ")
    url = urlBeginning + article
    fileName = input("What file shall we write the contents into (format: .txt - added automatically): ") + ".txt"
    return [url, fileName]

def scrapeProcess(userInput):
    tagTextList = []
    gottenGains = requests.get(userInput[0])
    soup = BeautifulSoup(gottenGains.content, "html.parser")
    tags = soup.find_all('p')
    for tag in tags:
        tagTextList.append(tag.text)
    return tagTextList

def process():
    userInput = userInputRequest()
    tagTextList = scrapeProcess(userInput)
    WikipediaScraper_FileWriter.fileWriter(tagTextList, userInput[1])
    print("The results have been written to the desired .txt file")



def main():
    userWantsToStop = False
    while not userWantsToStop: 
        process()
        userWantsToStop = mainWhileLoop()
    print("Thank you for using the Wikipedia scraper!")

main()