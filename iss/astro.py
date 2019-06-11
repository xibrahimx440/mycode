#!/usr/bin/env python3

import urllib.request, json

majortom = 'http://api.open-notify.org/astros.json'

groundctrl = urllib.request.urlopen(majortom)

helmet = groundctrl.read()

helmetson = json.loads(helmet.decode('utf-8'))


people = helmetson['people']

for i in people:
    print(f'the names of the people in the ship is: {i["name"]}')
    print(f'the craft is {i["craft"]}')

