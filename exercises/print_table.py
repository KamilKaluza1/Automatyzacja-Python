tableData = [
    ['Alicja', 'Bob', 'Karol', 'Dawid'],
    ['jabłka', 'pomarańcze', 'wiśnie', 'banany'],
    ['psy', 'koty', 'łosie', 'gęsi'],
    ]

def print_table(tableData):
    lenght =[]
    for value in tableData:
        for x in value:
            lenght.append(len(x))
    for x in range(len(tableData[0])):
        for row in tableData:
            print(row[x].rjust(max(lenght)),end=' ')
        print('')

print_table(tableData)