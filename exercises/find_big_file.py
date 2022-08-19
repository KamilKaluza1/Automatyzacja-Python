# przejść przez wszystkie pliki na dysku 
# sprawdzić rozmiar każdego
# jeżeli przekracza 10 MB wyświetlić rozmiar i bezwzględną ścieżkę dostępu 
import os 

#os.path.getsize()


# testowo przechodzimy przez wszystkie pliki w automatyzacji 
automatyzacja = 'C:\\Users\\48533\\OneDrive\\Pulpit\\Automatyzacja nudnych zadań python'
for folderName, subfolders, filenames in os.walk(automatyzacja):
    for filename in filenames:
        path = (folderName + "\\" + filename)
        size = os.path.getsize(path)
        if size > 150000:
            print(path)
            print(size)




# for folderName, subfolders, filenames in os.walk(automatyzacja):
#     print('Katalog bieżący to ' + folderName)
#     # for subfolder in subfolders:
#     #     print('PODKATALOG KATALOGU ' + folderName + ': ' + subfolder)
#     for filename in filenames:
#         print('PLIK KATALOGU ' + folderName + '\\' + filename)
#     print('')