#!/usr/bin/env python3

import urllib.request, json

majortom = 'http://api.open-notify.org/astros.json'

groundctrl = urllib.request.urlopen(majortom)

helmet = groundctrl.read()

helmetson = json.loads(helmet.decode('utf-8'))

print(f'\n\nconverted python data:\n\n{helmetson}')

print(f'\n\n people in space: {helmetson["number"]}')
people = helmetson['people']
print(people)
