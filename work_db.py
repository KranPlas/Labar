import sqlite3
from datetime import datetime


# Создание базы данных (файл)
conn = sqlite3.connect('labar.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT NOT NULL,
    created_at TEXT NOT NULL
)
''')

# Добавление записи
cursor.execute('''
INSERT INTO Users (name, email, role, created_at) 
VALUES (?, ?, ?, ?)
''', ('homyacheLLo', 'hgkfgn75fv@gmail.com', 'user', datetime.now()))


cursor.execute('''
CREATE TABLE IF NOT EXISTS PCs (
    pc_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    inst_date TEXT NOT NULL,
    inst_place TEXT NOT NULL
)
''')

cursor.execute('''
INSERT INTO PCs (name, inst_date, inst_place) 
VALUES (?, ?, ?)
''', ('PC-666KIR', '19.09.2013', 'C:'))


cursor.execute('''
CREATE TABLE IF NOT EXISTS Programs (
    software_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    version TEXT NOT NULL,
    release_date TEXT NOT NULL,
    developer TEXT NOT NULL,
    category TEXT NOT NULL
)
''')

cursor.execute('''
INSERT INTO Programs (name, version, release_date, developer, category) 
VALUES (?, ?, ?, ?, ?)
''', ('Steam', 'Unknown', '12.09.2003', 'Valve', 'Games'))

# Получение данных
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()