# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.

def displayInventory(inventory):
    countSum = 0
    for items, count in inventory.items():
        countSum += count
        print(str(count) + ' ' + items)

    print('Total number of items: ' + str(countSum))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)