from Getters import *

def story4(debug = False):
    if debug: print("story4 Function")

    print("\n")
    friendName4 = getWord("Enter a name: ", debug)
    badname1 = getbadname("Enter a name of a bad person: ", debug)
    death1 = getdeath("Enter a name of a painful way to die: ", debug)
    
    out = "\n"
    out += "One day me and my friend, " + friendName3
    out += " Got kidnapped by , " + badname1
    out += " he sentences us to be " + death1 + "to death"
    out += " we say our goodbyes until " + badname1 + " has a change of heart and lets us go ,Hooray"
    
    
    return out
