
#Mary Ann Green
#2/12/2018
#Unit 2
#TtlPurch.py
#This program calculates 5 purchased items based on the sale tax

#Sales tax constant
SALES_TAX = 0.06

#Item 1 price
item_1 = float(input('What is the price of item 1? '))
print('Item 1: ', format(item_1, '.2f'))

#Item 2 price
item_2 = float(input('What is the price of item 2? '))
print('Item 2: ', format(item_2, '.2f'))

#Item 3 price
item_3 = float(input('What is the price of item 3? '))
print('Item 3: ', format(item_3, '.2f'))

#Item 4 price
item_4 = float(input('What is the price of item 4? '))
print('Item 4: ', format(item_4, '.2f'))

#Item 5 price
item_5 = float(input('What is the price of item 5? '))
print('Item 5: ', format(item_5, '.2f'))

#Subtotal, adding all 5 items together
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
float(subtotal)
print('Subtotal: ', format(subtotal, '.2f'))

#subtotal with sale tax, mulitiplying the subtotal by the sale tax
tax = subtotal * SALES_TAX
float(tax)
print('Tax: ', format(tax, '.2f'))

#Total, adding the sale tax to the subtotal
total = subtotal + tax
float(total)
print('Total: ', format(total, '.2f'))

#The program with the Output sample session
#Enter the price of each item
#The program will calculate the subtotal, tax and the total of the items
#What is the price of item 1? 5.99
#What is the price of item 2? 4.99
#What is the price of item 3? 7.99
#What is the price of item 4? 3.89
#What is the price of item 5? 6.78
#subtotal 29.64
#Tax 1.78
#Total 31.42

