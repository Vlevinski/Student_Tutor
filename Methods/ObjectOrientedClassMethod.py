###
#
###
# copy the list from pdf like
# fodselsNummer,firstName,lastName,age,email,programmingCourse
# create record file Student Records.txt

#   class declaration
class Student():
    def int(self,sN,fN,lN,age,email,pCourse):
        self.sN =sN
        self.fN =fN
        self.lN= lN
        self.age= age
        self.email=email
        self.pCourse=pCourse


#   the method for record display
    def DisplayName(self):
        print(self.fN, self.lN)

# create a class instance
student = Student()

# set-up of class parameters
student.sN = "123456"
student.fN = "Nick"
student.lN = "Pann"
student.age = 33
student.email ="nick@yahoo.com"

# call of class method
student.DisplayName()

###
#  sys.out
###
#
#run the program with python with following command:
#python StudentRecords,py
#You will see the result:
#
# ---> Nick Pann
