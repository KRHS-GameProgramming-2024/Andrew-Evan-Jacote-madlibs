from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    animal1 = getAnimal("Enter a name of animal: ", debug)
    movie1 = getMovie("Enter a name of movie: ", debug)
    movie2 = getMovie("Please enter another movie: ", debug)
    food1 = getfood("Enter a name of a Food: ", debug)
    food2 = getfood("Please name another Food: ", debug)
    games1 = getGame("Enter a name of a game: ", debug)

    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += " found an animal on the street called a, " + animal1
    out += " we took the " + animal1
    out += " back home and took great care of it."
    out += " But then we had the idea of bringing the " + animal1
    out += " to the theater to watch " + movie1
    out += " with some " + food1
    out += " the movie started to get really boring so we left."
    out += " After the movie we decided to get some " +food2
    out += " at one of my favorite restaurants."
    out += "After we ate we went back home and played " +games1
    out += "after we've been playing for hours a new movie from our favorite series came out called " +movie2
    out = "hint is pa"

    return out








































































