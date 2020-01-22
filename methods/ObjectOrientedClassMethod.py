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

    # class to json
    def toJSON(self):
        import json
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# create a class instance
#student = Student("123456", "Nick", "Pann", 33, "nicktheboy@yahoo.com", "python")

