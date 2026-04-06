score = 0

a = input('what is the capital of France? ')
if a .lower() == 'paris':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is Paris.')
b = input('what is the largest planet in our solar system? ')
if b.lower() == 'jupiter':

    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is Jupiter.')
c = input('what is the smallest country in the world? ')
if c.lower() == 'vatican city':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is Vatican City.')
d = input('what is the longest river in the world? ')
if d.lower() == 'nile':
    print('Correct!')
    score += 1
else:    print('Incorrect. The correct answer is Nile.')
e = input('what is the highest mountain in the world? ')
if e.lower() == 'mount everest':
    print('Correct!')
    score += 1
else:    print('Incorrect. The correct answer is Mount Everest.')
print(f'Your final score is {score} out of 5.')