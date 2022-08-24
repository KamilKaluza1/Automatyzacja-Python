import requests, sys, webbrowser, bs4

print("wyszukiwanie")
res = requests.get("http://google.pl/search?q=" + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")
# print(soup)
linkElems = soup.select(".egMi0 a")
print(linkElems)
print("\n")

linkElems = soup.select(".egMi0 a")
numOpen = min(2, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.pl' + linkElems[i].get('href'))