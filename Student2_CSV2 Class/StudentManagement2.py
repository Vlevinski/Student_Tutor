

import csv

My_list =[]
My_data = []
class Student:
    def __init__(self, fodselsNummer,firstName, lastName, age, email, pCourse, x):
        self.sN = fodselsNummer
        self.fN = firstName
        self.lN = lastName
        self.age = age
        self.email = email
        self.pCourse = pCourse
        self.x = x

with open('StudentRecords.txt', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)
        student = Student(row[0],row[1],row[2],row[3], row[4], row[5],row[6])
        My_list.append(student)

print(My_list)

item = My_list[0]
print( item.sN, item.fN, item.lN, item.age, item.email, item.pCourse, item.x)       #sN fN lN age email pCourse x
for item in My_list[1:]:
    print( item.sN, item.fN, item.lN, item.age, item.email, item.pCourse, item.x)


