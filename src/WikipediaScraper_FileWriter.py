import os

def fileExistence(fileName):
    return os.path.exists(fileName)

def fileEmptyVerification(fileName):
    file = open(fileName, "r", encoding="utf-8")
    fileIsEmpty = True #A boolean that stays true only if no written lines are detected in the file
    for line in file: 
        if(len(line) > 0):
            fileIsEmpty = False
            break
    file.close()
    return fileIsEmpty 

def writeProcess(tagTextList, fileName):
    written = open(fileName, "w", encoding="utf-8")
    for tagText in tagTextList:
        written.write(tagText)
    written.close()

def getOldContent(fileName):
    lineList = []
    file = open(fileName, "r", encoding="utf-8")
    for line in file:
        lineList.append(line)
    file.close()
    return lineList

def containOldContent(oldContent, fileName): #Backs up the previous result that was scraped
    fileName_olderStuff = fileName.replace(".txt", "")
    fileName_olderStuff = fileName + "_oldContent.txt"
    file = open(fileName_olderStuff, "w", encoding="utf-8")
    file.write("_____________(New Content Dump Comes Here)_____________")
    for content in oldContent:
        file.write(content)
    file.close()

def oldScrapeProcessor(fileName): #Handles situations where data has been previously scraped
    oldContent = getOldContent(fileName)
    containOldContent(oldContent, fileName)

def fileWriter(tagTextList, fileName):
    fileExists = fileExistence(fileName)
    if(fileExists): #If the file already exists, we need to make sure it's empty
        fileIsEmpty = fileEmptyVerification(fileName)
        if(fileIsEmpty):
            writeProcess(tagTextList, fileName) 
        else:
            oldScrapeProcessor(fileName) #If the file is empty, we want to spare the old results
    else: #If file doesn't exist, we're free to create it an start writing
        writeProcess(tagTextList, fileName)
