import csv
#https://stackoverflow.com/questions/47182821/python-creating-objects-from-csv-import-list
#https://stackoverflow.com/questions/47445586/how-to-read-the-contents-of-a-csv-file-into-a-class-with-each-csv-row-as-a-class
class Student():
    def __init__(self,*args):
        self.label="Tokyo"
        self.sN, self.fN, self.lN, self.age, self.email, self.pCourse, self.x = args

    def __str__(self):
        return self.label

    def DisplayNames(self):
        print (self.fN,self.lN)
 #       return [self.fN, self.lN]

def importList():
    with open('StudentRecords.txt','r') as f:
        reader = csv.reader(f)
        return [Student(*row) for row in reader]

'''
# By creating a dictionary
persons = []
with open('StudentsRecoords.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        persons.append({'name': row[0], 'age': int(row[1]), 
                        'hobbies': row[2:]})

    for row in reader:
        persons.append({'name': row[0], 'age': int(row[1]),
                        'hobbies': row[2:]})
'''

#print (importList())

#for item in importList():
#    print( item.sN, item.fN, item.lN, item.age, item.email, item.pCourse, item.x)
#    print(item.DisplayName()[0], item.DisplayName()[1])

for item in importList()[1:]:
    item.DisplayNames()
#    print(item.__str__())
#    print (item.fN,item.lN)
