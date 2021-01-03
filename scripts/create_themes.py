#!/usr/bin/env python3
import requests
from os import mkdir
from os.path import exists, isfile, isdir
import re


def fetch():
    result = requests.get('https://stands.fosdem.org/submission/api/themes')
    result.raise_for_status()
    return result.json()


def slug(name):
    illegal_r = re.compile('[^A-Za-z0-9_-]')
    return illegal_r.sub('-', name.lower())


def create_skeleton(theme_o):
    path = '../content/themes/{0}'.format(slug(theme_o['theme']))
    static_path = '../static/themes/{0}'.format(slug(theme_o['theme']))
    if not exists(path):
        mkdir(path)
    if not exists(static_path):
        mkdir(static_path)
    _index = """---
title: {0}
description: |
    {1}
logo: img/lib/material-icons/{2}.svg
---
""".format(
    theme_o['theme'],
    theme_o['description'],
    slug(theme_o['theme'])
)
    if not exists('{0}/_index.md'.format(path)):
        with open('{0}/_index.md'.format(path), 'w') as fh:
            fh.write(_index)


def main():
    print('Fetching list of themes ... ', end=None)
    try:
        themes = fetch()
    except Exception as e:
        print('[FAILED]')
        print('\t\t {0}'.format(e))
        return(10)
    else:
        print('[OK]')
    for theme in themes:
        print('Creating skeleton for {0} ... '.format(theme['theme']), end=None)
        try:
            create_skeleton(theme)
        except Exception as e:
            print('[FAILED]')
            print('\t\t {0}'.format(e))
        else:
            print('[OK]')
    return 0



if __name__ == '__main__':
    exit(main())

