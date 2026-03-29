print('Hello, I am your personal calculator!')
print('What would you like me to do?')

def bob_is_sigma(expr):
    if '+' in expr:
        a = expr.split('+')
        print(int(a[0])+int(a[1]))
    elif '-' in expr:
        b = expr.split('-')
        print(int(b[0])-int(b[1]))
    elif '*' in expr:
        c = expr.split('*')
        print(int(c[0])*int(c[1]))
    elif '/' in expr:
        d = expr.split('/')
        print(int(c[0])/int(c[1]))



while True:
    result1=input('')
    if result1=='':
        print('Invalid Operation!')
    
    elif result1!='':
        if result1=='reset' or result1=='r':
            break
        else:
            bob_is_sigma(result1)