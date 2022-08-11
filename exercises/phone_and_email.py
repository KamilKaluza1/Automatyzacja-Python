#! python3
#phone_and_email.py - Wyszukuje numery telefonów i adresy email w schowku.
import pyperclip, re

phone_regex = re.compile(r'''(#tworzy wrzozec
    (\d{3}|\(\d{3}\))?             #3 cyfry lub 3 cyfry w nawiasie może tego wgl nie być 
    (\s|-|\.)?                     # znak białyn lub myślnik lub kropka może nie wystąpić 
    (\d{3})                        # 3 cyfry
    (\s|-|\.)                      # znak białyn lub myślnik lub kropka
    (\d{4})                        # 4 cyfry
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # (dow liczba spacji ext,x,ext. dow l spacji wewn od 2do5 cyfr) opcjonalnie 
    )''', re.VERBOSE) 

# Utworzenie wyrażenia regularnego dopasowującego adres emai.

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # Nazwa użytkownika złożona z możliwych znaków 
    @                   # znak@
    [a-zA-Z0-9.-]+      # Nazwa domeny 
    (\.[a-zA-Z]{2,4})   # Kropka i później cokolwiek pl com net
    )''', re.VERBOSE)   # Umożliwa zapis j.w.

# Wyszukanie dopasowań w schowsku.

text = str(pyperclip.paste()) # Pobiera zawartosć schowka
matches = []  #Tworzy pustą liste matches

for groups in phone_regex.findall(text): # iteruje przez grupy wyszukane w texcie 
    phone_num = '-'.join([groups[1], groups[3], groups[5]]) # tworzy nuymer do wyświetelenia
    if groups[8] != '': #sprawdza czy został podny numer wewnętrzny
        phone_num += ' x' + groups[8] #jeżeli został dodaje go po x 
    matches.append(phone_num) # przygotowany do wyświetlenia numer zostanie dodany do listy 

for groups in email_regex.findall(text): # iteruje znalezione w tekscie @ 
    matches.append(groups[0]) #dodaje poprawne wartości do lisy

# Skopiowanie wyników do schowka.

if len(matches) > 0: #jeżeli lista nie jest pusta wyświetla ją w sformatowany spodosób 
    pyperclip.copy('\n'.join(matches))
    x='\n'.join(matches)
    print(f"Skopiowano do schowka:\n{x}")
else: #jeżeli jest pusta informuje o braku wyników 
    print("nie znaleziono numeru telfonu ")

