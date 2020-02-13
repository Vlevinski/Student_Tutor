#!python3.7
###
#  The main project file:  StudentManagement.py
###

from Python.StudentRecordClass import StudentRecordsClass
import Python.EncodeDecodeClass
import csv

fieldNames = ["fodselsNummer",
              "firstName",
              "lastName",
              "age",
              "email",
              "programmingCourse"]
valid_course = ["python",
                "java",
                "php",
                "c++"]
# student records, encoded records, decoded records
my_list = []
my_elist = []
my_dlist = []

# get StudentRecordsFile  if exist
try:
    students = list(csv.DictReader(open('data/StudentRecords.txt')))
except FileNotFoundError:
    students = []

#    print("New records file created, ")
print("The file StudentRecordsFile, records: ", len(students))


#   ask to start o finish users data enter
def startEnterInfo():
    while True:
        answer = input("Would you like to enter a student’s information? Type Y for Yes or N for No:")
        answer = answer.upper()
        print (answer)
        if "N" in answer:
            return False
        elif "Y" in answer:
            return True
        print("\n Oops something is buggy")


# ask to enter fodselsNummer
def ask_fodselsNummer():
    while True:
        answer = input("Fodselsnummer :")
        ans = answer.isdigit()
        if ans is True:
            return answer
        print("\n Oops something is buggy")


# ask to enter first Name
def ask_firstName():
    while True:
        answer = input("First name :")
        ans = answer.isalpha()
        if ans is True:
            return answer.title()
        print("\n Oops something is buggy")


# ask to enter last Name
def ask_lastName():
    while True:
        answer = input("Last name :")
        ans = answer.isalpha()
        if ans is True:
            return answer.title()
        print("\n Oops something is buggy")


# ask to enter User age
def ask_age():
    while True:
        answer = input("Age :")
        ans = answer.isdigit()
        if ans is True:
            return answer
        print("\nOops something is buggy")


# ask to enter User email
def ask_email():
    while True:
        answer = input("E-mail :")
        if "@" in answer:
            return answer
        print("\n Oops something is buggy")


# ask to enter pCourse
def ask_programmingCourse():
    courses = ["python", "java", "php", "c++"]
    while True:
        answer = input("Programming course :")
        answer = answer.lower()
        if answer in courses:
            return answer
        print("\n Oops something is buggy")


# ask for propts to select function
def ask_Propmts():
    while True:
        print("\n1. Would you like to see a list of registered students?")
        print("2. Would you like to see a class list for specific subject")
        print("3. Would you like to see who your oldest student is?")
        print("4. Would you like to see who your youngest student is?")
        answer = input("Enter number for the selected task, or X to skip this:")
        if answer in ["1", "2", "3", "4", "X", "x"]:
            return answer
        print("\n Oops something is buggy")


# display all Students names
def DisplayAllStudents():
    print("\nStudents registered are:")
    for student in students:
        print("\t", student["firstName"], student["lastName"])


# display python subject users
def DisplaySubjectClassList(subjectname):
    subjRecords = [item for item in students if item["programmingCourse"] == subjectname]
    print("\nThe students registered for ", subjectname, end=" ")
    print(" are:")
    if len(subjRecords):
        for student in subjRecords:
            print("\t", student["firstName"], student["lastName"])
    else:
        print(" None")


# display eldest student
def DisplayOldest():
    ageRecords = [int(item["age"]) for item in students]
    max_v = 1
    for item in ageRecords:
        if max_v < item:
            max_v = item
    print("\nThe eldes student(s):", end=" ")
    [print(item["firstName"], item["lastName"], end=", ") for item in students if int(item["age"]) == max_v]
    print(" age", max_v)


# dispaly yanguest user
def DisplayYoungest():
    ageRecords = [int(item["age"]) for item in students]
    min_v = 100
    for item in ageRecords:
        if min_v > item:
            min_v = item
    print("\nThe youngest student(s):", end=" ")
    [print(item["firstName"], item["lastName"], end=", ") for item in students if int(item["age"]) == min_v]
    print(" age", min_v)


