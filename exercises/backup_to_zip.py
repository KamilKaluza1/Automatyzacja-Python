import zipfile, os

def backupToZip(folder):
    # Umieszczenie w archiwum ZIP całej zawartości katalogu
    folder = os.path.abspath(folder) # bezwzględna ścieżka 
    # Ustalenie nazwy pliku jaka powinna zostać użyta przez kod na podstawie istniejących plików
    number = 1 
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    # Utworzenie archiwum ZIP
    print('Tworzenie archiwum %s...', (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # Przejście przez cale drzewo katalogu i kompresja plików we wszystkich podkatalogach
    for foldername, subfolders, filenames in os.walk(folder):
        print('Dodawanie plików w %s..', (foldername))
        # dodamoe bieżącego katalogu do archiwum ZIP
        backupZip.write(foldername)
        # Dodanie wszystkich plików znajdujących się w tym katalogu do archiwum ZIP
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue # W archiwum nie umieszamy archium 
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("gotowe")
backupToZip('C:\\Users\\48533\\OneDrive\\Pulpit\Automatyzacja nudnych zadań python\\exercises\\katalog')