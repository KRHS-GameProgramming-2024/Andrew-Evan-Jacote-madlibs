from Getters import *

def Story3(debug = False):
    if debug: print("Story3 Function")

    print("\n")
    friendName3 = getWord("Enter a name: ", debug)
    movie1 = getMovie("Enter a name of a Movie: ", debug)
    food1 = getfood("Enter a name of a Food: ", debug)
    food2 = getfood("Please enter another Food: ", debug)
    animal1 = getAnimal("Enter name of animal: ", debug)
    games1 =  getGame("Enter the name of a game: ", debug)
    
    out = "\n"
    out += "Then me and my friend, " + friendName3
    out += " decided we wanted to go see , " + movie1
    out += " when we got to the theatre we decided to get " + food1
    out += " but the " +food1
    out += " was horrible so we got " +food2
    out += " instead."
    out += " we sit down and leave halfway through " + movie1 + " because it was bad"
    out += "We decided to go back home to walk our " +animal1
    out += "we got very tired so"
    out += "we thought it would be a good idea to go back home and play " +games1
    out += " we decide to take a shortcut home in a dark ally"
    out += "\n"
    out += "the hint is sta"
    
    
    return out
