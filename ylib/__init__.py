#!python3.7
#

import csv


def j_print(obj):
    import json
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def set_names(csv1="data/one.csv", csv2="data/two.csv"):
    # two csv filenames by default
    return csv1, csv2


def strip_clear(row):
    # strip strings in the list
    return [str.strip(item) for item in row]


def str_row(row):
    # join string with \n at the end
    return ",".join(row) + "\n"


def read_csv(name):
    # read file
    return list(csv.reader(open(name)))


def write_csv(j_list, filename):
    # write file as textual
    with open(filename, "w") as f:
        [f.write(str_row(row)) for row in j_list]


def csv_info(name):
    # count rows and  names of csv file
    dt = list(csv.reader(open(name)))
    rows = len(dt)
    names = len(dt[0])
    print("\nFile: ", name,"\nrows: ", rows,"\nnames:", names)
    return name, rows, names
