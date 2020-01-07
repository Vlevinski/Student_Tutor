####
#  The main project file:  StudentManagement.py
####

from StudentRecordClass import StudentRecordsClass
import EncodeDecodeClass
import csv

fieldNames = ["fodselsNummer", "firstName", "lastName", "age", "email", "programmingCourse"]
valid_course = ["python", "java", "php", "c++"]
my_list = []  # list of dicts with records
my_elist = []  # list of dict  with encoded records
my_dlist = []  # lidt of dict with decoded records

# get old students as StudentRecordsFile  if exist
try:
    students = list(csv.DictReader(open('data/StudentRecords.txt')))
except Exception:
    students = []
#    print("New records file created, ")
print("The file StudentRecordsFile, records: ", len(students))


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
    max = 1
    for item in ageRecords:
        if max < item:
            max = item
    print("\nThe eldes student(s):", end=" ")
    names = ""
    [print(item["firstName"], item["lastName"], end=", ") for item in students if int(item["age"]) == max]
    print(" age", max)


# dispaly yanguest user
def DisplayYoungest():
    ageRecords = [int(item["age"]) for item in students]
    min = 100
    for item in ageRecords:
        if min > item:
            min = item
    print("\nThe youngest student(s):", end=" ")
    names = ""
    [print(item["firstName"], item["lastName"], end=", ") for item in students if int(item["age"]) == min]
    print(" age", min)


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

# print(dtemp)

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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # take all letters except the first 'shift' characters, and
    # add those letters to the end instead
    rotated = alphabet[5:] + alphabet[:5]
    translate_map = str.maketrans(alphabet, rotated)
    return strin.lower().translate(translate_map)


# ROT (+5)  decode method
def decode(strin):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # take all letters except the first 'shift' characters, and
    # add those letters to the end instead
    rotated = alphabet[5:] + alphabet[:5]
    translate_map = str.maketrans(rotated, alphabet)
    return strin.translate(translate_map)


# encode list creation
def encodeList(ilist, olist):
    for item in ilist:
        erow = {}
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
        erow = {}
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


# wrute student records file entered by admin
def writeRecordsFile(filename, recordsList):
    with open(filename, mode='w') as csv_file:
        fieldnames = ["fodselsNummer", "firstName", "lastName", "age", "email", "programmingCourse"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in recordsList:  # my_list, my_elist or my_dlist
            writer.writerow(item)


def askEncode():
    answer = None
    while answer != "Y" or answer != "N":
        answer = input("Do you want to create an Encrypted version of the file? Type Y for Yes or N for No:")
        answer = answer.upper()
        if answer == "N":
            return False
        elif answer == "Y":
            return True
        print("\n Oops something is buggy")


def askDecode():
    answer = None
    while answer != "Y" or answer != "N":
        answer = input("Do you want to create an Decripted version of the file? Type Y for Yes or N for No:")
        answer = answer.upper()
        if answer == "N":
            print("The assessment is over. Have a nice day.")
            exit(0)
        elif answer == "Y":
            return True
        print("\n Oops something is buggy")


def main():
    # promps and act, x and Y..,Y... - Finish
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
            en = EncodeDecodeClass
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
