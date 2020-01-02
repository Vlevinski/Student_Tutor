import csv

# [City(id='1', latitude='35.6832085', longitude='139.8089447', city='Tokyo', label='Tokyo', yr1970='23.3', yr1975='26.61', yr1980='28.55', yr1985='30.3', yr1990='32.53', yr1995='33.59', yr2000='34.45', yr2005='35.62')]

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

filepath = "cities.csv"

if __name__ == '__main__':
    with open(filepath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(row)
            city = City(**row)
            print(city)
            print(city.__str__())
