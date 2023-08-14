#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)
    if len(sentence) == 0:
        return str_len, None
    else:
        return str_len, sentence[0]
