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
# List of words we can pick randomly
word_list: List[str] = ["Leather", "Fish", "Cat", "Math"]

random_word: str = word_list[random.randint(0, len(word_list) - 1)]
print(random_word)