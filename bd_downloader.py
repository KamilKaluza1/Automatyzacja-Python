import requests, os, bs4

url = 'https://www.wcoforever.net/dragonball-episode-1-english-dubbed-2'
os.makedirs('bd', exist_ok=True)
for epizod in range(153):
    print(f"Pobieranie strony {url}")
    res = requests.get(url)
    res.raise_for_status() # forbidden 403 jak pominąć ??

    soup = bs4.BeautifulSoup(res.text)

    video = soup.find_all(id="video-js_html5_api")


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