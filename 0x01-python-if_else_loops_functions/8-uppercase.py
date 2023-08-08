#!/usr/bin/python3

def uppercase(str):
    temp = ""
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            temp += chr(ord(letter) - 32)
        else:
            temp += letter

    print(temp)
