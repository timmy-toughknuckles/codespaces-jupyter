a = input('Enter your first number: ')
b = input('Enter your second number: ')
operation = input('Enter the operation you want to perform (e.g. +, -, *, /): ')
if operation == '+':
    print(float(a) + float(b))
elif operation == '-':
    print(float(a) - float(b))
elif operation == '*':
    print(float(a) * float(b))
elif operation == '/':
    print(float(a) / float(b))

while True:
    c = input('If you want, you can type "reset" or "r" to reset the calculator: ')
    if c == "Don't ask me again":
        while True:
            a = input('Enter your first number: ')
            b = input('Enter your second number: ')
            operation = input('Enter the operation you want to perform (e.g. +, -, *, /): ')
            if operation == '+':
                print(float(a) + float(b))
            elif operation == '-':
                print(float(a) - float(b))
            elif operation == '*':
                print(float(a) * float(b))
            elif operation == '/':
                print(float(a) / float(b))
    if c == 'reset' or c == 'r':
        break
    if c == 'no':
        a = input('Enter your first number: ')
        b = input('Enter your second number: ')
        operation = input('Enter the operation you want to perform (e.g. +, -,  *, /): ')
        if operation == '+':
            print(float(a) + float(b))
        elif operation == '-':
            print(float(a) - float(b))
        elif operation == '*':
            print(float(a) * float(b))
        elif operation == '/':
            print(float(a) / float(b))