#!/usr/bin/python3
for number in range(0, 99):
    print("{:02d}".format(number, hex(number)), end=' ')
print("{}".format(number + 1))
