#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        print(chr(ord(letter) - 32)
                if ord('a') <= ord(letter) <= ord('z') else letter, end='')
    print()
