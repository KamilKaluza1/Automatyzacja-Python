#! python3
# backupToZip.py — Katalog wraz z całą zawartością zostaje umieszczony w archiwum ZIP, którego nazwa jest inkrementowana za każdym razem.
import zipfile
import os
def backupToZip(folder):
 # Umieszczenie w archiwum ZIP całej zawartości katalogu
    folder = os.path.abspath(folder) # Upewniamy się, że otrzymaliśmy bezwzględną ścieżkę dostępu do folderu.
 # Ustalenie nazwy pliku, jaka powinna zostać użyta przez kod na podstawie istniejących plików.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
 # Utworzenie archiwum ZIP.
    print(f'tworzenie archiwum {zipFilename}')
    backupZip = zipfile.zipFile(zipFilename, 'w')
 # TODO: Przejście przez całe drzewo katalogu i kompresja plików we wszystkich podkatalogach.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"dodawanie pików w {foldername}...")
        #dodanie bieżącego katalogu do archiwum zip
        backupZip.write(foldername)
        # Dodanie wszystkich plików najdujących się w tym katalodu do archiwum zip
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Gotowe!')
backupToZip('C:\\delicious')

# (!) Przejście przez drzewo katalogu i archiwizacja jedynie plików z określonymi
# rozszerzeniami, takimi jak .txt i .py, nic poza tym.
# (!) Przejście przez drzewo katalogu i archiwizacja wszystkich plików
# z wyłączeniem zawierających określone rozszerzenia, na przykład .txt i .py.
# (!) Wyszukanie katalogu w drzewie katalogów, który będzie miał większą liczbę
# plików niż podana lub będzie używał największej ilości miejsca na dysku.