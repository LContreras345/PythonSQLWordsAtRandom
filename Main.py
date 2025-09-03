import random
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

with open('WordList.sql', 'r') as f:
    sql_script = f.read()
cursor.executescript(sql_script)

cursor.execute("SELECT WordName, WordType, WordDefinition FROM WordList")
words = cursor.fetchall()
for row in cursor.fetchall():
    print(row)

class MainMenu:
    def __init__(self, displaymenu):
        print("Hello! Welcome to the Random Word Generator")
        print("Select your option:")
        print("===========================================")
        print("1. Word of the day")
        print("Write the number to select > Press Enter:")
        select = input()
        if select == "1":
            print(f"You have selected: {select}")
            a = WordOfTheDay()

class WordOfTheDay:
    def __init__(self):
        print("The word of the day is:")
        word = random.choice(words)
        print(f"{word[0]}", "//", f"{word[1]}", "//", f"{word[2]}")
        print("Write A to return to menu")
        goback = input()
        if goback.lower() == "a":
            print("===========================================")
            print("===========================================")
            displaymenu = MainMenu("")


displaymenu = MainMenu("")







