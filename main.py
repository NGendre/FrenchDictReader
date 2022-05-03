import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# REQUIRES GECKODRIVER
# MUST IMPORT SELENIUM

# Functions
def verifyPageExists(browser):
    if browser.find_elements(By.TAG_NAME, 'h1').__contains__("Server Error in '/dictionnaires' Application."):
        return False
    else:
        return True


# Init webdriver
options = Options()

browser = webdriver.Firefox(options=options)
url = "https://www.larousse.fr/dictionnaires/francais/oui/"
pageIterator = 1;
browser.get(url + str(pageIterator))

time.sleep(3)
popup = browser.find_element(By.ID, "onetrust-accept-btn-handler")
popup.click()
# Init dictionnary
dictionnary = []
time.sleep(1)

while pageIterator < 20:
    if (verifyPageExists(browser)):
        definitionPage = browser.find_elements(By.CLASS_NAME,"DivisionDefinition")
        definition = []
        for defin in definitionPage:
            definition.append(defin.text)
        word = browser.find_element(By.CLASS_NAME, "AdresseDefinition").text
        dictionnary.append([word, definition])
    pageIterator = pageIterator + 1
    browser.get(url + str(pageIterator))
    time.sleep(1)


print(dictionnary)
# while len(linkList)>0:
#     wordIt = 0
#     while wordIt<len(linkList):
#         browser.get(linkList[wordIt])
#         word = browser.find_element(By.CLASS_NAME, "dico").text
#         definition = browser.find_element(By.XPATH,
#             "/html/body/div[1]/div[2]/article/div[3]/section[1]/div/div[1]/dl[1]/dd[1]").text
#         dictionnary.append([word, definition])
#         browser.back()
#         wordIt += 1
#     pageIt+=1
#     browser.get("https://www.universalis.fr/alpha-dictionnaire/A/"+pageIt+"/")
#     pageRows = browser.find_element(By.XPATH, "//html/body/div[2]/div[2]/article/section[1]/div/ul")
#     links = browser.find_elements(By.CLASS_NAME, "list-group-item-action")
#     linkList = []
#     for l in links:
#         linkList.append(l.get_attribute("href"))


# for w in words:
#    w.click()
