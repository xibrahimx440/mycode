#!/usr/bin/env python3

import csv

def main():

    with open ('vendor.csv', 'r') as vendorfile:
        vendata = csv.reader(vendorfile, delimiter=',')

        for row in vendata:
            print(f'The ipaddress is {row[2]} requires the driver {row[3]}')


main()
