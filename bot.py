import os  
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = os.getenv("BOT_TOKEN :8592484270:AAEJEp4IY966ZYAUtDQqNtwCoXCiqgqOhJE") 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bonjour 👋 Je suis votre chatbot.")
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        user_message = update.message.text.lower()

        if "bonjour" in user_message:
            response = "Bonjour 👋 Comment puis-je vous aider ?"
        elif "prix" in user_message:
            response = "Voici notre grille tarifaire."
        else:
            response = "Je n’ai pas compris votre demande."

        await update.message.reply_text(response)
if __name__ == '__main__':
    if not TOKEN:
        print("Erreur : Le token BOT_TOKEN n'est pas défini.")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
        app.run_polling()
