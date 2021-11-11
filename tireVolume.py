import math
from datetime import datetime

width = int(input('What is the width of the tire in mm? (ex: 150) '))
aRatio = int(input('What is the aspect ratio of the tire? (ex: 70) '))
diameter = int(input('What is the diameter of the tire in inches? (ex: 20) '))
price = 0
number = ''

volume = (math.pi * width**2 * aRatio * (width * aRatio + 2540 * diameter)) / 10000000000

if volume <= 35:
    price = 50
elif volume <= 55:
    price = 80
elif volume <= 75:
    price = 110
else:
    price = 150

date = datetime.now()

print()
print(f'The approximate volume is {volume:.2f} liters')
yes_no = input(f'The price for that size tire is ${price}, would you like to purchase it? (Y/N): ')

if yes_no.lower() == 'y':
    number = input('What is your phone number? ')

with open('volumes.txt', 'at') as volumes:
    print(f'{date:%Y-%m-%d}, {width}, {aRatio}, {diameter}, {volume:.2f}, {number}', file=volumes)
