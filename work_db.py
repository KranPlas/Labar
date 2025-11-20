import sqlite3

# Создание базы данных (файл)
conn = sqlite3.connect('labar.db')
cursor = conn.cursor()

# Создание таблицы Компьютер
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT NOT NULL,
    role TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
)
''')

# Добавление записи
cursor.execute("INSERT INTO Users (username) VALUES ('KranPlas')")
cursor.execute("INSERT INTO Users (email) VALUES ('karapuchka2007@gmail.com')")
cursor.execute("INSERT INTO Users (role) VALUES ('admin')")

# Получение данных
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()