import os
import psycopg2
from flask import Flask

app = Flask(__name__)

# Отримуємо налаштування зі Змінних Середовища (ті, що в docker-compose)
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def hello():
    return 'Головна сторінка (HOT RELOAD ПРАЦЮЄ!)'

@app.route('/db-test')
def db_test():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Виконуємо простий SQL запит
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f'Успішне підключення! Версія бази: {db_version}'
    except Exception as e:
        return f'Помилка підключення: {str(e)}'

