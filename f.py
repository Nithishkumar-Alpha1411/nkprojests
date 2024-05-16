import random
import os

number = random.randint(1,10)

guess = input("Silly Game! Guess number between 1 and 10")
guess = int(guess)

if guess == number:
    print("you won!")
else:
    os.remove("D:\test\nk1")
          
