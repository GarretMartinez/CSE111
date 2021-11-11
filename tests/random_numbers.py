import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)

    append_random_numbers(randnums)
    print(randnums)

    append_random_numbers(randnums, 3)
    print(randnums)




def append_random_numbers(numbers_list, quantity = 1):

    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


main()