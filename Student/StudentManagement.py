import string
from Student.StudentRecordClass import StudentRecordClass
import csv

               # dictionary with key names
studentData = {
                "fodselsNummer":"",
                "firstName" : "",
                "lastName" : "",
                "age": "",
                "email" : "",
                "programmingCourse" : ""
            }

               #the list with dictionary keys names

studentNames = ["fodselsNummer","firstName","lastName","age","email","programmingCourse"]
dictNames = ["sN","fN","lN","age","email","pCourse","x"]

studentRecords = [{'sN': '1', 'fN': 'John', 'lN': 'Smith', 'age': '15', 'email': 'johnsmith@yahoo.com', 'pCourse': 'python', 'x': 'False'},
                  {'sN': '2', 'fN': 'Jane', 'lN': 'Doe', 'age': '37', 'email': 'janeDoe@yahoo.com', 'pCourse': 'java', 'x': 'False'},
                  {'sN': '3', 'fN': 'Peter', 'lN': 'Pan', 'age': '67', 'email': 'peterpan@yahoo.com', 'pCourse': 'php', 'x': 'False'},
                  {'sN': '4', 'fN': 'Lizzy', 'lN': 'Fizz', 'age': '22', 'email': 'lizzyfizz@yahoo.com', 'pCourse': 'python', 'x': 'False'},
                  {'sN': '5', 'fN': 'Catherine', 'lN': 'Tabby', 'age': '33', 'email': 'cateherinetabby@yahoo.com', 'pCourse': 'python', 'x': 'False'}]

studentsList = []
studentsData =[]
dtemp =[]


#   ask to start o finish users data enter
def startEnterInfo():
    answer = None
    while answer != "Y" or answer!= "N":
        answer = input ("Would you like to enter a student’s information? Type Y for Yes or N for No:")
        answer= answer.upper()
        if answer =="N":
            return False
        elif answer == "Y":
            return  True
        print ( "\n Oops something is buggy")

# ask to enter fodselsNummer
def ask_fodselsNummer():
    answer = None
    while answer != "Y" :
        answer = input ("Fodselsnummer :")
        ans= answer.isdigit()
        if ans == True:
            return answer
        print ( "\n Oops something is buggy")

# ask to enter first Name
def ask_firstName():
    answer = None
    while answer != "123" :
        answer = input ("First name :")
        ans= answer.isalpha()
        if ans == True:
            return answer.title()
        print ( "\n Oops something is buggy")

# ask to enter last Name
def ask_lastName():
    answer = None
    while answer != "123" :
        answer = input ("Last name :")
        ans= answer.isalpha()
        if ans == True:
            return answer.title()
        print ( "\n Oops something is buggy")

# ask to enter User age
def ask_age():
    answer = None
    while answer != "Y" :
        answer = input ("Age :")
        ans= answer.isdigit()
        if ans == True:
            return answer
        print ( "\nOops something is buggy")

# ask to enter User email
def ask_email():
    answer = None
    while answer != "Y" :
        answer = input ("E-mail :")
        ans= "@" in answer   #and "yahoo.com" in answer
        if ans == True:
            return answer
        print ( "\n Oops something is buggy")

#ask to enter pCourse
def ask_programmingCourse():
    answer = None
    while answer != "123" :
        answer = input ("Programming course :")
        answer = answer.lower()
        ans = "python" in answer                # or "java" in answer or "php" in answer
        if ans == True:
            return answer
        print ( "\n Oops something is buggy")

# ask for propts to select function
def ask_Propmts():
    answer = None
    while answer != "None" :
        print ("\n 1. Would you like to see a list of registered students?")
        print ("2. Would you like to see a class list for specific subject")
        print ("3. Would you like to see who your oldest student is?")
        print ("4. Would you like to see who your youngest student is?")
        answer = input ("Enter number for the selected task, or X to skip this:")
#        answer= answer.upper()
        if answer in ["1", "2", "3", "4", "X" , "x"]:
            return answer
        print ( "\n Oops something is buggy")

# display all Students names
def DisplayAllStudents():
    print ("\nStudents registered are:")
    for student in studentsData[1:]:
        print (student["fN"],student["lN"])
#    print(studentsData[1:])

# display python subject users
def DisplaySubjectClassList(subjectname):
    subjRecords = [item for item in studentsData if item["pCourse"] ==subjectname]
    print ("\nThe students registered for ", subjectname, end=" ")
    print (" are:")
    if len(subjRecords):
        for student in subjRecords:
            print (student["fN"],student["lN"])
    else:
        print (" None")

# display oldest student
def DisplayOldest():
    ageRecords = [int(item["age"]) for item in studentsData[1:] ]
    max=1
    for item in ageRecords:
        if  max < item:
            max = item
    print("\nThe agest student:",max)
#    print (ageRecords)

#dispaly yanguest user
def DisplayYoungest():
    ageRecords = [int(item["age"]) for item in studentsData[1:] ]
    min= 100
    for item in ageRecords:
        if  min > item:
            min = item

    print("\nThe youngest student: is", min)
#    print (ageRecords)

#wrute student recor file entered by admin
def writeStudentRecordsFile():
    import csv

    with open('StudentRecords.txt', mode='w') as csv_file:
        fieldnames = dictNames #studentNames
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in dtemp: #studentRecords:
            writer.writerow(item)
        print ("\n Records file saved")

# create Class records
def createClass():
    with open('StudentRecords.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            studentsList.append(StudentRecordClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))   # parameters
            studentsData.append({"sN": row[0],"fN": row[1], "lN":row[2],"age":row[3],"email":row[4],"pCourse":row[5],"x":row[6]})

# start dataentry dialog with User
dataentry  = startEnterInfo(); print (dataentry)
while dataentry:
    iD = ask_fodselsNummer(); print(iD)
    fN= ask_firstName(); print(fN)
    lN = ask_lastName(); print(lN)
    age = ask_age(); print (age)
    email = ask_email(); print(email)
    pCourse =  ask_programmingCourse(); print(pCourse)
    dtemp.append({"sN":iD, "fN":fN, "lN":lN, "age": age, "email":email, "pCourse": pCourse, 'x':False })
    dataentry  = startEnterInfo(); print (dataentry)
print (dtemp)
next()
#wrte student records file
if len(dtemp):
    writeStudentRecordsFile()
def main():

    createClass()
    # promps for methods selction
    fentry = ask_Propmts(); print (fentry)
    while fentry:
        if fentry == "1" :
            DisplayAllStudents()
        elif fentry == "2" :
            DisplaySubjectClassList('python')
        elif fentry == "3" :
            DisplayOldest()
        elif fentry == "4":
            DisplayYoungest()
        elif fentry == "x" or fentry == "X":
            print ("\n Coding is not admitted")
        fentry = ask_Propmts(); print (fentry)

if __name__ == '__main__':
    main()

