#You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary
# #where the keys are string values describing the item in the inventory and the value is an integer value
# detailing how many of that item the player has.
import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+ ' ' +k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
