#!/usr/bin/python3
"""
Module: 5-text_indentation
Prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.
"""
def text_indentation(text):
    """
    Function: text_indentation(text).
    Parameters:
      - text: text to be operated on.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False

    for c in range(len(text)):
        if skip_space:
            if text[c] == ' ':
                continue
            else:
                skip_space = False

        if text[c] in ('.', '?', ':'):
            print("\n")
            skip_space = True
        else:
            print(f"{text[c]}", end="")
