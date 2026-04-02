while True:
    a = input('Enter your first number: ')
    b = input('Enter your second number: ')
    print(a + ' + ' + b + ' = ' + str(float(a) + float(b)))
    print(a + ' - ' + b + ' = ' + str(float(a) - float(b)))
    print(a + ' * ' + b + ' = ' + str(float(a) * float(b)))
    if float(b) == 0:
        print(a + ' / ' + b + ' = Error: Division by zero is not allowed.')
    else:
        print(a + ' / ' + b + ' = ' + str(float(a) / float(b)))