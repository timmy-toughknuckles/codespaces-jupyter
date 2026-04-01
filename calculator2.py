def calculator():
    a = input('Enter your first number: ')
    b = input('Enter your second number: ')
    operation = input('Enter the operation you want to perform (e.g. +, -, *, /): ')
    if operation == '+':
        print(float(a) + float(b))
    if operation == '-':
        print(float(a) - float(b))
    if operation == '*':
        print(float(a) * float(b))
    if operation == '/':
        if float(b) == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(float(a) / float(b))




calculator()

while True:
    c = input('If you want, you can type "reset" or "r" to reset the calculator: ')
    if c == "Don't ask me again":
        while True:
            calculator()
    if c == 'reset' or c == 'r':
        break
    if c == 'no':
        calculator()
        