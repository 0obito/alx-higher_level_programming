#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while True:
        if i == x:
            print("")
            return count
        try:
            print("{:d}".format(my_list[i]), end="")
        except TypeError:
            i += 1
            continue
        except ValueError:
            i += 1
            continue
        i += 1
        count += 1
