def TitleScreen(debug = False):
    if debug: print("TitleScreen Function")
    
    s = "|--------------------------------------|\n"
    s+= "| Mablibs thing                        |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|                    By Andrew Parker  |\n"
    s+= "|                       Evan Henley    |\n"
    s+= "|                       Jacote Ryder   |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|       Press enter to continue        |\n"
    s+= "|--------------------------------------|\n"

    return s



def MainMenu(debug = False):
    if debug: print("MainMenu Function")
    
    s = "|--------------------------------------|\n"
    s+= "|               Madlibs                |\n"
    s+= "|                                      |\n"
    s+= "|  1) Story 1                          |\n"
    s+= "|                                      |\n"
    s+= "|  2) Story 2                          |\n"
    s+= "|                                      |\n"
    s+= "|  3) Story 3                          |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|  Q) Quit                             |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|                                      |\n"
    s+= "|--------------------------------------|\n"

    return s

def updateMenu(menu, num):
    lines = menu.split('\n')
    if num == 1:
        lines[3] =  "|  1) Story 1         complete         |\n"
    elif num == 2:
        lines[5] =  "|  2) Story 2         complete         |\n"
        
    if num == 123:
        lines[9] =  "|  4) Story 4                          |\n"
        
    out = ""
    for line in lines:
        out += line
        
    return out
