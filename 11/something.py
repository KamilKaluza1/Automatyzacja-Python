from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com/')



try:
    elem = browser.find_element(By.TAG_NAME, 'h1')
    print('Znaleziono element  wraz z taką nazwą klasy!' )
except:
    print('nie udało sie znaleść elementu wraz z podaną nazwą klasy')