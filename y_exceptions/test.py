#!python3.7
#

# classic method
try:
    file = open('test.txt', 'r')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e
