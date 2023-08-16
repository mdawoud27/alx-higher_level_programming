#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        flag = 1
        k = ''
        for key, value in a_dictionary.items():
            if flag:
                k = key
                flag = 0
            if a_dictionary[key] > a_dictionary[k]:
                a_dictionary[k] = a_dictionary[key]
                k = key
        return k
    return None
