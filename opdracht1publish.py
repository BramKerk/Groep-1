#   Opdracht 2.1
print(  """
Name
Adres
Mobiel
"""  )

#   Opdracht 2.2
sales = float(input('Total sales: '))
profit = sales * 0.23
print("Total profit is: ", profit)

#   Opdracht 2.3
pounds = float(input('Pounds: '))
kg = pounds * 0.454
print('Kg: ', format(kg, '.2f'))

#   Opdracht 2.4
item0 = float(input('Price of item 1: '))
item1 = float(input('Price of item 2: '))
item2 = float(input('Price of item 3: '))
item3 = float(input('Price of item 4: '))
item4 = float(input('Price of item 5: '))
subtotal = item0 + item1 + item2 + item3 + item4
tax = float(1.07)
total = subtotal * tax
print('Subtotal:', format(subtotal, '.2f'))
print('Tax: 7%')
print('Total:', format(total, '.2f'))

#   Opdracht 2.5
mph = 70
print('Distance after 6 hours:', 6 * mph, 'miles')
print('Distance after 10 hours:', 10 * mph, 'miles')
print('Distance after 15 hours:', 15 * mph, 'miles')

#   Opdracht 2.7
md = float(input('Enter miles driven:'))
gu = float(input('Enter gallons used:'))
mpg = md / gu
print('Miles-per-gallon:', format(mpg, '.2f'), 'm/g')

#   Opdracht 2.10
sugar0 = float(1.5 / 48)
butter0 = float(1 / 48)
flour0 = float(2.75 / 48)
cookies = float(input('How many cookies do you want?'))
sugar1 = sugar0 * cookies
butter1 = butter0 * cookies
flour1 = flour0 * cookies
print('You will need', format(sugar1, '.0f'), 'cups of sugar')
print('You will need', format(butter1, '.0f'), 'cups of butter')
print('You will need', format(flour1, '.0f'), 'cups of flour')




