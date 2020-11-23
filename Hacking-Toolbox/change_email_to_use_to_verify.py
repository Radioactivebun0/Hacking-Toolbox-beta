x = input('What Email do you want to use? ')
print(f'Using Email: {x}')

with open('email.txt', 'w') as a:
    a.write(x)

