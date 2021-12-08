from gamecomponents import gamevars
from PIL import Image
from colorama import init
from colorama import Fore

def total(value):

    init()

    if value <= 60: 
        gamevars.characters = gamevars.characters [0]
        print(Fore.CYAN + "It's " + gamevars.characters)
        RocketRaccoon = Image.open("rocket.jpg")
        RocketRaccoon.show()
    elif value <= 75: 
        gamevars.characters = gamevars.characters [1]
        print(Fore.GREEN + "It's " + gamevars.characters)
        Gamora = Image.open("gamora.jpg")
        Gamora.show()
    elif value <= 180: 
        gamevars.characters = gamevars.characters [2]
        print(Fore.RED + "It's " + gamevars.characters)
        BuckyBarnes = Image.open("bucky.jpg")
        BuckyBarnes.show() 
    elif value <= 185: 
        gamevars.characters = gamevars.characters [3]
        print(Fore.RED + "It's " + gamevars.characters)
        WandaMaximoff = Image.open("wanda.jpg")
        WandaMaximoff.show()
    elif value <= 230: 
        gamevars.characters = gamevars.characters [4]
        print(Fore.GREEN + "It's " + gamevars.characters)
        Hulk = Image.open("hulk.jpg")
        Hulk.show()

    

        

