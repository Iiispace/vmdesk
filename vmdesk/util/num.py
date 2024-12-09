import decimal, re

from itertools import count, filterfalse
from bisect import bisect_right


DECIMAL_CONTEXT = decimal.Context()
DECIMAL_CONTEXT.prec = 20

def float_to_str(f):
    #|
    return format(DECIMAL_CONTEXT.create_decimal(repr(f)), 'f')
    #|


def r_unsign32(n):
    #|
    return n + (1 << 32) & 0b11111111111111111111111111111111
    #|

def r_sign32(n):
    #|
    if n <= 0b1111111111111111111111111111111:
        return n
    return n - (1 << 32)
    #|

#| List --------------------------------------------------------------------------------------------------

def r_smallest_miss(set1, smallest):
    #| Iterate the first number not in set
    #| {1, 2}, 1 ==> 3
    return next(filterfalse(set1.__contains__, count(smallest)))
    #|

def r_nearest_not_in_list(ints, n):
    if n not in ints: return n

    lower = n - 1
    upper = n + 1

    while True:
        if lower not in ints:
            return lower
        if upper not in ints:
            return upper
        lower -= 1
        upper += 1
    #|
def r_best_new_int_miss(ints, new_int, offset, xmin, xmax):
    if new_int <= xmin: new_int = xmin
    elif new_int >= xmax: new_int = xmax

    x = new_int
    for _ in ints:
        if x <= xmin: x = xmin
        elif x >= xmax: x = xmax

        if x in ints:
            x += offset
            continue

        return x

    return r_nearest_not_in_list(ints, x)
    #|

#|
#| String ------------------------------------------------------------------------------------------------

def split_upper(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s.replace(" ", ""))
    #|

#|
#| Color -------------------------------------------------------------------------------------------------
#|