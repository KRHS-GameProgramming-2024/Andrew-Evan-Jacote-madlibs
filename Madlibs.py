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
    
while not done:
        
    if Story1 == false and Story2 == false and Story3 == false:
        print(MainMenu(debug))
        
    elif Story1 == true and Story2 == false and Story3 == false:
        print(MainMenu2(debug))
        
    elif Story1 == false and Story2 == true and Story3 == false:
        print(MainMenu3(debug))
        
    elif Story1 == false and Story2 == false and Story3 == true:
        print(MainMenu4(debug))
        
    elif Story1 == true and Story2 == true and Story3 == false:
        print(MainMenu5(debug))
        
    elif Story1 == true and Story2 == false and Story3 == true:
        print(MainMenu6(debug))
        
    elif Story1 == false and Story2 == true and Story3 == true:
        print(MainMenu7(debug))
        
    elif Story1 == true and Story2 == true and Story3 == true:
        print(MainMenu8(debug))
        choice = getMenuOption(debug)
        
        if choice == "Q":
            exit();
        
        elif choice == "1":
            print(Story1())
            print("\n")
            input("Press enter")

        elif choice == "2":
            print(Story2())
            print("\n")
            input("Press enter")
            
        elif choice == "3":
            print(Story3())
            print("\n")
            input("Press enter")

        elif choice == "4":
            print(story4())
            print("\n")
            input("Press enter")


Madlibs(False)
