file = open('file.txt', 'r')
fileContent = file.read()
fileContent = fileContent.split()
file.close()
przymiotnik = input('Podaj przymiotnik:')
rzeczownik = input('Podaj rzeczownik:')
czasownik = input('Podaj czasownik:')
przys = input('Podaj przysłówek:')
for i in fileContent:
    if i == 'PRZYMIOTNIK':
        fileContent[fileContent.index(i)] = przymiotnik
    elif i == 'RZECZOWNIK':
        fileContent[fileContent.index(i)] = rzeczownik
    elif i == 'CZASOWNIK':
        fileContent[fileContent.index(i)] = czasownik
    elif i == 'PRZYS':
        fileContent[fileContent.index(i)] = przys
fileContent = ' '.join(fileContent)
file = open('file.txt', 'w')
file.write(fileContent)
file.close()