# przejść przez wszystkie pliki na dysku 
# sprawdzić rozmiar każdego
# jeżeli przekracza 10 MB wyświetlić rozmiar i bezwzględną ścieżkę dostępu 
import os 


automatyzacja = 'C:\\'
howMany = 0
for folderName, subfolders, filenames in os.walk(automatyzacja):
    for filename in filenames:
        path = (folderName + "\\" + filename)
        size = os.path.getsize(path)
        if size > 10000000:
            print(path)
            print(size)
            howMany += 1
            print(howMany)
