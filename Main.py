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
        print("2. Add words and description")
        print("Write the number to select > Press Enter:")
        select = input()
        if select == "1":
            print(f"You have selected: {select}")
            a = WordOfTheDay()
        elif select == "2":
            print(f"You have seleceted: {select}")
            b = AddWordAndDescription()

class WordOfTheDay:
    def __init__(self):
        while True:
            print("The word of the day is:")
            word = random.choice(words)
            print(f"{word[0]}", "//", f"{word[1]}", "//", f"{word[2]}")
            print("Write A to return to menu / Write R for a random word")
            word_menu_choice = input()
            if word_menu_choice.lower() == "a":
                print("===========================================")
                print("===========================================")
                MainMenu("")
                break
            elif word_menu_choice.lower() != "r":
                print("Invalid choice. Please enter 'A' or 'R'.")

class AddWordAndDescription:
    def __init__(self):
        print("Welcome to Word Management.")
        print("===========================================")
        print("===========================================")
        print("Please input the new word:")
        word_add = input()
        print("Please input the word type (e.g. noun, adjective, adverb, etc.)")
        word_type = input()
        print("Please input the definition or meaning of the word: ")
        word_definition = input()
        cursor.execute(
            "INSERT INTO WordList (WordName, WordType, WordDefinition) VALUES (?, ?, ?)",
            (word_add, word_type, word_definition)
        )
        conn.commit()
        with open('WordList.sql', 'a') as f:
            f.write(
                f"INSERT INTO WordList (WordName, WordType, WordDefinition) VALUES ('{word_add}', '{word_type}', '{word_definition}');\n"
            )
        print("Great! The word, its type and definition has been added.")

class AddWordAndDescription:
    def __init__(self):
        print("Welcome to Word Management.")
        print("===========================================")
        print("===========================================")
        print("Please input the new word:")
        word_add = input()
        print("Please input the word type (e.g. noun, adjective, adverb, etc.)")
        word_type = input()
        print("Please input the definition or meaning of the word: ")
        word_definition = input()
        cursor.execute(
            "INSERT INTO WordList (WordName, WordType, WordDefinition) VALUES (?, ?, ?)",
            (word_add, word_type, word_definition)
        )
        conn.commit()
        with open('WordList.sql', 'a') as f:
            f.write(
                f"INSERT INTO WordList (WordName, WordType, WordDefinition) VALUES ('{word_add}', '{word_type}', '{word_definition}');\n"
            )
        print("Great! The word, its type and definition has been added.")
        print(f"'{word_add}' / '{word_type}' / '{word_definition}'")
        print("Returning to menu...")
        # To do: Give the choice to allow user to add another word
        MainMenu("")

displaymenu = MainMenu("")







