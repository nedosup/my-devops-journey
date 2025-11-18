from flask import Flask
app = Flask(__name__) # Створюємо екземпляр додатку

@app.route('/') # Вказуємо URL-шлях
def hello_world():
    return 'Привіт! Я додаток на Flask. Ви це бачите!'

@app.route('/test') # Інший URL-шлях
def test_page():
    return 'Версія 2.0: Реліз успішний!'

