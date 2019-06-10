#!/usr/bin/env python3

import csv

def main():

    fille = open('vendor.csv','r')
    cont = fille.read()
    vendata = csv.reader(fille, delimiter=',')
    fille.close()

    print(vendata)
    #for row in vendata:
        #print(f'The ipaddress is {row[2]} requires the driver {row[3]}')


main()
