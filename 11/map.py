#! python3
# Wywietla w przeglądarce mape na podstawie adersu podanego w wierszu poleceń lub schowku

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    adress = ' '.join(sys.argv[1:]) # pobranie adresu z cmd
else:
    adress = pyperclip.paste()

webbrowser.open(f'https://www.google.pl/maps/place/{adress}')