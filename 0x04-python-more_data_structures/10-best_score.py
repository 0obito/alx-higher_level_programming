#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        num = 0
        for i, v in a_dictionary.items():
            if v > num:
                num = v
                name = i
        return name
    else:
        return None
