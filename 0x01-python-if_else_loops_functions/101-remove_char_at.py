#!/usr/bin/python3

def remove_char_at(str, n):
    edited = ""
    i = 0
    for c in str:
        if i != n:
            edited = edited + c
        i = i + 1
    return edited
