#!/usr/bin/python3
for ch in range(97, 97 + 26):
    if ord('q') == ord(chr(ch)) or ord('e') == ord(chr(ch)):
        continue
    print('{}'.format(chr(ch)), end="")
