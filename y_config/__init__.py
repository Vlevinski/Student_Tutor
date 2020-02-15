def write_conf(config, path):
    '''

    :param config:  configparser instance
    :param path:    config file path
    :return:
    '''
    with open(path, 'w') as f:
        config.write(f)
    return True
