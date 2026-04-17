import sqlite3


# A4
conn = sqlite3.connect('users.db')
#рука с ручко
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE if not exists users (
name VARCHAR(50) not null,
age INTEGER not null,
hobby TEXT    
    )
''')
conn.commit()

# CRUD Create - Read - Update - Delete

def creat_user(name, age, hobby):
    cursor.execute(f'INSERT INTRO users(name, age, hobby) VALUES (?, ?, ?)', (name, age, hobby))



creat_user('Ardager', 27, 'Python')
