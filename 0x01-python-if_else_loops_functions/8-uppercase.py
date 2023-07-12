#!/usr/bin/python3
# 8-uppercase.py

def print_last_digit(number):
    """print the last digit of a number and return it."""
    print(abs(number) % 10, end="")
    return(abs(number) % 10)
