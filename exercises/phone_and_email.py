#! python3
#phone_and_email.py - Wyszukuje numery telefonów i adresy email w schowku.
import pyperclip, re

phone_regex = re.compile(r'''(
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

text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    print(groups)
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

#TODO: Skopiowanie wyników do schowka.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    x='\n'.join(matches)
    print(f"Skopiowano do schowka:\n{x}")
else:
    print("nie znaleziono numeru telfonu ")

