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
endNumber = 5


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
    with open('dictionnary.csv','w',newline='') as csvfile:
        write = csvfile.writer(csvfile,delimiter=',')
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
def wordAndDefinition(browser):
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
            dictionnary.append(wordAndDefinition(browser))
        pageIterator = pageIterator + 1
        browser.get(url + str(pageIterator))

    print(dictionnary)
    return dictionnary
def log(string):
    print(string)

listToCsv([['système abh', ['Ensemble des substances antigéniques ubiquitaires qui définissent les sujets des groupes sanguins A, B, AB et O.']], ['abhorrer', ["Littéraire. Éprouver de l'aversion pour quelque chose ou quelqu'un ; détester, exécrer : Abhorrer le mensonge.Synonymes :abominer - détester - exécrer - haïr - honnirContraires :adorer - affectionner - chérir"]], ['abiétacée', ["Arbre résineux tel que le sapin, l'épicéa, les diverses espèces de pin, le mélèze et le cèdre.Synonyme :pinacée"]], ['abiétique', []], ['abîme (Réf. ortho. abime)', ["1. Littéraire. Gouffre naturel, cavité, précipice d'une profondeur insondable, ou lieu, espace qui n'a pas de limites assignables.Synonyme :abysse", '2. Division, désaccord profond entre des personnes, différence importante, distance considérable entre des choses : Cette rivalité a creusé un abîme entre eux.Synonymes :barrière - fossé - gouffre - séparation', "3. Littéraire. Désastre, échec, situation désespérée : Aller, courir à l'abîme. Toucher le fond de l'abîme.", "4. En héraldique, point central de l'écu.Synonyme :cœur", "5. Dans l'iconographie chrétienne, séjour des démons, symbolisé parfois par une tête d'homme hideuse, de mine féroce, sortant du sommet d'un cône figurant le monde."]]])

#readDictionnary(url,startNumber,endNumber)