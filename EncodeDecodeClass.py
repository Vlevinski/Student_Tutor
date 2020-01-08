import csv

###
#    params for writeRecordsFile()
###

my_list = []


class EncodeDecodeClass:

    # class conctructor
    def __init__(self, *args):
        self.fodselsNummer, self.firstName, self.lastName, self.age, self.email, self.programmingCourse = args

    #   load file from StudentRecords.txt file
    def getFile(self):
        with open('StudentRecords.txt', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                my_list.append(dict(row))

    def DisplayNames(self, item):
        print("\t", item[self.firstName], item[self.lastName])

    def EncodeStudentList(self):
        pass

    def DecodeStudentList(self):
        pass

print("EncodeDecodeClass is available")


