#!/usr/bin/python3

import re

def round_val(x, r):
    # looking for the last to characters for conditional statements.
    z = str(int(x * (10 ** (r + 1))))
    q = z[-2:]

    # finding index position of decimal point
    point = str(x).index(".")

    # finding length of decimal number as a string
    length = len(str(x))

    # multiplying x into an integer value, since modulus doesn't work with floating numbers very well.
    mod1 = x * (10 ** (length - (point + 1)))

    # result of modulus into 5 needs to be zero for rounding even to occur.
    mod2 = mod1 % 5

    # checking conditions are met for rounding even
    if re.findall("^[02468]?5$", q) and mod2 == 0.0:
        ans = (mod1 - 5) / 10 ** (length - (point + 1))
        # this syntax works along the lines of "{:.2f}".format(val, decimal_point). .2f would be 2 decimal points
        # i.e. "{:.decimal_pointf}".format(val, decimal_point)
        # for some more info https://mkaz.blog/code/python-string-format-cookbook/
        ans = "{:.{}f}".format(ans, r)
        print("Answer is: " + ans)
        return
    elif re.findall("^[13579]5$", q) and mod2 == 0.0:
        ans = (mod1 + 5) / 10 ** (length - (point + 1))
        ans = "{:.{}f}".format(ans, r)
        print("Answer is: " + ans)
        return
    else:
        ans = "{:.{}f}".format(x, r)
        print("Answer is: " + ans)
        return


# forever loop while run = y
# calls the round_val function and passes in the parameters x and r.
run = "y"
while run == "y":
    x = float(input('Decimal number for rounding: '))
    r = int(input('Number of decimal points: '))
    round_val(x, r)
    run = input("Do you want to continue? Type 'y' if you do: ")
