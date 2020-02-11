#!python3.7
#

import csv

#srip rows of csv file
def y_lib_help():
    return ''' Library modules: 
    - print json                        j_print(obj)                                        
    - set names to clear csv            set_names(csv1="data/one.csv", csv2="data/two.csv") 
    - strip list of items               strip_clear(row)                                   
    - join items of the list            str_row(row)                                        
    - load csv file as list of rows     read_csv(name)                                      
    - write list of rows to file        write_csv(j_list, filename)                         
    - get general info of csv file      def csv_info(name)                                  
    '''


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
    print("\nFile: ", name, "\nrows: ", rows, "\nnames:", names)
    return name, rows, names