# wrute student recor file entered by admin
def writeStudentRecordsFile(fname, students):
    with open(fname, mode='w') as csv_file:
        fieldnames = ["fodselsNummer", "firstName", "lastName", "age", "email", "programmingCourse"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in students:
            writer.writerow(item)
        print("\n Records file saved")


# start dataentry dialog with User
dataentry = startEnterInfo()
while dataentry:
    iD = ask_fodselsNummer()
    fN = ask_firstName()
    lN = ask_lastName()
    age = ask_age()
    email = ask_email()
    pCourse = ask_programmingCourse()

    students.append({"fodselsNummer": iD, "firstName": fN, "lastName": lN, "age": age, "email": email,
                     "programmingCourse": pCourse})
    print("New record to StidentsRecordsFile.txt,records: ", len(students))
    dataentry = startEnterInfo()

# wrte student records file
if len(students):
    writeStudentRecordsFile('data/StudentRecords.txt', students)


# DidplayStudentnamesmethod
def display_names(stu, mylist):
    print("Sudent names :")
    for item in mylist[1:]:
        stu.DisplayNames(item)


# digitns encode method
def digits_encode(sin):
    return sin[::-1]


# ROT (+5) encode method
def encode(strin):
    return strin.lower()


# ROT (+5)  decode method
def decode(strin):
    return strin


# encode list creation
def encodeList(ilist, olist):
    for item in ilist:
        erow = dict()
        erow["fodselsNummer"] = digits_encode(item["fodselsNummer"])
        erow["firstName"] = encode(item["firstName"])
        erow["lastName"] = encode(item["lastName"])
        erow["age"] = digits_encode(item["age"])
        erow["email"] = encode(item["email"])
        erow["programmingCourse"] = encode(item["programmingCourse"])
        olist.append(erow)
    return olist


# decode list creation
def decodeList(ilist, olist):
    for item in ilist:
        erow = dict()
        erow["fodselsNummer"] = digits_encode(item["fodselsNummer"])
        erow["firstName"] = decode(item["firstName"])
        erow["firstName"] = erow["firstName"].capitalize()
        erow["lastName"] = decode(item["lastName"])
        erow["lastName"] = erow["lastName"].capitalize()
        erow["age"] = digits_encode(item["age"])
        erow["email"] = decode(item["email"])
        erow["programmingCourse"] = decode(item["programmingCourse"])
        olist.append(erow)
    return olist


# write student records file entered by admin
def writeRecordsFile(filename, recordsList):
    with open(filename, mode='w') as csv_file:
        fieldnames = ["fodselsNummer", "firstName", "lastName", "age", "email", "programmingCourse"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in recordsList:  # my_list, my_elist or my_dlist
            writer.writerow(item)


def askEncode():
    while True:
        answer = input("Do you want to create an Encrypted version of the file? Type Y for Yes or N for No:")
        answer = answer.upper()
        if "N" in answer:
            return False
        elif "Y" in answer:
            return True
        print("\n Oops something is buggy")


def askDecode():
    while True:
        answer = input("Do you want to create an Decripted version of the file? Type Y for Yes or N for No:")
        answer = answer.upper()
        if "N" in answer:
            print("The assessment is over. Have a nice day.")
            exit(0)
        elif "Y" in answer:
            return True
        print("\n Oops something is buggy")


def main():
    fentry = ask_Propmts()
    print(fentry)
    while fentry:
        if fentry is "1":
            DisplayAllStudents()
        elif fentry is "2":
            DisplaySubjectClassList('python')
        elif fentry is "3":
            DisplayOldest()
        elif fentry is "4":
            DisplayYoungest()
        elif fentry is "x" or fentry is "X":
            # en = EncodeDecodeClass
            encodef = askEncode()
            if encodef:
                encodeList(students, my_elist)
                writeStudentRecordsFile('data/EncodedStudentRecords.txt', my_elist)
            decodef = askDecode()
            if decodef:
                decodeList(my_elist, my_dlist)
                writeStudentRecordsFile('data/DecodedStudentRecords.txt', my_dlist)
        fentry = ask_Propmts()
        print(fentry)


if __name__ == '__main__':
    main()
