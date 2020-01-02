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
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)

        # create instances
        student = Student(row['sN'],row['fN'],row['lN'], row['age'], row['email'], row['pCourse'],row ['x'])
        My_data.append(student)  # create list of dicts
        My_list.append(dict(row)) # create list of elemts of class instances

print(My_list)
print(My_data)

#OrderedDict([('sN', '1234'), ('fN', 'Nick'), ('lN', 'Parson'), ('age', '55'), ('email', 'n@email.com'), ('pCourse', 'python'), ('x', 'False')])
#OrderedDict([('sN', '3232'), ('fN', 'Jannete'), ('lN', 'Dion'), ('age', '24'), ('email', 'j@email.com'), ('pCourse', 'python'), ('x', 'False')])
#OrderedDict([('sN', '5432'), ('fN', 'Celine'), ('lN', 'Carpenter'), ('age', '27'), ('email', 'seline@yahoo.com'), ('pCourse', 'python'), ('x', 'False')])
#[{'sN': '1234', 'fN': 'Nick', 'lN': 'Parson', 'age': '55', 'email': 'n@email.com', 'pCourse': 'python', 'x': 'False'}, {'sN': '3232', 'fN': 'Jannete', 'lN': 'Dion', 'age': '24', 'email': 'j@email.com', 'pCourse': 'python', 'x': 'False'}, {'sN': '5432', 'fN': 'Celine', 'lN': 'Carpenter', 'age': '27', 'email': 'seline@yahoo.com', 'pCourse': 'python', 'x': 'False'}]
#[<__main__.Student object at 0x7f355312c7d0>, <__main__.Student object at 0x7f355312c9d0>, <__main__.Student object at 0x7f355312cb90>]

