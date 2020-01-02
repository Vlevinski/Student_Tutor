import csv

#with open('cities.csv', 'rb') as f:
with open('cities.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    class City:
        def __init__(self, **fields):
            self.__dict__.update(**fields)

        def __repr__(self):  # Added to make printing instances show their contents.
            fields = ', '.join(('{}={!r}'.format(fieldname, getattr(self, fieldname))
                                   for fieldname in fieldnames))
            return('{}({})'.format(self.__class__.__name__, fields))

    cities = [City(**row) for row in reader]

print(cities)
print (cities.__repr__())
