#! python3
# download_xkcd.py - Pobiera wszystkie komiksy opublikowane w witrynie xkcd

import requests, os, bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith("#"):
    print(f"Pobieranie strony {url}")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Nie udało sie odnaleść obazu komiksu")
    else:
        comicUrl = f"http:{comicElem[0].get('src')}"
        print(f"pobieranie obrazu {comicUrl}")
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = f"http://xkcd.com{prevLink.get('href')}"
print("gotowe")
