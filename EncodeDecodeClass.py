####
#     EncodeDecodeClass to implement file encode/decode operations,   use python ver3.7
####

class EncodeDecodeClass():

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

    # encode function to create EncodedStudentRecords.txt
#    def EncodeStudentList(self):
#       pass
    # decode function for EncodedStudentRecords.txt
#    def DecodeStudentList(self):
#        pass

    def digits_encode(self, sin):
        return sin[::-1]

    def str_encode(self, shift,sin):
        # 	encode/decode
        #	x = rot_encode(13,'Hello World')
        #	y = rot_encode(-13,x)

        from string import ascii_lowercase as lc
        from string import ascii_uppercase as uc
        print (n,s)
        lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
        return lambda s: s.translate(lookup)


import string

def rot(s, n=13):
    '''Encode string s with ROT-n, i.e., by shifting all letters n positions.
    When n is not supplied, ROT-13 encoding is assumed.
    '''
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    upper_start = ord(upper[0])
    lower_start = ord(lower[0])
    out = ''
    for letter in s:
        if letter in upper:
            out += chr(upper_start + (ord(letter) - upper_start + n) % 26)
        elif letter in lower:
            out += chr(lower_start + (ord(letter) - lower_start + n) % 26)
        else:
            out += letter
    return(out)

def invrot(s, n=13):
    '''Decode a string s encoded with ROT-n-encoding
    When n is not supplied, ROT-13 is assumed.
    '''
    return(rot(s, -n))

#reverse function
def reverse_value(x):
    return x[::-1]


def rot_encode(n, s):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    print (n,s)
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

#print(rot_encode(5,'Hello World'))


#a = "123456789"
#print (a)
#b= reverse_value(a)
#print (b)
#s = "Jonn Pann"
#print (s)



x = rot_encode(13,'Hello World')
y = rot_encode(-13,x)
print(x) # Uryyb Jbeyq
print(y) # Hello World
