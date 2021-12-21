#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number >= 0:
    helper = number % 10
else:
    helper = -number % 10 * -1
print("Last digit of {:d} and is {:d}".format(number, helper), end="")
if helper > 5:
    print("and is greater than 5".format(helper, number))
elif helper == 0:
    print("and is 0".format(number))
elif helper < 6 and helper != 0:
    print("and is less than 6 and not 0".format(helper, number))
else:
    print("and is 0")
