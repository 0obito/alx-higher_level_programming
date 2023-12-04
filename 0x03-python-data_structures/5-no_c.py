#!/usr/bin/python3

def no_c(my_string):
    output = ""
    for character in my_string:
        if character.lower() != "c":
            output = output + character
    return output
