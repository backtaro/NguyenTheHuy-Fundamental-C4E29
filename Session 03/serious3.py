# 3a
from random import *

word = ("champion")
correct = word
mixed = ""

while word:
    position = randrange(len(word))
    mixed += word[position]
    word = word[:position] + word[(position + 1):]

print("The mixed word is:", mixed)
guess = input("Your answer: ")
while guess != correct:
    print(":(")
    guess = input("Your answer: ")
if guess == correct:
    print("Hura")

# #3b
from random import *

WORDS = ("meticulous", "champion", "hexagon")
word = choice(WORDS)
correct = word
mixed = ""
while word:
    position = randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("The mixed word is:", mixed)
guess = input("Your answer: ")
while guess != correct:
    print(":(")
    guess = input("Your answer: ")
if guess == correct:
    print("Hura")

