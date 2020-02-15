def write_conf(config, path):
    with open(path, 'w') as f:
        config.write(f)
    return True
