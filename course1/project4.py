from random import *

lives = 8
# Random
magic_number = randint(0, 100)
number = 0

while lives > 0:
    print(f".: Lives: {lives}:.")
    number = int(input("Enter a number between 0-100: "))
    if number < 0 or number > 100:
        print(f"{number} is OUT of 0 - 100 range")
    elif number > magic_number:
        print(f"{number} is MAJOR to magic number")
    elif number < magic_number:
        print(f"{number} is MINOR to magic number")
    else:
        break
    lives -= 1

if lives > 0:
    print(f"\n¡Congrulations, you found the magic number ({magic_number})!")
else:
    print(f"¡\nEres un pendejo ajaja, el magic number was {magic_number}!")
