#!python3.7
#

import configparser

conf = configparser.ConfigParser()

cnf = {"default":  {"one": 1, "two": True}}
conf.read_dict(cnf)
print (conf.sections())

print("\n", conf['default'])
a = conf['default']
print (a.items())
print(conf['default']['one'])

cnf1 = {"section1": {"three": 1, "four": "yes"}}
conf.read_dict(cnf1)
print ("\n", conf.sections())
