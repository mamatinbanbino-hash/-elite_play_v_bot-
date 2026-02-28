import os
import telebot
from flask import Flask, request

# 1. Configuration (Sécurité : Utilise les variables d'environnement Vercel)
TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

# 2. Route pour recevoir les messages de Telegram (Webhook)
@app.route('/api/index', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Interdit", 403

# 3. Logique du Bot : Réponse à toutes les questions
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_text = message.text
    chat_id = message.chat.id
    
    # Ici, tu peux ajouter une logique d'IA ou de recherche
    reponse = f"🤖 Bot Elite Play V :\n\nTu as demandé : {user_text}\n\nStatut : En cours de traitement via Vercel."
    
    bot.send_message(chat_id, reponse)

# Nécessaire pour Flask sur Vercel
if __name__ == "__main__":
    app.run()
