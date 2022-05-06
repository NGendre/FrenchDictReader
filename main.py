import time
import re
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# REQUIRES GECKODRIVER
# MUST IMPORT SELENIUM

#settings
url = "https://www.larousse.fr/dictionnaires/francais/oui/"
startNumber = 1
endNumber = 90000


# Functions
def verifyPageExists(browser):
    if browser.find_elements(By.TAG_NAME, 'h1'):
        print("if 1")
        if browser.find_element(By.TAG_NAME, 'h1').text == "Server Error in '/dictionnaires' Application.":
            print('if 2')
            return False
    return True
def filterWord(wordToVerify):
    returnedWord = wordToVerify
    if ',' in wordToVerify:
        wordToVerify = wordToVerify.split(",")
        returnedWord = wordToVerify[0]
    return returnedWord
def filterString(stringToVerify):
    verifiedString = re.sub('\n','',stringToVerify)
    verifiedString = verifiedString.replace('\ue82c ','')
    return verifiedString
def listToCsv(listOfWords):
    fields=['mot','definition']
    f= open('dictionnary.csv','w',newline='',encoding='utf-8')
    write = csv.writer(f,delimiter=',')
    write.writerow(fields)
    write.writerows(listOfWords)
def initWebdriver(url,startNumber):
    options = Options()
    browser = webdriver.Firefox(options=options)

    browser.get(url + str(startNumber))
    time.sleep(2)
    popup = browser.find_element(By.ID, "onetrust-accept-btn-handler")
    popup.click()
    return browser
def readPage(browser):
    definitionPage = browser.find_elements(By.CLASS_NAME, "DivisionDefinition")
    definition = []
    word = filterWord(filterString(browser.find_element(By.CLASS_NAME, "AdresseDefinition").text))
    log(word)
    for defin in definitionPage:
        log(defin)
        definition.append(filterString(defin.text))
    return [word,definition]
def readDictionnary(url,startNumber,endNumber):
    pageIterator = startNumber
    dictionnary = []
    browser = initWebdriver(url,startNumber)
    while pageIterator < endNumber:
        log(pageIterator)
        if (verifyPageExists(browser)):
            dictionnary.append(readPage(browser))
        pageIterator = pageIterator + 1
        browser.get(url + str(pageIterator))
    return dictionnary
def log(string):
    print(string)

dictionnary = readDictionnary(url,startNumber,endNumber)
listToCsv(dictionnary)

