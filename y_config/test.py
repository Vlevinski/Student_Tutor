from y_config import *
import configparser

path = "conf.ini"
config = configparser.ConfigParser()

cfg = '''
[data.ini]
one = 1
two = 27/01/05
db = my_db
col = False
'''

config.read_string(cfg)
write_conf(config, path)
