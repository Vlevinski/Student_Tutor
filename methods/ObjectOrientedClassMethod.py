###
#   create record file methods Records.txt
###


#   class constructor
class Student:

    def __init__(self, sN, fN, lN, age, email, pCourse):
        self.sN = sN
        self.fN = fN
        self.lN = lN
        self.age = age
        self.email = email
        self.pCourse = pCourse

    #   the method
    def DisplayName(self):
        print(self.fN, self.lN)


# create a class instance
student = Student("123456", "Nick", "Pann", 33, "nicktheboy@yahoo.com", "python")

# call of class method
student.DisplayName()

###
#  sys.out
###

#
# run the program with python with following command:
# python StudentRecords,py
# You will see the result:
#
# ---> Nick Pann
