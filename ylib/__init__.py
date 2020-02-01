#!python3.7
#

import csv


def j_print(obj):
    import json
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_names():
    # two filenames by default
    one = "data/one.csv"
    two = "data/two.csv"
    return one, two


def yclear(row):
    # strip a string row
    return [str.strip(item) for item in row]


def str_row(row):
    # join string with \n at end
    return ",".join(row) + "\n"


def read_csv(name):
    # read file
    return list(csv.reader(open(name)))


def write_csv(j_list, filename):
    # write file as textual
    with open(filename, "w") as f:
        [f.write(str_row(row)) for row in j_list]


def csv_info(name):
    # coount rows and  names of csv file
    dt = list(csv.reader(open(name)))
    rows = len(dt)
    names = len(dt[0])
    print("File: ", name)
    print("rows: ", rows)
    print("names:", names)
    return name, rows, names
