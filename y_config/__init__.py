def write_conf(config, path):
    # save config file
    with open(path, 'w') as f:
        config.write(f)
    return True


def set_string():
    # declare string with config section
    return '''
[data.ini]
one = 1
two = 27/01/05
db = my_db
col = False
'''


def show_config(conf):
    # print config
    for section_name in conf.sections():
        print('Section:', section_name)
        print('  Options:', conf.options(section_name))
        for name, value in conf.items(section_name):
            print('  {} = {}'.format(name, value))
        print()
