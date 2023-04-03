import json
import configparser


def get_test_data(key):
    with open('test_data.json') as f:
        data = json.load(f)
    return data[key]


def get_config_value(key):
    config = configparser.ConfigParser()
    config.read('credentials.ini')
    return config['login'][key]
