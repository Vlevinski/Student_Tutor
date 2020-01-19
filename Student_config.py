#!python3.7
###
#   App configurator
###
import configparser

# string declaration
cfg_data = '''
[mysql]
host = localhost
user = user7
passwd = s$cret
db = ydb
'''

#init config
config = configparser.ConfigParser()
config.read_string(cfg_data)
'''
# show parameters
host, user, passwd, db = config['mysql'].values()
print( host,user,passwd,db)

# write to filr
with open('conf/liteDB.ini', 'w') as configfile:
    config.write(configfile)

# read from file
config1 = configparser.ConfigParser()
config1.read('conf/liteDB.ini')

# show file data
host, user, passwd, db = config1['mysql'].values()
print( host,user,passwd,db)

#show file sections
sections = config1.sections()
print(f'Sections: {sections}')
'''
# create new section as dict
cfg_data = {
    'progresql': {'host': 'localhost', 'user': 'user5',
              'passwd': 's$$ret', 'db': 'mdb'}
}

# new config section
config2 = configparser.ConfigParser()
config2.read_dict(cfg_data)

# write to filr
with open('conf/liteDB.ini', 'w') as configfile:
    config.write(configfile)
    config2.write(configfile)
