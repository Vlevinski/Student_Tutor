from y_config import *
import configparser

path = "conf.ini"
conf = configparser.ConfigParser()

sec1 = '''
[default]
one = 1
two = 27/01/01
three = False
four = "Yes, it is"
'''

cfg = set_string(conf, sec1)

# conf.read_string(cfg)


# conf.read(conf, path)

show_config(conf, 'sqlite')

sec2 = '''
[section1]
one = 2
two = 28/01/01
three = True
four = "No, it not"
'''

set_string(conf, sec2)
show_config(conf, 'sqlite')

write_conf(conf, path)
