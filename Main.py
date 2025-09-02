class MainMenu:
    def __init__(self, displaymenu):
        print("Hello! Welcome to the Random Word Generator")
        print("Select your option:")
        print("===========================================")
        print("1. Word of the day")
        print("Write the number to select > Press Enter:")
        select = input()
        if select == "1":
            selected = WordOfTheDay()

class WordOfTheDay:
    def __init__(self):
        print("The word of the day is:")



displaymenu = MainMenu("")






