from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://play2048.co/')
htmlElem = driver.find_element(By.TAG_NAME, "html")


while True:
    htmlElem.send_keys(Keys.ARROW_UP)
    htmlElem.send_keys(Keys.ARROW_RIGHT)
    htmlElem.send_keys(Keys.ARROW_DOWN)
    htmlElem.send_keys(Keys.ARROW_LEFT)
    
    try:
        agine = driver.find_element(By.CLASS_NAME, "retry-button")
        agine.click()
    except:
        continue
#pomysł 