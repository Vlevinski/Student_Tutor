import csv

#  file city.csv as 'r" and not 'rb
with open('city.csv', 'r') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    class City:
        def __init__(self, **fields):
            self.__dict__.update(**fields)

        def __repr__(self):  # Added to make printing instances show their contents.
            fields = ', '.join(('{}={!r}'.format(fieldname, getattr(self, fieldname))
                                   for fieldname in fieldnames))
            return('{}({})'.format(self.__class__.__name__, fields))

    Cities = [City(**row) for row in reader]

print(Cities)

###
#
###
#
# [City(id='1', latitude='35.6832085', longitude='139.8089447', city='Tokyo', label='Tokyo', yr1970='23.3', yr1975='26.61', yr1980='28.55', yr1985='30.3', yr1990='32.53', yr1995='33.59', yr2000='34.45', yr2005='35.62')]
