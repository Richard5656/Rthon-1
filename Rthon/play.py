import  subprocess, time
import data/inventory_equipment_items_etc as iet # acronym
gold_amount = 200
health = 100
attack = 3
flag = 0


#### FOOD STORE ####
def foodstore():
    global gold_amount
    print("You walk in the food store..")
    time.sleep(2)
    print("You smell something..")
    time.sleep(2)
    print("Your mind wonder's on what that smell could be..")
    time.sleep(2)
    print("A lady appears in front of you behind a counter. And asks:")
    time.sleep(2)
    print("Food Shop Cashier: May i take your order?")
    time.sleep(2)
    print("""
    [1] Sushi [4 Gold]
    [2] Shrimp [3 gold]
    [3] Chicken [6 gold]
    [4] Fish [9 gold]
    [5] Hotdog [2 gold]
    [6] spam [2 gold]
    [7] Exit the shop
    """)
    print("Pick a food.")
    food_choice = input("> ")
    if food_choice == '1':
        print("" + register_name + ":" + " Oh may i take Some sushi?")
        time.sleep(3)
        print("Food Shop Cashier: Coming Right up!.. That will be about 4 Gold!")
        time.sleep(3)
        print("You pay 4 gold to her.")
        gold_amount -= 4
        time.sleep(3)
        print("Your balence is currently: " + str(gold_amount))
        time.sleep(3)
        print("The lady gives you a pan of sushi")

    if food_choice == '2':
        print("" + register_name + ":" + " Oh may i take some Shrimp?")
        time.sleep(3)
        print("Food shop cashier: Coming right up! That will be 3 gold!")
        time.sleep(3)
        print("You hand the lady  gold. ")
        gold_amount -= 3
        print("Your balence is currently: " + str(gold_amount))
        time.sleep(2)
        print("The lady hands you a pan of shrimp")

    if food_choice == '3':
        print("" + register_name + ":" + " Oh may i take some Chicken?")
        time.sleep(3)
        print("Food shop cashier: Coming right up! That will be 6 gold!")
        time.sleep(3)
        print("You hand the lady 6 gold. ")
        gold_amount -= 6
        print("Your balence is currently: " + str(gold_amount))
        time.sleep(2)
        print("The lady hands you a pan of chicken")

    if food_choice == '4':
        print("" + register_name + ":" + " Oh may i take some Fish?")
        time.sleep(3)
        print("Food shop cashier: Coming right up! That will be 9 gold!")
        time.sleep(3)
        print("You hand the lady 9 gold. ")
        gold_amount -= 9
        print("Your balence is currently: " + str(gold_amount))
        time.sleep(2)
        print("The lady hands you a pan of Fish.")

    if food_choice == '5':
        print("" + register_name + ":" + " Oh may i take a hotdog?")
        time.sleep(3)
        print("Food shop cashier: Coming right up! That will be 2 gold!")
        time.sleep(3)
        print("You hand the lady 2 gold. ")
        gold_amount -= 2
        print("Your balence is currently: " + str(gold_amount))
        time.sleep(2)
        print("The lady hands you a hotdog.")

    if food_choice == '6':
        print("" + register_name + ":" + " Oh may i take some spam?")
        time.sleep(3)
        print("Food shop cashier: Coming right up! That will be 2 gold!")
        time.sleep(3)
        print("You hand the lady 2 gold. ")
        gold_amount -= 2
        print("Your balence is currently: " + str(gold_amount))
        time.sleep(2)
        print("The lady hands you a pan of spam.")

    print("You eat your food and gained 12+ health!")
    time.sleep(3)
    subprocess.call("clear", shell=True)
    menu()


    if food_choice == '7':
        print("You decide to leave the shop.")
        time.sleep(3)
        menu()
##########################################FUNCTIONS#####################################################################

#### MAIN MENU ####
def menu():
    print("""
    [1] Character Stat's
    [2] Store's
    [3] Missions
    [4] List inventory
    [5] Go to dungeon
    """)
    print("What would you like to do?")

    choice = input("> ")
    if choice == '1':
        subprocess.call("clear", shell=True)
        character_stats()


    elif choice == '2':
        # Start
        print("""
        [1] Food store.
        [3] Weapon sword.
        """)
        store_choice = input("> ")
        if store_choice == '1':
            subprocess.call("clear", shell=True)
            foodstore()
    elif choice == '4':
        iet.list_inventory()
        menu()
    else:
        print("Invalid option")
        menu()






def character_stats():
    print("NAME: " + register_name +"\n\n")
    print(f"HP: {health}")
    print(f"ATTACK STRENGTH: {attack}")
    print("GOLD: $" + str(gold_amount) + '\n\n')
    print("Type 'back' to go to the main menu")
    back = input("> ")
    if back == 'back':
        subprocess.call("clear", shell=True)
        menu()
    else:
        print("Invalid option")
        menu()

print("""
[1] Warrior
[2] Miner
""")

print("Pick a job.")
job = input("> ")

if job == '1':
    print("As a warrior you get: A stone sword, a stone chestplate, a stone knife")
    iet.additem_to_inventory(iet.stone_sword)
    iet.additem_to_inventory(iet.stone_knife)
    iet.additem_to_inventory(iet.stone_chest_plate)

if job == '2':
    print("As a miner you get: A flashlight, a copper pickaxe, a 10x10 backpack.")
    iet.additem_to_inventory(iet.flashlight)
    iet.additem_to_inventory(iet.copper_pickaxe)
    iet.additem_to_inventory(iet.backpack_10x10)

register_name = input("Enter a name: ")
print("As a start you get 200 worth of gold")
time.sleep(3)


# Call The main menu function when the py file starts.
subprocess.call("clear", shell=True)
menu()
