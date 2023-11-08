from Getters import *

def story4(debug = False):
    if debug: print("story4 Function")

    print("\n")
    friendName4 = getWord("Enter a name: ", debug)
    badname1 = getWord("Enter a name of a bad person: ", debug)
    badname2 = getWord("Enter a name of another bad person: ", debug)
    badname3 = getWord("Enter a name of another bad person: ", debug)
    badname4 = getWord("Enter a name of another bad person: ", debug)
    death1 = getDeath("Enter a name of a painful way to die: ", debug)
    animal1 = getAnimal("Enter a name of animal: ", debug)
    food1 = getfood("Enter a name of a Food: ", debug)
    
    
    out = "\n"
    out += "one day in a spooky dark alley me and my friend, " + friendName4
    out += " Got kidnapped by  " + badname1 + "," + badname2 + "," + badname3 + ",and " + badname4 
    out += " they sentences us to be " + death1 + "'d to death by an " +animal1 +" eating " +food1
    out += " we say our goodbyes until " + badname1 + " has a change of heart and saves us by getting rid of " + badname2 +" " badname3 +" " badname4
    
    
    return out
