from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8592484270:AAFI1lFZj3fC6Yu3uHvZzjm6M3GRiCOBu10"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bonjour 👋 Je suis votre chatbot.")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
   if update.message and update.message:
       user_message = update.message.text.lower()

    if "bonjour" in user_message:
        response = "Bonjour 😊 Comment puis-je vous aider ?"
    elif "prix" in user_message:
        response = "Voici notre grille tarifaire."
    else:
        response = "Je n’ai pas compris votre demande."

    await update.message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
