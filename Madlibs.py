from Screens import *
from Getters import *
from Story1 import *
from Story2 import *
from Story3 import *
from story4 import *

def Madlibs(debug = False):
    if debug: print("Welcome to debug")
    
    print(TitleScreen(debug))
    try:
        input("Press enter")
    except:
        pass
    
    done = False
    completed = []
    fourUnlock = False
    menu = MainMenu(debug)
    while not done:
        print(menu)
        choice = getMenuOption(fourUnlock, debug)
            
        if choice == "Q":
            exit();
        
        elif choice == "1":
            print(Story1())
            print("\n")
            input("Press enter")
            menu = updateMenu(menu, 1)
            completed += [1]

        elif choice == "2":
            print(Story2())
            print("\n")
            input("Press enter")
            menu = updateMenu(menu, 2)
            completed += [2]
            
        elif choice == "3":
            print(Story3())
            print("\n")
            input("Press enter")
            menu = updateMenu(menu, 3)
            completed += [3]

        elif choice == "4":
            print(story4())
            print("\n")
            input("Press enter")
            menu = updateMenu(menu, 4)
            completed += [4]
            
        if 1 in completed and 2 in completed and 3 in completed:
            menu = updateMenu(menu, 123)
            fourUnlock = True


Madlibs(False)
