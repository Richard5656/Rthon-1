import __main__ as maine
import os

inventory = []
main_slot = []
equipment = []
missions = []
buyable = []



#add price value to item dictionarys

i=0
def list_inventory():
    global i

    if(i == 0):
        os.system("clear")
        print(str(maine.register_name) + "'s Inventory:\n\n")
        
    print("["+ str(i) +"]" + str(inventory[i]['name']))

    i+=1 

    if(i<len(inventory)):
        list_inventory()
    
        

def additem_to_inventory(item):
    inventory.append(item)


def stone_sword_usage():
	pass

def stone_knife_usage():
	pass


def flashlight_usage():
    pass


def copper_pickaxe_usage():
    pass

def backpack_10x10_usage():
    pass

stone_sword = {
    "name": "Stone Sword",
	"attack": 10,
	"usage": stone_sword_usage
}


stone_knife = {
    "name": "Stone Knife",
	"attack": 5,
	"usage": stone_knife_usage
}

stone_chest_plate ={
    "name": "Stone Chest Plate",
	"defense": 4
}

flashlight ={
    "name": "Flashlight",
    "usage": flashlight_usage
}

copper_pickaxe = {
    "name": "Copper Pickaxe",
    "usage": copper_pickaxe_usage
}

backpack_10x10 = {
    "name": "backpack_10x10",
    "usage": backpack_10x10_usage

}
