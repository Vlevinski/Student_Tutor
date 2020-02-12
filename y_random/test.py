#!python3.7
#

from y_random import *


def get_cols(n):
    cols = []
    while True:
        if n > 9:
            n = 9
        itm = r_range(0, 9)
        if itm not in cols:
            cols.append(itm)
            if len(cols) == n:
                break
    return cols


r_init()
print("Init: done")

table_size = [5, 9]
column = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
cls = get_cols(5)
cls.sort()

print(cls)
print([column[i] for i in cls])
