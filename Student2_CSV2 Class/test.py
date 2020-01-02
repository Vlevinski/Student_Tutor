import csv
#https://stackoverflow.com/questions/47182821/python-creating-objects-from-csv-import-list
class Student():
    def __init__(self,*args):
        self.sN, self.fN, self.lN, self.age, self.email, self.pCourse, self.x = args

    def DisplayName(self):
        print (self.fN, self.lN)

def importList():
    with open('StudentRecords.txt','r') as f:
        reader = csv.reader(f)
        return [Student(*row) for row in reader]

#print (importList())

for item in importList()[1:]:
    item.DisplayName()
