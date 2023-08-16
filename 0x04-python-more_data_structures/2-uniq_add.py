#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    return sum(map(lambda x: x, my_set))
