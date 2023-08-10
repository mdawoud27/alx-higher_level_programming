#!/usr/bin/python3

import sys

def add_argvs():
    argvs = sys.argv
    sum_argvs = 0
    for i in range(1, len(argvs)):
        sum_argvs += int(argvs[i])

    print(sum_argvs)


if __name__ == '__main__':
    add_argvs()
