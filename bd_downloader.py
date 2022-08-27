
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

#2 przypisujesz przeglądarkę bierzesz strone 
driver = webdriver.Firefox()
driver.get('https://www.wcoforever.net/dragonball-episode-1-english-dubbed-2')
action = ActionChains(driver)
htmlElem = driver.find_element(By.TAG_NAME, "html")
htmlElem.send_keys(Keys.END)

id ='video-js_html5_api'
action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).perform()


# https://lb.watchanimesub.net/getvid?evid=zddAlnLRd3eM_kWe7vs1SV6dx-qbEA0u0tuBfkNjI2vCT70A1MDPKBvaHr62gJVgnJDKEBi2IiF4fX8YxNfJXcLSLvu737-VK34D4G-3Z3XWyQi29bwU2GtSVprvrR8DBmNI6z30OO7W7pm9MzndQxUZYIm_100ZPA-yiQDy0WVnYPcU8ns5Z_OtEwLDnDACk4L0cI2CyAgq5160thqX9EkPlmyHZ2znleKpHwDrvnuzD0a5XlGiE_7_QWXHkG57dhIrBSJHOaXBlPytI4Rb_Srdvd4ReUjdY3m2aDPISQZSBv_vGdIPQ8ODsb7xPHyt0noVDv6xwoui1ct8ZdAPPKzxTUn0k_nme5D_JsAfoPRv536NmOYn3i4_vDzbaEnfwTjjhrSEqIiBykZoSCvyzEbouz4MPP117PclgIa7osJd-vyCUNAS421tlic8cMCB





# import requests, os, bs4

# url = 'https://www.wcoforever.net/dragonball-episode-1-english-dubbed-2'
# os.makedirs('bd', exist_ok=True)
# for epizod in range(153):
#     print(f"Pobieranie strony {url}")
#     res = requests.get(url)
#     print(res)

#     soup = bs4.BeautifulSoup(res.text)

#     video = soup.find_all(id="video-js_html5_api")


#     if comicElem == []:
#         print("Nie udało sie odnaleść obazu komiksu")
#     else:
#         comicUrl = f"http:{comicElem[0].get('src')}"
#         print(f"pobieranie obrazu {comicUrl}")
#         res = requests.get(comicUrl)
#         res.raise_for_status()

#         imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
#         for chunk in res.iter_content(100000):
#             imageFile.write(chunk)
#         imageFile.close()

#     prevLink = soup.select('a[rel="prev"]')[0]
#     url = f"http://xkcd.com{prevLink.get('href')}"
# print("gotowe")