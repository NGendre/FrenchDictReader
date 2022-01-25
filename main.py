import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# REQUIRES GECKODRIVER
# MUST IMPORT SELENIUM

# Init webdriver
options = Options()

browser = webdriver.Firefox(options=options)
url = "https://www.universalis.fr/alpha-dictionnaire/A/1/"
browser.get(url)

time.sleep(1)
popup = browser.find_elements(By.CLASS_NAME,"css-19u7rjk")
popup[0].click()
#Init dictionnary
dictionnary = []
time.sleep(1)

links = browser.find_elements(By.CLASS_NAME, "list-group-item-action")
linkList = []
for l in links:
    linkList.append(l.get_attribute("href"))




pageIt = 1

while len(linkList)>0:
    wordIt = 0
    while wordIt<len(linkList):
        browser.get(linkList[wordIt])
        word = browser.find_element(By.CLASS_NAME, "dico").text
        definition = browser.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/article/div[3]/section[1]/div/div[1]/dl[1]/dd[1]").text
        dictionnary.append([word, definition])
        browser.back()
        wordIt += 1
    pageIt+=1
    browser.get("https://www.universalis.fr/alpha-dictionnaire/A/"+pageIt+"/")
    pageRows = browser.find_element(By.XPATH, "//html/body/div[2]/div[2]/article/section[1]/div/ul")
    links = browser.find_elements(By.CLASS_NAME, "list-group-item-action")
    linkList = []
    for l in links:
        linkList.append(l.get_attribute("href"))






#for w in words:
#    w.click()
