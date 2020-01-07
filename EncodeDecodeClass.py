import csv

###
#    params for writeRecordsFile()
###
#
#                   field names of StudentRecordsFile.txt
cnames = ["fodselsNummer", "firstName", "lastName", "age", "email", "programmingCourse"]
stRedFileName = 'StudentRecords.txt'                    #filename
stEncRecFileName = 'EncodedStudentRecords.txt'          #filename
stDecRecFileName = 'DecodedStudentRecords.txt'          #filename
my_list = []        #list of dicts with records
my_elist = []       #list of dict  with encoded records
my_dlist = []       #lidt of dict with decoded records


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


