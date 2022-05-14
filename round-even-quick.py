from decimal import *


def round_val(x, r):
    # set precision to 56 significant figures (whatever is required),
    # using the decimal module to round half even
    getcontext().prec = 56
    factor = Decimal(1) / 10 ** r
    num1 = Decimal(x).quantize(factor, rounding=ROUND_HALF_EVEN)
    return num1


# forever loop while run = y for testing purposes.
# calls the round_val function and passes in the parameters x and r.
run = "y"
while run == "y":
    x = Decimal(input('Decimal number for rounding: '))
    r = int(input('Number of decimal points: '))
    result = round_val(x, r)
    print(result)
    run = input("Do you want to continue? Type 'y' if you do: ")
