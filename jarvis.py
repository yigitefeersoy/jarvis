import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from groq import Groq

#Ayarlar
TELEGRAM_TOKEN = "TELEGRAM_BOTUNUN_TOKENI" #readme.md yi oku
GROQ_API_KEY = "GROQ_API_KEYIN" #readme.md yi oku

client = Groq(api_key=GROQ_API_KEY)

logging.basicConfig(level=logging.INFO)

#Groq AI 
def ask_ai(user_id, text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """Senin adin Jarvis.
Bir Telegram chatbotusun.
Sana 'sen kimsin' denirse kendini tanitirsin.
Turkce konusursun.""" #content kısmında bu ai'in kim olduğunu anlatıyosun ona hayat veriyosun gibi
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content

# Telegram
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.message.from_user.id

    reply = ask_ai(user_id, text)
    await update.message.reply_text(reply)

# Main 
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("[BOT] Jarvis aktif.")
    app.run_polling()

if __name__ == "__main__":
    main()