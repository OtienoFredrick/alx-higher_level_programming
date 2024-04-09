#!/usr/bin/python3
n = 'abcdefghijklmnopqrstuvwxyz'
for i in n:
    if i == 'e' or i == 'q':
        continue
    else:
        print("{}".format(i), end="")
