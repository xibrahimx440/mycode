#!/usr/bin/env python3

import urllib.request, json, turtle


eoss = 'http://api.open-notify.org/iss-now.json'

trackiss = urllib.request.urlopen(eoss)

ztrack = trackiss.read()

results = json.loads(ztrack.decode('utf-8'))

print(f'converted python data: {results}\n\n')

input('ISS data received!!!! press any key to continue!\n\n')

location = results['iss_position']

lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)


screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set the resolution

screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic('iss_map.gif')



screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))
iss.penup()
iss.goto(lon, lat)
turtle.mainloop()

