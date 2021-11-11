import math

items = int(input('Enter the number of items: '))
ipb = int(input('Enter the number of items per box: '))

boxes = items / ipb

print()
print(f'For {items} items, packing {ipb} items per box, you will need {math.ceil(boxes)} boxes.')
