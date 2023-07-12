#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """prints the number from 1 to 100 separated by a space.
    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of a number.
    For the multiples of three and five, print FizzBuzz instead of a number.
    """
    for number in range (1, 101):
        if number % 3 = 0 and number % 5 == 0:
            print("FizzBuzz", end="")
        elif number % 3 == 0:
            print("Fizz", end="")
        elif number % 5 == 0:
            print("Buzz", end="")
        else:
            print("{}".format(number), end="")
