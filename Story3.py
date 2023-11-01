from Getters import *

def Story3(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName3 = getWord("Enter a name: ", debug)
    movie1 = getMovie("Enter a name of a Movie: ", debug)
    food1 = getFood("Enter a name of a Food: ", debug)
    
    out = "\n"
    out += "One day me and my friend, " + friendName3
    out += " decided we wanted to go see , " + movie1
    out += "when we got to the theatre and we decided to get" + food1
    
    
    return out
