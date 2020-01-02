
# copy text with field names from your pdf
#  * create file_record
#  * create file StudentsRecods.txt
#  *read the file

file_record = "fodselsNummer,firstName,lastName,age,email,programmingCourse"

f = open("StudentRecords.txt", "a")
f.write(file_record)
f.close()

#open and read the file after the appending:
f = open("StudentRecords.txt.txt", "r")
print(f.read())
