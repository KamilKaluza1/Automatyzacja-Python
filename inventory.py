inventory = {'lina': 1, 'pochodnia': 6, 'złote monety': 42, 'sztylet': 1, 'strzała': 12}

def displayInwentory(inventory):
    print('inwentarz: ')
    item_total = 0 
    for k, v in inventory.items():
        print(f"{k}: {v}")
        item_total = item_total + v
    print(f"w sumie {item_total} przedmiotów")

displayInwentory(inventory)