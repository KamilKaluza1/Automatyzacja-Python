#! python3
# renname_dates.py — Zmienia nazwę pliku wraz z datą w formacie amerykańskim (MM-DD-RRRR) na datę w formacie europejskim (DD-MM-RRRR).
import shutil, os, re

# Utworzenie wyrażenia regularnego dopasowującego pliki zawierające w nazwie datę w formacie amerykańskim.

datePattern = re.compile(r"""^(.*?) # Cały tekst przed datą.
 ((0|1)?\d)- # Jedna lub dwie cyfry określające miesiąc.
 ((0|1|2|3)?\d)- # Jedna lub dwie cyfry określające dzień.
 ((19|20)\d\d) # Cztery cyfry określające rok.
 (.*?)$ # Cały tekst po dacie.
 """, re.VERBOSE)



# Iteracja przez pliki znajdujące się w katalogu roboczym.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None: # Pominięcie plików bez daty.
        continue
    beforePart = mo.group(1) # Pobranie poszczególnych fragmentów nazwy pliku.
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yerPart = mo.group(6)
    afterPart = mo.group(8)



# Przygotowanie nazwy pliku zawierającej datę w formacie europejskim.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yerPart + afterPart
# Pobranie pełnych, bezwzględnych ścieżek dostępu do pliku.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# Zmiana nazwy plików.
    print('Rennaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)
