#!python3.7
#  Reading csv file into class instances

import csv


class Sheet:

    # content of csv into class, row as a instance
    def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row))


class SheetId:

    # content of csv into class, row as a instance, with id
    def __init__(self, row, header, the_id):
        self.__dict__ = dict(zip(header, row))
        self.the_id = the_id

    def __repr__(self):
        return self.the_id


with open('data/simple.csv', 'r') as f:
    reader = csv.DictReader(f)

    # read field names
    fieldnames = reader.fieldnames


    class Rows:

        # dict content of csv into class, row as a instance
        def __init__(self, **fields):
            self.__dict__.update(**fields)

        def __repr__(self):  # Added to make printing instances show their contents.
            fields = ', '.join(('{}={!r}'.format(fieldname, getattr(self, fieldname))
                                for fieldname in fieldnames))
            return '{}({})'.format(self.__class__.__name__, fields)


    # read rows of **fields
    rows = [Rows(**row) for row in reader]

# example of usage
'''
data = list(csv.reader(open('data/simple.csv')))
instances = [Sheet(i, data[0]) for i in data[1:]]
print(instances)

data = list(csv.reader(open('data/simple.csv')))
instances_id = [SheetId(a, data[0], "row_{}".format(i + 1)) for i, a in enumerate(data[1:])]
print(instances_id)

print(rows)
'''
