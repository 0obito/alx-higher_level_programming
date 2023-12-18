#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if (count >= x):
                raise Exception("Reached given limit.")
            print(f"{i}", end="")
        except Exception:
            print("")
            return count
        except IndexError:
            print("")
            return count
        count += 1
    print("")
    return count
