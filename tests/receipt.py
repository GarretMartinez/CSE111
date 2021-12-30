import csv
from datetime import datetime
def main():
    try:

        products = read_products()
        
        print("Store-Co")
        print()

        price = 0
        tot_price = 0
        count = 0

        #Open the file and read the id's, prices, names, and costs
        with open("tests/request.csv", "rt") as list:
            reader = csv.reader(list)
            next(reader)
            for row in reader:
                item_id = row[0]
                price = products[item_id][2]
                name = products[item_id][1]
                quantity = int(row[1])
                tot_price += float(price) * quantity
                count += 1

                #print receipt items
                print(f'{name} {quantity} @ {price}')

            #Calculate tax and print final total, thank you, and date
            print()
            tax = tot_price * 0.06
            date_time = datetime.now()

            print(f'You ordered {count} items subtotaling {tot_price:.2f}')
            print(f'Tax: {tax:.2f}')
            print(f'Final total: {round(tax + tot_price, 2)}')

            print()
            print('Thank you for shopping at Store-Co!')
            print(date_time.strftime("%B %m %Y, %I:%M %p"))

    
    #exception cases
    except FileNotFoundError as error:
        print(error)
        print("Please choose a different file.")

    except PermissionError as perm_err:
        print(perm_err)
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")

    except ValueError as val_err:
        print("Error:", val_err)

    except (csv.Error, KeyError) as error:
        print(f"Error: line in code is"
                " formatted incorrectly.")

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