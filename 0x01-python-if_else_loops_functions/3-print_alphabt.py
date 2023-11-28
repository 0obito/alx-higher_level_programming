#!/usr/bin/python3
alpha = ord('a')
while alpha <= ord('z'):
    if alpha == ord('e') or alpha == ord('q'):
        alpha = alpha+1
        continue
    print("{}".format(chr(alpha)), end='')
    alpha = alpha+1
