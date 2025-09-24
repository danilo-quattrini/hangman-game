"""
Let's start by thinking what components we can use for our game?
 - List? <- This one is better
 - Dict?
 - Variables? <- We can use it either

I think the game work like this:
    1. First we write/define the word the user should guess (Maybe we can implement a list of words?).
    2. Then we save the first and the last letter into a List
        (We define the list before with the size of the word).
    3. While in the middle of the list, we leave an empty space.
    4. Then the script will ask the user to write a word (cheks if it's a word and not a phrase)
    5. If the user guess the word, then we will add the word into the list (list.append())
    6. Whereas, if the word is the wrong one we will display a piece of the hang man, that shown its mistake.
"""
# Use the random library to pick a random value from a list
import random
from typing import List
def word_formatter(word_to_guess: str):
    field_list = list()
    for character in word_to_guess:
        if character not in word_to_guess[1: len(word_to_guess) - 1]:
            field_list.append(character)
        else:
            field_list.append("_")
    print(field_list)


    while life != 0:
        print("==>", end="\r")
        letter_guessed = str(input())
        while len(letter_guessed) > 1:
            print("Just one word not a string!!")
            break
def main():
    # List of words we can pick randomly
    word_list: List[str] = ["Leather", "Fish", "Cat", "Math"]

    generated_word: str = word_list[random.randint(0, len(word_list) - 1)]
    word_formatter(generated_word)

if __name__ == "__main__":
    main()