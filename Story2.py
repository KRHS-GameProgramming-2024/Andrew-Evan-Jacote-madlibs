from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    animal1 = getAnimal("Enter a name of animal: ", debug)

    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += " found an animal on the street called a, " + animal1
    out += " we took the " + animal1
    out += " back home and took great care of it."
    out += " But then we had the idea of bringing the " + animal1
    out += " to the theater"

    return out








































































