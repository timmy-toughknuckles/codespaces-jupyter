
while True:
    a = input('What unit do you want to convert from? (cup, pint, quart, gallon): ')
    b = float(input('Enter the amount you want to convert: '))
    if a.lower() == 'cup':
        print(b, 'cups is equal to', b / 2, 'pints and ', b / 4, 'quarts and ', b / 16, 'gallons')
    elif a.lower() == 'pint':
        print(b, 'pints is equal to', b * 2, 'cups and ', b / 2, 'quarts and ', b / 8, 'gallons')
    elif a.lower() == 'quart':
        print(b, 'quarts is equal to', b * 4, 'cups and ', b * 2, 'pints and ', b / 4, 'gallons')
    elif a.lower() == 'gallon':
        print(b, 'gallons is equal to', b * 16, 'cups and ', b * 8, 'pints and ', b * 4, 'quarts')
    else:
        print('Invalid unit. Please enter cup, pint, quart, or gallon.')