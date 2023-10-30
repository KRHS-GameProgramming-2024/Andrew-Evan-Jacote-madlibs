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
    
    Animal = ["Giraffe",
    "Zebra", 
    "Dog", 
    "Cat",
    "Monkey",
    "Penguin",
    "Parrot",
    "Gorilla",
    "Ant eater",
    "Horse",
    "Horse",
    "Tiger",
    "Cow",
    "Snake",
    "Bear",
    "Wolf",
    "Sloth",
    "Leopard",
    "Cheetah",
    "Frog",
    "Goat",
    "Capybara",
    "Sheep",
    "Sharks",
    "Otter",
    "Racoon",
    "Narwhal",
    "Deer",
    "Quokka",
    "Koala",
    "Donkey",
    "Panda",
    "Red Panda",
    "Cougar",
    "Ferret",
    "Hippo",
    "Squirrel",
    "Meerkat",
    
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

