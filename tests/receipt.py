import csv
def main():

    products = read_products()
    print(products)

    price = 0
    with open("tests/request.csv", "rt") as list:
        reader = csv.reader(list)
        next(reader)
        for row in reader:
            item_id = row[0]
            cost = products[2]
            if item_id in products:
                price += cost

        print(cost)


def read_products():
    products = {}

    with open("tests/products.csv", "rt") as list:
        reader = csv.reader(list)
        next(reader)
        for row in reader:
            key = row[0]
            products[key] = row
    return products






main()