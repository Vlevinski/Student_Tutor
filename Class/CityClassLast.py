# https://stackoverflow.com/questions/47445586/how-to-read-the-contents-of-a-csv-file-into-a-class-with-each-csv-row-as-a-class


import csv


class City:
    def __init__(self, *kwargs):
        self.id, self.latitude, self.longitude, self.city, \
        self.label, self.year_1970, self.year_1975, self.year_1980, \
        self.year_1985, self.year_1990, self.year_1995, self.year_2000, \
        self.year_2005 = kwargs

    def __str__(self):
        return self.label


if __name__ == '__main__':
    with open('city.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            city = City(*row)
        print(city)
        print(city.id, city.latitude, city.longitude)
#
###
#
###
#   Tokyo
# 1 35.6832085 139.8089447
