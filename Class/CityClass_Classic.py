import csv


class City:

    def __init__(self, id,latitude,longitude,city,label):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.label = label

    def id_item(self):
        print(self.id)

city_list = []

with open('city.csv', newline='') as csv_file:
    id = csv.reader(csv_file)
    next(id, None)  # skip the header
    # Unpack the row directly in the head of the for loop.
    for row in id:
        # get values
        id,latitude,longitude,city,label = row[0],row[1],row[2],row[3],row[4]
        print (id,latitude,longitude,city,label )

        # Now create the City instance and append it to the list.
        city_list.append(City(id,latitude,longitude,city,label))
        city_item = City(id,latitude,longitude,city,label)

print(city_list[0].id, city_list[0].city)
print( city_item.id,city_item.city)

