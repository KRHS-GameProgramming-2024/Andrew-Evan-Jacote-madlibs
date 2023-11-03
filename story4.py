from Getters import *

def Story4(debug = False):
    if debug: print("Story4 Function")

    print("\n")
    friendName3 = getWord("Enter a name: ", debug)
    badname1 = getbadname("Enter a name of a bad person: ", debug)
    death1 = getdeath("Enter a name of a painful way to die: ", debug)
    
    out = "\n"
    out += "One day me and my friend, " + friendName3
    out += " decided we wanted to go see , " + movie1
    out += " when we got to the theatre we decided to get " + food1
    out += " we sit down and leave halfway through " + movie1 + " because it was bad"
    
    
    return out
