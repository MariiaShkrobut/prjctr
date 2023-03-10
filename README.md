Це тестовий набір для API. Він містить по чотири тести для категорій "Адреси" та "Категорії", які перевіряють, чи можна зробити виклик до API, додати нову адресу або категорію, оновити створену адресу або категорію та видалити створену адресу або категорію.

Щоб запустити цей код, Вам потрібно:

1. Завантажити та встановити Python на свій комп'ютер.
2. Встановити бібліотеку requests. Ви можете зробити це, виконавши команду "pip install" requests у терміналі.
3. Відкрити текстовий редактор, такий як Notepad.
4. Скопіюйте код з цього вікна та вставте його у відкритий текстовий редактор.
5. Збережіть файл з розширенням .py, наприклад, "test_api.py".
6. Відкрийте командний рядок (для Windows) або термінал (для Mac або Linux).
7. Перейдіть до директорії, де збережений файл з кодом командою cd "тут вкажіть шлях до диреткорії"
8. Запустіть тести командою "python test_api.py" або "python test_api.py -s -v"  щоб побачити повідомлення з самих тестів.

Тести до категорії "Адреси".
Перший тест test_can_call_endpoint() просто перевіряє, чи можна зробити запит до вказаної точки входу (ENDPOINT) за допомогою методу GET і чи повертається статус код 200. 

Другий тест test_can_add_new_address() виконує запит методом POST, щоб створити нову адресу, яка передається як рядок з форматом XML, у кінці виводиться створений ID адреси.

Третій тест test_can_update_the_address() також використовує метод POST для створення нової адреси, а потім виконує метод PUT, щоб оновити адресу за допомогою вказаного ID. Після оновлення адреси тест перевіряє, чи повертається статус код 200 і чи оновлено прізвище адреси на "Group two Updated". У кінці виводиться ID оновленої адреси.

Четвертий тест test_can_delete_the_address() також використовує метод POST для створення нової адреси. Потім він використовує метод DELETE для видалення адреси за допомогою вказаного ID. Тест перевіряє, чи повертається статус код 200 після видалення адреси та перевіряє, чи повертається статус код 404 після спроби отримати інформацію за видаленим ID. У кінці виводиться ID видаленої адреси.

Тести до категорії "Категорії".
Перший тест test_can_call_endpoint_categories() перевіряє, чи можна зробити запит GET до ендпоінту /categories.

Другий тест test_can_create_category() перевіряє можливість створення нової категорії за допомогою запиту POST до ендпоінту /categories. Запит відправляє XML-документ, який містить дані про нову категорію.

Третій тест test_cannot_update_the_category() перевіряє, чи неможливо оновити категорію за допомогою запиту PUT до ендпоінту /categories/{id}. Запит відправляє XML-документ з оновленими даними про категорію.

Четвертий тест test_cannot_delete_the_category() перевіряє, чи неможливо видалити категорію за допомогою запиту DELETE до ендпоінту /categories/{id}.
