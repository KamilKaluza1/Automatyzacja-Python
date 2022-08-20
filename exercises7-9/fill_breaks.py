# wyszukuje wszystkie pliki o podanym prefiksie .txt z danego katalogu 
# ustala przerwy w numeracji 
# przesuwa następny plik  w miejsce brakującego elementu zmieniając jego nazwe 
import os, re 
katalog = 'C:\\Users\\48533\\OneDrive\\Pulpit\Automatyzacja nudnych zadań python\\exercises\\katalog'


listOfDirs = os.listdir(katalog)
for dir in listOfDirs:
    if dir.endswith('.txt'):
        print(dir)