#!/usr/bin/env python3
import requests
from os import mkdir
from os.path import exists, isfile, isdir
import configparser
import re
import yaml


def fetch():
    result = requests.get('https://stands.fosdem.org/submission/api/accepted')
    result.raise_for_status()
    return result.json()


def create_submodule_config(path_name, stand_o, config):
    if stand_o['submission']['digital_edition']['stand_website_static']:
        config['submodule "content/stands/{0}"'.format(path_name)] = {
            'path': 'content/stands/{0}'.format(path_name),
            'url': stand_o['submission']['digital_edition']['stand_website_code']
        }
    if stand_o['submission']['digital_edition']['stand_website_static']:
        config['submodule "static/stands/{0}"'.format(path_name)] = {
            'path': 'static/stands/{0}'.format(path_name),
            'url': stand_o['submission']['digital_edition']['stand_website_static']
        }


def create_skeleton(path_name, stand_o):
    path = '../content/stands/{0}'.format(path_name)
    static_path = '../static/stands/{0}'.format(path_name)
    if not exists(path):
        mkdir(path)
    if not exists(static_path):
        mkdir(static_path)
    _index_contents = {
        'title': stand_o['submission']['project']['name'],
        'themes': [
            stand_o['submission']['project']['theme']['theme']
        ],
        'website': stand_o['submission']['project']['website'],
        'logo': 'stands/{0}/logo.png'.format(path_name),
        'description': stand_o['submission']['project']['description'],
        'showcase': stand_o['submission']['digital_edition']['showcase'],
        'new_this_year': stand_o['submission']['digital_edition']['new_this_year'],
        'layout': 'stand',
        'chatroom': stand_o['submission']['project']['chatroom']
    }
    _index = """---
{0}---""".format(yaml.dump(_index_contents, default_flow_style=False))
    if not exists('../content/stands/{0}.md'.format(path_name)):
        with open('../content/stands/{0}.md'.format(path_name), 'w') as fh:
            fh.write(_index)


def main():
    print('Fetching list of accepted stands ... ', end=None)
    submodule_config = configparser.ConfigParser()
    invalid_r = re.compile('[^a-zA-Z0-9_-]', flags=re.IGNORECASE)
    try:
        accepted_stands = fetch()
    except Exception as e:
        print('[FAILED]')
        print('\t\t {0}'.format(e))
        return(10)
    else:
        print('[OK]')
    for stand in accepted_stands:
        print('Creating skeleton for {0} ... '.format(stand['submission']['project']['name']), end=None)
        path_name = invalid_r.sub('_', stand['submission']['project']['name']).lower()
        try:
            create_skeleton(path_name, stand)
        except Exception as e:
            print('[FAILED]')
            print('\t\t {0}'.format(e))

        try:
            create_submodule_config(path_name, stand, submodule_config)
        except Exception as e:
            print('[FAILED]')
            print('\t\t {0}'.format(e))
        else:
            print('[OK]')
    
    with open('../.gitmodules', 'w') as configfile:
        submodule_config.write(configfile)
    return 0



if __name__ == '__main__':
    exit(main())

