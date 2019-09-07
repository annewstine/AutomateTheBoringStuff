#Code from displayInventory program
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, quantity in inventory.items():
        #k = item, v = quantity
        print(str(quantity)+ ' ' +item)
        item_total = item_total + quantity
    print("Total number of items: " + str(item_total))

#New code
def addToInventory(inventory, addedItems):
    #rename k; k = loot
    for loot in addedItems:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

