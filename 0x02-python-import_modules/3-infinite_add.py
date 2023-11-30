#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num = 0
    i = 1
    while len(argv) > i:
        num += int(argv[i])
        i += 1
    print("{}".format(num))
