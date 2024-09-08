import psycopg2
from faker import Faker
import random

conn = psycopg2.connect(
    host="localhost",  
    database="test_db", 
    user="root",
    password="root"
)

cur = conn.cursor()

fake = Faker()



def seed_users(n):
    for _ in range(n):
        fullname = fake.name()
        email = fake.unique.email()
        cur.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s)",
            (fullname, email)
        )


def seed_status():
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cur.execute(
            "INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
            (status,)
        )



def seed_tasks(n):
    cur.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cur.fetchall()]

    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cur.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
            (title, description, status_id, user_id)
        )


seed_users(10) 
seed_status()  
seed_tasks(20)  

conn.commit()
cur.close()
conn.close()

print("Таблиці успішно заповнені випадковими даними.")
