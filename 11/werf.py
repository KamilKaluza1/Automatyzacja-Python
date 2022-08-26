# Utwórz program, który po otrzymaniu adresu URL strony internetowej spróbuje
# pobrać wszystkie strony internetowe, do których prowadzą łącza z podanej.



import requests, bs4, os


res = requests.get('https://www.oldentis.pl/index.php#')
soup = bs4.BeautifulSoup(res.text, features="html.parser")
links = soup.find_all("a")
how_many = 0
for link in links:
    check = str(link.get('href'))
    if check.startswith("http"):
        how_many+=1
        res2 = requests.get(check)
        try:
            res2.raise_for_status()
        except:
            print(f"nie udało sie pobrać strony {check} błąd 404")
        name = f"{how_many}.html"
        siteFile = open(name, 'wb')
        for chunk in res2.iter_content(1000000):
            siteFile.write(chunk)
        siteFile.close()

