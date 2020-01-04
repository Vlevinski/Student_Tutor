import csv
class City:
   def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row))

data = list(csv.reader(open('city.csv')))
instances = [City(i, data[0]) for i in data[1:]]
print(instances[0].__dict__)

###
#   sys.out: --->
##
#{'id': '1', 'latitude': '35.6832085', 'longitude': '139.8089447', 'city': 'Tokyo', 'label': 'Tokyo', 'yr1970': '23.3', 'yr1975': '26.61', 'yr1980': '28.55', 'yr1985': '30.3', 'yr1990': '32.53', 'yr1995': '33.59', 'yr2000': '34.45', 'yr2005': '35.62'}

#===
#test
#for item in data:
#    print(item)
# Out:
#['id', 'latitude', 'longitude', 'city', 'label', 'yr1970', 'yr1975', 'yr1980', 'yr1985', 'yr1990', 'yr1995', 'yr2000', 'yr2005']
#['1', '35.6832085', '139.8089447', 'Tokyo', 'Tokyo', '23.3', '26.61', '28.55', '30.3', '32.53', '33.59', '34.45', '35.62']
