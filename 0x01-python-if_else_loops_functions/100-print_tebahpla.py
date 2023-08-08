#!/usr/bin/python3

a, z, i = 'a', 'z', 1

while ord(z) >= ord(a):
    print('{}'.format(z) if i % 2 != 0 else '{}'.format(chr(ord(z) - 32)),
          end='')
    z = chr(ord(z) - 1)
    i += 1
