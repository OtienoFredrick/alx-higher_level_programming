#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 1:
    print("{} is negative" .format(number))
elif number > 1:
    print("{} is postive". format(number))
