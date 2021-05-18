#!/bin/python3

import os
import sys
import csv
import json
from pprint import pprint

with open('src/repositories.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    repositories = [(name.split('/')[1], url) for [name, _, _, language, _, url, _, _] in readCSV if language == 'JavaScript']

if not os.path.exists('repositories'):
    os.makedirs('repositories')

projects = {}

PROCESS_NUMBER = 2

HALF = int(len(repositories) / PROCESS_NUMBER)

START = 0 if int(sys.argv[1]) == 0 else HALF
END = START + HALF

for (name, url) in repositories[START:END]:
    print(name)

    path = f'repositories/{name}'

    os.system(f'[ -d {path} ] || git clone {url} {path}')
    os.system(f'cd {path} && dlf "license_finder report --format json --prepare --save=license_finder_report.json" && cd ..')

    with open(f'{path}/license_finder_report.json') as jsonfile:
        projects[name] = json.loads(jsonfile.read())

    os.system(f'rm -rf {path}')

with open('./projects.json', 'w') as jsonfile:
    json.dump(projects, jsonfile)
