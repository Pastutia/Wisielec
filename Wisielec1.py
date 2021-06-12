#Python 3.9 Wisielec (wersja pierwsza)

import sys
import random

print("\nWitaj w grze Wisielec\n")

no_of_tries = 5

print("\nUWAGA UŻYWAJ DUŻYCH LITER!!!\n")

words = ["ANAKODNA", "POMOC", "TANIEC", "MAŁPA"]

word = random.choice(words)

used_letters = []

user_word = []


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_stat_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("użyte litery:", used_letters)
    print()


for _ in word:
    user_word.append("_")

while True:
    letter = input("Wprowadź literę: ")
    used_letters.append(letter)

    found_indexes = (find_indexes(word, letter))

    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        no_of_tries -= 1

    if no_of_tries == 0:
        print("Hasło nie zostało odganięte")
        print()
        print("Koniec gry:(")
        sys.exit(0)

    else:
        for index in found_indexes:
            user_word[index] = letter

            if "".join(user_word) == word:
                print("Brawo, to jest to słowo!", word)
                sys.exit(0)

    show_stat_of_game()