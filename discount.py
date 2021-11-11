from datetime import datetime

dateTime = datetime.now()

day = datetime.weekday(dateTime)

tax = 0.06

subtotal = float(input('Enter the sub total: '))

salesTaxAmount = subtotal * tax
print()

if (day == 1 or day == 2) and subtotal >= 50:
    discount = subtotal * .10
    print(f'Discount amount: {discount:.2f}')
    
    amount = subtotal - discount
    finTax = amount * tax
    print(f'Sales tax: {finTax:.2f}')

    finTotal = finTax + amount
else:
    finTax = subtotal * tax
    print(f'Sales tax: {finTax:.2f}')

    finTotal = subtotal * tax + subtotal

print(f'Total: {finTotal:.2f}')
