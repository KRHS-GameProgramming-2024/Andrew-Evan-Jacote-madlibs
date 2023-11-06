from Getters import *

def Story3(debug = False):
    if debug: print("Story3 Function")

    print("\n")
    friendName3 = getWord("Enter a name: ", debug)
    movie1 = getMovie("Enter a name of a Movie: ", debug)
    food1 = getfood("Enter a name of a Food: ", debug)
    
    out = "\n"
    out += "One day me and my friend, " + friendName3
    out += " decided we wanted to go see , " + movie1
    out += " when we got to the theatre we decided to get " + food1
    out += " we sit down and leave halfway through " + movie1 + " because it was bad"
    out += " we decide to take a shortcut home in a dark ally"
    
    
    return out
