import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def auto_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type in ["group", "supergroup"]:
        await context.bot.leave_chat(update.effective_chat.id)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, auto_leave))

app.run_polling()
