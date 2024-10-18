from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

# Telegram bot username'i
TELEGRAM_BOT_USERNAME = 'YOUR_BOT_USERNAME'
# Web ilova manzili
AUTH_URL = 'https://your-server.com/auth/telegram'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth/telegram')
def auth_telegram():
    # Telegramdan keladigan so'rov ma'lumotlarini olish
    user_id = request.args.get('id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    username = request.args.get('username')

    # Ma'lumotlarni konsolga chiqarish
    print(f"User ID: {user_id}, First Name: {first_name}, Last Name: {last_name}, Username: {username}")

    # Foydalanuvchi ma'lumotlarini web sahifaga yuborish
    return render_template('user_info.html', user_id=user_id, first_name=first_name, last_name=last_name, username=username)

if __name__ == '__main__':
    app.run(debug=True)
