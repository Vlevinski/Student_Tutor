#!python3.7
####
#     StudentRecordClass to implement methods class,   use python ver3.7
####


class StudentRecordsClass:

    # class conctructor
    def __init__(self, fodselsNummer, firstName, lastName, age, email, programmingCourse):
        self.fodselsNummer = fodselsNummer
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
        self.programmingCourse = programmingCourse

    # print students full name method
    def DisplayName(self):
        print(self.firstName, self.lastName)

