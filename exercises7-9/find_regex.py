import re, os
# Utwórz program otwierający wszystkie pliki typu .txt znajdujące się w katalogu
# oraz szukający wierszy dopasowanych do podanego przez użytkownika wyrażenia
# regularnego. Wynik działania programu powinien być wyświetlony na ekranie.

# Otwiera i przeszukuje wszystkie pliki txt znajdujące się w bieżącym katalogu OKOKOK
# Szuka wyrażenia regularnego podanego przez użytkownika 
# Wyświetla liczbę odnalezionych wyrażeń regularnych 

item = input("czego szukać?")

is_Kansas = re.compile(str(item))
is_txt= re.compile(r'(txt)$')
fund = 0


for file in os.listdir('katalog'):
    if is_txt.search(file) != None:
        path = os.path.join(os.getcwd(), "katalog", file)
        fileOpen = open(path, 'r')
        fileContent = fileOpen.read()
        i = is_Kansas.findall(fileContent)
        fund += len(i)

print(f"znaleziono {fund} wyników wyszukiwania")