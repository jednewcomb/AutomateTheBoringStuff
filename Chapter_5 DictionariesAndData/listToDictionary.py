def addToInventory(inventory, list):
    for i in range(len(list)):
        inventory.setdefault(list[i], 0)
        inventory[list[i]] = inventory[list[i]] + 1

    countSum = 0
    for items, count in inventory.items():
        countSum += count
        print(str(count) + ' ' + items)

    print('Total number of items: ' + str(countSum))

inventory = {'gold coin' : 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inventory, dragonLoot)