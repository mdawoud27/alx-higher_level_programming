#!/usr/bin/python3

def remove_char_at(str, n):
    temp = ""
    cnt = 0
    for i in str:
        if cnt == n:
            cnt += 1
            continue
        temp += i
        cnt += 1
    return temp
