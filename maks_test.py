#Python restaruant
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(2)

menu = ' ' + input('Шо ти там поїсти хочеш, пиши через кому якщо багато, все в наявності \n')
order = menu.split(',')
a = 0
d = '.'

print('\nВаше замовлення соколики:\n')
for c in order:
    if len(c) > 2:
        b = randint(0, 50)
        a = a + b
        while (len(d) + len(str(c.strip())) + len(str(b))) < 35:
           d = d + '.'
        print(c.strip() + d + str(b))
        d = '.'
    else:
        c = 'За повітря ми тут теж платимо'
        b = randint(0, 50)
        a = a + b
        while (len(d) + len(str(c.strip())) + len(str(b))) < 35:
           d = d + '.'
        print(c.strip() + d + str(b))
        d = '.'
else:
    f = '\nВсього за вашим замовленням' + str(a)
    while (len(d) + len(f)) < 36:
        d = d + '.'
    print('\nВсього за вашим замовленням'+ d + str(a))