inventory = {'lina': 1, 'pochodnia': 6, 'złote monety': 42, 'sztylet': 1, 'strzała': 12}

dragonLoot = ['złote monety', 'sztylet', 'złote monety', 'złote monety', 'ruby']

def displayInwentory(inventory):
    print('inwentarz: ')
    item_total = 0 
    for k, v in inventory.items():
        print(f"{k}: {v}")
        item_total = item_total + v
    print(f"w sumie {item_total} przedmiotów")


def add_to_inventory(inventory, dragonLoot):
    for value in dragonLoot:
        inventory.setdefault(value, 0)
        inventory[value] = inventory[value] +1
    displayInwentory(inventory)



add_to_inventory(inventory, dragonLoot)