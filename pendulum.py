import math

length = float(input('What is the length of the pendulum? '))

time = 2 * math.pi * (math.sqrt(length / 9.81))

print(f'{time:.2f}')
