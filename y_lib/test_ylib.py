#!python3.7
#
import os
from y_lib import csv_info, y_lib_help

print (os.listdir("y_lib/data"))
csv_info("y_lib/data/office.csv")
print( y_lib_help())
