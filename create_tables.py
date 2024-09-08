import psycopg2

conn = psycopg2.connect(
    host="localhost",  
    database="test_db", 
    user="root",
    password="root"
)

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER REFERENCES status(id),
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    );
''')

conn.commit()
cur.close()
conn.close()

print("Таблиці створено.")
