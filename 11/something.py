from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')

try:
    password = browser.find_element(By.NAME, 'pass')
    password.send_keys('not_realPassword')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('not_real@email.com')
    password.submit()
    print('Udana - nieudana próba logowania ' )
except:
    print('błąd')