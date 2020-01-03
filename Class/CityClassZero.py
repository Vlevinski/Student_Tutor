import csv

#data = list(csv.DictReader(open("city.csv")))
#fieldnames = data[0]
#print(fieldnames)
##
# OrderedDict([('id', '1'), ('latitude', '35.6832085'), ('longitude', '139.8089447'), ('city', 'Tokyo'), ('label', 'Tokyo'), ('yr1970', '23.3'), ('yr1975', '26.61'), ('yr1980', '28.55'), ('yr1985', '30.3'), ('yr1990', '32.53'), ('yr1995', '33.59'), ('yr2000', '34.45'), ('yr2005', '35.62')])
# exit(999)
#
with open('city.csv', 'r') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

#    reader = csv.reader(f)
#    rows=[row for row in reader]
#    fieldnames = rows[0]

#    fields =rows[1:]
#    print ( fieldnames)
#    print(fields)
# ['id', 'latitude', 'longitude', 'city', 'label', 'yr1970', 'yr1975', 'yr1980', 'yr1985', 'yr1990', 'yr1995', 'yr2000', 'yr2005']
# [['1', '35.6832085', '139.8089447', 'Tokyo', 'Tokyo', '23.3', '26.61', '28.55', '30.3', '32.53', '33.59', '34.45', '35.62']]

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
#  sys.out
###

#[City(id='1', latitude='35.6832085', longitude='139.8089447', city='Tokyo', label='Tokyo', yr1970='23.3', yr1975='26.61', yr1980='28.55', yr1985='30.3', yr1990='32.53', yr1995='33.59', yr2000='34.45', yr2005='35.62')]
