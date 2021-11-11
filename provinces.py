def main():
    provinces = list_provinces("provinces.txt")
    provinces.pop(0)
    provinces.pop(-1)
    print(provinces)
    print()

    for item in range(len(provinces)):
        if provinces[item] == 'AB':
            provinces[item] = 'Alberta'

    print(provinces)
    count = provinces.count('Alberta')
    print()
    print(f'Alberta appears {count} times in the list')




def list_provinces(provinces_txt):

    lines = []

    with open(provinces_txt, "rt") as provinces:
        for line in provinces:
            clean_line = line.strip()
            lines.append(clean_line)

    return lines



main()