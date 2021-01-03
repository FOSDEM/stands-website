#!/usr/bin/env python3
import requests
from os import mkdir
from os.path import exists, isfile, isdir


def fetch():
    result = requests.get('http://localhost:8000/submission/api/accepted')
    result.raise_for_status()
    return result.json()


def create_skeleton(stand_o):
    path = '../content/stands/{0}'.format(stand_o['submission']['project']['name'].lower())
    static_path = '../static/stands/{0}'.format(stand_o['submission']['project']['name'].lower())
    if exists('{0}/.git'.format(path)):
        # Pull
        cmd = 'git pull origin master'
    else:
        # Clone
        cmd = 'git clone {0}'.format(stand_o['submission']['digital_edition']['stand_website_code'])
    if exists('{0}/.git'.format(static_path)):
        # Pull
        static_cmd = 'git pull origin master'
    else:
        # Clone
        static_cmd = 'git clone {0}'.format(stand_o['submission']['digital_edition']['stand_website_static'])


def main():
    print('Fetching list of accepted stands ... ', end=None)
    try:
        accepted_stands = fetch()
    except Exception as e:
        print('[FAILED]')
        print('\t\t {0}'.format(e))
        return(10)
    else:
        print('[OK]')
    for stand in accepted_stands:
        print('Pulling code for {0} ... '.format(stand['submission']['project']['name']), end=None)
        try:
            create_skeleton(stand)
        except Exception as e:
            print('[FAILED]')
            print('\t\t {0}'.format(e))
        else:
            print('[OK]')
    return 0



if __name__ == '__main__':
    exit(main())

