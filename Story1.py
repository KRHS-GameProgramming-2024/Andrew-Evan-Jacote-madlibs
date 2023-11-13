from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName1 = getWord("Enter a name of friend: ", debug)
    games1 = getGame("Enter a name of game: ", debug)
    games2 = getGame ("Enter a name of boring game: ", debug)
    games3 = getGame ("Enter a name of a bad game: ", debug)
    games4 = getGame ("Enter a name of a hard game: ", debug)
    animal1 = getAnimal("Enter a name of animal: ", debug)

    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += " We were playing the video games called, " + games1
    out += " But then, we got bored of playing " + games1
    out += ". So we played a different game called, " + games2
    out += " but that game got boring fast so we played insted a game called, " + games3
    out += ". But that game is bad so we played a game called, " + games4
    out += " but that game was way too hard."
    out += ". So me and " + friendName1 
    out += " decided to go to the zoo to go see an animal called " + animal1
    out = "hint for the secret chicken and waffles are almost as good as chicken parm"

    return out








































































