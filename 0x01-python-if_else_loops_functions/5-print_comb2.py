#!/usr/bin/python3
for i in range(0, 100):
    print('{:d}'.format(i) if i > 10 else '0{:d}'.format(i), end='')
    print('\n' if i == 99 else ', ', end='')
