'''This script will fetch code languages for all repos from a Github organization.'''

import urllib.request
import json

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():

    urlData ="https://api.github.com/orgs/newrelic/repos"
    jsonData = getResponse(urlData)
    # print the code language and repo name
    for i in jsonData['repos']:
        print(f'Language: {i["language"]["language_name"]} , Name : {i["name"]["repo_name"]}')

if __name__ == '__main__':
    main()

# @TODO
# resolve TypeError: list indices must be integers or slices, not str

                  
