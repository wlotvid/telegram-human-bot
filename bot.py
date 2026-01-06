import random
import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv(8023487115:AAG8O6Tv7dOJ6T8RqxoA4gpcZqOEFQ_NwyA)

REPLY_CHANCE = 0.15

replies = [
    "lol",
    "😂",
    "💀",
    "nah",
    "same",
    "idk",
    "fr",
    "👀"
]

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    if random.random() > REPLY_CHANCE:
        return

    await asyncio.sleep(random.randint(10, 45))
    await update.message.reply_text(random.choice(replies))

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
