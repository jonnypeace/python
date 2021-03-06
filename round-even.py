#!/usr/bin/python3

import re
import decimal
from decimal import *


def round_val(x, r):
    # finding index position of decimal point
    point = str(x).index(".")

    # finding length of decimal number as a string
    length = len(str(x))

    # left of the decimal
    left_d = str(x)[:point]

    # right of the decimal
    right_d = str(x)[point + 1:]

    # concatenate left and right of the decimal (avoid floating math problems)
    l_and_r = (left_d + right_d)

    # looking for the last to characters for conditional statements.
    last_two = str(l_and_r)[-2:]

    # result of modulus into 5 needs to be zero for rounding even to occur.
    mod1 = float(l_and_r) % 5

    # checking conditions are met for rounding even
    if re.findall("^[02468]?5$", last_two) and mod1 == 0.0:
        ans = round((float(l_and_r) - 5) / 10 ** (length - (point + 1)), r)
        # this syntax works along the lines of "{:.2f}".format(val, decimal_point). .2f would be 2 decimal points
        # i.e. "{:.decimal_pointf}".format(val, decimal_point)
        # for some more info https://mkaz.blog/code/python-string-format-cookbook/
        ans = "{:.{}f}".format(ans, r)
        # print("Answer is (1st if): " + ans)
        return ans
    elif re.findall("^[13579]5$", last_two) and mod1 == 0.0:
        ans = (float(l_and_r) + 5) / 10 ** (length - (point + 1))
        ans = "{:.{}f}".format(ans, r)
        # print("Answer is (2nd if): " + ans)
        return ans
    else:
        ans = "{:.{}f}".format(x, r)
        # print("Answer is (3rd if): " + ans)
        return ans


# forever loop while run = y
# calls the round_val function and passes in the parameters x and r.
# while loop for testing purposes.
run = "y"
while run == "y":
    x = Decimal(input('Decimal number for rounding: '))
    r = int(input('Number of decimal points: '))
    calc = round_val(x, r)
    print("Answer is: " + str(calc))
    # run = input("Do you want to continue? Type 'y' if you do: ")
    run = "y"
