#!/usr/bin/python3

a, z, i = 'a', 'z', 1

while ord(z) >= ord(a):
    print(z if i % 2 != 0 else chr(ord(z) - 32), end='')
    z = chr(ord(z) - 1)
    i += 1
