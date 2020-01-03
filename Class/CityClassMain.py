# https://stackoverflow.com/questions/47445586/how-to-read-the-contents-of-a-csv-file-into-a-class-with-each-csv-row-as-a-class


-1

import csv


class City:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.city = kwargs.get('city')
        self.label = kwargs.get('label')
        self.year_1970 = kwargs.get('yr1970')
        self.year_1975 = kwargs.get('yr1975')
        self.year_1980 = kwargs.get('yr1980')
        self.year_1985 = kwargs.get('yr1985')
        self.year_1990 = kwargs.get('yr1990')
        self.year_1995 = kwargs.get('yr1995')
        self.year_2000 = kwargs.get('yr2000')
        self.year_2005 = kwargs.get('yr2005')

    def __str__(self):
        return self.label


if __name__ == '__main__':
    with open('city.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            city = City(**row)
            print(city)
            print(city.id, city.latitude, city.longitude)

#Tokyo
#1 35.6832085 139.8089447
