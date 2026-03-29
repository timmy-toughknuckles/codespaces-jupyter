print('Hello, I am your personal calculator!')
print('What would you like me to do?')

def bob_is_sigma(expr):
    if '+' in expr:
        a = expr.split('+')
        print(float(a[0])+float(a[1]))
    elif '-' in expr:
        b = expr.split('-')
        print(float(b[0])-float(b[1]))
    elif '*' in expr:
        c = expr.split('*')
        print(float(c[0])*float(c[1]))
    elif '/' in expr:
        d = expr.split('/')
        print(float(d[0])/float(d[1]))



while True:
    result1=input('')
    if result1=='':
        print('Invalid Operation!')
    
    elif result1!='':
        if result1=='reset' or result1=='r':
            break
        else:
            bob_is_sigma(result1)