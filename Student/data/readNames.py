import csv


class Students:
    def __init__(self, **kwargs):
        self.sN = kwargs.get('fodselsNummer')
        self.fN = kwargs.get('firstName')
        self.lN = kwargs.get('lastName')
        self.age = kwargs.get('age')
        self.email = kwargs.get('email')
        self.pCourse = kwargs.get('programmingCourse')
        self.x = kwargs.get('X')

def studentsList(self ):
    def importList():
        with open('StudentRecords_old.txt', 'r') as f:
            reader = csv.reader(f)
            return [Students(name) for name in reader]



        print ("Students registered are:")
        for student in self.label:
            print (student["fN"],student["lN"])
