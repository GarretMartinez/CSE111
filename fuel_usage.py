def main():

    start = int(input('Enter the starting odometer number (in miles): '))
    end = int(input('Enter the ending odometer number (in miles): '))
    fuel = float(input('Enter the amount of fuel consumed (in gallons): '))

    mpg = miles_per_gallon(start, end, fuel)
    lp100k = lp100k_from_mpg(mpg)

    print()
    print(f'{mpg:.1f} miles per gallon')
    print(f'{lp100k:.2f} liters per 100 kilometers')

def miles_per_gallon(start, end, fuel):
    mpg = (end - start) / fuel

    return mpg

def lp100k_from_mpg(mpg):

    lp100k = 235.215 / mpg

    return lp100k

main()