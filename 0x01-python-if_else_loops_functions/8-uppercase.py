#!/usr/bin/python3

def uppercase(str):

    i = 0
    while i < len(str):
        if ord(str[i]) <= ord('z') and ord(str[i]) >= ord('a'):
            upper = chr(ord(str[i]) - 32)
            if i == len(str) - 1:
                print("{}".format(upper))
            else:
                print("{}".format(upper), end='')

        else:
            if i == len(str) - 1:
                print("{}".format(str[i]))
            else:
                print("{}".format(str[i]), end='')
        i = i + 1
