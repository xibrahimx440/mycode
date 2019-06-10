#!/usr/bin/env python3

my_list = ['192.168.0.5', 5060,'UP']

print(f'my first item is (IP): {my_list[0]}')
print(f'my second item is (port): {my_list[1]}')
print(f'my third item is (state): {my_list[2]}')


new_list = [5060, '80', 55, '10.0.0.1', '10.20.30.1', 'ssh']

print(f'when i {new_list[5]}, into IP addresses {new_list[3]} or {4} I ams am ubable to ping ports {new_list[0]},{new_list[1]}, or {new_list[2]}.')


def main():
    networklists = [
            ['ios', '10.0.2.1'],
            ['ios', '10.0.55.1'],
            ['ios-xr', '10.0.3.1'],
            ['junos', '10.0.10.1'],
            ['eos','10..0.14.1.']
            ]

    for driveandip in networklists:
        print(f'SSH into {driveandip[1]} using driver {driveandip[0]}')

main()


