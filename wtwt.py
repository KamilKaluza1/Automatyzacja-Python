#odpalenie bota w selenium input klawiatury wciskanie guzików
#1 Importy :
#2 przypisujesz przeglądarkę bierzesz strone
#3 złap stronę i wciśnij strzałke w górę  
#4 spróbój wcisnąć przycisk retry, jak nie ma daj znać.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#2 przypisujesz przeglądarkę bierzesz strone 
driver = webdriver.Firefox()
driver.get('https://play2048.co/')
#3 złap stronę i wciśnij strzałke w górę 
htmlElem = driver.find_element(By.TAG_NAME, "html")
# inne By ID|NAME|LINK_TEXT|TAG_NAME|CLASS_NAME|CSS_SELECTOR
htmlElem.send_keys(Keys.ARROW_UP)
# inne Keys END|ENTER|F4|HOME|ALT
#4 spróbój wcisnąć przycisk retry, jak nie ma daj znać.
try:
    agine = driver.find_element(By.CLASS_NAME, "retry-button")
    agine.click()
except:
    print("nie ma")