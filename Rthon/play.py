import os, subprocess, time
print("loading..")
time.sleep(2)

#### HELP ####
def help():
    print("To pick an option enter a command based on whats on the screen.")
    time.sleep(4)
    print("To Exit type 'exit'")
    time.sleep(2)
    print("Type 'back' to go back to the main menu")
    help = input("> ")
    if help == 'back':
        main_menu()


#### MAIN MENU ####
def main_menu():
    print('##################')
    print('##     Rthon    ##')
    print('##################')
    print('##################')
    print('##    -play     ##')
    print('##    -help     ##')
    print('##    -quit     ##')
    print('##################')
    print('##copyright 2021##')
    print('##################')
    print("Pick a option!")
    main_menu = input("> ")

    if main_menu == 'play':
        os.chdir('Data')
        subprocess.call("python game.py", shell=True)

    if main_menu == 'help':
        help()

    if main_menu == 'quit':
        subprocess.call("exit", shell=True)

#### CALL MAIN MENU WHEN FILE STARTS ####
main_menu()


