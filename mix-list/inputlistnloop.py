#!/usr/bin/env/python3

def main():
    networklist = []
    filee = open('driverip.txt', 'r')
    cont = filee.readlines()
    filee.close()

    for line in cont:
        networklist.append(line.rstrip('\n').split(' '))
    
    for networklistt in networklist:
        print(f'SSH into {networklistt[1]} using driver {networklistt[0]}')
    

main()
