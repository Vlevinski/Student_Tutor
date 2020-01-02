import csv
from collections import namedtuple

City = namedtuple('City',
                  'lat lon cityName label '
                  'yr1970 yr1975 yr1980 yr1985 yr1990 yr1995 yr2000 yr2005 yr2010')

with open('cities.csv') as f:
    cities = [City(*row[1:]) for row in csv.reader(f)
              if row[0] != 'label']
