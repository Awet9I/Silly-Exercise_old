# The Star Trek writers are on strike and you need some new Sci-Fi sounding words that the actors can talk about
# https://www.youtube.com/watch?v=h4idB5KAfyc
import random
import os

words_1 = [
    "Hyperdimentional",
    "Electron",
    "hyperspace",
    "Pocket Universe",
    "Photon",
    "Wave",
    "Beam",
]
words_2 = [
    "Combuster",
    "Emitter",
    "Dampener",
    "Array",
    "Android",
    "Cyborg",
    "Torpedo",
    "Sail",
    "Terraformner",
    "Elevator",
]

with open("words1.txt", "r", encoding="utf8") as file:
    words_from_file = file.read()

input_list = words_from_file.split(" ")
print(input_list)
print(random.choice(words_1) + " " + random.choice(words_2))


def gen_word(num1, num2):
    first_choice, second_choice = random.sample(input_list, num1), random.sample(
        words_2, num2
    )
    first_choice_str = " ".join(map(str, first_choice))
    second_choice_str = " ".join(map(str, second_choice))
    s = f"This is the first list {first_choice_str} and this is the second list {second_choice_str}"
    print(s)
    joined = s.split(" ")
    print(joined)


gen_word(4, 5)
