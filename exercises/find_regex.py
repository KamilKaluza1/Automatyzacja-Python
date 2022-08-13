import re, os
# Otwiera i przeszukuje wszystkie pliki txt znajdujące się w bieżącym katalogu
# Szuka wyrażenia regularnego podanego przez użytkownika 
# Wyświetla liczbę odnalezionych wyrażeń regularnych 
# re.compile(r'[A]')




for file in os.listdir('katalog'):
    open((os.path.abspath(str(file)), 'r')