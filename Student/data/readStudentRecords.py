import csv
#data = list(csv.DictReader(open("StudentRecords_old.txt")))
#print (data)
#print("Records", len(data))


import csv
studentList=[]

class Students:
    def __init__(self, **kwargs):
        self.label = kwargs.get('label')
        self.sN = kwargs.get('fodselsNummer')
        self.fN = kwargs.get('firstName')
        self.lN = kwargs.get('lastName')
        self.age = kwargs.get('age')
        self.email = kwargs.get('email')
        self.pCourse = kwargs.get('programmingCourse')
        self.x = kwargs.get('X')

def DisplayNames(self ):
        print ("Students registered are:")
        for student in self.label:
            print (student["fN"],student["lN"])


if __name__ == '__main__':
    with open('StudentRecords_old.txt', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(row)
            studentList.append( Students(sN=row['fodselsNummer'], fN = row['firstName'], lN= row['lastName'], age=row['age'],pCourse=row['programmingCourse'], x= row['X']))

        print(studentList)
        for item in studentList:
            print (item.fN)
