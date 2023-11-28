#!/usr/bin/python3

def uppercase(str):

    i = 0
    while i < len(str):

        alpha = str[i]
        if ord(str[i]) <= ord('z') and ord(str[i]) >= ord('a'):
            alpha = chr(ord(str[i]) - 32)

        if i == len(str) - 1:
            print("{}".format(alpha))
        else:
            print("{}".format(alpha), end='')

        i = i + 1
