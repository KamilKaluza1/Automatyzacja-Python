# Importuj BeautifulSoup i request
#1 Pobierz strone z internetu, utwórz obiekt bs4
#2 znajdź wszystkie linki z obiektu bs4 
#3 sprawdź czy prowadzą do strony internetowej 
#4 sprawdź czy srona da sie pobrać 
#5 zapisz pod nazwą z rozszerzeniem html

import requests, bs4
#1 Pobierz strone z internetu, utwórz obiekt bs4
res = requests.get('https://www.oldentis.pl/index.php#')
soup = bs4.BeautifulSoup(res.text, features="html.parser")
#2 znajdź wszystkie linki z obiektu bs4 
links = soup.find_all("a")
# .find_all(id='id'|"p"|"title"|id=True|class_="sister")
how_many = 0
#3 sprawdź czy prowadzą do strony internetowej 
for link in links:
    check = str(link.get('href'))
    if check.startswith("http"):
        how_many+=1
        res2 = requests.get(check)
        try:#4 sprawdź czy srona da sie pobrać 
            res2.raise_for_status()
        except:
            print(f"nie udało sie pobrać strony {check} błąd ")
        #5 zapisz pod nazwą z rozszerzeniem html
        name = f"{how_many}.html"
        siteFile = open(name, 'wb')# Tryb binarny zapis
        for chunk in res2.iter_content(1000000):
            siteFile.write(chunk)
        siteFile.close()

