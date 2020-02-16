def write_conf(conf, path):
    # save config file
    with open(path, 'w') as f:
        conf.write(f)
    return True


def set_string(conf, name=None):
    # declare string with config section
    if name is None:
        return '''
[DEFAULT]
'''
    else:
        return conf.read_string(name)


def set_dict(conf, name):
    # read config from dict
    if name is None:
        name = {"DEFAULT": ""}
    return conf.read_dict(name)


def show_config(conf):
    # print config
    for section_name in conf.sections():
        print('Section:', section_name)
        print('  Options:', conf.options(section_name))
        for name, value in conf.items(section_name):
            print('  {} = {}'.format(name, value))
        print()


def read_config(conf, name=None):
    # read config from file
    if name is None:
        name = "conf.ini"
    return conf.read(name)
