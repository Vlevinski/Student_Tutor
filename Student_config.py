#!python3.7

###
#   App configurator
###
import configparser

# string declaration
cfg_data = '''
[sqlite]
host = localhost
user = user7
passwd = s$cret
db = ydb
'''

#init config
config = configparser.ConfigParser()
config.read_string(cfg_data)

# write to filr
with open('conf/liteDB.ini', 'w') as config_file:
    config.write(config_file)

