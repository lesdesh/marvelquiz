from gamecomponents import gamevars

def total(value):
    #do logic to see what character

    if value <= 180: 
        gamevars.characters = gamevars.characters [0]
        print("It's " + gamevars.characters)
    elif value <= 70: 
        gamevars.characters = gamevars.characters [1]
        print("It's " + gamevars.characters)
    elif value <= 110: 
        gamevars.characters = gamevars.characters [2]
        print("It's " + gamevars.characters)
    elif value <= 60: 
        gamevars.characters = gamevars.characters [3]
        print("It's " + gamevars.characters)
    elif value <= 230: 
        gamevars.characters = gamevars.characters [4]
        print("It's " + gamevars.characters)

        

