#!/usr/bin/python3
# 2-print_alphabet.py
"""print the alphabet in lowercase, not followed by a newline"""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
