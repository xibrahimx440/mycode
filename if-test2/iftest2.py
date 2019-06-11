#!/usr/bin/env python3

ipchk = '192.168.0.1'

if ipchk:
    print(f'Looks like the IP address was set: {ipchk}\n')

ipchk = input('please enter an I.P address\n')

if ipchk:
    print(f'The IP address you entered was: {ipchk}\n')
else:
    print('you did not provide an input.')


ipchk = input('Apply an IP ADDRESS\n')

if ipchk == '192.168.70.1':
    print(f'looks like the IP address of the Gateway was given: {ipchk} This is not recommended!!!')
elif ipchk:
    print(f'The IP address given was: {ipchk}')
else:
    print('No input was given')



