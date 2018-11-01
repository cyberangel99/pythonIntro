#Sales tax constant
SALES_TAX = 0.06

#Item 1
item_1 = float(input('What is the price of item 1? '))
print('Item 1: ', format(item_1, '.2f'))

#Item 2
item_2 = float(input('What is the price of item 2? '))
print('Item 2: ', format(item_2, '.2f'))

#Item 3
item_3 = float(input('What is the price of item 3? '))
print('Item 3: ', format(item_3, '.2f'))

#Item 4
item_4 = float(input('What is the price of item 4? '))
print('Item 4: ', format(item_4, '.2f'))

#Item 5
item_5 = float(input('What is the price of item 5? '))
print('Item 5: ', format(item_5, '.2f'))

#Subtotal
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
float(subtotal)
print('Subtotal: ', format(subtotal, '.2f'))

#subtotal with sale tax
tax = subtotal * SALES_TAX
float(tax)
print('Tax: ', format(tax, '.2f'))

#Total
total = subtotal + tax
float(total)
print('Total: ', format(total, '.2f'))
