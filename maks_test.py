#Python restaruant
# generate random integer values
from random import randint
randint(10,1000)

# Просимо користувача ввести страви
menu = ' ' + input('Шо ти там поїсти хочеш, пиши через кому якщо багато, все в наявності \n')
# Виділяємо страви через кому у список
order = menu.split(',')
# Змінна для подальшого використання у загальній сумі замовлення
order_sum = 0
# Змінна для того, що рівномірно вирівняти результат крапками
variable_for_dots_length = '.'

# Виводимо результат 
print('\nВаше замовлення соколики:\n')
# Перебираємо наш список зі страв/напоїв 
for order_items in order:
    # Якщо довжина замовлення більш 2 символів то запускаємо подальші розрахунки
    if len(order_items) > 2:
        # зберігаємо рандомну ціну у змінну, що далі її використовувати для вирівняння
        random_cost = randint(10, 1000)
        # Складаємо рандомну ціну з загальною сумою, яка на початку буде 0
        order_sum = order_sum + random_cost
        # запускаємо цикл з крапками, який враховує довжину замовлення а в пусті місця ставить крапки, як в прикладі ДЗ
        while (len(variable_for_dots_length) + len(str(order_items.strip())) + len(str(random_cost))) < 35:
           variable_for_dots_length = variable_for_dots_length + '.'
        # виводимо строку з 1 замовленням   
        print(order_items.strip() + variable_for_dots_length + str(random_cost))
        # обнуляємо довжину крапок, так як наступні дані можуть не співпадати по довжині
        variable_for_dots_length = '.'
    # якщо замовлення пусте або недостатньо довге працює цей код
    else:
        # міняємо пусту змінну на це жартівливе повідомлення, далі працює за прикладом вище
        order_items = 'За повітря ми тут теж платимо'
        random_cost = randint(10, 1000)
        order_sum = order_sum + random_cost
        while (len(variable_for_dots_length) + len(str(order_items.strip())) + len(str(random_cost))) < 35:
           variable_for_dots_length = variable_for_dots_length + '.'
        print(order_items.strip() + variable_for_dots_length + str(random_cost))
        variable_for_dots_length = '.'
# виводимо повідомлення з загальною сумою замовлення
else:
    # ввожу змінну для того, щоб легше читалось, це для підрахунку довжини строки
    for_order_all_len = '\nВсього за вашим замовленням' + str(order_sum)
    # запускаємо цикл з крапками, який враховує довжину строк а в пусті місця ставить крапки, як в прикладі ДЗ
    while (len(variable_for_dots_length) + len(for_order_all_len)) < 36:
        variable_for_dots_length = variable_for_dots_length + '.'
    # виводимо останнє повідомлення з загальною сумою
    print('\nВсього за вашим замовленням'+ variable_for_dots_length + str(order_sum))