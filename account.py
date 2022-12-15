"""
account.py

- Read/Write accounts to local config file
- Load accounts info from config
"""
import json


def read_config():
    with open('config.json') as f:
        config = json.load(f)
    return config


def write_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f)


def add_account(name: str, account: str, password: str,
                area: str):
    if account == '' or password == '' or area == '':
        raise Exception('Invalid Inputs!')
    config = read_config()
    if name not in config.keys():
        config[name] = {
            'account': account,
            'password': password,
            'area': area
        }
        write_config(config)
    else:
        raise Exception('Account already exists!')


def edit_account(name, new_attr):
    config = read_config()
    if name in config.keys():
        i = 1
        for key in config[name].keys():
            if new_attr[i] != '':
                config[name][key] = new_attr[i]
            i += 1
        if new_attr[0] != '':
            if new_attr[0] not in config.keys():
                config[new_attr[0]] = config.pop(name)
        write_config(config)


def delete_account(name):
    config = read_config()
    if name in config.keys():
        config.pop(name)
        write_config(config)


def get_login_args(name):
    config = read_config()
    return config[name]['account'], config[name]['password'], config[name]['area']


def get_accounts():
    config = read_config()
    ret = []
    for name in config.keys():
        ret.append([name, config[name]['account'], config[name]['password'], config[name]['area']])
    return ret


def show_accounts():
    print(read_config())
