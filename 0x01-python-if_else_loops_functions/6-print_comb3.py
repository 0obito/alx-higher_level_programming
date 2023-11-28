#!/usr/bin/python3
for firstDigit in range(10):
    for secondDigit in range(firstDigit + 1, 10):
        if firstDigit == 8 and secondDigit == 9:
            print("{:d}{:d}".format(firstDigit, secondDigit))
            continue
        print("{:d}{:d}".format(firstDigit, secondDigit), end=', ')
