def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("Please select an option")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "Q"):
                option = "Q"
                goodInput = True

        elif (option == "1" or 
            option == "one" or 
            option == "One" or
            option == "story one" or
            option == "Story one" or
            option == "story 1" or
            option == "Story 1" or
            option == "story1" or
            option == "Story1" ):
                option = "1"
                goodInput = True
                
        elif (option == "2" or 
            option == "two" or 
            option == "Two" or
            option == "story two" or
            option == "Story two" or
            option == "story 2" or
            option == "Story 2" or
            option == "story2" or
            option == "Story2" ):
                option = "2"
                goodInput = True

        elif (option == "3" or 
            option == "three" or 
            option == "Three" or
            option == "story three" or
            option == "Story three" or
            option == "story 3" or
            option == "Story 3" or
            option == "story3" or
            option == "Story3" ):
                option = "3"
                goodInput = True
        
        elif (option == "4" or 
            option == "four" or 
            option == "Four" or
            option == "story four" or
            option == "Story four" or
            option == "story 4" or
            option == "Story 4" or
            option == "story4" or
            option == "Story4" ):
                option = "4"
                goodInput = True
          
        else:
            print("Please make a valid choice")
            
    return option
    

def getWord(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print (" Don't use bad word bro")
            
    return word
    
def getGame(prompt, debug = False):
    if debug: print("getGame Function")
    
    goodInput = False
    
    games = ["minecraft",
    "roblox",
    "tf2",
    "team fortress 2",
    "counter strike",
    "csgo",
    "counter strike 2",
    "cs2",
    "fortnite",
    "persona 5",
    "cod",
    "call of duty"
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print (" Don't use bad word bro")
        elif word.lower() not in games:
            goodInput = False
            print (" Sorry, I don't know that one.")
            
    return word

def getAnimal(prompt, debug = False):
    if debug: print("getAnimal Function")
    
    goodInput = False
    
    Animal = ["giraffe",
    "zebra", 
    "dog", 
    "cat",
    "monkey",
    "penguin",
    "parrot",
    "gorilla",
    "ant eater",
    "horse",
    "tiger",
    "cow",
    "snake",
    "bear",
    "wolf",
    "sloth",
    "leopard",
    "cheetah",
    "frog",
    "goat",
    "capybara",
    "sheep",
    "shark",
    "otter",
    "racoon",
    "narwhal",
    "deer",
    "quokka",
    "koala",
    "donkey",
    "panda",
    "red panda",
    "cougar",
    "ferret",
    "hippo",
    "squirrel",
    "meerkat",
    "elephant"]
    
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print (" Don't use bad word bro")
        elif word.lower() not in Animal:
            goodInput = False
            print (" Sorry, I don't know that one.")
            
    return word
    
def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False
        
        

swearList = ["shit",
            "cock",
            "bitch",
            "fuck",
            "cunt",
            "pussy",
            "ass",
            "asshole"
            ]






def getMovie(prompt, debug = False):
    if debug: print("getMovie Function")

    goodInput = False

            
    movieList = ["strays",
                "barbie",
                "cars2"
                ]
                
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if word.lower() not in movieList:
            goodInput = False
            print ("thats not in theaters bud")
    return word

            
def getfood(prompt, debug = False):
    
    
    
    
    if debug: print("getFood Function")

    goodInput = False

            
    foodList = ["popcorn",
                "lasagna",
                "fried chicken"
                ]
                
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if word.lower() not in foodList:
            goodInput = False
            print ("pick again we got popcorn, lasagna, and fried chicken")
    return word


def getDeath(prompt, debug = False):
    if debug: print("getDeath Function")

    goodInput = False

            
    DeathList = ["hung",
                "snoo snoo",
                "shot",
                "beat",
                "poison",
                "torture"
                ]
                
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if word.lower() not in DeathList:
            goodInput = False
            print ("thats sick pick something a little more tame bud")
    return word
