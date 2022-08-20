# Przechodzenie przez drzewo katalogu wyszukiwanie plików o określonym rozszerzeniu .jpg
# znalezione pliki wklejamy do nowego katalogu znalezione 
import os, shutil
katalog = 'C:\\Users\\48533\\OneDrive\\Pulpit\Automatyzacja nudnych zadań python\\exercises\\katalog'
znalezione = 'C:\\Users\\48533\\OneDrive\\Pulpit\\Automatyzacja nudnych zadań python\\exercises\\znalezione'
for folderName, subfolders, filenames in os.walk(katalog):
    for filename in filenames:
        if filename.endswith(".jpg"):
            path = folderName + "\\" + filename
            print(path)
            shutil.copy(path, znalezione)
