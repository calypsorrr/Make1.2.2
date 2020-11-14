#!/usr/bin/env python
"""
Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
"""


import random
import time


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():
    print("There are some numbers between 1 and 10, you just have to guess ")  # Printing something out
    time.sleep(2)                                                              # Program stops for 2 seconds
    RANDOM_NUMBER = random.randint(1, 10)                                      # Generating a random number
    guess = 0                                                                  # Guessing starts with 0
    count = 0                                                                  # Count starts with 0


    while guess != RANDOM_NUMBER:                                              # When guess is equel to RANDOM_NUMBER
        guess = input("Enter a guess between 1 and 10 ")                       # Asking a input between 1 and 10

        guess = int(guess)
        count += 1                                                      # Everytime user guesses counter goes up with 1

        if guess < RANDOM_NUMBER:                                       # If the guess was lower than the number
            print("Too low")                                            # Print Too low
        elif guess > RANDOM_NUMBER:                                     # If the guess was higher than the number
            print("Too high")                                           # print Too high
        else:                                                           # if it isn't 1 of the 2 above then this
            print("Good job")                                           # print Good job
            print("You took only", count, "tries")                      # print you took only, (how many guesses) tries

if __name__ == '__main__':  # code to execute if called from command-line
    main()
