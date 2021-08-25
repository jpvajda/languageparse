'''This script will fetch code languages for all repos from a Github organization.'''

import requests
import json


def repo_fetch():
    '''gets repos'''
    response = requests.get('https://api.github.com/orgs/newrelic/repos')
    repos = response.json()
    for i in repos:
        i.get['name']


def lang_fetch():
    '''gets language'''
    response = requests.get(
        'https://api.github.com/repos/newrelic/{repos}/languages')
    data = response.json()
    for i in data:
        print(i)


if __name__ == '__main__':
    lang_fetch()

# @TODO
# iterate through all repos in the newrelic org
