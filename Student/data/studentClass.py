import csv

my_list = []

class Student():
    def __init__(self, sN, firstName ):
        self.sN = sN
        self.fN = firstName

def main():

    with open('students.txt','r') as f:
        reader = csv.reader(f)
        for row in reader:
            my_list.append(Student(row[0],row[1]))   # parameters
            print (row[0],row[1])
    for item in my_list:
        print(item.sN,item.fN)
    iD = [id.sN for id in my_list[1:]]
    print(iD)
    names =[id.fN for id in my_list[1:]]
    print (names)
if __name__ == '__main__':
    main()
