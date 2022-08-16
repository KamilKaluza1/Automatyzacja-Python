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


 
# TODO: Iteracja przez pliki znajdujące się w katalogu roboczym.
# TODO: Pominięcie plików bez daty.
# TODO: Pobranie poszczególnych fragmentów nazwy pliku.
# TODO: Przygotowanie nazwy pliku zawierającej datę w formacie europejskim.
# TODO: Pobranie pełnych, bezwzględnych ścieżek dostępu do pliku.
# TODO: Zmiana nazwy plików.
