import sqlite3

# Создаем подключение к базе данных (если её нет, то она будет создана)
conn = sqlite3.connect('example.db')

# Создаем курсор, который позволит нам выполнять SQL-запросы
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# Добавляем несколько записей в таблицу
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 28))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 35))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Charlie', 22))

# Сохраняем изменения (коммитим) и закрываем соединение с базой данных
conn.commit()
conn.close()

# Теперь давайте получим данные из базы данных

# Снова открываем соединение
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Выполняем запрос, чтобы получить всех пользователей
cursor.execute('SELECT * FROM users')

# Получаем все строки результата
users = cursor.fetchall()

# Выводим данные на экран
for user in users:
    print(f'ID: {user[0]}, Name: {user[1]}, Age: {user[2]}')

# Закрываем соединение с базой данных
conn.close()
