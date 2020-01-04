####
#  The main project file:  StudentManagement.py
####

from StudentRecordClass import StudentRecordsClass
import csv

studentsList = []
studentsData = []


#   ask to start o finish users data enter
def startEnterInfo():
    answer = None
    while answer != "Y" or answer != "N":
        answer = input("Would you like to enter a student’s information? Type Y for Yes or N for No:")
        answer = answer.upper()
        if answer == "N":
            return False
        elif answer == "Y":
            return True
        print("\n Oops something is buggy")


# ask to enter fodselsNummer
def ask_fodselsNummer():
    answer = None
    while answer != "Y":
        answer = input("Fodselsnummer :")
        ans = answer.isdigit()
        if ans == True:
            return answer
        print("\n Oops something is buggy")


# ask to enter first Name
def ask_firstName():
    answer = None
    while answer != "123":
        answer = input("First name :")
        ans = answer.isalpha()
        if ans == True:
            return answer.title()
        print("\n Oops something is buggy")


# ask to enter last Name
def ask_lastName():
    answer = None
    while answer != "123":
        answer = input("Last name :")
        ans = answer.isalpha()
        if ans == True:
            return answer.title()
        print("\n Oops something is buggy")


# ask to enter User age
def ask_age():
    answer = None
    while answer != "Y":
        answer = input("Age :")
        ans = answer.isdigit()
        if ans == True:
            return answer
        print("\nOops something is buggy")


# ask to enter User email
def ask_email():
    answer = None
    while answer != "Y":
        answer = input("E-mail :")
        ans = "@" in answer  # and "yahoo.com" in answer
        if ans == True:
            return answer
        print("\n Oops something is buggy")


# ask to enter pCourse
def ask_programmingCourse():
    valid_course = ["python", "java", "php", "c++"]
    answer = None
    while answer != "123":
        answer = input("Programming course :")
        answer = answer.lower()
        # or "java" in answer or "php" in answer
        if answer in valid_course:
            return answer
        print("\n Oops something is buggy")


# ask for propts to select function
def ask_Propmts():
    answer = None
    while answer != "None":
        print("\n1. Would you like to see a list of registered students?")
        print("2. Would you like to see a class list for specific subject")
        print("3. Would you like to see who your oldest student is?")
        print("4. Would you like to see who your youngest student is?")
        answer = input("Enter number for the selected task, or X to skip this:")
        #        answer= answer.upper()
        if answer in ["1", "2", "3", "4", "X", "x"]:
            return answer
        print("\n Oops something is buggy")


# display all Students names
def DisplayAllStudents():
    print("\nStudents registered are:")
    for student in dtemp:
        print(student["firstName"], student["lastName"])


# display python subject users
def DisplaySubjectClassList(subjectname):
    subjRecords = [item for item in dtemp if item["programmingCourse"] == subjectname]
    print("\nThe students registered for ", subjectname, end=" ")
    print(" are:")
    if len(subjRecords):
        for student in subjRecords:
            print(student["firstName"], student["lastName"])
    else:
        print(" None")


# display eldest student
def DisplayOldest():
    ageRecords = [int(item["age"]) for item in dtemp]
    max = 1
    for item in ageRecords:
        if max < item:
            max = item
    print("\nThe eldes student(s):", end=" ")
    names = ""
    [print(item["firstName"], item["lastName"], end=", ") for item in dtemp if int(item["age"]) == max]
    print(" age", max)


# dispaly yanguest user
def DisplayYoungest():
    ageRecords = [int(item["age"]) for item in dtemp]
    min = 100
    for item in ageRecords:
        if min > item:
            min = item
    print("\nThe youngest student(s):", end=" ")
    names = ""
    [print(item["firstName"], item["lastName"], end=", ") for item in dtemp if int(item["age"]) == min]
    print(" age", min)


# wrute student recor file entered by admin
def writeStudentRecordsFile():
    with open('StudentRecords.txt', mode='w') as csv_file:
        fieldnames = ["fodselsNummer", "firstName", "lastName", "age", "email", "programmingCourse"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in dtemp:  # studentRecords:
            writer.writerow(item)
        print("\n Records file saved")


# create Class records
def createClass():
    with open('StudentRecords.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            studentsList.append(
                StudentRecordsClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  # parameters
            studentsData.append(
                {"sN": row[0], "fN": row[1], "lN": row[2], "age": row[3], "email": row[4], "pCourse": row[5],
                 "x": row[6]})


dtemp = []
fieldNames = ["fodselsNummer", "firstName", "lastName", "age", "email", "programmingCourse"]
valid_course = ["python", "java", "php", "c++"]

# load StudentRecordsFile if exist
try:
    dtemp = list(csv.DictReader(open('StudentRecords.txt')))
except:
    dtemp = []
print("The file StudentRecordsFile, records: ", len(dtemp))

# start dataentry dialog with User
dataentry = startEnterInfo()
print(dataentry)
while dataentry:
    iD = ask_fodselsNummer()
    print(iD)
    fN = ask_firstName()
    print(fN)
    lN = ask_lastName()
    print(lN)
    age = ask_age()
    print(age)
    email = ask_email()
    print(email)
    pCourse = ask_programmingCourse()
    print(pCourse)
    dtemp.append({"fodselsNummer": iD, "firstName": fN, "lastName": lN, "age": age, "email": email,
                  "programmingCourse": pCourse})
    dataentry = startEnterInfo()
    print(dataentry)

print(dtemp)

# wrte student records file
if len(dtemp):
    writeStudentRecordsFile()


def main():
    # promps for methods selction
    fentry = ask_Propmts()
    print(fentry)
    while fentry:
        if fentry == "1":
            DisplayAllStudents()
        elif fentry == "2":
            DisplaySubjectClassList('python')
        elif fentry == "3":
            DisplayOldest()
        elif fentry == "4":
            DisplayYoungest()
        elif fentry == "x" or fentry == "X":
            print("\n X is not admitted")
        fentry = ask_Propmts()
        print(fentry)


if __name__ == '__main__':
    main()
